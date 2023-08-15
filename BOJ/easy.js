const fs = require("fs");
let n = fs.readFileSync("./sample.txt").toString().trim();
let num = +n;
let cnt = 0;
while (true) {
  cnt++;
  temp = Math.floor(num / 10) + (num % 10);
  num = (num % 10) * 10 + (temp % 10);
  if (num === Number(n)) {
    break;
  }
}
console.log(cnt);
