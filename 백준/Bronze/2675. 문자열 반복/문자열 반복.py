cnt = int(input())

for i in range(cnt):
    A, B = map(str, input().split())
    A = int(A)
    B = list(B)
    
    for j in range(len(B)):
        print(B[j]*A, end='')
    print('')