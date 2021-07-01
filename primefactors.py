import math

def isPrime(i):
    if i==1: return False
    if i==2 or i==3: return True
    if i%2==0 or i%3==0: return False

    for j in range(5,math.isqrt(i),6):
        if i%j == 0: return False
    
    return True


def pFactors(n):
    if n==1: return 0
    res = []
    tmp = n
    i=2
    while(i<n): #Change to while loop
        if isPrime(i) and tmp%i==0:
            res.append(i)
            tmp = int(tmp/i)
            # print(i, tmp)
            i=2
        i+=1
    return res if len(res)>0 else [n]

print(pFactors(813))