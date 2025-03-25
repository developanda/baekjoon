check_lst = []
for i in range(1,31):
    check_lst.append(i)
    
for j in range(28):
    A = int(input())
    check_lst.remove(A)
    
print(min(check_lst))
print(max(check_lst))