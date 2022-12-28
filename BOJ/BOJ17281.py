from itertools import permutations
import sys
input = sys.stdin.readline

n = int(input())
info = [list(map(int, input().split())) for _ in range(n)]

score = 0
for order in list(map(list, permutations(range(1, 9)))):
    order.insert(3, 0)
    tmp_score = 0
    b1, b2, b3 = 0, 0, 0
    inning = 0
    cnt_out = 0
    player = 0
    while inning < n :
        if info[inning][order[player]] == 0:
            cnt_out += 1
        elif info[inning][order[player]] == 1 : 
            tmp_score += b3
            b1, b2, b3 = 1, b1, b2
        elif info[inning][order[player]] == 2 : 
            tmp_score += b2 + b3
            b1, b2, b3 = 0, 1, b1
        elif info[inning][order[player]] == 3 : 
            tmp_score += b1, b2, b3
            b1, b2, b3 = 0, 0, 1
        elif info[inning][order[player]] == 4 : 
            tmp_score += b1 + b2 + b3 + 1
            b1, b2, b3 = 0, 0, 0

        player = (player + 1) % 9

        if cnt_out >= 3 :  # 3진 아웃
            inning += 1   # 3아웃이 나와야 다음 inning으로 감
            cnt_out = 0
            b1, b2, b3 = 0, 0, 0

    if tmp_score > score:
        score = tmp_score
print(score)