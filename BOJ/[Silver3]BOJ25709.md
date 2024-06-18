# 1 빼기

[1 빼기](https://www.acmicpc.net/problem/25709)

### 문제

민겸이는 1 빼기를 할 수 있는 능력을 가지고 있다. 1 빼기란, 다음의 두 연산 중 하나를 골라 수행하는 것이다.

1. 가지고 있는 수에서 1을 뺀다.
2. 가지고 있는 수에 있는 1을 하나 지운다. 지우고 난 뒤 좌우의 수들을 순서대로 다시 합쳐 하나의 수로 만든다. 이때 맨 앞의 연속되는 0은 지워진다.

민겸이가 최초로 가지고 있는 정수가 하나 주어질 때, 이 수를 0으로 만들기 위해 최소 몇 번의 1 빼기가 필요한지 구해보자.

### 입력

민겸이가 가지고 있는 정수 N이 주어진다.

### 출력

민겸이가 해당 수를 0으로 만들기 위해서 최소 몇 번의 1 빼기가 필요한지 출력한다.

### 제한

1 ≤ N ≤ 10^9

### 알고리즘 설계

1. 가진 수에서 1빼기
2. 가진 수에서 1을 삭제하기

한 번에 위 두가지 경우를 처리할 수 있다.  
이 두가지를 실행했을 때 더 적은 숫자를 만드는 방법을 선택하여 실행하고, 새로 나온 결과값을 n으로 업데이트하여 이 n이 0이 될 때까지 실행하는 횟수를 센다.

### 시간 복잡도

𝑂(𝑁log𝑁)

### 코드

```js
const fs = require("fs");
const Ns = fs.readFileSync("./sample.txt").toString().split("\n").map(Number);

Ns.forEach((N) => {
  let answer = 0;
  let n = N;
  for (let i = 0; i < N + 1; i++) {
    const first = n - 1; // n에서 1빼기
    const stringifiedN = String(n);
    const oneIndex = stringifiedN.includes("1");
    if (oneIndex && n !== 0) {
      const one = stringifiedN.indexOf("1");
      const deletedString =
        stringifiedN.slice(0, one) + stringifiedN.slice(one + 1);
      const second = +deletedString; // 아니면 글자 1빼고 숫자로 만들기
      n = Math.min(first, second);
      answer++;
    } else {
      n = first;
      answer++;
    }
    if (n === 0) {
      break;
    }
  }
  console.log(answer);
  // console.log(arr);
});
```
