N = int(input())

if N==0:
    print(1)
else:
    a = 1
    for i in range(2, N+1):
        a = a*i
    print(a)