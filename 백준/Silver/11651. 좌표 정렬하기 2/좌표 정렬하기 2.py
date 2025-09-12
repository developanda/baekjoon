N = int(input())
n_lst = []

for i in range(N):
    x, y = map(int, input().split())
    n_lst.append([y, x])

n_lst.sort()

for j in n_lst:
    print(j[1], j[0])