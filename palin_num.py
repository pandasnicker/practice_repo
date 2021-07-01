def isPalin(n):
    rev = 0
    m=n
    while n!=0:
        lst = n%10
        rev = rev*10+lst
        n = n//10
    print(rev)
    return m==rev

print(isPalin(152))