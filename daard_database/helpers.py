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
        new_dict[key] = inventory[key]

        for key2, val2 in bone_relations[key].items():
            if key not in new_dict[key]:
                new_dict[key][key2] = ''.join(val2) if type(val2) is list else val2

        new_dict[key] = ''.join([f'({key}: {value})' for key, value in new_dict[key].items()])

    c_b_t_bc_rel = ''.join([f'({key}:\n{value})' for key, value in new_dict.items()])
    c_b_t_bc_rel = c_b_t_bc_rel.replace("<", "less than")
    c_b_t_bc_rel = c_b_t_bc_rel.replace(">", "more than")
    c_b_t_bc_rel = c_b_t_bc_rel.replace("\n","").replace("\r","")
    return  c_b_t_bc_rel

def get_technics(instance):
    bone_relations = getattr(instance, "bone_relations", {})
    technic = []
    for key in bone_relations.keys():
        t = bone_relations[key].get("technic")
        if (t is not None):
            technic.append(t)
    technic = set(technic)
    technic = ', '.join(technic)
    return technic
