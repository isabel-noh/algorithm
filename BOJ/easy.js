const fs = require("fs");
const [m, ...input] = fs.readFileSync("./sample.txt").toString().split("\n");

const [k, n] = m.split(" ").map((e) => +e);
const arr = input.map((e) => +e).sort((a, b) => a - b);
// k <= n
// 랜선을 모두 N개의 같은 길이의 랜선으로 만들고 싶었기 때문에 K개의 랜선을 잘라서 만들어야 한다.
// 최대 랜선의 길이

let answer = 0;

let left = 0;
let right = arr[arr.length - 1];
console.log(left, right);

while (left <= right) {
  let count = 0;
  const mid = Math.floor((left + right) / 2);
  for (let i = 0; i < arr.length; i++) {
    count += Math.floor(arr[i] / mid);
  }

  if (count >= n) {
    answer = mid;
    left = mid + 1;
  } else {
    right = mid - 1;
  }
}

console.log(right);
