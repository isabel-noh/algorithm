# BOJ - 구간 합 구하기 4

[BOJ - 구간 합 구하기 4](https://www.acmicpc.net/problem/11659)

### 문제

수 N개가 주어졌을 때, i번째 수부터 j번째 수까지 합을 구하는 프로그램을 작성하시오.

### 입력

첫째 줄에 수의 개수 N과 합을 구해야 하는 횟수 M이 주어진다. 둘째 줄에는 N개의 수가 주어진다. 수는 1,000보다 작거나 같은 자연수이다. 셋째 줄부터 M개의 줄에는 합을 구해야 하는 구간 i와 j가 주어진다.

### 출력

총 M개의 줄에 입력으로 주어진 i번째 수부터 j번째 수까지 합을 출력한다.

### 제한

- 1 ≤ N ≤ 100,000
- 1 ≤ M ≤ 100,000
- 1 ≤ i ≤ j ≤ N

### 알고리즘 설계

처음에는 문제 그대로 i부터 j까지 더하는 방식으로 문제를 풀이하려고 했으나 틀렸었다.  
구간 합이라는 문제를 인식하고, sums라는 배열에 각 칸에 0부터 i번째까지의 누적 값을 더하여 저장하였다.  
그 다음, console.log()의 호출을 여러번 하지 않게 하기 위해서 results라는 배열에 모든 값을 저장해주기로 했다.  
마지막으로 i부터 j까지의 구간합을 구하기 위해서 sums의 j번째 값에서 i-1번째 값을 뺀다면 i부터 j까지의 구간의 합과 동일하다는 것에서 착안하여 문제를 풀이하였다.

### 코드

```js
const fs = require("fs");
const [nm, numbers, ...arr] = fs
  .readFileSync("./sample.txt")
  .toString()
  .split("\n")
  .map((el) => el.split(" ").map(Number));
const [N, M] = nm;

const sums = new Array(N).fill(0);
sums[0] = numbers[0];
for (let i = 1; i <= N - 1; i++) {
  sums[i] = sums[i - 1] + numbers[i];
}
const results = [];
for (const [i, j] of arr) {
  const r = i > 1 ? sums[j - 1] - sums[i - 2] : sums[j - 1];
  results.push(r);
}
console.log([...results].join("\n"));
```

### 틀린 코드

````js
const results = [];
for (const [i, j] of arr) {
  let sum = 0;
  for (let l = i - 1; l <= j - 1; l++) {
    sum += numbers[l];
  }
  results.push(sum);
}
console.log([...results].join("\n"));

```;
````

### 시간 복잡도

O(N)
