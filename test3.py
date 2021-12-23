#이진탐색 3번

n, m = map(int, input().split())
data = list(map(int, input().split()))

height = 0

for i in range(0, max(data) + 1):
    result = 0
    for j in range(n):
        if data[j] > i:
          result += (data[j] - i)
        else:
            result += 0

    if result == m:
        height = max(height, i)

print(height)