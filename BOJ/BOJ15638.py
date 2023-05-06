# BOJ 15638 감시
# [BOJ 15638 감시](https://www.acmicpc.net/problem/15683)
# 문제
# 스타트링크의 사무실은 1×1크기의 정사각형으로 나누어져 있는 N×M 크기의 직사각형으로 나타낼 수 있다. 사무실에는 총 K개의 CCTV가 설치되어져 있는데, CCTV는 5가지 종류가 있다. 각 CCTV가 감시할 수 있는 방법은 다음과 같다.

# 1번 CCTV는 한 쪽 방향만 감시할 수 있다. 2번과 3번은 두 방향을 감시할 수 있는데, 2번은 감시하는 방향이 서로 반대방향이어야 하고, 3번은 직각 방향이어야 한다. 4번은 세 방향, 5번은 네 방향을 감시할 수 있다.

# CCTV는 감시할 수 있는 방향에 있는 칸 전체를 감시할 수 있다. 사무실에는 벽이 있는데, CCTV는 벽을 통과할 수 없다. CCTV가 감시할 수 없는 영역은 사각지대라고 한다.

# CCTV는 회전시킬 수 있는데, 회전은 항상 90도 방향으로 해야 하며, 감시하려고 하는 방향이 가로 또는 세로 방향이어야 한다.

# 지도에서 0은 빈 칸, 6은 벽, 1~5는 CCTV의 번호이다. 위의 예시에서 1번의 방향에 따라 감시할 수 있는 영역을 '#'로 나타내면 아래와 같다.

# CCTV는 벽을 통과할 수 없기 때문에, 1번이 → 방향을 감시하고 있을 때는 6의 오른쪽에 있는 칸을 감시할 수 없다.

# 위의 예시에서 감시할 수 있는 방향을 알아보면 아래와 같다.

# CCTV는 CCTV를 통과할 수 있다. 아래 예시를 보자.
# 위와 같은 경우에 2의 방향이 ↕ 3의 방향이 ←와 ↓인 경우 감시받는 영역은 다음과 같다.

# 사무실의 크기와 상태, 그리고 CCTV의 정보가 주어졌을 때, CCTV의 방향을 적절히 정해서, 사각 지대의 최소 크기를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 사무실의 세로 크기 N과 가로 크기 M이 주어진다. (1 ≤ N, M ≤ 8)

# 둘째 줄부터 N개의 줄에는 사무실 각 칸의 정보가 주어진다. 0은 빈 칸, 6은 벽, 1~5는 CCTV를 나타내고, 문제에서 설명한 CCTV의 종류이다. 

# CCTV의 최대 개수는 8개를 넘지 않는다.

# 출력
# 첫째 줄에 사각 지대의 최소 크기를 출력한다.

# 20
from copy import deepcopy
import sys
sys.stdin = open('sample.txt')

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
result = N * M

dt = [(0, 1), (1, 0), (0, -1), (-1, 0)] 
cctv = [[[0], [1], [2], [3]], 
        [[0, 2], [1, 3]], 
        [[0, 1], [0, 3], [1, 2], [2, 3]], 
        [[0, 1, 2], [1, 2, 3], [0, 2, 3], [0, 1, 3]], 
        [[0, 1, 2, 3]]
    ]

for i in range(N):
    for j in range(M):
        if arr[i][j] == 6:  # 사각지대에 벽은 포함되지 않음
            result -= 1

def check(i, j, dir, temp):
    for d in dir:
        ni, nj = i, j
        while True : 
            ni, nj = ni + dt[d][0], nj + dt[d][1]
            if 0 <= ni < N and 0 <= nj < M and temp[ni][nj] != 6:
                if temp[ni][nj] == 0: # 감시가능
                    temp[ni][nj] = -1
            else:
                break            


def dfs(idx, arr):
    global result
    t = deepcopy(arr) # 왜 deepcopy?
    
    if idx == len(temp):  # 왜 for문 안쓰고 ? 
        count = 0
        for i in t:
            count += i.count(0)  # 사각지대 수
        if result > count :
            result = count
        return 
    
    a, b, c = temp[idx]
    for i in cctv[c-1]:
        check(a, b, i, t)
        dfs(idx + 1, t)
        t = deepcopy(arr)

temp = []
for i in range(N):
    for j in range(M):
        if arr[i][j] in [1, 2, 3, 4, 5]:
            temp.append((i, j, arr[i][j]))


dfs(0, arr) # 시작 인덱스
print(result)