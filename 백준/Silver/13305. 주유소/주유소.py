n = int(input())
road = list(map(int, input().split()))
oil_price = list(map(int, input().split()))
cost = oil_price[0]
payment = 0

for i in range(n-1):
    if cost >= oil_price[i]:
        cost = oil_price[i]
    payment += cost * road[i]
    
print(payment)