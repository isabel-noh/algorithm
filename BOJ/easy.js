// import sys
// sys.stdin = open('./sample.txt')

// def solution(num, a):
//     dp = [[0] * (num) for _ in range(2)]
//     for i in range(num):
//         if i == 0:
//             dp[0][i], dp[1][i] = a[0][i], a[1][i]
//         elif i == 1:
//             dp[0][i] = dp[1][i-1] + arr[0][i]
//             dp[1][i] = dp[0][i-1] + arr[1][i]
//         else:
//             dp[0][i] = arr[0][i] + max(dp[1][i-1], dp[0][i-2], dp[1][i-2])
//             dp[1][i] = arr[1][i] + max(dp[0][i-1], dp[0][i-2], dp[1][i-2])
//     result = max(max(dp[0]), max(dp[1]))
//     return result

// T = int(input())
// for t in range(T):
//     n = int(input())
//     arr = [list(map(int, input().split())) for _ in range(2)]
//     print(solution(n, arr))

const fs = require("fs");
const [T, ...input] = fs.readFileSync("./sample.txt").toString().split("\n");

function solution(n, arr) {
  const dp = [...new Array(2)].map((el) => new Array(n).fill(0));
  for (let i = 0; i < n; i++) {
    if (i === 0) {
      dp[0][i] = arr[0][i];
      dp[1][i] = arr[1][i];
    } else if (i === 1) {
      dp[0][i] = dp[1][i - 1] + arr[0][i];
      dp[1][i] = dp[0][i - 1] + arr[1][i];
    } else {
      dp[0][i] = arr[0][i] + Math.max(dp[1][i - 1], dp[0][i - 2], dp[1][i - 2]);
      dp[1][i] = arr[1][i] + Math.max(dp[0][i - 1], dp[0][i - 2], dp[1][i - 2]);
    }
  }
  const max_a = Math.max(...dp[0]);
  const max_b = Math.max(...dp[1]);
  const result = Math.max(max_a, max_b);
  return result;
}
for (let t = 0; t < +T; t++) {
  const num = input.shift();
  const arr = [];
  const arr1 = input
    .shift()
    .split(" ")
    .map((el) => +el);
  const arr2 = input
    .shift()
    .split(" ")
    .map((el) => +el);
  arr.push(arr1);
  arr.push(arr2);
  console.log(solution(+num, arr));
}
