N, M = map(int, input().split())
arr = sorted(list(set(map(int, input().split()))))
print(arr)
s = []
def f(j):
    if len(s) == M:
        print(*s)
        return
    for i in range(j, len(arr)):
            s.append(arr[i])
            f(i)
            s.pop()

f(0)