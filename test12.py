#그래프 이론 1-1(서로소 집합 알고리즘)

# def find_parent(parent, i):
#     if parent[i] != i:
#         return find_parent(parent, parent[i])
#     return i

#경로 압축 ver
# def find_parent(parent, i):
#     if parent[i] != i:
#         parent[i] = find_parent(parent, parent[i])
#     return parent[i]
#
# def union(parent, a, b):
#     a = find_parent(parent, a)
#     b = find_parent(parent, b)
#     if a < b:
#         parent[b] = a
#     else:
#         parent[a] = b
#
# v, e = map(int, input().split())
# parent = [0] * (v + 1)
#
# for i in range(1, v + 1):
#     parent[i] = i
#
# for i in range(e):
#     a, b = map(int, input().split())
#     union(parent, a, b)
#
# print('각 원소 집합: ', end = '')
# for i in range(1, v + 1):
#     print(find_parent(parent, i), end = ' ')
#
# print()
#
# print('부모 테이블: ', end = '')
# for i in range(1, v + 1):
#     print(parent[i], end = ' ')

#그래프 이론 1-2(서로소 집합 사이클)

# def find_parent(parent, i):
#     if parent[i] != i:
#         parent[i] = find_parent(parent, parent[i])
#     return parent[i]
#
# def union(parent, a, b):
#     a = find_parent(parent, a)
#     b = find_parent(parent, b)
#     if a < b:
#         parent[b] = a
#     else:
#         parent[a] = b
#
# v, e = map(int, input().split())
# parent = [0] * (v + 1)
#
# for i in range(1, v + 1):
#     parent[i] = i
#
# cycle = False
#
# for i in range(e):
#     a, b = map(int, input().split())
#     if find_parent(parent, a) == find_parent(parent, b):
#         cycle = True
#         break
#     else:
#         union(parent, a, b)
#
# if cycle == True:
#     print('사이클 발생')
# else:
#     print('사이클 발생 X')

#그래프 이론 1-3(신장 트리-크루스칼 알고리즘)

# def find_parent(parent, i):
#     if parent[i] != i:
#         parent[i] = find_parent(parent, parent[i])
#     return parent[i]
#
# def union_parent(parent, a, b):
#     a = find_parent(parent, a)
#     b = find_parent(parent, b)
#     if a < b:
#         parent[b] = a
#     else:
#         parent[a] = b
#
# v, e = map(int, input().split())
# parent = [0] * (v + 1)
#
# ed = []
# result_cost = 0
#
# for i in range(1, v + 1):
#     parent[i] = i
#
# for _ in range(e):
#     a, b, cost = map(int, input().split())
#     ed.append((cost, a, b))
#
# #cost 기준으로 정렬
# ed.sort()
#
# for i in ed:
#     cost, a, b = i
#     if find_parent(parent, a) != find_parent(parent, b):
#         union_parent(parent, a, b)
#         result_cost += cost
#
# print(result_cost)

#그래프 이론 1-4(위상 정렬 알고리즘)

from collections import deque

v, e = map(int, input().split())
enter = [0] * (v + 1)
graph = [[] for i in range(v + 1)]

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    enter[b] += 1

def topology_sort():
    result = []
    q = deque()
    for i in range(1, v + 1):
        if enter[i] == 0:
            q.append(i)
    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            enter[i] -= 1
            if enter[i] == 0:
                q.append(i)

    for i in result:
        print(i, end = ' ')

topology_sort()