// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(A) {
  // Implement your solution here
  const dp = new Array(A.length).fill(0);
  // how select the elements to be merged ?..
  let a = 0,
    b = 0;
  for (let i = 0; i < A.length; i++) {
    if (i === 0) {
      // 1st element
      dp[i] = A[i];
    } else if (i === 1) {
      // 2nd element
      dp[i] = Number(String(dp[i - 1]) + String(A[i]));
    } else {
      dp[i] = Math.max(
        dp[i - 2] + Number(String(A[i - 1]) + String(A[i])),
        dp[i - 1] + A[i]
      );
    }
  }
  return dp[dp.length - 1];
}

solution([2, 2, 3, 5, 4, 0]);
solution([3, 19, 191, 91, 3]);
solution([12, 6, 18, 10, 1, 0]);
solution([2, 1, 0, 1, 2, 9, 1, 0]);
