N = int(input())
n_lst = list(map(int, input().split()))

max_val = max(n_lst)

sum_val = 0

for i in range(N):
    sum_val = sum_val + n_lst[i]/max_val*100
    
print(sum_val/N)
