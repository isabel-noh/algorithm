# BOJ - Silver - 뒤집어진 소수

[BOJ - Silver - 뒤집어진 소수](https://www.acmicpc.net/problem/10859)

### 문제

어제 자다가 알람 시계를 떨어뜨렸는지, 08:15분이 51:80분이 되어 있었다. 그때 나는 디지털로 표시된 어떤 숫자는 180도 뒤집혔을 때도 숫자가 될 수 있다는 걸 깨달았다.

소수 18115211이 디지털로 표시된 그림
18115211이 180도 뒤집혀서 11251181이 되었다. (소수가 아님)

0,2,5,8 은 뒤집혀서도 0,2,5,8 그대로이다.
1은 그냥 왼쪽으로 옮겨진다.
6 은 9가 되고, 9는 6이 된다.
3, 4, 7 은 더 이상 숫자가 아니다.

내가 좋아하는 숫자는 소수이다. 당신이 할 일은 주어진 숫자가 소수인지, 뒤집혀서도 소수인지 확인하는 것이다.

### 입력

첫 번째 줄에 N이 주어진다 (1 ≤ N ≤ 1016).

N의 첫 숫자는 0이 아니다.

### 출력

첫 번째 줄에 N이 소수이고 뒤집혀서도 소수이면 "yes"를 출력하고, 아니면 "no"를 출력한다.

### 알고리즘 설계

`check` 함수로 인자로 들어온 숫자가 소수인지 아닌지 감별합니다.

`check` 함수의 `answer` 변수는 인자로 들어온 숫자의 약수 개수를 셉니다. `answer`이 0이라면 해당 숫자는 소수인 것입니다.

`rotate` 함수로 인자로 들어온 숫자를 180도 뒤집습니다.

해당 숫자에 3,4,7이 들어있으면 어차피 뒤집어도 숫자가 안나오므로, no를 리턴하고 프로그램을 종료합니다.

rotate함수로 input으로 주어진 숫자를 뒤집습니다. → `rotatedNum`

input으로 주어진 숫자와 `rotatedNum` 를 check함수를 돌려서 둘다 소수임이 증명되면 yes를 리턴합니다. 그렇지 않다면 no를 리턴합니다.

### 코드

```js
const fs = require("fs");
const num = fs.readFileSync("./sample.txt").toString().split("");
let rotatedNum = 0;

if (num.includes("3") || num.includes("4") || num.includes("7")) {
  console.log("no");
  return;
}

const rotate = (str) => {
  let init = str.reverse();
  for (let i = 0; i < str.length; i++) {
    if ([0, 1, 2, 5, 8].includes(init[i])) {
      continue;
    } else if (init[i] === "6") init[i] = "9";
    else if (init[i] === "9") init[i] = "6";
  }
  return init;
};
initialNum = +num.join("");
rotatedNum = +rotate(num).join("");

const isPrime = (n) => {
  let answer = 0;
  for (let i = 2; i <= Math.sqrt(n); i++) {
    if (n % i === 0) {
      answer++;
    }
  }
  if (answer || n === 1) return false; // 2이상의 수로 나눠지면 소수가 아님
  return true;
};

// N이 소수인지
if (isPrime(initialNum) && isPrime(rotatedNum)) {
  console.log("yes");
} else {
  console.log("no");
}
```
