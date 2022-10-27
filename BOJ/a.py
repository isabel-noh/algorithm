import sys
sys.stdin = open('sample.txt')
M, N = map(int, input().split())
# 3이상 16이하
for i in range(M, N+1):
    if i == 1:
        continue
#     for j in range(2, i):       # 시간초과
    for j in range(2, int(i**0.5)+1):
        print(i, j)
        if i % j == 0:
            break
    else:
        print(i)