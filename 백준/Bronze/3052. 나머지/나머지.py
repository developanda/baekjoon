B_lst = []

for i in range(10):
    A = int(input())
    B = A%42
    
    B_lst.append(B)

print(len(set(B_lst)))