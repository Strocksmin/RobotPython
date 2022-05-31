import re


def main(source):
    p_values = r"(#-?[0-9]*)"
    p_keys = r"(option\s?.?[a-z]*\_?\d?[0-9]*)"
    response = {}
    new_source = source.replace('\n', ' ')
    keys = re.findall(pattern=p_keys, string=new_source)
    values = re.findall(pattern=p_values, string=new_source)
    for i in range(len(keys)):
        keys[i] = keys[i].replace("option ", "")
    for i in range(len(values)):
        values[i] = values[i].replace('#', '')
    for i in range(len(keys)):
        response[keys[i]] = int(values[i])
    return response
