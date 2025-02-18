H, M = map(int,input().split())
Set = int(input())

Set_H = Set//60
Set_M = Set%60

R_H = H + Set_H
R_M = M + Set_M

if R_M >= 60:
    R_M = R_M - 60
    R_H = R_H + 1
    
if R_H >= 24:
    R_H = R_H - 24
    
print(R_H, R_M)
