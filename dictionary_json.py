json_dict = {}


def json_parser(json):

    new_dictionary = {}
    key_name = ""
    value_name = ""
    reading_key = None
    value = None
    key_position = 0
    value_position = 0
    key1 = ""
    accumulator = ""

# data2 = '''{"key": "smalue1", "key2": "smalue2"}'''
    for character in json:
        accumulator += character
        print(accumulator)
        # if key is None:
        #     if character == '"':
        #         key_name += character
        #         key_position += 1
        #         print(key_position)
        #     if key_position > 0:
        #         print("more than 0")
        #         if character != '"':
        #             key_name += character
        #         else:
        #             key1 = key_name
        #             key = False
        #             new_dictionary[key1] = None
        #             print('this is the key ' + key1)
        # if key is False:
        #     pass
                # value = True
                # while value is True:
                #     if '"':
                #         value_name = value_name + character
                #         value_position += 1
                #     if value_position > 0:
                #         if '"':
                #             value1 = value_name
                #             value = False
                #             new_dictionary[key1] = value1
                            # print('this is the value ' + value1)
        # print(new_dictionary)
