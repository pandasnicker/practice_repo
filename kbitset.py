def kbit(n,k):
    r = 1<<k
    print(f'{n:032b}')

    print(f'{r:032b}')
    return n&r>=1

print(kbit(39,5))