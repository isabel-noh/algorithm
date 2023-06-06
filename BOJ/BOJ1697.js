// BOJ 1697 숨바꼭질
// [BOJ 1697 숨바꼭질](https://www.acmicpc.net/problem/1697)

// 문제
// 수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.

// 수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.

// 입력
// 첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.

// 출력
// 수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.

// 힌트
// 수빈이가 5-10-9-18-17 순으로 가면 4초만에 동생을 찾을 수 있다.

const fs = require("fs");
// const input = fs.readFileSync("/dev/stdin").toString().trim().split(" ");
const input = fs.readFileSync("./sample.txt").toString().trim().split(" ");
const n = parseInt(input[0]);
const k = parseInt(input[1]);

function bfs(n, k) {
  const queue = [n];
  const visited = [];
  for (let i = 0; i <= 20; i++) {
    visited.push(-1);
  }
  visited[n] = 0;
  while (queue.length > 0) {
    let cur = queue.shift();
    var new_cur;
    if (cur === k) {
      return visited[cur];
    }
    for (let i = 0; i < 3; i++) {
      if (i === 0) {
        new_cur = cur - 1;
      } else if (i === 1) {
        new_cur = cur + 1;
      } else if (i === 2) {
        new_cur = cur * 2;
      }

      if (visited[new_cur] === -1 && cur >= 0 && cur <= 100000) {
        queue.push(new_cur);
        visited[new_cur] = visited[cur] + 1;
      }
    }
  }
}

let res = bfs(n, k);
console.log(res);
