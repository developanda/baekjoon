import sys

N = int(input())
num_lst = []

for i in range(N):
    tmp_num = int(sys.stdin.readline())
    num_lst.append(tmp_num)
    
num_lst.sort()

for j in (num_lst):
    print(j)