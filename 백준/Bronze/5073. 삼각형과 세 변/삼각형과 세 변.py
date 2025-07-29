while True:
    a, b, c = map(int, input().split())
    if a==b==c==0:
        break
    elif (a+b<=c)|(b+c<=a)|(c+a<=b):
        print('Invalid')
    elif a==b==c:
        print('Equilateral')
    elif (a==b)|(b==c)|(a==c):
        print('Isosceles')
    else:
        print('Scalene')