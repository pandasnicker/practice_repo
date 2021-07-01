# program to check of integer is palindrome
# returns false if the number is negative or a multiple of 10

def isPalindrome(x):
    if 0 <= x < 10:
        return True
    
    if x < 0 or x%10 == 0:
        return False
    
    s = str(x)
    i=1
    while i-1 <= int(len(s)/2):
        # print(s[i-1],s[-i])
        if s[i-1] != s[-i]:
            return False
        i+=1
    
    return True

print(isPalindrome(121))