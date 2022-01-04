#그래프 이론 2번

def find_parent(parent, i):
    if parent[i] != i:
        parent[i] = find_parent(parent, parent[i])
    return parent[i]

def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
parent = [0] * (n + 1)

for i in range(n + 1):
    parent[i] = i

for _ in range(m):
    test, a, b = map(int, input().split())
    if test == 0:
        union(parent, a, b)
    elif test == 1:
        if find_parent(parent, a) == find_parent(parent, b):
            print('YES')
        else:
            print('NO')
