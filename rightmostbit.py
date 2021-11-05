def posOfRightMostDiffBit(m,n):
    #Your code here
    if m==0 or n==0:
        res = m|n
    else:
        res = m^n
    c = 1
    while res!=0:
        if res&1 == 1:
            return c
        res>>=1
        print(res)
        c+=1
    return -1

print(posOfRightMostDiffBit(8,2))