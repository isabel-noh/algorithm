const fs = require("fs");
const [...input] = fs.readFileSync("./sample.txt").toString().split("");

let cnt = new Map();
// Map에서는 foreach를 사용할 수 없어서 틀린 것!!!

input.forEach((element) => {
  if (cnt.has(element)) {
    cnt.set(element, cnt.get(element) + 1);
  } else {
    cnt.set(element, 1);
  }
});
// map을 사전 순서에 맞게 정렬하고 다시 map으로 변경
//==========================================
// 로케일(언어, 지역, 국가)에 따라 문자의 정렬 순서를 다르게 설정할 수 있습니다.
// localeCompare 메서드는 두 개의 문자열을 비교하여 다음과 같은 값을 반환합니다:
// 음수(-1): 첫 번째 문자열이 두 번째 문자열보다 사전적으로 앞에 옵니다.
// 0: 두 문자열이 동일하게 정렬됩니다.
// 양수(1): 첫 번째 문자열이 두 번째 문자열보다 사전적으로 뒤에 옵니다.
cnt = new Map(Object.values([...cnt]).sort((a, b) => a[0].localeCompare(b[0])));

let notEvenChar = "";
let notEven = 0;
cnt.forEach((value, key) => {
  if (value % 2) {
    notEven++;
    notEvenChar = key;
  }
});
function makePalindrome(map, notEvenWord, notEven) {
  let result = "";
  for (let [key, val] of map) {
    let t = "";
    for (let i = 0; i < Math.floor(val / 2); i++) {
      t += key;
    }
    result += t;
  }
  const half = result.split("").reverse().join("");
  if (notEven === 1) {
    return result + notEvenWord + half;
  } else {
    return result + half;
  }
}

if (notEven && notEven !== 1) {
  return console.log("I'm Sorry Hansoo");
} else {
  return console.log(makePalindrome(cnt, notEvenChar, notEven));
}
