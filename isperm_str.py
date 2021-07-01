# check if the 2 strings are permutation of each other

def ispermutation(str1, str2):
    return sorted(str1) == sorted(str2)

print(ispermutation("gulam", "maluG"))

