'''
Replace a set of multiple sub strings with a new string in main string.
'''

import re

def replaceMultiple(mainString, toBeReplaces, newString):
    # Iterate over the strings to be replaced
    for elem in toBeReplaces :
        # Check if string is in the main string
        if elem in mainString :
            # Replace the string
            mainString = mainString.replace(elem, newString)
    
    mainString = mainString.strip()
    return  mainString

def keySpecs(response):
    
    key_specs_list = response
    key_specs_list = [x for x in key_specs_list if '\n' not in x]

    year_reg = re.findall(r'(?:.*)(\d\d\d\d)(?:.*\()(.*)(?:\))', key_specs_list[0])
    m_mileage = re.match(r'[1-9]\d{0,2}(\.\d{3})*(,\d+)?', key_specs_list[2])
    m_engine_size = re.match(r'[1-9]\d*(\.\d+)?', key_specs_list[3])
    m_bhp = re.match(r'\d+', key_specs_list[4])

    key_dict = {
        'year': year_reg[0][0], 
        'registration': year_reg[0][1],
        'body_type': key_specs_list[1],
        'mileage': m_mileage[0],
        'engine_size': m_engine_size[0],
        'bhp': m_bhp[0],
        'transmission': key_specs_list[5],
        'fuel_type': key_specs_list[6],
    }
    return key_dict