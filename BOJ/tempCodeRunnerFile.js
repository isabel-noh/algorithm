const fs = require("fs");
// const input = fs.readFileSync("/dev/stdin");
const [a, ...input] = fs
  .readFileSync("./sample.txt")
  .toString()
  .trim()
  .split("\n");
const [N, H] = a.split(" ");

let answer = 0;

function solution(n, h, arr) {
  const imos = Array(h).fill(0); // 1차원 배열에 표기하는 방법 - 한 행 당 지나가는 장애물 표시
  // [0, 0, 0, 0, 0, 0, 0]
  for (let i = 0; i < n; i++) {
    let height = +arr[i];
    if (i % 2 === 0) {
      // 올라가는 장애물
      for (let j = h - 1; j > height; j--) {
        imos[j] += 1;
      }
    } else {
      // 내려가는 장애물
      for (let j = 0; j < height; j++) {
        imos[j] += 1;
      }
    }
  }

  let min = Math.min(...imos);
  let cnt = imos.filter((el) => el === min).length;

  console.log(min, cnt);
}

solution(+N, +H, input);
