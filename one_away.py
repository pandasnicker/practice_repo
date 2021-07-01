# program to check if a string is just one character away from another string

def oneaway(str1, str2):
    st1 = str1 if len(str1) < len(str2) else str2
    st2 = str2 if len(str1) > len(str2) else str1

    for i in range(len(st1)):
        # print("Looking at str1 {} and str2 {}".format(st1[i], st2[i]))
        # print(st1[0:i]+st1[i+1:] , st2[0:i]+st2[i+1:])
        if st1[0:i]+st1[i+1:] in st2[0:i]+st2[i+1:]:
            return True

    return False

print(oneaway("galerism","paler"))