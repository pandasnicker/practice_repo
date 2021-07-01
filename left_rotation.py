#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':

    n = int(input('Enter number of items: '))
    d = int(input('Enter number of rotations: '))
    arr = list(map(int, input().strip().split()))[:n]
    # temparr = arr
    # for i in range(d):
    #     item = int(temparr.pop(0))
    #     temparr = temparr + [item]
    #     print(temparr)

    d= d%n
    for i in range(d,n):
        print(arr[i],end=' ')
    
    for i in range(0,d):
        print(arr[i],end=' ')
    
    # arr = temparr
    # print(arr)