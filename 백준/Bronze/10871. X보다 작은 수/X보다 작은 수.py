N, X = map(int, input().split())
b_list = list(map(int, input().split()))

for i in range(N):
    if b_list[i] < X:
        print(b_list[i], end=' ')