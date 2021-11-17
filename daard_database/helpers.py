import json
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


def format_bone_relations(instance):
    inventory = getattr(instance, "inventory", {})
    bone_relations = getattr(instance, "bone_relations", {})
    new_dict = {}

    for key in inventory.keys():
        item_name = inventory[key]["label"]

        # refactor: use dict comprehension
        inventory[key].pop('svgid', None)
        inventory[key].pop('label', None)
        inventory[key].pop('id', None)
        inventory[key].pop('section', None)
        inventory[key].pop('name', None)
        new_dict[item_name] = inventory[key]
        new_dict[item_name]["changes"] = bone_relations[key].get("changes", "")

    c_b_t_bc_rel = ''.join([f'{key} : {value}' for key, value in new_dict.items()])
    c_b_t_bc_rel = c_b_t_bc_rel.replace("<", "less than ")
    c_b_t_bc_rel = c_b_t_bc_rel.replace(">", "more than ")
    return c_b_t_bc_rel

def get_technics(instance):
    bone_relations = getattr(instance, "bone_relations", {})
    technic = []
    for key in bone_relations.keys():
        changes_key = bone_relations[key].get("changes")
        if (changes_key is not None):
          for change_item in changes_key:
              item = change_item.get("technic", None)
              if item is not None:
              	technic.append(item)

    technic = set(technic)
    technic = ', '.join(technic)
    return technic
