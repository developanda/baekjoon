N, M = map(int, input().split())
N_list = []

for i in range(1,N+1):
    N_list.append(i)
    
for k in range(M):
    A, B = map(int, input().split())
    N_list[B-1], N_list[A-1] = N_list[A-1], N_list[B-1]
    
for i in range(N):
    print(N_list[i], end=' ')