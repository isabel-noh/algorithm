# BOJ 1074 Z
# [BOJ 1074 Z](https://www.acmicpc.net/problem/1074)

# 문제
# 한수는 크기가 2N × 2N인 2차원 배열을 Z모양으로 탐색하려고 한다. 예를 들어, 2×2배열을 왼쪽 위칸, 오른쪽 위칸, 왼쪽 아래칸, 오른쪽 아래칸 순서대로 방문하면 Z모양이다.
# N > 1인 경우, 배열을 크기가 2N-1 × 2N-1로 4등분 한 후에 재귀적으로 순서대로 방문한다.
# 다음 예는 22 × 22 크기의 배열을 방문한 순서이다.
# N이 주어졌을 때, r행 c열을 몇 번째로 방문하는지 출력하는 프로그램을 작성하시오.
# 다음은 N=3일 때의 예이다.

# 입력
# 첫째 줄에 정수 N, r, c가 주어진다.

# 출력
# r행 c열을 몇 번째로 방문했는지 출력한다.

# 제한
# 1 ≤ N ≤ 15
# 0 ≤ r, c < 2N
import sys
sys.setrecursionlimit(1000000)
# sys.stdin = open('sample.txt')

n, c, r = map(int, input().split())
count = 0
m = 2 ** n
# def z(start_x, start_y, end_x, end_y, n):
#     global count
#     if (r == start_x and c == start_y):
#         return
    
#     if r >= ((end_x+1-start_x)//2) and c >= ((end_y+1-start_y)//2):
#         count += (n*n//4*3)
#         z(start_x+((end_x+1-start_x)//2), start_y+((end_y+1-start_y)//2), start_x+((end_x+1-start_x)//2)+n//2-1, start_y+((end_y+1-start_y)//2)+n//2-1, n//2)
#     elif r < ((end_x+1-start_x)//2) and c >= ((end_y+1-start_y)//2):
#         count += (n*n//4*2)
#         z(start_x, start_y+((end_y+1-start_y)//2), start_x+(n//2)-1, start_y+((end_y+1-start_y)//2)+(n//2)-1, n//2)
#     elif r >= ((end_x+1-start_x)//2) and c < ((end_y+1-start_y)//2):
#         count += (n*n//4*1)
#         z(start_x+((end_x+1-start_x)//2), start_y, start_x+((end_x+1-start_x)//2)+n//2-1, start_y+n//2-1, n//2) 
#     else:
#         z(start_x, start_y, start_x+(n//2)-1, start_y+(n//2)-1, n//2)
        
# z(0, 0, 2 ** n - 1, 2 ** n - 1, m)

def z(start_x, start_y, n):
    print(start_x, start_y, n)
    global count
    if (r == start_x and c == start_y):
        return
    if r >= (n//2+start_x) and c >= (start_y+n//2):  # 4사분면
        count += (n*n//4*3)
        z(n//2+start_x, start_y+n//2, n//2)
    elif r < (n//2+start_x) and c >= (start_y+n//2): # 3사분면
        count += (n*n//2)
        z(start_x, start_y+n//2, n//2)
    elif r >= (n//2+start_x) and c < (start_y+n//2): # 2사분면
        count += (n*n//4)
        z(n//2+start_x, start_y, n//2) 
    else: # 1사분면
        z(start_x, start_y, n//2)
        
z(0, 0, m)
print(count)

start_x = 0
start_y = 0
while True:
    if r == start_x and c == start_y:
        break
    if r >= (m//2+start_x) and c >= (start_y+m//2):  # 4사분면
        count += (m*m//4*3)
        start_x, start_y = m//2+start_x, start_y+m//2
        m = m // 2
    elif r < (m//2+start_x) and c >= (start_y+m//2):  # 3사분면
        count += (m*m//2)
        start_x, start_y = start_x, start_y+m//2
        m = m // 2
    elif r >= (m//2+start_x) and c < (start_y+m//2):  # 2사분면
        count += (m*m//4)
        start_x, start_y = m//2+start_x, start_y
        m = m // 2
    else: # 1사분면
        start_x, start_y = start_x, start_y
        m = m // 2
    
print(count)