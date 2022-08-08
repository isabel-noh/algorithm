
import sys
sys.stdin = open("sample.txt")

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    arr_N = []

    for i in range(N):
        arr_N.append(list(input())) # 각 줄을 문자 하나하나로 쪼갠 이차원 배열

    # 뒤집기
    arr_M = list(map(list, zip(*arr_N))) # arr_N의 행열을 뒤집은 이차원 배열
    
    for i in arr_N:
        for j in range(len(i)//2):
            if i[j : len(i)-j] == i[len(i)-j-1 : j-1 : -1]:
                print("".join(i[j : len(i)-1]))

    for i in arr_M: 
        for j in range(len(i)//2):
            if i[j : len(i)-j] == i[len(i)-j-1 : j-1 : -1]:
                print("".join(i[j : len(i)-1]))