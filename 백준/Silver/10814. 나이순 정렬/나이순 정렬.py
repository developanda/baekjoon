N = int(input())
n_lst = []

for i in range(N):
    x, y = map(str, input().split())
    n_lst.append([int(x), y])
    
n_lst.sort(key=lambda m: m[0])

for j in n_lst:
    print(j[0], j[1])