N, M = map(int, input().split())
n_lst = list(map(int, input().split()))

sum_m = 0
final_m = 0

for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            a = n_lst[i]
            b = n_lst[j]
            c = n_lst[k]
                
            sum_m = a + b + c
            if M < sum_m:
                pass
            elif (M-sum_m) < (M-final_m):
                final_m = sum_m
            else:
                pass
print(final_m)