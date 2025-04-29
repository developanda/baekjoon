temp = list(map(int, input().split()))
check_lst = [1, 1, 2, 2, 2, 8]

for n in range (6):
    result = check_lst[n] - temp[n]
    print(result, end=' ')