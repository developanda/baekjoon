A_list = []

for i in range(9):
    a = int(input())
    A_list.append(a)
    
print(max(A_list))
print(A_list.index(max(A_list))+1)