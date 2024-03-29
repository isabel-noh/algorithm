// // you can write to stdout for debugging purposes, e.g.
// // console.log('this is a debug message');

// function solution(A) {
//   let answer = 1;
//   // Implement your solution here
//   const sortedA = [...A].sort((a, b) => a - b);

//   if (sortedA[sortedA.length - 1] <= 0) {
//     answer = 1;
//   } else {
//     const arr = new Array(sortedA[sortedA.length - 1]).fill(0);
//     for (let i = 0; i < sortedA.length; i++) {
//       if (sortedA[i] <= 0) {
//         continue;
//       } else {
//         arr[sortedA[i] - 1]++;
//       }
//       if (arr[sortedA[i] - 2] === 0 && sortedA[i] >= 0) {
//         answer = sortedA[i] - 1;
//         break;
//       }
//     }
//     if (!arr.includes(0)) {
//       answer = sortedA[sortedA.length - 1] + 1;
//     }
//   }
//   console.log(answer);
//   return answer;
// }
// solution([1, 3, 6, 4, 1, 2]);
// solution([1, 2, 3]);
// solution([-3, -1]);

// // 44%

const visited = [...new Array(2)].map(() => new Array(2).fill(0));
console.log(visited);
