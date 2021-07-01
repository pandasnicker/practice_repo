# program to check if a given string is a permutation of a Palindrome

def palin_perm(string1):
    str1dict = {}


    for s in string1.lower().replace(' ',''):
        if s in str1dict.keys():
            str1dict.update({s:int(str1dict.get(s)+1)})
        else:
            str1dict.update({s:1})
    
    odds = 0
    for i in str1dict.values():
        if i%2 != 0:
            odds += 1
        
    return odds < 2


print(palin_perm("taco cat"))