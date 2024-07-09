# BOJ - Silver1 - 도미노 넘어뜨리기

[BOJ - Silver1 - 도미노 넘어뜨리기](https://www.acmicpc.net/problem/25633)

### 문제

N개의 도미노가 일렬로 세워져 있다. 도미노에는 무게가 존재하는데, i번째 도미노의 무게는 a_i이다. 단현이는 N개의 도미노 중 일부 도미노를 제거할 수 있다. 만약 남은 도미노에서 i번째 도미노를 제거하면 i번째 도미노의 양옆의 도미노가 이웃하게 된다.

단현이는 이렇게 일부를 제거하고 남은 도미노가 완벽하게 나열되도록 만들고 싶다. 도미노가 완벽하게 나열되었다는 것은, 나열된 도미노에서 첫 번째 도미노를 넘어뜨렸을 때 마지막 도미노까지 차례로 넘어진다는 것을 의미한다.

일부를 제거하고 남은 M개의 도미노에서 j번째 도미노의 무게를 b_j라고 하자. j(2 <= j <= M)번째 도미노가 넘어지기 위해서는 첫 번째 도미노부터 j - 1번째 도미노까지 모두 넘어져야 하고, 넘어진 도미노의 무게를 합한 값이 b_j보다 크거나 같아야 한다.

단현이는 N개의 도미노에서 일부 도미노를 제거해서 완벽하게 나열되도록 만들고 싶다. 완벽하게 나열할 수 있는 도미노의 최대 개수는 얼마일까?

### 입력

첫째 줄에 도미노의 개수 N(1<= N <= 1000)이 주어진다.

둘째 줄에 정수 a_1, a_2, ... , a_N이 주어진다.  
a_i(1 <= a_i <= 1,000,000)는 i번째 도미노의 무게이다.

### 출력

완벽하게 나열할 수 있는 도미노의 최대 개수를 출력한다.

### 알고리즘 설계

j번째 도미노가 넘어지려면 0~j-1번째까지 도미노의 합이 j번째 도미노의 무게보다 크거나 같아야 한다.

countDp에는 누적 최대 도미노 개수를 기재한다. dp에는 countDp에 대한 누적합을 기록한다.  
최대 도미노 개수를 세는 것이 키 포인트이기 때문에, 0부터 i-1번째까지 countDp 중에 가장 큰 숫자, 즉 최대 도미노 개수와 그의 index를 기억한다.
i번째 도미노의 무게보다 여태까지의 넘어간 도미노의 총 무게가 더 작고, 넘어간 도미노의 개수도 최대인 경우가 있을 때, i번째의 dp 값에 i번째 도미노의 무게를 추가하여 업데이트 해준다. 만약 그런 경우가 없다면, i번째 dp의 값은 i번째 도미노의 무게 그 자체가 된다. 해당 도미노를 넘기려면 그 도미노가 첫번째 도미노가 되는 것이다.

### 코드

```js
const fs = require("fs");
const [n, input] = fs.readFileSync("./sample.txt").toString().split("\n");
const arr = input.split(" ").map(Number);
const dp = [...new Array(+n)].fill(0);
const countDp = [...new Array(+n)].fill(1);
dp[0] = arr[0];
for (let i = 1; i < +n; i++) {
  let maxIdx = 0;
  let maxCount = 0;
  for (let j = 0; j < i; j++) {
    if (maxCount <= countDp[j] && dp[j] >= arr[i]) {
      maxCount = countDp[j];
      maxIdx = j;
    }
  }
  if (maxCount) {
    dp[i] = dp[maxIdx] + arr[i];
    countDp[i] = countDp[maxIdx] + 1;
  } else {
    dp[i] = arr[i];
  }
}
console.log(Math.max(...countDp));
```
