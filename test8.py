#다이나믹 프로그래밍 5번

n, m = map(int, input().split())
money = []

for i in range(n):
    money.append(int(input()))

d = [10001] * (m + 1)
d[0] = 0

for i in range(n):
    for j in range(money[i], m + 1):
        d[j] = min(d[j], d[j - money[i]] + 1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])
