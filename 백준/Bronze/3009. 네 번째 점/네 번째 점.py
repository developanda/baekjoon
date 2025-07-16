a, b = map(int, input().split())
c, d = map(int, input().split())
e, f = map(int, input().split())

if a == e:
    if b == d:
        print(c, f)
    elif b == f:
        print(c, d)
    else: 
        print(c, b)
elif a == c:
    if b == d:
        print(e, f)
    elif b == f:
        print(e, d)
    else: 
        print(e, b)
else:
    if b == d:
        print(a, f)
    elif b == f:
        print(a, d)
    else: 
        print(a, b)  