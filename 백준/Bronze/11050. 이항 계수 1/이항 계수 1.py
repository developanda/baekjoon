N, K = map(int, input().split())
a=1
b=1
c=1

for i in range(2,N+1):
    a = a*i

for j in range(2,K+1):
    b = b*j

for k in range(2,(N-K+1)):
    c = c*k
    
print(a//(b*c))