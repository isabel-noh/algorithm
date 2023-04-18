
import sys
sys.stdin = open('sample.txt')
n = int(input())
arr = [0]
for _ in range(n):
    arr.append(int(input()))

result = []

# 0, 1 2 3 4 5 6 7
# 0, 3 1 1 5 5 4 6

# 결국 싸이클이 도는지를 확인하는 문제 

def dfs(v, i): # v = arr2의 index, i = arr1의 값
    visited[v] = True 
    w = arr[v]  # w = arr2의 값
    if not visited[w]:  # arr2의 값 확인 안했다면
        dfs(w, i) # arr2[arr2[v]]를 확인하러 가는 셈
    elif visited[w] and w == i: # 방문한 적도 있고, arr[v]와 arr1의 값, 즉 i의 값이 같다면 순환 돈다는 의미
        result.append(w)

for i in range(1, n+1): # 0번부터 n번까지 확인 -> arr1 로써
    visited = [False] * (n+1)
    dfs(i, i)

print(len(result))
for i in result:
    print(i)