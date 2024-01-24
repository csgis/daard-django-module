forms = {

    "general": {
        "bone_amount": {
            "name": "bone_amount",
            "label": "Bone amount",
            "hidden_from_api": True,
            "mandatory": True,
            "type": "selectfield",
            "help_text": "Please choose one value",
            "values": [('>75%', '>75%',),
                       ('<75%', '<75%',),
                       ('absent', 'Absent',),
                       ('unknown', '% unknown',)]
        }
    },
    # 1 step
    "disease": {
        "subadults": {
            "name": "subadults",
            "label": "Subadult",
            "mandatory": False,
            "type": "checkbox",
            "help_text": "Disease affects subadults?",
            "values": ""
        },

        "adults": {
            "name": "adults",
            "label": "Adult",
            "mandatory": False,
            "type": "checkbox",
            "help_text": "Disease affects adults?",
            "values": ""
        },
        "disease": {
            "name": "disease",
            "label": "Disease",
            "mandatory": True,
            "type": "rest-selectfield",
            "url": "/api/disease-search/",
            "params": "?search_age=<subadults|adults>&fields=id,name,<adults|subadults>",
            "note": "<adults,subadults> are checked options from fields ADULTS & SUBADULTS",
            "help_text": "Please choose one value",
            "values": ""
        },
        "age_class": {
            "name": "age_class",
            "label": "Age class",
            "mandatory": True,
            "type": "selectfield",
            "help_text": "Please choose one value",
            "values": [('Foetus', 'Fetus',),
                       ('Infans', 'Infans',),
                       ('Adolescent', 'Adolescent',),
                       ('Early Adult', 'Early Adult',),
                       ('Late Adult', 'Late Adult',),
                       ('Senile', 'Senile',),
                       ('0–3', '0 – 3 years',),
                       ('4–6', '4 – 6 years',),
                       ('7–12', '7 – 12 years',),
                       ('13–20', '13 – 20 years',),
                       ('21–35', '21 – 35 years',),
                       ('36–50', '36 – 50 years',),
                       ('50+', '50 + years',),
                       ('Unknown', "Unknown"), ]
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
            "label": "Age freetext",
            "mandatory": False,
            "type": "textfield",
            "help_text": "Age information as freetext",
            "values": "",
            "note": "Visible if AGE_FREETEXT_CHECKBOX=checked"
        },
        "age_estimation_method": {
            "name": "age_estimation_method",
            "label": "Methods age estimation",
            "mandatory": False,
            "type": "textfield",
            "help_text": "Methods used for age estimation",
            "values": "",
            "note": ""
        },
        "narrower_age_class_freetext": {
            "name": "narrower_age_class_freetext",
            "label": "Narrower age",
            "mandatory": False,
            "type": "textfield",
            "help_text": "Narrower age class as freetext",
            "values": "",
            "note": ""
        },
        "sex": {
            "name": "sex",
            "label": "Sex",
            "mandatory": True,
            "type": "selectfield",
            "help_text": "Please choose one value",
            "values": [('f', 'F',),
                       ('f?', 'F?',),
                       ('unknown', 'Unknown',),
                       ('m', 'M',),
                       ('m?', 'M?',), ]
        },
        "sex_freetext": {
            "name": "sex_freetext",
            "label": "Sex freetext",
            "mandatory": False,
            "type": "textfield",
            "help_text": "Sex determination method",
            "values": "",
            "note": ""
        },
        "size_from": {
            "name": "size_from",
            "label": "Size from",
            "mandatory": False,
            "type": "textfield",
            "help_text": "Insert body sizes from f.e 176.50",
            "note": "takes input like 176.50",
            "values": []
        },
        "size_to": {
            "name": "size_to",
            "label": "Size to",
            "mandatory": False,
            "type": "textfield",
            "help_text": "Insert body sizes f.e. 180.50",
            "note": "takes input like 180.50",
            "values": []
        },
        "size_freetext": {
            "name": "size_freetext",
            "label": "Size method",
            "mandatory": False,
            "type": "textarea",
            "help_text": "Method used for size calculations",
            "note": "",
            "values": []
        }
    },

    # step 2
    "inventory": {
        "PLACEHOLDER": {
            "name": "",
            "values": ""
        }
    },

    # Step 3 should be dynamically generated

    # step 4
    "site": {
        "reference_images": {
            "name": "reference_images",
            "label": "Reference images",
            "mandatory": False,
            "type": "textfield",
            "help_text": "If you are interested to upload pictures, please contact the editors.",
            "values": []
        },
        "origin": {
            "name": "origin",
            "label": "Origin",
            "type": "radiogroup",
            "help_text": "",
            "mandatory": True,
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
        "position": {
            "name": "position",
            "label": "Position (Click on map)",
            "mandatory": True,
            "type": "hiddenfield",
            "help_text": "The position as string 'lat,long'. This field will be filled in automatically.",
            "values": []
        },
        "site": {
            "name": "site",
            "label": "City, Country",
            "mandatory": True,
            "type": "textfield",
            "help_text": "City and Country",
            "values": []
        },
        "archaeological_tombid": {
            "name": "archaeological_tombid",
            "label": "Grave-ID",
            "mandatory": False,
            "type": "textfield",
            "help_text": "Please choose one value",
            "note": "visible if origin.objects.archaeological = checked;",
            "values": []
        },
        "archaeological_individualid": {
            "name": "archaeological_individualid",
            "label": "Individual-ID",
            "mandatory": False,
            "type": "textfield",
            "help_text": "Please choose one value",
            "note": "visible if origin.objects.archaeological = checked;",
            "values": []
        },
        "archaeological_funery_context": {
            "name": "archaeological_funery_context",
            "label": "Funerary context",
            "mandatory": True,
            "type": "selectfield",
            "help_text": "Please choose one value",
            "note": "visible if origin.objects.archaeological = checked;",
            "values": [('primary', 'Primary',),
                       ('secondary', 'Secondary',),
                       ('unknown', 'Unknown',),
                       ('commingled', 'Commingled',)]
        },
        "archaeological_burial_type": {
            "name": "archaeological_burial_type",
            "label": "Burial type",
            "mandatory": True,
            "type": "selectfield",
            "help_text": "Please choose one value",
            "note": "visible if origin.objects.archaeological = checked;",
            "values": [('single', 'Single',),
                       ('double', 'Double',),
                       ('multiple', 'Multiple',),
                       ('unknown', 'Unknown',)]
        },
        "storage_place": {
            "name": "storage_place",
            "label": "Storage place",
            "mandatory": True,
            "type": "selectfield",
            "help_text": "You can choose more than one value",
            "values": [('institution_1', 'Institution 1',),
                       ('institution_2', 'Institution 2',),
                       ('institution_3', 'Institution 3',),
                       ('unknown', 'Unknown',)]
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
            "label": "Storage place freetext",
            "mandatory": False,
            "type": "textfield",
            "help_text": "The INDIVIDUAL ID",
            "note": "visible if storage_place_checkbox = checked;",
            "values": []
        },
        "chronology": {
            "name": "chronology",
            "label": "Chronology",
            "mandatory": True,
            "type": "textfield",
            "help_text": "Define the time period using the 3 fields (from, to, BCE/CE). Furthermore, an optional free text can be entered. ",
            "options": []
        },
        "dating_method": {
            "name": "dating_method",
            "label": "Dating object",
            "mandatory": True,
            "type": "selectfield",
            "help_text": "You can choose more than one value",
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
        "chronology_checkbox": {
            "name": "chronology_checkbox",
            "label": "",
            "mandatory": False,
            "type": "checkbox",
            "help_text": "Add additional chronology information?",
            "values": ""
        },
        "chronology_freetext": {
            "name": "chronology_freetext",
            "label": "Chronology freetext",
            "mandatory": False,
            "type": "textarea",
            "help_text": "Add additional chronology information as freetext",
            "note": "visible if chronology_checkbox = checked;",
            "values": []
        }
    },

    # step 5
    "publication": {
        "dna_analyses": {
            "name": "dna_analyses",
            "label": "DNA analyses",
            "mandatory": True,
            "type": "selectfield",
            "help_text": "Please choose one value",
            "values": [('successful', 'Successful',),
                       ('unsuccessful', 'Unsuccessful',),
                       ('absent', 'Absent',),
                       ('unknown', 'Unknown',)]
        },
        "dna_analyses_link": {
            "name": "dna_analyses_link",
            "label": "DNA analyses link",
            "mandatory": False,
            "type": "textfield",
            "help_text": "Link to reference",
            "values": []
        },
        "published": {
            "name": "published",
            "label": "Already published?",
            "mandatory": False,
            "type": "checkbox",
            "help_text": "",
            "values": ""
        },
        "doi": {
            "name": "doi",
            "label": "DOI",
            "mandatory": False,
            "type": "textfield",
            "note": "only visible if PUBLICATION_CHECKBOX is checked",
            "help_text": "Digital Object Identifier if available",
            "values": []
        },
        "references": {
            "name": "references",
            "label": "References",
            "mandatory": False,
            "type": "textarea",
            "note": "only visible if PUBLICATION_CHECKBOX is checked",
            "help_text": "Further reference; please use the APA referencing style",
            "values": []
        },
        "comment": {
            "name": "comment",
            "label": "Comment",
            "mandatory": False,
            "type": "textarea",
            "note": "",
            "help_text": "Any further comments",
            "values": []
        },
        "differential_diagnosis": {
            "name": "differential_diagnosis",
            "label": "Differential Diagnosis",
            "mandatory": False,
            "type": "textarea",
            "note": "a custom field for Differential Diagnosis",
            "help_text": "The Differential Diagnosis (not mandatory)",
            "values": []
        }

    }


}
