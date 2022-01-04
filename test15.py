#그래프 이론 4번

from collections import deque
import copy

n = int(input())
enter = [0] * (n + 1)
graph = [[] for i in range(n + 1)]
time = [0] * (n + 1)

#i는 해당 과목
for i in range(1, n + 1):
    data = list(map(int, input().split()))
    time[i] = data[0]
    #x는 선수 과목
    #ex) 2과목이나 3과목을 들으려면 1과목을 선수 해야함 -> graph[1] = [2, 3]
    for x in data[1 : -1]:
        enter[i] += 1
        graph[x].append(i)

def topology_sort():
    #time 리스트 복사
    result_time = copy.deepcopy(time)
    q = deque()

    for i in range(1, n + 1):
        if enter[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        #now는 선수 과목, i는 상위 과목
        for i in graph[now]:
            result_time[i] = max(result_time[i], result_time[now] + time[i])
            enter[i] -= 1
            if enter[i] == 0:
                q.append(i)

    for i in range(1, n + 1):
        print(result_time[i])

topology_sort()