
# Bubble sort iterative and recursive solution

def bubbleIt(arr):
    if len(arr) == 0: return 0
    l = len(arr)
    for i in range(0,l):
        for j in range(i,l):
            if j<l and arr[i]>arr[j]:
                tmp = arr[j]
                arr[j] = arr[i]
                arr[i] = tmp
    
    return arr

lst = [5,6,8,2,3,-1,0]
print(bubbleIt(lst))