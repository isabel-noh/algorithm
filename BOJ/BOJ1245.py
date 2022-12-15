# BOJ 1245 농장 관리
# [BOJ 1245 농장 관리](https://www.acmicpc.net/problem/1245)

# 문제
# 농부 민식이가 관리하는 농장은 N×M 격자로 이루어져 있다. 민식이는 농장을 관리하기 위해 산봉우리마다 경비원를 배치하려 한다. 이를 위해 농장에 산봉우리가 총 몇 개 있는지를 세는 것이 문제다.
# 산봉우리의 정의는 다음과 같다. 산봉우리는 같은 높이를 가지는 하나의 격자 혹은 인접한 격자들의 집합으로 이루어져 있다. (여기서 "인접하다"의 정의는 X좌표 차이와 Y좌표 차이 모두 1 이하일 경우로 정의된다.) 또한 산봉우리와 인접한 격자는 모두 산봉우리의 높이보다 작아야한다.
# 문제는 격자 내에 산봉우리의 개수가 총 몇 개인지 구하는 것이다.

# 입력
# 첫째 줄에 정수 N(1 < N ≤ 100), M(1 < M ≤ 70)이 주어진다. 둘째 줄부터 N+1번째 줄까지 각 줄마다 격자의 높이를 의미하는 M개의 정수가 입력된다. 격자의 높이는 500보다 작거나 같은 음이 아닌 정수이다.

# 출력
# 첫째 줄에 산봉우리의 개수를 출력한다.
from collections import deque
import sys
sys.stdin = open('sample.txt')
input = sys.stdin.readline

N, M = map(int, input().split()) 
arr = []
for n in range(N):
    arr.append(list(map(int, input().split())))

bonguri = 0
delta = [(1, 0), (1, 1), (0, 1), (1, -1), (-1, 0), (-1, -1), (0, -1), (-1, 1)]
visited = [([0] * M) for _ in range(N)]

def bfs() : 
    global visited, q, bonguri
    flag = True  # 현재 위치가 봉우리가 될 수 있는지 여부 체크
    while q:
        i, j = q.popleft()
        visited[i][j] = 1 
        for di, dj in delta:
            ni, nj = i + di, j + dj

            if 0 <= ni < N and 0 <= nj < M :
                if arr[ni][nj] > arr[i][j] :  # 현재 위치 주변에 나보다 높은 곳이 있으면 봉우리 ㄴㄴ
                    flag = False
                    
                # 현재 위치 주변에 나랑 높이가 같고 visited한 적이 없으면 봉우리인지 확인해야해서 queue에 추가 (바로 위 if 문에서 False가 되었으면 아래 if문도 봉우리는 아니지만 visited처리해서 봉우리 아님을 기록할 수 있음)
                if arr[ni][nj] == arr[i][j] and visited[ni][nj] == 0:
                    q.append([ni, nj])
                
    # q 한 개가 끝나면 같은 높이 그 주변의 산맥은 확인한 것!
    # flag가 여전히 true이면 이것은 봉우리임! 
    if flag == True:
        bonguri += 1

for i in range(N):
    for j in range(M):
        if visited[i][j] == 0:  # 모든 위치에서 visited 안 한 경우에만 확인 (위의 bfs함수에서 각 위치와 높이가 같은 인접한 위치는 모두 확인하고 옴)
            q = deque()
            q.append([i, j])
            bfs()

print(bonguri)