# BOJ - Gold1 - 실질적 약수

[BOJ - Gold1 - 실질적 약수](https://www.acmicpc.net/problem/2247)

### 문제

두 자연수 A와 B가 있을 때, A = BC를 만족하는 자연수 C를 A의 약수라고 한다. 모든 자연수 N은 1과 자기 자신(N)을 약수로 갖게 된다.

실질적 약수(actual divisor)라는 것이 있다. 자연수 N의 약수들 중에서 1과 자기 자신(N)을 제외한 약수를 실질적 약수라고 한다. 따라서 6의 실질적 약수는 2, 3이며, 13의 실질적 약수는 없다.

SOD(Sum Of Divisor)라는 함수를 정의하자. SOD(n)은 정수 n의 모든 실질적 약수의 합을 가리킨다. 따라서 SOD(6) = 5이며, SOD(13) = 0이다. 한편, CSOD(Cumulative SOD)라는 함수도 정의해 볼 수 있다. CSOD(n)은 SOD(1) + SOD(2) + … + SOD(n)이라고 하자.

CSOD(n)을 구하는 프로그램을 작성하시오.

### 입력

첫째 줄에 정수 n이 주어진다.

### 출력

첫째 줄에 CSOD(n)을 1,000,000으로 나눈 나머지를 출력한다.

### 제한

1 ≤ n ≤ 200,000,000

### 알고리즘 설계

처음에는 문제에서 주어진대로, CSOD를 만들고 그 안에서 SOD를 호출해서 일일히 계산하는 방식으로 답을 구하였으나 시간 초과가 났다.
범위가 1부터 2억까지인데, for문을 한 번 반 돌게되어 시간 복잡도가 `O(num ^3/2 )` 가 되므로, 시간초과가 날 수 밖에 없었다.

### 코드 - 시간초과

```js
const fs = require("fs");
const n = +fs.readFileSync("./sample.txt").toString();
//1과 자기 자신(N)을 제외한 약수

const SOD = (num) => {
  let answer = 0;
  for (let i = 2; i <= Math.sqrt(num); i++) {
    if (num % i === 0 && i !== num) {
      answer += i;
      {
        answer += Math.floor(num / i) !== i ? Math.floor(num / i) : 0;
      }
    }
  }
  console.log(num, answer);
  return answer;
};

const CSOD = (num) => {
  let answer = 0;
  const arr = new Array(num).fill(0);
  for (let i = 1; i <= num; i++) {
    answer += SOD(i);
  }
  return answer;
};

console.log(CSOD(n) % 1000000);
```

### 정답 코드

다른 사람의 방법을 참고한 방법이다.

n이 20이라고 가정하자.
이 때 1부터 20까지의 모든 숫자의 실질적 약수를 적어보면 다음과 같다.

```
4 - 2
6 - 2, 3
8 - 2, 4
9 - 3
10  - 2, 5
12 - 2, 3, 4, 6
14 - 2, 7
15 - 3, 5
16 - 2, 4, 8
18 - 2, 3, 6, 9
20 - 2, 4, 5, 10
```

여기에서 실질적 약수들의 개수를 정리해보면 아래와 같다.

```
2 - 9개
3 - 5개
4 - 4개
5 - 3개
6 - 2개
7 - 1개
8 - 1개
9 - 1개
10 - 1개
```

여기에서 다음과 같은 식을 추론할 수 있다.  
1부터 n까지 실질적 약수는 2부터 n/2까지 나오고, 각 약수의 개수는 (n/2) - 1개이다. `(Math.floor(n / i) - 1))`

그래서 모든 실질적인 약수의 합을 구하게 되면 `각 약수 * (Math.floor(n / i) - 1))`를 더한 것이 된다.

여기에 추가적으로 더해야할 것이 어차피 결국 100만의 나머지만 return할 것이기 때문에 매 for문 마다 `% 1000000`를 answer이 100만을 넘어가지 않도록 해주어야 한다는 것이었다.

```js
// n까지 i의 배수의 개수
let answer = 0;
for (let i = 2; i <= Math.floor(n / 2); i++) {
  answer += (i * (Math.floor(n / i) - 1)) % 1000000;
}
console.log(answer % 1000000);
```
