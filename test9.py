#최단경로 1-1(다익스트라)

# import sys
# input = sys.stdin.readline
# INF = int(1e9)
#
# n, m = map(int, input().split())
# start = int(input())
# graph = [[] for i in range(n + 1)]
# visited = [False] * (n + 1)
# distance = [INF] * (n + 1)
#
# for _ in range(m):
#     a, b, c = map(int, input().split())
#     graph[a].append((b, c))
#
# def dstra(start):
#     distance[start] = 0
#     visited[start] = True
#     for i in graph[start]:
#         distance[i[0]] = i[1]
#     for j in range(n - 1):
#         now = get_smallest_node()
#         visited[now] = True
#         for k in graph[now]:
#             cost = distance[now] + k[1]
#             if cost < distance[k[0]]:
#                 distance[k[0]] = cost
#
# def get_smallest_node():
#     min_v = INF
#     index = 0
#     for i in range(1, n + 1):
#         if distance[i] < min_v and visited[i] == False:
#             min_v = distance[i]
#             index = i
#     return index
#
# dstra(start)
#
# for i in range(1, n + 1):
#     if distance[i] == INF:
#         print("INFI")
#     else:
#         print(distance[i])

#최단경로 1-2(다익스트라-heapq)

# import heapq
# import sys
# input = sys.stdin.readline
# INF = int(1e9)
#
# n, m = map(int, input().split())
# start = int(input())
# graph = [[] for i in range(n + 1)]
# distance = [INF] * (n + 1)
#
# for _ in range(m):
#     a, b, c = map(int, input().split())
#     graph[a].append((b, c))
#
# def dstra(start):
#     q = []
#     #heappush(리스트, (거리, 노드)) 거리 짧은 순으로 pop
#     heapq.heappush(q, (0, start))
#     distance[start] = 0
#     while q:
#         dist, now = heapq.heappop(q)
#         #방문한 노드라면 무시
#         if distance[now] < dist:
#             continue
#         for i in graph[now]:
#             cost = dist + i[1]
#             if cost < distance[i[0]]:
#                 distance[i[0]] = cost
#                 heapq.heappush(q, (cost, i[0]))
#
# dstra(start)
#
# for i in range(1, n + 1):
#     if distance[i] == INF:
#         print("INFI")
#     else:
#         print(distance[i])

#최단경로 1-3(플로이드 워셜)

INF = int(1e9)

n = int(input())
m = int(input())
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

for i in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][i] + graph[i][b])

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if graph[a][b] == INF:
            print("INFI", end = " ")
        else:
            print(graph[a][b], end = " ")
    print()
