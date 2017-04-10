pirates = [
    {'Name': 'Olaf', 'has_wooden_leg': False, 'gold': 12},
    {'Name': 'Uwe', 'has_wooden_leg': True, 'gold': 9},
    {'Name': 'Jack', 'has_wooden_leg': True, 'gold': 16},
    {'Name': 'Morgan', 'has_wooden_leg': False, 'gold': 17},
    {'Name': 'Hook', 'has_wooden_leg': True, 'gold': 20},
]

# Write a function that takes any list that contains pirates as in the example,
# And returns a list of names containing the pirates that
# - have wooden leg and
# - have more than 15 gold

def pirate_list(lst):   # open a new function with lst arg.
    """Function for returns a list of names containing the pirates that have wooden leg and have more than 15 gold"""
    dict_list = []      # open an empty list
    
    for dct in lst:     # check every dicts(elements in the 'pirates' list) 
        if dct['has_wooden_leg'] is True and dct['gold'] > 15: # if statments
            dict_list.append(dct['Name'])   # append value of 'Name' keys to the empty list
    return dict_list    # return the correct answer


print(pirate_list(pirates))