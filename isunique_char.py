
def isuniq(st):
    for i in range(len(st)):
        if i < len(st) and st[i] in st[i+1:]:
            return False

    return True

print(isuniq('abcdefghi'))