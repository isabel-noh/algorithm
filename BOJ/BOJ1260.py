# 문제
# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

# 입력
# 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

# 출력
# 첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.

# import sys
# sys.stdin = open('sample.txt')

import sys 
sys.stdin = open('sample.txt')

N, M, v = map(int, input().split())
arr = [[] for _ in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    # 간선은 양방향
    arr[a].append(b)
    arr[b].append(a)
    arr[a].sort()
    arr[b].sort()

visit_seq = []
visited = [0] * (N+1)
def dfs(a, v):
     # [[], [2, 3], [1, 5], [1, 4], [3, 5], [2, 4]]
    visited[v] = 1 # 1번 방문
    visit_seq.append(v)
    for i in arr[v]: # 2,3,4
        if visited[i] == 0:
            dfs(arr, i)
    return visit_seq

def bfs(a, v):
    visited = [0] * (N+1)
    visited[v] = 1
    return
print(dfs(arr, v))
print(arr)