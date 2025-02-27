A = int(input())
cnt = A//4 
answer = 'int'

for _ in range(cnt):
    answer = 'long ' + answer

print(answer)