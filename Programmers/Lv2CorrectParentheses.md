# Programmers Stack/Queue - Right Parentheses

[Programmers Stack/Queue - Right Parentheses ](https://school.programmers.co.kr/learn/courses/30/lessons/12909)

## 문제 설명

괄호가 바르게 짝지어졌다는 것은 '(' 문자로 열렸으면 반드시 짝지어서 ')' 문자로 닫혀야 한다는 뜻입니다. 예를 들어

"()()" 또는 "(())()" 는 올바른 괄호입니다.
")()(" 또는 "(()(" 는 올바르지 않은 괄호입니다.
'(' 또는 ')' 로만 이루어진 문자열 s가 주어졌을 때, 문자열 s가 올바른 괄호이면 true를 return 하고, 올바르지 않은 괄호이면 false를 return 하는 solution 함수를 완성해 주세요.

### 제한사항

- 문자열 s의 길이 : 100,000 이하의 자연수
- 문자열 s는 '(' 또는 ')' 로만 이루어져 있습니다.

### 입출력 예

| s        | answer |
| -------- | ------ |
| "()()"   | true   |
| "(())()" | true   |
| ")()("   | false  |
| "(()("   | false  |

#### 문제풀이

간단히 stack을 활용하여 풀이하는 문제이다.

1. char이 여는 괄호인 경우, stack에 넣는다.
2. char 이 닫는 괄호인 경우, stack의 마지막 기호가 여는 괄호인 경우, 세트가 되므로 stack의 마지막 괄호를 pop한다.
3. stack의 마지막 기호가 닫는 괄호인 경우, char을 stack에 넣는다.
4. string을 모두 돈 뒤, stack에 여전히 세트가 되지 못하여 남은 괄호가 있다면, 이는 올바른 괄호가 아니므로 answer = false가 된다.

```js
function solution(s) {
  var answer = true;
  const stack = [];
  for (const char of s) {
    if (char === "(") {
      stack.push(char);
    } else {
      if (stack[stack.length - 1] === "(") {
        stack.pop();
      } else {
        stack.push(char);
      }
    }
  }
  if (stack.length > 0) {
    answer = false;
  }

  return answer;
}
```
