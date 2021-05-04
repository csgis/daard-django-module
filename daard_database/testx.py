forms = {
    "AGE_CLASS": {
        "name" : "AGE_CLASS",
        "mandatory": True,
        "type": "Selectfield",
        "help_text": "Please choose exatly one value",
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
    "BASE_CLASS": {
        "name" : "BASE_CLASS",
        "mandatory": True,
        "type": "Selectfield",
        "help_text": "Please choose exatly one value",
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
}

new_form = []
for i in forms:
    new_values = []
    for name,value in forms[i]['values']: new_values.append({"name": name, "value": value})
    forms[i]["values"] = new_values
    new_form.append(forms[i])

print(new_form)