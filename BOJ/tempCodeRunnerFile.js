
const arr = input.split(" ").map(Number);
const dp = [...new Array(+n)].fill(0);
const countDp = [...new Array(+n)].fill(1);
dp[0] = arr[0];
for (let i = 1; i < +n; i++) {
  let maxIdx = 0;
  let maxValue = 0;
  for (let j = 0; j < i; j++) {
    if (maxValue <= dp[j]) {
      maxValue = dp[j];
      maxIdx = j;
    }
  }
  console.log(i, maxIdx, maxValue);
  if (maxValue >= arr[i]) {
    dp[i] = maxValue + arr[i];
    countDp[i] = countDp[maxIdx] + 1;
  } else {
    dp[i] = arr[i];
  }
  //   if (dp[i - 1] >= arr[i]) {
  //     dp[i] = dp[i - 1] + arr[i];
  //     countDp[i] += 1;
  //   } else {
  //     dp[i] = arr[i];
  //   }
}
console.log(dp);
console.log(countDp);
console.log(Math.max(...countDp));