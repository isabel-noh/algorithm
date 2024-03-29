// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(N) {
  // Implement your solution here
  let answer = "";
  // N : length of String
  // initial String : 'a' * N
  let n = N;
  const arr = [];
  for (let i = 0; i < 26; i++) {
    arr.push(2 ** i);
  }
  while (n > 0) {
    inner: for (let i = 0; i < arr.length; i++) {
      if (n > arr[arr.length - 1]) {
        // current n is smaller than
        answer += "z";
        n -= arr[arr.length - 1];
        break inner;
      } else if (n === arr[i]) {
        answer += String.fromCharCode(97 + i);
        n -= arr[i];
        break inner;
      } else if (n < arr[i]) {
        // current n is smaller than arr[i]
        answer += String.fromCharCode(97 + i - 1);
        n -= arr[i - 1];
        break inner;
      }
    }
  }
  return answer;
}
solution(11);
solution(1);
solution(67108876);
solution(1000000000);
