import sys 
sys.stdin = open('sample.txt')

N = int(input())
seats = [([0] * N) for _ in range(N)]

delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def condition3(s, a):
    global seats
    i, j = a[0][0], a[0][1]
    # a.sort(key=lambda x:(x[0], x[1]))
    # for i, j in a:
    #     if seats[i][j] == 0:
    seats[i][j] = s
    #        break
    #     else:
    #         continue

def condition2(s, seat):
    global seats
    # print(seat)
    vacancy = [([0]*N) for _ in range(N)]
    max_vacancy = 0
    for i, j in seat:
        vacant = 0
        for di, dj in delta:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N and seats[ni][nj] == 0:
                vacancy[i][j] += 1
                vacant += 1
            if vacant > max_vacancy:
                max_vacancy = vacant
            
    new_seats=[]
    for i in range(N):
        for j in range(N):
            if vacancy[i][j] == max_vacancy and (i,j) in seat:
                new_seats.append((i, j))
    # print('new_seats', new_seats)
    # print(seats)
    # print(vacancy)
    if len(new_seats) == 1: 
        i = new_seats[0][0]
        j = new_seats[0][1]
        if seats[i][j] == 0:
            seats[i][j] = s
            return
    else:
        condition3(s, new_seats)

def condition1(s, arr):  # arr 은 친구 잇는지 
    global seats
    frnds_cnt = [([0]*N) for _ in range(N)]  # 각 자리에 들어갔을 때 친구가 몇 명이 주변에 있는지를 보여주는 arr
    max_frnds = 0
    for i in range(N):
        for j in range(N):
            if seats[i][j] == 0: # 비어있는 칸 중에서 
                cnt = 0
                for di, dj in delta:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < N and 0 <= nj < N and seats[ni][nj] in arr: 
                        cnt += 1
                frnds_cnt[i][j] = cnt # 각 자리에 친구가 몇명있는지 
                if max_frnds < cnt:
                    max_frnds = cnt # 최대 친구 

    seat = []
    
    for i in range(N):
        for j in range(N):
            if frnds_cnt[i][j] == max_frnds: # 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 
                seat.append((i, j))
    # print(seat)
    if len(seat) == 1:
        i = seat[0][0]
        j = seat[0][1]
        if seats[i][j] == 0:
            seats[i][j] = s
            return
    else:
        condition2(s, seat) # 학생 번호, 앉을 수 있는 좌석 list
total = []
for m in range(N*N):
    likey = list(map(int, input().split()))
    total.append(likey)
    # print(likey)
    student = likey.pop(0)

    condition1(student, likey)
    likey.append(student)

# likey = [(list(map(int, input().split()))) for _ in range(N**2)]

# 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.
# 1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
# 2를 만족하는 칸도 여러 개인 경우에는 행의 번호가 가장 작은 칸으로, 그러한 칸도 여러 개이면 열의 번호가 가장 작은 칸으로 자리를 정한다.

def check_satisfaction(aa, like):
    score = 0
    for i in like:
        student = i.pop() # 학생
        count = 0
        for k in range(N): # 각 자리
            for j in range(N):
                if aa[k][j] == student: #해당 자리가 나오면 
                    for di, dj in delta: 
                        ni, nj = k + di, j + dj
                        if 0 <= ni < N and 0 <= nj < N and aa[ni][nj] in i:
                            count += 1
        if count == 1:
            score += 1
        elif count == 2:
            score += 10
        elif count == 3:
            score += 100
        elif count == 4:
            score += 1000
        else:
            pass

    return score
# print(seats)

# 이제 학생의 만족도를 구해야 한다. 학생의 만족도는 자리 배치가 모두 끝난 후에 구할 수 있다. 학생의 만족도를 구하려면 그 학생과 인접한 칸에 앉은 좋아하는 학생의 수를 구해야 한다. 그 값이 0이면 학생의 만족도는 0, 1이면 1, 2이면 10, 3이면 100, 4이면 1000이다.
# print(seats)
sc = check_satisfaction(seats, total)
# 학생의 만족도의 총 합을 구해보자.
print(sc)