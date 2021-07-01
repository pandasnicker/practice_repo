
def longestsubstr(s):
    lst = []
    mlst = []
    cnt = 0
    for i in range(len(s)):
        if lst.count(s[i]) == 0:
            lst.append(s[i])
            cnt += 1
        else:
            mlst.append(cnt)
            lst.clear()
            if len(mlst) != 0 and i == len(s):
                i = len(mlst)-1
            else:
                i = 0
        print(lst)
    return max(mlst)

print(longestsubstr("Gulam"))