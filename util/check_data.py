def if_exists(data, row, keys):
    new_data = {}
    for index, key in enumerate(keys):
        if key not in data:
            new_data[key] = row[index]
        else:
            new_data[key] = data[key]
    return new_data


def check_parameters(keys, required_keys):
    for k in required_keys:
        if k not in keys:
            return False
    return True


def default_values(data, keys):
    new_data = {}
    for key in keys:
        if key not in data:
            new_data[key] = ""
        else:
            new_data[key] = data[key]
    return new_data
