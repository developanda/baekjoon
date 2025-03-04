roof_cnt = int(input())

for i in range(roof_cnt):
    A, B = map(int, input().split())
    print("Case #"+ str(i+1)+ ":", A+B)