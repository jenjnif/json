json_dict = {}

# data2 = '''{"key1": "smalue1", "key2": "smalue2"}'''
def json_parser(json):
    accumulator = ""
    key_pair_list = []

    for character in json:
        accumulator += character
        if character == ',':
            key_pair_list.append(accumulator)
            accumulator = ""
            print(key_pair_list)

    key_pair_list.append(accumulator)
    print(key_pair_list)
