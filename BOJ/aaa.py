# BOJ14217
# 첫째 줄에는 도시의 개수 n,도로의 개수 m이 주어진다. 다음 m개의 줄에는 두 도시가 주어진다.(2≤n≤500,1≤m≤n*(n-1)/2)

# 다음 줄에는 도로 정비 계획에 들어가 있는 도로의 수 q가 주어지고, 다음 q줄에는 a i j가 주어지는데, a가 1일때는 두 도시 i,j를 잇는 도로를 만들고, a가 2일때는 i,j를 잇는 도로를 없앤다. (1≤q≤500,1≤a≤2, 1≤i,j≤n)

# 두 도시 사이에 이미 도로가 있는데 또 도로를 만들거나, 도로가 없는데 없애는 불가능한 경우는 입력으로 들어오지 않는다.

# 수도는 1번도시이다.

from collections import deque
import sys
sys.stdin = open('sample.txt')
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]
for _ in range(m):
    i, j = arr[_]
    arr.append([j, i])

q = int(input())

def bfs(i):
    global arr
    p = 0
    q = deque([[i, p]])
    visited = [0 for _ in range(n+1)]
    while q:
        item, path = q.popleft()
        visited[item] = path
        if item == 1: 
            return max(visited)
        else: 
            for i in range(len(arr)):
                if arr[i][0] == item and visited[arr[i][1]] == 0:
                    visited[arr[i][1]] = path
                    q.append([arr[i][1], path+1])
    return -1

for _ in range(q):
    a, i, j = map(int, input().split())
    b = []
    if a == 1:
        arr.append([i, j])
        arr.append([j, i])
        for k in range(1, n+1):
            if k == 1:
                b.append(0)
            else:
                b.append(bfs(k))
    else:
        arr.remove([i, j])
        arr.remove([j, i])
        for k in range(1, n+1):
            if k == 1:
                b.append(0)
            else:
                b.append(bfs(k))
    print(*b, sep=' ')

