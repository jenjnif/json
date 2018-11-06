import dictionary_json

# creating a dictionary in Python

data = {"key": "value1",
        "key2": "value2"}

value1 = data["key"]

print(value1)

value2 = data["key2"]

print(value2)


# this is json that looks a bit like a Python dictionary but is a string

data2 = '''{"key": "smalue1", "key2": "smalue2"}'''

# this is a fairly crude way of finding the information from json that we
# need - a better solution is below
smalue1 = data2[9:16]
smalue2 = data2[28:35]
print(smalue1)
print(smalue2)

# better solution to get the information out of the json file

# look through the string assigned to data2,
# if you find "key" when you get to next " save characters until next "
# store these characters as smalue1


dictionary_json.json_parser(data2)





