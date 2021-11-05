# find the one odd element out from the given array [1..n+1]. Every number occurs exactly once. Find the missing number.

def oddone(arr):
    res = 0
    for i in range(max(arr)+1):
        res=res^i
    print(res)
    res1 = 0
    for i in arr:
        res1 = res1^i
    print(res1)
    return res^res1

print(oddone([1,4,5,2,3,7]))