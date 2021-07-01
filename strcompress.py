# program to compress a string with consecutive repeated characters (compresses characters at their positions in the original string)

def comp(string):
    s_new = ""
    count = 1
    for i in range(len(string)):
        if i+1 < len(string) and string[i] == string[i+1]:
            count += 1
        else:
            s_new += string[i] + str(count)
            count = 1


    return s_new


print(comp("aabbbbddaa"))