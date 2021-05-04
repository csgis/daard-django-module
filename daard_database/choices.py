forms = {

    "general":{
        "bone_amount": {
            "name": "bone_amount",
            "label": "BONE AMOUNT",
            "hidden_from_api": True,
            "mandatory": True,
            "type": "selectfield",
            "help_text": "Please choose exactly one value",
            "values": [('>75%', '>75%',),
                       ('<75%', '<75%',),
                       ('absent', 'ABSENT',),
                       ('unknown', 'UNKNOWN',)]
        }
    },

    # 1 step
    "disease": {
        "subadults": {
            "name": "subadults",
            "label": "SUBADULTS",
            "mandatory": False,
            "type": "checkbox",
            "help_text": "Disease affects subadults?",
            "values": ""
        },

        "adults": {
            "name": "adults",
            "label": "ADULTS",
            "mandatory": False,
            "type": "checkbox",
            "help_text": "Disease affects adults?",
            "values": ""
        },
        "disease": {
            "name": "disease",
            "label": "DISEASE",
            "mandatory": True,
            "type": "rest-selectfield",
            "url": "/api/disease-search/",
            "params": "?search_age=<subadults|adults>&fields=id,name,<adults|subadults>",
            "note": "<adults,subadults> are checked options from fields ADULTS & SUBADULTS",
            "help_text": "Please choose exactly one value",
            "values": ""
        },
        "age_class": {
            "name": "age_class",
            "label": "AGE CLASS",
            "mandatory": True,
            "type": "selectfield",
            "help_text": "Please choose exactly one value",
            "values": [('Foetus', 'Foetus',),
                       ('0–3', '0 – 3',),
                       ('4–6', '4 – 6',),
                       ('7–12', '7 – 12',),
                       ('13–20', '13 – 20',),
                       ('21–35', '21 – 35',),
                       ('36–50', '36 – 50',),
                       ('50+', '50 +',),
                       ('Unknown', "Unknown"), ]
        },
        "age": {
            "name": "age",
            "label": "AGE",
            "mandatory": False,
            "type": "selectfield",
            "help_text": "Please choose exactly one value",
            "values": [('unknown', 'Unknown',),
                       ('does_not_apply', 'Does not apply',)]
        },
        "age_freetext_checkbox": {
            "name": "age_freetext_checkbox",
            "label": "",
            "mandatory": False,
            "type": "checkbox",
            "help_text": "Insert age class as freetext?",
            "values": ""
        },
        "age_freetext": {
            "name": "age_freetext",
            "label": "AGE FREETEXT",
            "mandatory": False,
            "type": "textfield",
            "help_text": "Age class as freetext?",
            "values": "",
            "note": "Visible if AGE_FREETEXT_CHECKBOX=checked"
        },
        "sex": {
            "name": "sex",
            "label": "SEX",
            "mandatory": True,
            "type": "selectfield",
            "help_text": "Please choose exactly one value",
            "values": [('f', 'F',),
                       ('f?', 'F?',),
                       ('unknown', 'UNKNOWN',),
                       ('m', 'M',),
                       ('m?', 'M?',), ]
        },
    },

    # step 2
    "inventory": {
            "PLACEHOLDER": {
                "name": "",
                "values":""
            }
        },

    # Step 3 should be dynamically generated

    # step 4
    "site": {
        "reference_images": {
            "name": "reference_images",
            "label": "REFERENCE IMAGES",
            "mandatory": False,
            "type": "inputfield",
            "help_text": "Link to iDAI.objects",
            "values": []
        },
        "origin": {
            "name": "origin",
            "label": "ORIGIN",
            "type": "group",
            "help_text": "",
            "values": "",
            "objects": {
                "archaeological": {
                    "name": "archaeological",
                    "label": "Archaeological",
                    "mandatory": False,
                    "type": "Radio",
                    "help_text": "",
                    "values": []
                },
                "collection": {
                    "name": "collection",
                    "label": "Collection",
                    "mandatory": False,
                    "type": "Radio",
                    "help_text": "",
                    "values": []
                }
            }
        },
        "archaeological_site": {
            "name": "archaeological_site",
            "label": "Site",
            "mandatory": False,
            "type": "rest-inputfield",
            "url": "/api/gazetteer-sites/",
            "params": "?q=<term>&task=<suggestion>|<site>",
            "help_text": "Search for gazetteer Information",
            "note": "visible if origin.objects.archaeological or origin.objects.archaeological = checked; should store a link and set lat long hidden fields",
            "values": []
        },
        "lat": {
            "name": "lat",
            "label": "lat",
            "mandatory": False,
            "type": "hiddenfield",
            "help_text": "The latitude",
            "values": []
        },
        "long": {
            "name": "long",
            "label": "lat",
            "mandatory": False,
            "type": "hiddenfield",
            "help_text": "The longitude",
            "values": []
        },
        "archaeological_tombid": {
            "name": "archaeological_tombid",
            "label": "TOMB ID",
            "mandatory": False,
            "type": "inputfield",
            "help_text": "The Tomb ID",
            "note": "visible if origin.objects.archaeological = checked;",
            "values": []
        },
        "archaeological_individualid": {
            "name": "archaeological_individualid",
            "label": "INDIVIDUAL ID",
            "mandatory": False,
            "type": "inputfield",
            "help_text": "The INDIVIDUAL ID",
            "note": "visible if origin.objects.archaeological = checked;",
            "values": []
        },
        "archaeological_funery_context": {
            "name": "archaeological_funery_context",
            "label": "FUNERY CONTEXT",
            "mandatory": True,
            "type": "selectfield",
            "help_text": "Please choose exactly one value",
            "note": "visible if origin.objects.archaeological = checked;",
            "values": [('primary', 'Primary',),
                       ('secondary', 'Secondary',),
                       ('unknown', 'UNKNOWN',)]
        },
        "archaeological_burial_type": {
            "name": "archaeological_burial_type",
            "label": "FUNERY CONTEXT",
            "mandatory": True,
            "type": "selectfield",
            "help_text": "Please choose exactly one value",
            "note": "visible if origin.objects.archaeological = checked;",
            "values": [ ('single', 'Single',),
                        ('double', 'Double',),
                        ('multiple', 'Multiple',),
                        ('unknown', 'UNKNOWN',)]
        },
        "storage_place": {
            "name": "storage_place",
            "label": "STORAGE PLACE",
            "mandatory": True,
            "type": "selectfield",
            "help_text": "Please choose exactly one value",
            "values": [('institution_1', 'Institution 1',),
                       ('institution_2', 'Institution 2',),
                       ('institution_3', 'Institution 3',),
                       ('unknown', 'UNKNOWN',)]
        },
        "storage_place_checkbox": {
            "name": "storage_place_checkbox",
            "label": "",
            "mandatory": False,
            "type": "checkbox",
            "help_text": "Insert storage place as freetext?",
            "values": ""
        },
        "storage_place_freetext": {
            "name": "storage_place_freetext",
            "label": "STORAGE PLACE FREETEXT",
            "mandatory": False,
            "type": "inputfield",
            "help_text": "The INDIVIDUAL ID",
            "note": "visible if storage_place_checkbox = checked;",
            "values": []
        },
        "storage_condition": {
            "name": "storage_place_freetext",
            "label": "STORAGE CONDITION",
            "mandatory": True,
            "type": "selectfield",
            "help_text": "Please choose exactly one value",
            "values": [('exhibition', 'Exhibition',),
                       ('accessible_for_study', 'Accessible for study',),
                       ('not_accessible_for_study', 'Not accessible for study',),
                       ('does_not_apply', 'Does not apply',),
                       ('unknown', 'UNKNOWN',)]
        },
        "chronology": {
            "name": "chronology",
            "label": "CHRONOLOGY",
            "mandatory": False,
            "type": "rest-inputfield",
            "url": "/api/chronology-periods/",
            "params": "?q=<term>",
            "help_text": "Search for chronology Information",
            "values": []
        },
        "chronology_checkbox": {
            "name": "chronology_checkbox",
            "label": "Add additional Information?",
            "mandatory": False,
            "type": "checkbox",
            "help_text": "",
            "values": ""
        },
        "chronology_freetext": {
            "name": "chronology_freetext",
            "label": "",
            "mandatory": False,
            "type": "inputfield",
            "help_text": "Add additional information",
            "note": "visible if chronology_checkbox = checked;",
            "values": []
        },
    },

    # step 5
    "publication": {
        "dating_method": {
            "name": "dating_method",
            "label": "DATING METHOD",
            "mandatory": True,
            "type": "selectfield",
            "help_text": "Please choose exactly one value",
            "values": [('human_bone', 'Human bone',),
                       ('animal_bone', 'Animal bone',),
                       ('horn', 'Horn',),
                       ('ivory', 'Ivory',),
                       ('tooth', 'Tooth',),
                       ('hair', 'Hair',),
                       ('skin', 'Skin',),
                       ('soft_tissues', 'Soft tissues',),
                       ('wood', 'Wood',),
                       ('textile', 'Textile',),
                       ('botanical_remains', 'Botanical remains',),
                       ('stratigraphic', 'Stratigraphic',),
                       ('funerary-structures', 'Funerary structures',),
                       ('grave_goods', 'Grave goods',),
                       ('archives', 'Archives',),
                       ('texts', 'Texts',),
                       ('epigraphic_sources', 'Epigraphic sources',),
                       ('numismatic', 'Numismatic',),
                       ]
        },
        "dna_analyses": {
            "name": "dna_analyses",
            "label": "DNA ANALYSES",
            "mandatory": True,
            "type": "selectfield",
            "help_text": "Please choose exactly one value",
            "values": [('successful', 'Successful',),
                       ('unsuccessful', 'Unsuccessful',),
                       ('absent', 'Absent',),
                       ('unknown', 'UNKNOWN',)]
        },
        "dna_analyses_link": {
            "name": "dna_analyses_link",
            "label": "DNA ANALYSES LINK",
            "mandatory": False,
            "type": "inputfield",
            "help_text": "Link to reference",
            "values": []
        },
        "publication": {
            "type": "group",
            "name": "publication",
            "label": "PUBLICATION",
            "values": [],
            "objects": {
                "published": {
                    "name": "published",
                    "label": "Published",
                    "mandatory": False,
                    "type": "checkbox",
                    "help_text": "",
                    "values": ""
                },
                "publication": {
                    "name": "publication",
                    "mandatory": True,
                    "type": "selectfield",
                    "note": "only visible if PUBLICATION_CHECKBOX is checked",
                    "help_text": "Please choose exactly one value",
                    "values": [('published', 'Published',),
                               ('unpublished', 'Unpublished',)]
                },
            }
        }

    }


}
