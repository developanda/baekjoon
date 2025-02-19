A, B, C = map(int, input().split())

dice_lst = [A, B, C]

if (A==B)&(B==C):
    print(10000+(A*1000))
elif (A==B)&(B!=C):
    print(1000+(A*100))
elif (B==C)&(A!=C):
    print(1000+(B*100))
elif (A==C)&(A!=B):
    print(1000+(C*100))
else:
    print(max(dice_lst)*100)
