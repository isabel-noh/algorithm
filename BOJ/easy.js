const fs = require("fs");
const [input, d] = fs.readFileSync("./sample.txt").toString().split("\n");

const arr = input.split(" ").map((el) => +el);

function solution(a, d) {
  let total_sec = d;
  let hour = 0;
  let minute = 0;
  let second = 0;
  while (total_sec > 0) {
    if (total_sec >= 3600) {
      hour = Math.floor(total_sec / 3600);
      total_sec = total_sec % 3600;
    } else if (total_sec >= 60) {
      minute = Math.floor(total_sec / 60);
      total_sec = total_sec % 60;
    } else {
      second = total_sec;
      break;
    }
  }
  return [hour, minute, second];
}

function check(h, m, s) {
  let hour = h;
  let minute = m;
  let second = s;
  while (hour > 23 || minute > 59 || second > 59) {
    if (hour > 23) {
      hour = hour - 24;
    } else if (minute > 59) {
      minute = minute - 60;
      hour += 1;
    } else if (second > 59) {
      second = second - 60;
      minute += 1;
    }
  }
  return [hour, minute, second];
}

const [hour, minute, second] = solution(arr, +d);
const [h, m, s] = check(arr[0] + hour, arr[1] + minute, arr[2] + second);
console.log(h, m, s);
