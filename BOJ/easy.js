const fs = require("fs");
// 과자 한 개의 가격이 K, 사려고 하는 과자의 개수가 N이고, 현재 가진 돈의 액수를 M이라 할 때 여러분은 동수가 부모님께 받아야 하는 모자란 돈을 계산하려고 한다.
const [k, n, m] = fs.readFileSync("./sample.txt").toString().split(" ");
let mommyYongdon = 0;
const totalPrice = +k * +n;
mommyYongdon = totalPrice - +m;
console.log(mommyYongdon);
