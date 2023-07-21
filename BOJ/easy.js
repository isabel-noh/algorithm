const fs = require("fs");
const input = fs.readFileSync("./sample.txt").toString().split("\n");
function check(str) {
  const stack = [];
  for (let i = 0; i < str.length; i++) {
    const bracket = str[i];
    if (["[", "(", "{"].includes(bracket)) {
      // 여는 괄호일 때
      stack.push(str[i]);
    } else if (["]", ")", "}"].includes(bracket)) {
      // 닫는 괄호일 때, stack의 마지막 문자가 같은 괄호 종류의 여는 괄호일 경우 해당 stack의 값을 pop하고, 아닐 경우 stack에 넣는다.
      if (bracket === "]") {
        if (stack[stack.length - 1] === "[") {
          stack.pop();
        } else {
          stack.push(bracket);
        }
      } else if (bracket === "}") {
        if (stack[stack.length - 1] === "{") {
          stack.pop();
        } else {
          stack.push(bracket);
        }
      } else if (bracket === ")") {
        if (stack[stack.length - 1] === "(") {
          stack.pop();
        } else {
          stack.push(bracket);
        }
      }
    }
  }
  if (stack.length > 0) {
    console.log("no");
  } else {
    console.log("yes");
  }
}

for (let i = 0; i < input.length; i++) {
  if (input[i] === ".") {
    break;
  }
  check(input[i]);
}
