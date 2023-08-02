const fs = require("fs");
const [n, input] = fs.readFileSync("./sample.txt").toString().split("\n");
const N = +n;
const arr = input.split(" ").map((el) => +el);

// 맨 처음에는 딸기우유를 한 팩 마신다.
// 딸기우유를 한 팩 마신 후에는 초코우유를 한 팩 마신다.
// 초코우유를 한 팩 마신 후에는 바나나우유를 한 팩 마신다.
// 바나나우유를 한 팩 마신 후에는 딸기우유를 한 팩 마신다.
let drink = 0;
let whatDrank = 0;
for (const el of arr) {
  if (drink === 0) {
    if (el === 0) {
      drink++;
    } else {
      continue;
    }
  } else {
    if (whatDrank === 0 && el === 1) {
      drink++;
      whatDrank = 1;
    } else if (whatDrank === 1 && el === 2) {
      drink++;
      whatDrank = 2;
    } else if (whatDrank === 2 && el === 0) {
      drink++;
      whatDrank = 0;
    }
  }
}

console.log(drink);
