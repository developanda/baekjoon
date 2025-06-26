N, K = map(int, input().split())
fac_list = []

for i in range(1,N+1):
    if N%i == 0:
        fac_list.append(i)
    else:
        pass

if len(fac_list) >= K:
    print(fac_list[K-1])
else:
    print(0)