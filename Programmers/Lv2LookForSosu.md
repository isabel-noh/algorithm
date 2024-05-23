# Programmers 완전탐색 - 소수찾기

[Programmers 완전탐색 - 소수찾기](https://school.programmers.co.kr/learn/courses/30/lessons/42839)

## 문제 설명

한자리 숫자가 적힌 종이 조각이 흩어져있습니다. 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.

각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.

### 제한사항

numbers는 길이 1 이상 7 이하인 문자열입니다.
numbers는 0~9까지 숫자만으로 이루어져 있습니다.
"013"은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미입니다.

### 입출력 예

| numbers | return |
| ------- | ------ |
| "17"    | 3      |
| "011"   | 2      |

#### 문제풀이

dfs를 활용하여 permutation을 뽑고, 그 안에서 소수인지를 판별하는 문제이다. 중복되는 아이템이 없도록 set에 값들을 저장해준다.
visited 배열에는 s의 문자열에 해당 숫자가 추가되었을 때, 방문했다는 표시를 해준다.  
s문자열에 아직 추가되지 않은 숫자라면, 추가하고 재귀로 dfs를 한번 더 들어간다.  
값이 임시저장되는 s의 길이가 우리가 원하는 길이가 되었다면, set에 추가하고, s에서 마지막에 추가한 숫자를 제거하고, visited에서도 미방문 처리해준다.

```js
function getPermutations(array) {
  const set = new Set();
  let s = "";
  const visited = new Array(array.length).fill(0);

  function dfs(s, len, v) {
    if (s.length === len) {
      set.add(Number(s));
      return;
    }
    for (let i = 0; i < array.length; i++) {
      if (v[i] === 0) {
        v[i] = 1;
        s += array[i];
        dfs(s, len, v);
        s = s.slice(0, s.length - 1);
        v[i] = 0;
      }
    }
  }

  for (let l = 1; l < array.length + 1; l++) {
    dfs(s, l, visited);
  }
  return set;
}

function solution(numbers) {
  var answer = 0;
  const arr = numbers.split("");
  const permutation = getPermutations(arr);

  // 소수 찾기
  function isPrime(x) {
    if (x === 0 || x === 1) {
      return false;
    }
    // 아리토스테네스의 체
    for (let i = 2; i <= Math.sqrt(x); i++) {
      if (x % i === 0) {
        return false;
      }
    }
    return true;
  }
  permutation.forEach((el) => {
    if (isPrime(el)) {
      answer++;
    }
  });

  return answer;
}
```
