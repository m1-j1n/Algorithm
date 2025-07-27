# 1238. 파티~~
import heapq

# N: 노드의 수, M: 간선의 수, X: 목적 노드
N, M, X = map(int, input().split())

graph = [[] for _ in range(N+1)]
reversed_graph = [[] for _ in range(N+1)]

for _ in range(M):
    s, e, t = map(int, input().split())
    graph[s].append([e, t])
    reversed_graph[e].append([s, t])

def dikstra(graph):
    dist = [float('inf')] * (N + 1)
    q = []

    start_node = X
    dist[start_node] = 0
    heapq.heappush(q, (0, start_node))

    while q:
        curr_time, curr_node = heapq.heappop(q)

        for next_node, next_time in graph[curr_node]:
            if dist[next_node] > curr_time + next_time:
                dist[next_node] = curr_time + next_time
                heapq.heappush(q, (curr_time + next_time, next_node))

    return dist

# 1. 그럼 일단 각 노드에서 X까지 도착하는 최단 거리 찾기
go_party = dikstra(reversed_graph)
go_home = dikstra(graph)

# 3. 그 다음에 두 리스트 합쳐서 제일 큰 값 출력
ans = []

for i in range(1,N+1):
    ans.append(go_party[i] + go_home[i])

print(max(ans))