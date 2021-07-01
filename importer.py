import os
from stat import *

import unixfileperm as t

f = str(input("Enter the path: "))

if os.path.isfile(f):
    permissions = oct(os.stat(f)[ST_MODE])[-3:]
    print(os.path.basename(f), " ",t.printUnixStylePerms(permissions))

if os.path.isdir(f):
    if os.listdir(f) != []:
        print('The path is a directory. Files are as follows: ')
        for fname in os.listdir(f):
            permissions = oct(os.stat(f)[ST_MODE])[-3:]
            print("{0:40s} -> {1} {2} ".format(os.path.basename(fname), ("file","dir")[os.path.isdir(fname)], t.printUnixStylePerms(permissions)))
    else:
        print("The directory is empty")