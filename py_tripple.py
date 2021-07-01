
from math import sqrt


def py_trip(n)->list:
    f_list=[]
    for i in range(1,n):
        for j in range(i,n):
            x = (sqrt(i**2 + j**2))
            if x.is_integer():
                f_list.append([i,j,int(x)])
    return f_list

def is_pytrip(a, b, c):
    return (a**2 + b**2) == c**2

# print(is_pytrip(7,24,25))
print(py_trip(100))
