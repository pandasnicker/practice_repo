
MIN = 1
MAX = 3

for i in range(MIN,MAX+1,1):
    for j in range(1,11):
        print(f'{i:2d} x {j:2d} = {i*j}',end=' | ')
    print()
    print('-'*150)
