total_price = int(input())
merchan = int(input())
sum_price = 0

for _ in range(merchan):
    price, cnt = map(int, input().split())
    sum_price = sum_price + (price*cnt)

if total_price == sum_price:
    print('Yes')
else:
    print('No')