# program to reverse a integer

def rev_int(x):
    if x == 0:
        return x

    reversed = int(str(x)[::-1]) if x > 0 else int(str(x)[0] + (str(x))[:0:-1])

    if abs(reversed) > (2**31)-1:
        return 0 
    else:
        return reversed

print(rev_int(156384741))