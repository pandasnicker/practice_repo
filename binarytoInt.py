
def bintoInt(num):
    l = len(num)
    res = 0

    for i in range(l):
        #print('i=',i)
        res = res+(int(num[i]) * 2**(l-i-1))
        #print(num[i],res)
    
    return res
print("The decimal value is: ", bintoInt('00101010101'))