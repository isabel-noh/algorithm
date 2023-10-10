# Programmers - sort - K번째 수

[Programmers - sort - K번째 수](https://school.programmers.co.kr/learn/courses/30/lessons/42748)

## 문제 설명

배열 array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때, k번째에 있는 수를 구하려 합니다.

예를 들어 array가 [1, 5, 2, 6, 3, 7, 4], i = 2, j = 5, k = 3이라면

array의 2번째부터 5번째까지 자르면 [5, 2, 6, 3]입니다.  
1에서 나온 배열을 정렬하면 [2, 3, 5, 6]입니다.  
2에서 나온 배열의 3번째 숫자는 5입니다.  
배열 array, [i, j, k]를 원소로 가진 2차원 배열 commands가 매개변수로 주어질 때, commands의 모든 원소에 대해 앞서 설명한 연산을 적용했을 때 나온 결과를 배열에 담아 return 하도록 solution 함수를 작성해주세요.

### 제한사항

array의 길이는 1 이상 100 이하입니다.
array의 각 원소는 1 이상 100 이하입니다.  
commands의 길이는 1 이상 50 이하입니다.  
commands의 각 원소는 길이가 3입니다.

### 입출력 예

| array                 | commands                          | return    |
| --------------------- | --------------------------------- | --------- |
| [1, 5, 2, 6, 3, 7, 4] | [[2, 5, 3], [4, 4, 1], [1, 7, 3]] | [5, 6, 3] |

#### 문제풀이

commands는 [a, b, c]의 형태로 입력되는 배열들의 모음이다.
array의 배열에서 a번째부터 b번째까지를 뽑아서 정렬한 뒤, c번째의 값을 answer 배열에 push해준다.
splice(i, j) 메서드는 i번째부터 j개를 짤라낸다. b - a + 1을 계산하면 몇 개를 잘라내야하는지 계산할 수 있다.

````js
function solution(array, commands) {
  var answer = [];
  for (const command of commands) {
    const [a, b, c] = command;
    const arr = [...array].splice(a - 1, b - a + 1).sort((a, b) => a - b);
    answer.push(arr[c - 1]);
  }
  return answer;
}

solution(
  [1, 5, 2, 6, 3, 7, 4],
  [
    [2, 5, 3],
    [4, 4, 1],
    [1, 7, 3],
  ]
);
```;
````
