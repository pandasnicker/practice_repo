# program to detect if a string is rotated version of another string

def isSubstring(str1, str2):
    if len(str1) != len(str2):
        return False
    
    for i in range(len(str1)):
        if str2[i:] in str1 and str2[:i] == str1[len(str1)-i:]:
            return True
    
    return False

print(isSubstring("GulamMohiddin", "MohiddinGulam"))