# Print the 2nd highest number in the integer list.

if __name__ == '__main__':
    n = int(input('Enter number of items: '))
    arr = list(map(int, input().strip().split()))[:n]
    
    print(arr)
    arr = list(sorted(arr))
    print(arr)
    max,runnerup = arr[-1],0
    for i in range(n-1,-1,-1):
        if arr[i]<max:
            runnerup = arr[i]
            break
    print(runnerup)