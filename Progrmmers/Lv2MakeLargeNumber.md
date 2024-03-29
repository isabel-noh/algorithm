# Programmers - Greedy - 큰 수 만들기

[Programmers - Greedy - 큰 수 만들기](https://school.programmers.co.kr/learn/courses/30/lessons/42883)

## 문제 설명

어떤 숫자에서 k개의 수를 제거했을 때 얻을 수 있는 가장 큰 숫자를 구하려 합니다.

예를 들어, 숫자 1924에서 수 두 개를 제거하면 [19, 12, 14, 92, 94, 24] 를 만들 수 있습니다. 이 중 가장 큰 숫자는 94 입니다.

문자열 형식으로 숫자 number와 제거할 수의 개수 k가 solution 함수의 매개변수로 주어집니다. number에서 k 개의 수를 제거했을 때 만들 수 있는 수 중 가장 큰 숫자를 문자열 형태로 return 하도록 solution 함수를 완성하세요.

### 제한 조건

- number는 2자리 이상, 1,000,000자리 이하인 숫자입니다.
- k는 1 이상 number의 자릿수 미만인 자연수입니다.

```js
function solution(number, k) {
  const stack = [];
  for (let index = 0; index < number.length; index++) {
    while (
      stack.length > 0 && // stack에 값이 없으면 일단 push
      // stack에 저장된 마지막 숫자보다 현재 확인중인 숫자가 더크고, 없애야 할 숫자의 개수가 남아있다면 -> 기존 숫자를 빼고 현재 숫자를 넣음
      //-> 계속 비교 반복 while
      stack[stack.length - 1] < number[index] &&
      k > 0
    ) {
      k--; // 숫자 하나 뺄 때마다 제거해야되는 숫자 개수 k 하나씩 줄어듦
      stack.pop();
    }
    stack.push(number[index]);
  }
  answer = stack.join("");

  if (k > 0) {
    // 만일 없애야 하는 숫자의 개수 k가 남아있다면 -> 뒤에서 남은 k개 잘라내기~
    const res = stack.splice(0, stack.length - k);
    answer = res.join("");
  }
  return answer;
}
```
