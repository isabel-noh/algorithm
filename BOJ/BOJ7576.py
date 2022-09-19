
import sys
from collections import deque

sys.setrecursionlimit(1000000) #1000000번 재귀가 가능하도록 변경하기

# 보관 후 `하루`가 지나면, 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은 익은 토마토의 영향을 받아 익게 된다. 하나의 토마토의 인접한 곳은 왼쪽, 오른쪽, 앞, 뒤 네 방향에 있는 토마토를 의미한다. 
di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]  # 왼 아래 오른 위
# 철수는 창고에 보관된 토마토들이 며칠이 지나면 다 익게 되는지, 그 '최소 일수'를 알고 싶어 한다.
#  단, 상자의 일부 칸에는 토마토가 들어있지 않을 수도 있다.
# 1 - 익은 토마토, 0 안익은 토마토, -1 토마토 없음
M, N = map(int,input().split())
bat = [list(map(int, input().split())) for _ in range(N)]
queue = deque()
count = 0
for i in range(N):
    for j in range(M):
        if bat[i][j] == 1:
            queue.append((j,i))

def ripen(a, b):
    global count
    for d in range(4):
        if 0 <= a+di[d] <= N - 1 and 0 <= b+dj[d] <= M - 1:
            if bat[b+dj[d]][a+di[d]] == 0 :
                bat[b+dj[d]][a+di[d]] = 1
                # print(bat)
                count += 1
                ripen(a+di[d], b+dj[d])
# def ripen(tomato):
#     while tomato:
#         i, j = tomato.pop(0)
#         for d in range(4):
#             ni, nj = i+di[d], j+dj[d]
#             if 0 <= ni < N and 0 <= nj < M:
#                 if bat[ni][nj] == 0:
#                     tomato.append((ni, nj))
#                     bat[ni][nj] = bat[i][j] + 1
#                 elif bat[ni][nj] == -1:
#                     pass
for i in range(len(queue)):
    ripen(queue[i][0], queue[i][1])


max_ = []
for i in bat:
    a = max(i)
    max_.append(a)
# 모두 익어있으면 0 모두 익지 못하면 -1  
for i in bat:
    if 0 in i:
        count = -1
        break
if count == -1 :
    print(count)
else:
    print(max(max_)-1)

# ------------------------------
# import sys
# from collections import deque

# sys.setrecursionlimit(1000000) #1000000번 재귀가 가능하도록 변경하기

# queue = deque()

# di = [1, 0, -1, 0]
# dj = [0, 1, 0, -1] 
# M, N = map(int, input().split())
# bat = [list(map(int, input().split())) for _ in range(N)]

# count = 0
# for i in range(N):
#     for j in range(M):
#         if bat[i][j] == 1:
#             queue.append((j,i))

# def ripen(queue):
#     while queue:
#         i, j = queue.popleft()
#         for d in range(4):
#             ni, nj = i+di[d], j+dj[d]
#             if 0 <= ni < N and 0 <= nj < M:
#                 if bat[ni][nj] == 0:
#                     queue.append((ni, nj))
#                     bat[ni][nj] = bat[i][j] + 1
#                 elif bat[ni][nj] == -1:
#                     pass
# ripen(queue)

# max_ = []
# for i in bat:
#     a = max(i)
#     max_.append(a)
# # 모두 익어있으면 0 모두 익지 못하면 -1  
# for i in bat:
#     if 0 in i:
#         count = -1
#         break
# if count == -1 :
#     print(count)
# else:
#     print(max(max_)-1)