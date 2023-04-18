from pprint import pprint
from itertools import combinations
import sys
sys.stdin = open('sample.txt')

n = int(input())
population = list(map(int, input().split()))
adj = []
arr = []
for _ in range(n):
    temp = list(map(int, input().split()))
    temp.pop(0)
    adj.append(temp)
    arr.append(_+1)


temp= []
for i in range(1, n):
    a = (list(combinations(arr, i)))
    for j in a:
        temp.append(j)
# temp1 = temp1[:len(temp1)//2]

minimum_gap = 1001

# adj[i]는 i와 인접한 지역들
def is_adjacent(idx): 
    global visited
    if len(temp[idx]) == 1:  # 길이가 1이면 visited처리하고, true 리턴 
        visited[temp[idx][0]] = 1
        return True
    q = [temp[idx][0]]
    while q:
        val = q.pop(0)
        visited[val] = 1
        for d in adj[val-1]:
            if visited[d] == 0 and d in temp[idx]: # d in temp[idx]가 연결된 item이 조합에 포함되어있는지를 확인하는 것
                q.append(d)

    for item in temp[idx]:
        if visited[item] == 0:
            return False
    else: 
        return True
    
temporal = []
for t in range(len(temp)//2):
    # 2개로 나눠지는 선거구이기 때문에 모든 조합을 2번으로 나눠서 bfs를 돎
    visited = [0] * (n+1)
    front = (is_adjacent(t))
    visited = [0] * (n+1)
    back = (is_adjacent(-1-t))
    if front and back: 
        temporal.append((t, -1-t))

for f, b in temporal:
    a_pop, b_pop = 0, 0
    for i in temp[f]:
        a_pop += population[i-1]
    for i in temp[b]:
        b_pop += population[i-1]
    if abs(a_pop - b_pop) < minimum_gap:
        minimum_gap = abs(a_pop - b_pop)
if minimum_gap == 1001:
    print(-1)
else:   
    print(minimum_gap)

