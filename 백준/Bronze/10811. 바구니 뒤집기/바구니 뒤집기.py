N, M = map(int, input().split())
b_lst = [i for i in range(1, N+1)]

for k in range(M):
    i, j = map(int, input().split())
    temp = b_lst[i-1:j]
    temp.reverse()
    b_lst[i-1:j] = temp

for l in range(N):
    print(b_lst[l], end=' ')