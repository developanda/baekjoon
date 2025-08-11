n = int(input())

for i in range(n):
    N, M = map(int, input().split())
    if N==1:
        print(M)
    elif N==M:
        print(1)
    else:
        O = M-N
        a=1
        b=1
        c=1
        for j in range(1,N+1):
            a = a*j
        for k in range(1,O+1):
            b = b*k
        for l in range(1,M+1):
            c = c*l
        print(c//(b*a))