// BOJ 1475 방 번호
// https://www.acmicpc.net/problem/1475

// 문제
// 다솜이는 은진이의 옆집에 새로 이사왔다. 다솜이는 자기 방 번호를 예쁜 플라스틱 숫자로 문에 붙이려고 한다.

// 다솜이의 옆집에서는 플라스틱 숫자를 한 세트로 판다. 한 세트에는 0번부터 9번까지 숫자가 하나씩 들어있다. 다솜이의 방 번호가 주어졌을 때, 필요한 세트의 개수의 최솟값을 출력하시오. (6은 9를 뒤집어서 이용할 수 있고, 9는 6을 뒤집어서 이용할 수 있다.)

// 입력
// 첫째 줄에 다솜이의 방 번호 N이 주어진다. N은 1,000,000보다 작거나 같은 자연수이다.

// 출력
// 첫째 줄에 필요한 세트의 개수를 출력한다.

const fs = require("fs");
const n = fs.readFileSync("./sample.txt").toString().trim();
// 0~9까지 한 세트
// 6, 9 는 교체 가능
let answer = 0;
const arr = new Array(10).fill(0); // 0부터 9까지니까 10개짜리 counting 배열 선언

for (let i = 0; i < n.length; i++) {
  const letter = n[i];
  arr[+letter] += 1;
}
function check6and9(a) {
  // 6이랑 9가 몇 개 있는지가 관건
  const count = a[6] + a[9];
  return Math.ceil(count / 2);
}
const sixnine = check6and9(arr);
// 6번째와 9번째는 몇개가 필요지 세었으니 0으로 초기화
arr[6] = 0;
arr[9] = 0;
if (sixnine > Math.max(...arr)) {
  answer = sixnine;
} else {
  answer = Math.max(...arr);
}
console.log(answer);
