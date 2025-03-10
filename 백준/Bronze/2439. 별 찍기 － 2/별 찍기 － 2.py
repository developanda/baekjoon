A = int(input())

for i in range(A):
    B = A-i-1
    blank = ' '
    star = '*'
    PS = str(blank)*B + str(star)*(i+1)
    print(PS)