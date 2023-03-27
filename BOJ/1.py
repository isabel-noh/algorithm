t = int(input())
for tc in range(t):
    arr = list(input())
    cur = [0, 0]
    dir = 3 # 0 : 오른쪽, 1 : 야래, 2 : 왼쪽, 3 : 위
    maxX, maxY = 0, 0
    minX, minY = 0, 0
    for a in arr:
        if a == 'F':
            if dir == 0:
                cur[0] += 1 
            elif dir == 1:
                cur[1] -= 1
            elif dir == 2 : 
                cur[0] -= 1
            else : 
                cur[1] += 1
        if a == 'B':
            if dir == 0:
                cur[0] -= 1 
            elif dir == 1:
                cur[1] += 1
            elif dir == 2 : 
                cur[0] += 1
            else : 
                cur[1] -= 1
        if a == 'L': # 0 : 오른쪽, 1 : 야래, 2 : 왼쪽, 3 : 위
            dir -= 1
            if dir == -1:
                dir = 3
        if a == 'R': # 0 : 오른쪽, 1 : 야래, 2 : 왼쪽, 3 : 위
            dir += 1
            if dir == 4:
                dir = 0
        if cur[0] > maxX: 
            maxX = cur[0]
        if cur[0] < minX: 
            minX = cur[0]
        if cur[1] > maxY: 
            maxY = cur[1]
        if cur[1] < minY: 
            minY = cur[1]
    print((maxX-minX) * (maxY-minY))