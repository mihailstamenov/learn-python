def double_string(string):
    new_string = ""
    for char in string:
        for i in range(2):
            new_string += char
    return new_string