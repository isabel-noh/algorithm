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
const [a, b] = fs.readFileSync("./sample.txt").toString().split("\n");

function longCommonSubsequence(str1, str2) {
  if (str1 === str2) {
    return str1.length;
  }

  dp = [...new Array(str1.length + 1)].map((el) =>
    new Array(str2.length + 1).fill(0)
  );
  for (let i = 1; i < str1.length + 1; i++) {
    for (let j = 1; j < str2.length + 1; j++) {
      if (str1[i - 1] === str2[j - 1]) {
        dp[i][j] = dp[i - 1][j - 1] + 1;
      } else {
        dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
      }
    }
  }
  return dp[str1.length][str2.length];
}

console.log(longCommonSubsequence(a, b));
