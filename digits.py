
def digits(n):
    import math
    if n==0: return 0
    return int(math.log10(abs(n)))+1

def digits1(m):
    if m==0: return 0
    return 1+digits1(m//10)

print(digits(-2))

print(digits1(123))