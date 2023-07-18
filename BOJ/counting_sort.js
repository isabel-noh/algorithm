const fs = require("fs");
const [n, ...input] = fs.readFileSync("./sample.txt").toString().split("\n");
const N = +n;
const arr = input.map((el) => +el);
const num_count_arr = new Array(10001).fill(0);

for (let i = 0; i < arr.length; i++) {
  num_count_arr[arr[i]]++;
}
for (let i = 0; i < num_count_arr.length; i++) {
  if (num_count_arr[i] != 0) {
    for (let j = 0; j < num_count_arr[i]; j++) {
      console.log(i);
    }
  }
}
