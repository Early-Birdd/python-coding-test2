#그래프 이론 3번

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

n , m = map(int, input().split())
parent = [0] * (n + 1)

for i in range(1, n + 1):
    parent[i] = i

ed = []

for _ in range(m):
    A, B, C = map(int, input().split())
    ed.append((C, A, B))

ed.sort()
result_cost = 0
max_ed_cost = 0

for i in ed:
    cost, a, b = i
    if find_parent(parent, a) != find_parent(parent, b):
        union(parent, a, b)
        result_cost += cost
        max_ed_cost = cost

print(result_cost - max_ed_cost)