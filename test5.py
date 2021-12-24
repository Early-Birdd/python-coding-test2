#다이나믹 프로그래밍 2번

n = int(input())

def make_one(n):
    count = 0
    while n > 1:
        if (n % 5) == 0:
            n /= 5
            count += 1
            continue
        if (n % 3) == 0:
            n /= 3
            count += 1
            continue
        if (n % 2) == 0:
            n /= 2
            count += 1
            continue
        n -= 1
        count += 1
    return count

print(make_one(n))