def join_strings(strings):
    res = ""
    for i in range(len(strings)):
        if i == (len(strings)-1):
            res = res + f"{strings[i]}"
        else:
            res = res + f"{strings[i]},"
    return res
