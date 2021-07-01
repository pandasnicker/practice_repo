

# def uniqStr(word):
#     l = len(word)
#     for i in range(0,l-1):
#         if word[i].lower() in [a for a in word[i+1:].lower()]:
#             return "Not Unique characters"
#     return "All Unique characters"

# print(uniqStr('Gulama'))


def uniqstr_nospl(word):
    l = len(word)
    for i in range(0,l-1):
        j = i+1
        while(j < l):
            if word[i].lower() == word[j].lower():
                return "Not Unique characters"
            j+= 1

    return "All Unique characters"

print(uniqstr_nospl('Gulam'))
