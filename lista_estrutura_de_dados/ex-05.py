

def fundir_dicionarios(dict1, dict2):
    output = dict(dict1)

    for key, value in dict2.items():
        if key not in output.keys():
            output[key] = value
        else:
            output[key] += value
    
    return output



dict1 = {'a': 10, 'b': 20, 'c': 30}
dict2 = {'b': 5, 'c': 15, 'd': 40}

print(fundir_dicionarios(dict1, dict2))