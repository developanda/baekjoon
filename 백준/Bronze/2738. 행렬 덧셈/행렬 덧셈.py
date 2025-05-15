n1, n2 = map(int, input().split())
A = []
B = []

for i in range(n1):
    temp = list(map(int , input().split()))
    A.append(temp)
    
for j in range(n1):
    temp = list(map(int , input().split()))
    B.append(temp)
    
for row in range(n1):
    for col in range(n2):
        print(A[row][col] + B[row][col], end=' ')
    print()