import json
from collections import OrderedDict
import logging
logger = logging.getLogger("geonode")
import urllib.request
import json

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
    bone_relations = getattr(instance, "bone_relations", {})
    amount = {
        ">75%": [], # above or below 75 but without bone change
        "<75%": [], # above or below 75 but without bone change
        "affected": [], # above or below 75 but with bone change
        "unknown": []
    }


    for item in inventory:
        amount_name = inventory[item]['amount']

        # check if bone has unknown or absent bones if no it is affected SOO
        if item in bone_relations and if '_changes' in bone_relations[item]:
            all_absent = []
            for relation in bone_relations[item]['_changes']:
                if 'absent' in relation['bone_change'] \
                        or 'Absent' == relation['bone_change'] \
                        or 'Unknown' in relation['bone_change'] \
                        or 'unknown' in relation['bone_change']:
                    all_absent.append(False)
                else:
                    all_absent.append(True)
        is_affected = True if any(all_absent) else False

        if amount_name == '>75%' or amount_name == '<75%':
            amount_name = 'affected' if is_affected else amount_name

        # combine absent and unknown
        if amount_name == 'absent' or amount_name == 'Absent' or amount_name == 'Unknown':
            amount_name = 'unknown'

        svg_ids = inventory[item]['svgid'] \
            .replace('bone', '') \
            .split(',')

        for id in svg_ids:
            if id not in amount[amount_name]:
                amount[amount_name].append(id)

        amount_json = json.dumps(amount)
        amount_urlencode = urllib.parse.quote(amount_json)
    return amount_urlencode

def replace_all(text, dic):
    for i, j in dic.items():
        text = text.replace(i, j)
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
                str_bones = ', '.join(item['bone_change'])
                str_bones = str_bones.rstrip(', ')
                str_bones = str_bones + ";"
                item['bone_change'] = str_bones

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
