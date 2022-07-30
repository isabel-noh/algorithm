# SWEA 구간합
[SWEA 구간합](https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do#none)

N개의 정수가 들어있는 배열에서 이웃한 M개의 합을 계산하는 문제이다. 
처음에 아래와 같이 풀었을 때는 계속 메모리 에러가 발생하였다. 

```python
T = int(input()) # testcase 
for i in range(T):
    # temp = input().split() # N, M
    # N = int(temp[0])
    # M = int(temp[1])
    N, M = map(input().split())

    arr = list(map(int, input().split()))  #1 2 3 4 5 6 7 8 9 10
    min_sum = sum(arr)
    max_sum = 0


    for k in range(0, N-M+1):
        sum = 0
        for j in range(k, M+k):
            sum += arr[j]
        max_sum = max(max_sum, sum)
        min_sum = min(min_sum, sum)

    print(f'#{i+1} {max_sum - min_sum}')
```
일일이 max의 값과 현재의 값을 비교하여 메모리를 과대하게 사용한 것 같다. 
아래와 같이 수정하여 각 배열의 합을 넣어줄 리스트를 만들고 그 안에서 max와 min을 바로 뽑아내어 계산해주었더니 해결되었다. 
```python
   sum_list = []
    for k in range(N-M+1):
        sum = 0
        for j in range(k, M+k):
            sum += arr[j]
        sum_list.append(sum)

    print(f'#{i+1} {max(sum_list) - min(sum_list)}')
```

