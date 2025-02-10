A = int(input())

a = A%4
b = A%100
c = A%400

if (a == 0)&(b!=0):
    print(1)
elif (b==0)&(c!=0):
    print(0)
elif (c==0):
    print(1)
else:
    print(0)