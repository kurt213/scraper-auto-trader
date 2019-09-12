'''
Replace a set of multiple sub strings with a new string in main string.
'''

import re

def replaceMultiple(main_string, to_be_replaces, new_string):
    # Iterate over the strings to be replaced
    for elem in to_be_replaces :
        # Check if string is in the main string
        if elem in main_string :
            # Replace the string
            main_string = main_string.replace(elem, new_string)
    
    main_string = main_string.strip()
    return  main_string

# Change this to class
def keySpecs(response, url):

    year_reg = [[0, 'N/A']]
    body_type = 'N/A'
    mileage = 0
    engine_size = 0.0
    bhp = 0
    transmission = 'N/A'
    fuel_type = 'N/A'
    body_type = 'N/A'
    doors = 'N/A'

    vehicle_make = re.findall(r'(?:make=)([A-Z0-9%\-]+)(?:&|$)', url)
    vehicle_make = vehicle_make[0].replace('%20', ' ')
    vehicle_model = re.findall(r'(?:model=)([A-Z0-9%\-!\+/]+)(?:&|$)', url)
    vehicle_model = vehicle_model[0].replace('%20', ' ')
    
    key_specs_list = response
    key_specs_list = [x for x in key_specs_list if '\n' not in x]

    for i, s in enumerate(key_specs_list):
        if 'reg)' in s:
            year_reg_index = i
            year_reg = re.findall(r'(?:.*)(\d\d\d\d)(?:.*\()(.*)(?:\))', key_specs_list[year_reg_index])
        elif 'miles' in s:
            mileage_index = i
            mileage = re.match(r'[0-9]\d{0,2}(\.\d{3})*(,\d+)?', key_specs_list[mileage_index])
            mileage = mileage[0]
        elif re.match('.*L$', s):
            engine_index = i
            engine_size = re.match(r'[0-9]\d*(\.\d+)?', key_specs_list[engine_index])
            engine_size = engine_size[0]
        elif 'bhp' in s:
            bhp_index = i
            bhp = re.match(r'\d+', key_specs_list[bhp_index])
            bhp = bhp[0]
        elif re.match('automatic|manual', s.lower()):
            transmission_index = i
            transmission = key_specs_list[transmission_index]
        elif re.match('petrol|diesel|hybrid|electric', s.lower()):
            fuel_index = i
            fuel_type = key_specs_list[fuel_index]
        elif re.match('.*door.*', s.lower()):
            doors_index = i
            doors = key_specs_list[doors_index]
        else:
            body_index = i
            body_type = key_specs_list[body_index]

    key_dict = {
        'year': year_reg[0][0], 
        'registration': year_reg[0][1],
        'body_type': body_type,
        'mileage': mileage,
        'engine_size': engine_size,
        'bhp': bhp,
        'transmission': transmission,
        'fuel_type': fuel_type,
        'vehicle_make': vehicle_make,
        'vehicle_model': vehicle_model,
        'doors': doors
    }
    return key_dict