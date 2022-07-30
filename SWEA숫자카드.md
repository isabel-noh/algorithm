# SWEA 숫자카드
[SWEA 숫자카드](learn-course-programming intermidate-파이썬 List1)
N장의 여러 숫자 카드를 주는데 해당 숫자카드중 제일 개수가 많은 숫자와 그 카드의 총 장수를 출력하는 문제이다. 

```python
T = int(input())
for i in range(T):

    N = int(input())
    ai = str(input())
    list_ai = []
    for j in ai:
        list_ai.append(int(j))

    list_num = list(set(list_ai))
    list_num.sort()
    max_count = 0
    max_idx = 0
    for k in list_num:
        if list_ai.count(k) >= max_count : 
            max_count = list_ai.count(k)
            max_idx = k

    print(f'#{i+1} {max_idx} {max_count}')

```
처음에는 {카드번호:카드수}의 딕셔너리를 만들어서 value를 기준으로 max를 뽑아 내었지만 
카드 장수가 같을 때는 적힌 숫자가 큰 쪽을 출력한다는 특징을 빼먹어서 여러번 재시도를 하여야했다. 

결국 sorting이 원활하게 되지 않아 새로 코드를 작성하여야 했다. 
list_num을 오름차순으로 sorting하여 카드를 앞에서부터 개수를 비교하였고, 만일 현재 max_count와 현재 숫자의 count 가 동일할 경우 현재 idx로 바꾸게 하여 카드 장수가 같을 때는 더 큰 숫자를 출력할 수 있게 하였다. 

조건을 놓치지 말자! 