import json
from collections import OrderedDict
import logging
logger = logging.getLogger("geonode")


def count_bones(instance):
    amount_of_bones = len(getattr(instance, "inventory", 0))
    return amount_of_bones

def get_bone_names(instance):

    inventory = getattr(instance, "inventory", {})
    if type(inventory) == str:
        inventory = json.loads(inventory)

    bone_names = ', '.join(x for x, y in inventory.items())
    return bone_names

def get_svgids(instance):
    inventory = getattr(instance, "inventory", {})
    if type(inventory) == str:
        inventory = json.loads(inventory)

    svgid_names = ','.join(y.get("svgid","") for x, y in inventory.items())
    return svgid_names


def replace_all(text, dic):
    for i, j in dic.items():
        text = text.replace(i, j)
        print(text)
    return text


def format_bone_relations(instance):
    inventory = getattr(instance, "inventory", {})
    bone_relations = getattr(instance, "bone_relations", {})
    new_dict = {}
    for key in inventory.keys():
        item_name = inventory[key]["label"]

        pops = ['svgid', 'label', 'id', 'section', 'name']
        for to_replace in pops:
            inventory[key].pop(to_replace, None)

        new_dict[item_name] = inventory[key]
        if key in bone_relations:
            new_dict[item_name]["changes"] = bone_relations[key].get("_changes", "")
            for item in new_dict[item_name]["changes"]:
                print(item)
                str_bones = ', '.join(item['bone_change'])
                str_bones = str_bones.rstrip(', ')
                str_bones = str_bones + ";"
                item['bone_change'] = str_bones
            print(new_dict[item_name]["changes"])

    c_b_t_bc_rel = ' ● '.join([f'{key}: {value}' for key, value in new_dict.items()])
    repls = OrderedDict([('<', 'less than '),
                         ('>', 'more than '),
                         ('{', ''),
                         ('}', ''),
                         ('amount', 'Amount'),
                         ('technic', 'Technic'),
                         ('bone_change', 'Bone change'),
                         ("'", ''),
                         (', Bone change', '; Bone change'),
                         (';]', ']'),
                         (';,', ';'),
                         (', changes:', '; Bone changes:'),
                         ]
                        )

    return replace_all(c_b_t_bc_rel, repls)

def get_technics(instance):
    bone_relations = getattr(instance, "bone_relations", {})
    technic = []
    for key in bone_relations.keys():
        changes_key = bone_relations[key].get("_changes")
        if (changes_key is not None):
          for change_item in changes_key:
              item = change_item.get("technic", None)
              if item is not None:
              	technic.append(item)

    technic = set(technic)
    technic = ', '.join(technic)
    return technic
