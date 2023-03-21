### BOJ 14923 미로 탈출
# ![BOJ 14923 미로 탈출](https://www.acmicpc.net/problem/14923)

### 문제
# 홍익이는 사악한 마법사의 꾐에 속아 N x M 미로 (Hx, Hy) 위치에 떨어졌다. 다행히도 홍익이는 마법사가 만든 미로의 탈출 위치(Ex, Ey)를 알고 있다. 하지만 미로에는 곳곳에 마법사가 설치한 벽이 있어 홍익이가 탈출하기 어렵게 하고 있다.
# 홍익이는 마법사의 연구실에서 훔친 지팡이가 있어, 벽을 길로 만들 수 있다. 그렇지만, 안타깝게도 마법의 지팡이는 단 한 번만 사용할 수 있다.
# 이때, 홍익이를 도와 미로에서 탈출할 수 있는지 알아보고, 할 수 있다면 가장 빠른 경로의 거리 D는 얼마인지 알아보자.
# 인접한 칸으로 이동하는데 똑같은 시간이 들고, 벽을 부수는 데 시간이 걸리지 않는다.

### 입력
# N M
# Hx Hy
# Ex Ey
# N X M 행렬
# 2 ≤ N ≤ 1000, 2 ≤ M ≤ 1000
# 1 ≤ Hx, Hy, Ex, Ey ≤ 1000
# (Hx, Hy) ≠ (Ex, Ey)
# 행렬은 0과 1로만 이루어져 있고, 0이 빈 칸, 1이 벽이다.

### 출력
# D (탈출 할 수 없다면, -1을 출력한다.)

### 힌트
# 제일 왼쪽 위 위치에서 제일 오른쪽 아래 위치로 이동하려면 (3,2) 벽을 파괴하고 이동하면 된다.
from collections import deque
from pprint import pprint
import sys
sys.stdin = open('sample.txt')

N, M = map(int, input().split())
Hx, Hy = map(int, input().split())  # 내 위치
Ex, Ey = map(int, input().split())  # 탈출 위치
arr = [list(map(int, input().split())) for _ in range(N)]
arr[Hx-1][Hy-1] = -1
arr[Ex-1][Ey-1] = 2
print(Hx, Hy)
print(Ex, Ey)
pprint(arr)

def bfs():
    queue = deque()
    queue.append((Hx, Hy))
    while queue:
        i, j = queue.popleft()
        for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0:
                visited[ni][nj] = 1
                queue.append((ni, nj))
            if ni == Ex and nj == Ey:
                return 

cnt = 0
visited = [[0] * M for _ in range(N)]
bfs()