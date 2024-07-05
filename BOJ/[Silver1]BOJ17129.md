# BOJ - Silver1 - 윌리암슨수액빨이딱따구리가 정보섬에 올라온 이유

[BOJ - Silver1 - 윌리암슨수액빨이딱따구리가 정보섬에 올라온 이유](https://www.acmicpc.net/problem/17129)

### 문제

윌리암슨수액빨이딱따구리 세 식구가 정보섬에 올라왔다!

세 윌리암슨수액빨이딱따구리는 정보섬 2층 어딘가에 모여 앉아 쉬고 있었는데, 저 멀리 청국장과 스시와 맥앤치즈가 있는 것을 발견했다! 아빠는 청국장, 엄마는 스시, 아이는 맥앤치즈가 먹고 싶다. 그래서 이 셋은 현위치로부터 가장 가까운 음식을 먹으러 가기로 했다.

정보섬 2층은 An×m의 격자로 표현된다. 어떤 Ai,j가 0이면 빈 복도여서 지나갈 수 있고, 1이면 장애물로 막혀 지나갈 수 없다. 윌리암슨수액빨이딱따구리 식구는 2, 청국장은 3, 스시는 4, 맥앤치즈는 5이다. 윌리암슨수액빨이딱따구리는 단위 시간마다 한 칸, 상하좌우로 움직일 수 있다. 2, 3, 4, 5는 장애물이 아니므로 지나갈 수 있다. 격자 밖으로는 나갈 수 없으며 시작점으로부터 시작점까지의 거리는 0이다. 시작점은 윌리암슨수액빨리딱따구리의 위치, 즉 2의 위치이다.

과연 윌리암슨수액빨이딱따구리 식구는 어떤 음식에 더 빨리 도착할 수 있을까?

### 입력

첫째 줄에 정보섬 2층의 크기 n과 m이 주어진다. (1 ≤ n,m ≤ 3000, 4 ≤ n×m ≤ 9×106)

이후 n행 m열에 걸쳐 0, 1, 2, 3, 4, 5로만 구성된 Ai,j가 주어진다. Ai,j와 Ai,j+1사이에 공백은 주어지지 않는다.

2, 3, 4, 5는 반드시 하나씩 존재하며 2, 3, 4, 5가 아닌 나머지는 0 또는 1이다.

### 출력

첫째 줄에 "TAK"(폴란드어로 YES를 의미)을 출력하고, 둘째 줄에 현위치에서 가장 빨리 도착할 수 있는 음식까지의 최단 거리를 출력한다.

아무 음식도 먹을 수 없으면 "NIE"(폴란드어로 NO를 의미)를 출력한다. 이외의 출력은 하지 않는다.

TAK과 NIE를 출력할 때 따옴표는 출력하지 않으며 반드시 대문자로 출력한다.

### 알고리즘 설계

간단한 bfs문제였다.
시작점 2의 위치를 찾고, 해당 위치에서부터 사방으로 이동하면서 cnt에 이동한 횟수를 기재한다. 동시에 이동한 위치는 visited에 1로 표시하여 주어, 이후에 재방문 하지 않도록 한다. 이동하면서 음식(3,4,5)를 만나면 그 즉시 종료한다.

### 코드

```js
const fs = require("fs");
const [arr, ...input] = fs.readFileSync("./sample.txt").toString().split("\n");
const [n, m] = arr.split(" ").map(Number);
const A = input.map((el) => el.split("").map(Number));
const foods = [3, 4, 5];
let result = 0;

const visited = [...new Array(n)].map((el) => [...new Array(m)].fill(0));
let si, sj;
let d = 0;
for (let i = 0; i < n; i++) {
  for (let j = 0; j < m; j++) {
    if (A[i][j] === 2) {
      si = i;
      sj = j;
    }
  }
}

const dir = [
  [0, 1],
  [1, 0],
  [0, -1],
  [-1, 0],
];

const bfs = (i, j, distance) => {
  const queue = [[i, j, distance]];
  visited[i][j] = 1;
  while (queue.length) {
    const [ci, cj, td] = queue.shift();
    for (const [di, dj] of dir) {
      const [ni, nj] = [ci + di, cj + dj];
      if (ni >= 0 && ni < n && nj >= 0 && nj < m) {
        if (foods.includes(A[ni][nj])) {
          // 음식이라면
          result = td + 1;
          return;
        } else if (A[ni][nj] === 0 && visited[ni][nj] === 0) {
          // 방문 안했고, 통로라면 방문 표시하고 queue에 들어가
          visited[ni][nj] = 1;
          queue.push([ni, nj, td + 1]);
        }
      }
    }
  }
};
bfs(si, sj, d);

console.log(result > 0 ? `TAK\n${result}` : `NIE`);
```
