def get_json_attr(json, name):
    if name in json.keys():
        return json[name]
    return None
