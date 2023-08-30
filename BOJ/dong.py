from copy import deepcopy

def change(nums):
    x = list(map(str, nums[0] + nums[1][::-1]))
    return "".join(x)

def spin(w, arr):
    if w == "A":
        arr[0], arr[1] = arr[1], arr[0]

    elif w == "B":
        a = arr[0].pop()
        b = arr[1].pop()
        arr[0] = [a] + arr[0]
        arr[1] = [b] + arr[1]

    elif w == "C":
        arr[0][1], arr[0][2], arr[1][1], arr[1][2] = arr[0][2], arr[1][2], arr[0][1], arr[1][1]

    else:
        arr[0][0], arr[1][-1] = arr[1][-1], arr[0][0]

    return arr

L = list(map(int, input().split()))
target = change([L[:4], L[4:][::-1]])

q = [[[1, 2, 3, 4], [8, 7, 6, 5]]]
start = "12345678"
visited = {
    start: 1
}
while 1:
    temp = q.pop(0)
    key = change(temp)

    if key == target:
        print(visited[key]-1)
        print(visited)
        quit()

    for W in "ABCD":
        newArr = spin(W, deepcopy(temp))
        number = change(newArr)
        if number not in visited:
            visited[number] = visited[key] + 1
            q.append(newArr)