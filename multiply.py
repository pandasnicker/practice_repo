
def mul(a,b):
    if b==0: return 0
    mx = max(a,b)
    mn = min(a,b)
    if mn%2==0:
        mx = mx<<1
        mn = mn>>1
    print(mn,mx)
    return mx+mul(mx, mn-1)

print(mul(250,55))