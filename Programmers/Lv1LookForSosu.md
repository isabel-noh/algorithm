# Programmers - 효율성 문제,, - 소수 찾기

[Programmers - 효율성 문제,, - 소수 찾기](https://school.programmers.co.kr/learn/courses/30/lessons/12921)

## 문제 설명

1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하는 함수, solution을 만들어 보세요.

소수는 1과 자기 자신으로만 나누어지는 수를 의미합니다.
(1은 소수가 아닙니다.)

### 제한 조건

n은 2이상 1000000이하의 자연수입니다.

### 입출력 예

| n   | result |
| --- | ------ |
| 10  | 4      |
| 5   | 3      |

#### 문제풀이

1. 기본적인 소수를 구하는 방식으로 문제를 풀이하였으나 효율성 문제에서 탈락하였다.  
    일반적으로 소수를 체크할 때에는 에라토스테네스의 체라는 알고리즘으로 풀이한다.
   x가 소수인지 판별할 때, 2부터 x까지 모두 판별하는 것이 아니라, x의 제곱근까지만 판별하는 것이다. x를 수가 나누면 몫이 생기는데, 몫 혹은 나누는 수는 반드시 x의 제곱근 이하이기 때문이라는 것이다. 그래서 이를 풀이하면 아래와 같은 코드가 나온다.  
    하지만 시간초과가 발생하였다.

   ```js
   function isPrime(x) {
     for (let i = 2; i <= Math.sqrt(x); i++) {
       // 소수인지 확인; 에라토스테네스의 체
       if (x % i === 0) {
         return false;
       }
     }
     return true;
   }
   ```

   전체 코드

```js
function isPrime(x) {
  for (let i = 2; i <= Math.sqrt(x); i++) {
    // 소수인지 확인; 에라토스테네스의 체
    if (x % i === 0) {
      return false;
    }
  }
  return true;
}
function solution(n) {
  var answer = 0;
  for (let j = 2; j <= n; j++) {
    if ((j !== 2 && j % 2 === 0) || (j !== 3 && j % 3 === 0)) {
      continue;
    } else {
      if (isPrime(j)) {
        answer++;
      }
    }
  }

  return answer;
}
```

2. 에라토스테네스의 체를 사용하되, checkArr이라는 배열을 만들고, 어떤 수의 배수가 되는 수는 false처리를 하여 소수가 아니라는 것을 표시해주는 방법을 사용하였다.  
   0, 1은 소수가 아니므로 false로 표시한다.  
   2부터 x의 제곱근까지 소수가 아닌지 맞는지를 판별한다.  
   판별하기 위해서, checkArr에 2부터 각 수의 배수들을 체크한다.
   하지만 모든 수를 일일히 체크하는 것이 아니라, checkArr에 아직 false로 변하지 않은 수들만 체크한다.
   2 --- 4, 6, 8  
   3 --- 6, 9  
   4는 이미 false이므로, pass  
   5 --- 10  
   이렇게 체크하면 소수만 false인 채로 남게 되고, true의 개수를 세면 된다.

```js
//소수는 1과 자기 자신(n)으로만 나누어지는 수 = n이 2부터 n-1까지의 수로 나누어 떨어지면 소수가 아님
function solution(n) {
  var answer = 0;
  const checkArr = new Array(n + 1).fill(true);
  checkArr[0] = false;
  checkArr[1] = false;
  for (let i = 2; i <= Math.sqrt(n); i++) {
    if (checkArr[i]) {
      for (let j = i * i; j < n + 1; j += i) {
        checkArr[j] = false;
      }
    }
  }
  answer = checkArr.filter((x) => x === true).length;
  return answer;
}
```
