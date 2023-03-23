# BOJ 2206 벽 부수고 이동하기
# #![BOJ 2206 벽 부수고 이동하기](https://www.acmicpc.net/problem/2206)

# 문제
# N×M의 행렬로 표현되는 맵이 있다. 맵에서 0은 이동할 수 있는 곳을 나타내고, 1은 이동할 수 없는 벽이 있는 곳을 나타낸다. 당신은 (1, 1)에서 (N, M)의 위치까지 이동하려 하는데, 이때 최단 경로로 이동하려 한다. 최단경로는 맵에서 가장 적은 개수의 칸을 지나는 경로를 말하는데, 이때 시작하는 칸과 끝나는 칸도 포함해서 센다.
# 만약에 이동하는 도중에 한 개의 벽을 부수고 이동하는 것이 좀 더 경로가 짧아진다면, 벽을 한 개 까지 부수고 이동하여도 된다.
# 한 칸에서 이동할 수 있는 칸은 상하좌우로 인접한 칸이다.
# 맵이 주어졌을 때, 최단 경로를 구해 내는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N(1 ≤ N ≤ 1,000), M(1 ≤ M ≤ 1,000)이 주어진다. 다음 N개의 줄에 M개의 숫자로 맵이 주어진다. (1, 1)과 (N, M)은 항상 0이라고 가정하자.

# 출력
# 첫째 줄에 최단 거리를 출력한다. 불가능할 때는 -1을 출력한다.
from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, list(input()))) for _ in range(n)]
dis = 0
magic = 1
def bfs():
    queue = deque()
    visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
    queue.append(( 0, 0, dis, magic ))
    visited[0][0][magic] = 1
    while queue : 
        i, j, d, c = queue.popleft()
        if i == n-1 and j == m-1: # 먼저 도착하면 끝
            return d
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < m and visited[ni][nj][c] == 0 : 
                visited[ni][nj][c] = 1
                if arr[ni][nj] == 1 and c == 1 :  # 벽인데 벽을 뚫을 수 있는 경우 
                    queue.append(( ni, nj, d + 1, c - 1))
                if arr[ni][nj] == 0: # 벽이 아닌 경우 
                    queue.append(( ni, nj, d + 1, c))
    return -1

result = bfs()
if(result == -1):
        print(result)
else: 
     print(result + 1)