# # BOJ 1914 하노이탑
# [BOJ 1914 하노이탑](https://www.acmicpc.net/problem/1914)

# ## 문제
# 세 개의 장대가 있고 첫 번째 장대에는 반경이 서로 다른 n개의 원판이 쌓여 있다. 각 원판은 반경이 큰 순서대로 쌓여있다. 이제 수도승들이 다음 규칙에 따라 첫 번째 장대에서 세 번째 장대로 옮기려 한다.

# 한 번에 한 개의 원판만을 다른 탑으로 옮길 수 있다.
# 쌓아 놓은 원판은 항상 위의 것이 아래의 것보다 작아야 한다.
# 이 작업을 수행하는데 필요한 이동 순서를 출력하는 프로그램을 작성하라. 단, 이동 횟수는 최소가 되어야 한다.

# ### 입력
# 첫째 줄에 첫 번째 장대에 쌓인 원판의 개수 N (1 ≤ N ≤ 100)이 주어진다.

# ### 출력
# 첫째 줄에 옮긴 횟수 K를 출력한다.

# N이 20 이하인 입력에 대해서는 두 번째 줄부터 수행 과정을 출력한다. 두 번째 줄부터 K개의 줄에 걸쳐 두 정수 A B를 빈칸을 사이에 두고 출력하는데, 이는 A번째 탑의 가장 위에 있는 원판을 B번째 탑의 가장 위로 옮긴다는 뜻이다. N이 20보다 큰 경우에는 과정은 출력할 필요가 없다.

n = int(input())
cnt = 0
def recur(n, start, middle, end):   
    if n == 1:
        print(start, end)  # 1개 옮길 때 시작 위치랑 목표 위치 출력
    else:
        recur(n-1, start, end, middle) # 마지막것을 제외하고 위의 n-1개를 1에서 중간 위치로 옮기고
        # recur(1, start, middle, end)    # 마지막 1개를 1번에서 목표위치로 이동 
        print(start, end)
        recur(n-1, middle, start, end)  # 마지막 것 제외하고 n-1개를 중간위치에서 목표위치로 이동

print(2**n-1) 
if n <= 20:
    recur(n, 1, 2, 3) # n개를 1번에서 3번으로 이동시키기