# 최고의 집합

[ProgrammersTheBestSet](https://school.programmers.co.kr/learn/courses/30/lessons/12938?language=javascript)

## 문제 설명

자연수 n 개로 이루어진 중복 집합(multi set, 편의상 이후에는 "집합"으로 통칭) 중에 다음 두 조건을 만족하는 집합을 최고의 집합이라고 합니다.

```
- 각 원소의 합이 S가 되는 수의 집합
- 위 조건을 만족하면서 각 원소의 곱 이 최대가 되는 집합
```

예를 들어서 자연수 2개로 이루어진 집합 중 합이 9가 되는 집합은 다음과 같이 4개가 있습니다.
{ 1, 8 }, { 2, 7 }, { 3, 6 }, { 4, 5 }
그중 각 원소의 곱이 최대인 { 4, 5 }가 최고의 집합입니다.

집합의 원소의 개수 n과 모든 원소들의 합 s가 매개변수로 주어질 때, 최고의 집합을 return 하는 solution 함수를 완성해주세요.

### 제한사항

최고의 집합은 오름차순으로 정렬된 1차원 배열(list, vector) 로 return 해주세요.
만약 최고의 집합이 존재하지 않는 경우에 크기가 1인 1차원 배열(list, vector) 에 -1 을 채워서 return 해주세요.  
자연수의 개수 n은 1 이상 10,000 이하의 자연수입니다.  
모든 원소들의 합 s는 1 이상, 100,000,000 이하의 자연수입니다.

#### 문제풀이

dfs로 조합을 만들어 풀이하려 했으나 메모리 초과하여 실패!

```js
function sum(arr) {
  let result = arr.reduce((a, b) => a + b, 0);
  return result;
}

function dfs(n, s, temp, answer) {
  if (temp.length === n && sum(temp) == s) {
    answer.push(temp.slice());
    return;
  }
  for (let i = 1; i < s; i++) {
    if (temp.length === 0 || (temp.length > 0 && temp[0] <= i)) {
      temp.push(i);
      dfs(n, s, temp, answer);
      temp.pop();
    }
  }
}

function solution(n, s) {
  var temp = [];
  var answer = [];
  dfs(n, s, temp, answer);
  console.log(answer);
  if (answer.length === 0) {
    return [-1];
  }
  return answer;
}
```

#### 문제풀이 2

중복집합(Multi-set)이기 때문에 같은 원소의 중복을 허용하게 된다 ( {4, 4} 허용 )  
주어진 자연수 s는 n개의 원소들의 합으로 이루어져 있다  
n개의 자연수를 가지고 합쳐서 s를 만들 수 있다면, `s를 n으로 나눈 몫이 그 조합들 중에서 곱이 최대인 값인 그룹의 시작값이 된다`.  
예) 9를 2로 나눈 몫 -> 4  
solution(2, 9)의 답은 {1, 8}, {2, 7}, {3, 6}, {4, 5} 중에서 제일 곱이 큰 {4, 5}

```js
function solution(n, s) {
  const answer = [];
  let max_start = Math.floor(s / n);

  if (max_start < 1) {
    // 나누었을 때 1보다 작으면 값이 없으므로 -1을 리턴
    return [-1];
  }
  for (let i = 0; i < n; i++) {
    answer.push(max_start); // n칸의 배열에 시작값인 max_start로 초기화 [4, 4]
  }

  // s를 n으로 나눴을 때, 나누어 떨어지지 않은 경우는 몇 개(s%n)의 값들은 max_start보다 1씩 크다는 의미이다.
  for (let i = 0; i < s % n; i++) {
    answer[i] = answer[i] + 1; // s를 n으로 나눈 나머지 를 answer의 각 값에 1씩 더하면 문제를 해결할 수 있다.
  }
  return answer.sort();
}

solution(2, 9); // {4, 5} // {1, 8}, {2, 7}, {3, 6}, {4, 5}
solution(2, 1); // -1
solution(2, 8); // {4, 4}
```
