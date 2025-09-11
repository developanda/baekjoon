N = int(input())
n_lst = []

for i in range(N):
    x, y = map(int, input().split())
    n_lst.append([x, y])
    
n_lst.sort()
for j in n_lst:
    print(j[0], j[1])