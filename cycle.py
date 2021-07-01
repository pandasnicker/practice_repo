from itertools import cycle
from time import sleep

for i in cycle(r'|/-\\'):
    print('\r',i,sep='',end='')
    sleep(0.1)