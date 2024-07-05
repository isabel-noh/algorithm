# BOJ - Silver1 - 피아노 체조

[BOJ - Silver1 - 피아노 체조](https://www.acmicpc.net/problem/21318)

### 문제

피아노를 사랑하는 시은이는 매일 아침 피아노 체조를 한다. 시은이는 N개의 악보를 가지고 있으며, 1번부터 N번까지의 번호로 부른다. 각 악보는 1 이상 109 이하의 정수로 표현되는 난이도를 가지고 있다. 난이도를 나타내는 수가 클수록 어려운 악보이다. 1 ≤ x ≤ y ≤ N 을 만족하는 두 정수 x, y를 골라 x번부터 y번까지의 악보를 번호 순서대로 연주하는 것이 피아노 체조이다.

시은이는 피아노 체조를 할 때, 지금 연주하는 악보가 바로 다음에 연주할 악보보다 어렵다면 실수를 한다. 다시 말하자면, i(x ≤ i < y)번 악보의 난이도가 i + 1번 악보의 난이도보다 높다면 실수를 한다.
특히, 마지막으로 연주하는 y번 악보에선 절대 실수하지 않는다.
시은이는 오늘도 피아노 체조를 하기 위해 두 정수 x와 y를 골랐고, 문득 궁금한 것이 생겼다. 오늘 할 피아노 체조에서 실수하는 곡은 몇 개나 될까 ?

### 입력

첫 번째 줄에 악보의 개수 N(1 ≤ N ≤ 100,000)이 주어진다.

두 번째 줄에 1번 악보부터 N번 악보까지의 난이도가 공백을 구분으로 주어진다.

세 번째 줄에 질문의 개수 Q(1 ≤ Q ≤ 100,000)이 주어진다.

다음 Q개의 줄에 각 줄마다 두 개의 정수 x, y(1 ≤ x ≤ y ≤ N)가 주어진다.

### 출력

x번부터 y번까지의 악보를 순서대로 연주할 때, 몇 개의 악보에서 실수하게 될지 0 이상의 정수 하나로 출력한다. 각 출력은 개행으로 구분한다.

### 알고리즘 설계

처음에는 문제 그대로 풀이했다. x부터 y까지 더하고 출력, 더하고 출력.
하지만 시간초과가 났다.

그래서 dp의 누적합을 활용하여 풀이하였다.
check 배열에 0부터 N까지 앞뒤 값을 비교해가면서 실수가나는 횟수를 누적하여 저장하였다.
이후 x에서 y까지 곡을 연주한다면 `check의 x번째 값-check의 y번째 값`를 구한다면 그 사이에서 일어난 실수만 계산할 수 있게 된다.

### 코드

```js
const fs = require("fs");
const input = fs.readFileSync("./sample.txt").toString().split("\n");
const N = +input.shift();
const musics = input.shift().split(" ").map(Number); // 1 ~ 109
const Q = +input.shift();
const arr = input.map((el) => el.split(" ").map(Number));

const check = new Array(N + 1).fill(0);
for (let i = 0; i < N - 1; i++) {
  if (musics[i] > musics[i + 1]) {
    check[i + 1] = i === 0 ? 1 : check[i] + 1;
  } else {
    check[i + 1] = i === 0 ? 0 : check[i];
  }
}
let result = [];
for (let i = 0; i < Q; i++) {
  const [x, y] = arr[i];
  result.push(check[y - 1] - check[x - 1]);
}

console.log(result.join("\n"));
```

### 틀린 부분 고친 방식

`console.log()`가 너무 오래걸려서 한 배열에 담아주고, `.join('\n')`으로 풀어주어 해결하였다.
