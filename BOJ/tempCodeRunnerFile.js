const fs = require("fs");
const [nm, numbers, ...arr] = fs
  .readFileSync("./sample.txt")
  .toString()
  .split("\n")
  .map((el) => el.split(" ").map(Number));
const [N, M] = nm;

const results = [];
for (const [i, j] of arr) {
  let sum = 0;
  for (let l = i - 1; l <= j - 1; l++) {
    sum += numbers[l];
  }
  results.push(sum);
}
console.log([...results].join("\n"));
