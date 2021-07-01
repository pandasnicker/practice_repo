# Print the content from a file.
# Code also changes the current working directory by using the self defined module changecwd.

import changecwd as cwd

cwd.changedir(r'C:\Users\mgula\Desktop')

currDir = cwd.cwd()
print('The current working directory is : ', currDir)

fullPath = currDir + r'\Queries.txt'

print(fullPath)

try:
    with open(fullPath,'r') as f:
        for content in f:
            print(content, end='')
        f.close()

except Exception:
    print('Exception occurred : ',repr(Exception))

