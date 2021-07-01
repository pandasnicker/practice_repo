# program to compress a string with consecutive repeated characters (compresses all characters in a string)

def comp2(string):
    s_new = ""
    str_hash = {}

    for i in range(len(string)):

        if string[i] not in str_hash.keys():
            str_hash[string[i]] = 1
        else:
            str_hash.update({string[i] : str_hash.get(string[i]) + 1})

    if max(list(str_hash.values())) > 1: 
        for key, value in str_hash.items():
            s_new += key + str(value)
    else:
        return string

    return s_new


print(comp2("aabbbbddaa"))