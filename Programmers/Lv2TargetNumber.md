# Programmers - DFS/BFS - Target Number

[Programmers - DFS/BFS - Target Number](https://school.programmers.co.kr/learn/courses/30/lessons/43165)

## 문제 설명

n개의 음이 아닌 정수들이 있습니다. 이 정수들을 순서를 바꾸지 않고 적절히 더하거나 빼서 타겟 넘버를 만들려고 합니다. 예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들려면 다음 다섯 방법을 쓸 수 있습니다.

-1+1+1+1+1 = 3  
+1-1+1+1+1 = 3  
+1+1-1+1+1 = 3  
+1+1+1-1+1 = 3  
+1+1+1+1-1 = 3  
사용할 수 있는 숫자가 담긴 배열 numbers, 타겟 넘버 target이 매개변수로 주어질 때 숫자를 적절히 더하고 빼서 타겟 넘버를 만드는 방법의 수를 return 하도록 solution 함수를 작성해주세요.

### 제한사항

- 주어지는 숫자의 개수는 2개 이상 20개 이하입니다.
- 각 숫자는 1 이상 50 이하인 자연수입니다.
- 타겟 넘버는 1 이상 1000 이하인 자연수입니다.

#### 문제풀이

dfs로 풀이한 문제이다.
dfs에는 매개변수로 2가지가 들어간다. 현재 확인중인 index, 현재까지의 더해진 값
-> 0번째 숫자부터 확인한다. 0번째 숫자는 0으로부터 더해지거나 빼질 수 있으므로, `dfs(0, -numbers[0]);`, `dfs(0, numbers[0]);`를 모두 실행한다.
-> 이 문제에서 dfs에서는 가지를 치고 내려가는 `트리`처럼 동작된다.
-> 0 - number[0]에 대해 더하거나 빼는 값 두 가지가 나온다. - 각각에 대해 number[1]에 대해 더하거나 빼는 값 두가지가 나온다(즉, 4가지) - ... 반복
그렇게 dfs를 돌다가 curSum이 target 숫자와 동일하면서 idx가 마지막 index와 동일한 경우, 즉 우리가 찾는 target의 경우가 맞을 때 answer을 +1해주고 return;한다.

```js
function solution(numbers, target) {
  var answer = 0;

  function dfs(idx, curSum) {
    if (curSum === target && idx === numbers.length - 1) {
      answer++;
      return;
    }

    if (idx + 1 < numbers.length) {
      dfs(idx + 1, curSum - numbers[idx + 1]);
      dfs(idx + 1, curSum + numbers[idx + 1]);
    }
  }

  dfs(0, -numbers[0]);
  dfs(0, numbers[0]);
  return answer;
}

solution([1, 1, 1, 1, 1], 3);
solution([4, 1, 2, 1], 4);
```
