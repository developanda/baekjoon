R = int(input())

for i in range(1, R+1):
    A, B = map(int, input().split())
    C = A+B
    print( "Case #" + str(i) + ":", A, "+", B, "=",C )