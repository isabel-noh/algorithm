const fs = require("fs");
const str = fs.readFileSync("./sample.txt").toString();
const [A, C] = str.split("\n");
let [a, b] = A.split(" ").map((el) => +el);
let c = +C;

b = b + c;
if (b > 59) {
  let nameoji = b % 60;
  let mok = Math.floor(b / 60);
  b = nameoji;
  a += mok;
}
if (a > 23) {
  a -= 24;
}
console.log(a, b);
