const fs = require("fs");
const [n, ...input] = fs.readFileSync("./sample.txt").toString().split("\n");
const N = +n;
const arr = input.map((el) => +el);

function quick_sort(a) {
  if (a.length < 2) {
    return a;
  }
  let val = a[0];
  let pivot = [];
  let low = [];
  let high = [];
  for (let i = 0; i < a.length; i++) {
    if (a[i] > val) {
      high.push(a[i]);
      continue;
    } else if (a[i] < val) {
      low.push(a[i]);
    } else {
      pivot.push(a[i]);
    }
  }
  return quick_sort(low).concat(pivot, quick_sort(high));
}
console.log(...quick_sort(arr));
