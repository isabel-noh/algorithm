# N개의 나무가 있다. 초기의 각 나무의 키가 주어진다. 하루에 한 나무에 물을 줄 수 있다. 첫 날은 물을 준 나무의 키가 1 자라고, 둘째 날은 물을 준 나무의 키가 2 자라고, 셋째 날은 물을 준 나무의 키가 1 자라는 식으로, 홀수 번째 날은 키가 1 자라고 짝수 번째 날은 키가 2 자란다. 

# 모든 나무의 키가 처음에 가장 키가 컸던 나무와 같아지도록 할 수 있는 최소 날짜 수를 계산하라. 어떤 날에는 물을 주는 것을 하지 않을 수도 있다.
 
# 예를 들어 나무가 2그루이고 각각의 높이가 4와 2라고 하자. 첫째 날에 물을 주게 되면, 나무의 높이를 모두 4로 만들기 위해서는 3일째까지 물을 주어야 한다. 둘째 날은 아무 일도 안 하게 된다. 하지만, 첫째 날을 쉬고 둘째 날에 물을 주면 2일 만에 나무의 높이가 모두 4가 된다.
# 케이스 수 30, N 제한 100, 나무 높이 최대 120

# [제약사항]
# 나무의 개수 N은 2 이상 100 이하이다. (2 ≤ N ≤ 100)
# 주어지는 나무의 초기 높이는 1 이상 120 이하이다.

# 입력
# 가장 첫 줄에는 테스트 케이스의 총 수가 주어진다. 그 다음 줄부터 각 테스트 케이스가 주어지며, 각 테스트 케이스는 2줄로 구성된다. 각 테스트 케이스의 첫째 줄에는 나무의 개수 N이 주어진다. 다음 줄에는 나무들의 높이가 N개의 자연수로 주어진다.

# 출력
# 출력의 각 줄은 ‘#x’로 시작하고, 공백을 한 칸 둔 다음 가능한 최소 날짜 수를 출력한다. 단, x는 테스트 케이스의 번호이다.
import sys
sys.stdin = open('sample.txt')
T = int(input())
for tc in range(1, T+1) :
    N = int(input())
    arr = list(map(int, input().split()))
    max_length = max(arr)
    day = 0
    while True :
        while arr[-1] != max_length:
            if arr[-1] == max_length:
                arr.pop()
        print(arr)
        day += 1
        arr.sort()
        flag = True
        for i in arr:
            if i != max_length:
                flag = False
                break
        if flag == True :
            break

        for i in arr:
            if i % 2 == 1 and day % 1 == 0 : # i가 홀수이고, 홀수번째 날이면 
                i += 1
                break
            elif i % 2 == 0 and day % 2 == 0 :
                i += 2
        


    
    result = 0
    print(f'#{tc} {result}')