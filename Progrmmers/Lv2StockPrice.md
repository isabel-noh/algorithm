# Programmers Stack / Queue - Stock price

[Programmers Stack / Queue - Stock price](https://school.programmers.co.kr/learn/courses/30/lessons/42584)

## 문제 설명

초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.

### 제한사항

- prices의 각 가격은 1 이상 10,000 이하인 자연수입니다.
- prices의 길이는 2 이상 100,000 이하입니다.

### 입출력 예

| prices          | return          |
| --------------- | --------------- |
| [1, 2, 3, 2, 3] | [4, 3, 1, 1, 0] |

### 입출력 예 설명

1초 시점의 ₩1은 끝까지 가격이 떨어지지 않았습니다.
2초 시점의 ₩2은 끝까지 가격이 떨어지지 않았습니다.
3초 시점의 ₩3은 1초뒤에 가격이 떨어집니다. 따라서 1초간 가격이 떨어지지 않은 것으로 봅니다.
4초 시점의 ₩2은 1초간 가격이 떨어지지 않았습니다.
5초 시점의 ₩3은 0초간 가격이 떨어지지 않았습니다.

#### 문제풀이 1. 시간초과 -> while문에 for문 사용해서인 듯

```js
function solution(prices) {
  var answer = []; // 가격이 떨어지지 않은 기간은 몇 초인지를 return
  const p = [...prices];
  while (p.length > 0) {
    const price = p.shift();
    let flag = true;
    let cnt = 0;
    for (let index = 0; index < p.length; index++) {
      cnt++;
      if (p[index] < price) {
        flag = false;
        break;
      }
    }
    answer.push(cnt);
  }
  return answer; // [4, 3, 1, 1, 0]
}
```

#### 문제풀이 2.

stack은 `상태 추적`으로 사용할 수 있다.  
상태 추적: 스택을 사용하면 상태를 추적하거나 복구해야 할 때 유용하다.예를 들어, 게임 상태의 이력을 저장하거나 다른 상황에서 상태를 복원하는 데 사용할 수 있다.  
아래 코드에서는 stack을 상태 추적의 용도로 사용하였다. 주식 가격이 상승하고 있다는 상태를 기록한다.

1. 가격이 떨어지지 않는 경우, stack에 저장
2. 가격이 떨어지는 경우, stack에 저장된 상승장의 정보 중 최근 가격 정보와 비교

가격이 떨어지지 않아왔던 list 중에서 최근 기록들(stack은 후입선출이므로) 중에서 현재 가격(prices[i])과 비교했을 때, 더 큰 기록은 더이상 가격이 이어지지 못하고, 현재 위치(i)에서 기간이 멈추기 때문에, 이를 비교하는 것이다.

```js
function solution(prices) {
  const answer = new Array(prices.length).fill(0); // 가격이 떨어지지 않은 기간은 몇 초인지를 return
  const stack = []; // 가격이 떨어지지 않는 경우의 index를 저장할 배열
  for (let i = 0; i < prices.length; i++) {
    if (i === 0) {
      stack.push(i);
    } else if (prices[i] >= prices[i - 1]) {
      // 1. 가격이 떨어지지 않는 경우, stack에 저장
      stack.push(i);
    } else if (prices[i] < prices[i - 1]) {
      // 2. 가격이 떨어지는 경우, stack에 저장된 상승장의 정보 중 최근 가격 정보와 비교
      while (stack.length) {
        // 가격이 떨어지지 않아왔던 list 중에서 최근 기록들 (stack은 후입선출이므로) 중에서 현재 가격(prices[i])과 비교했을 때, 더 큰 기록은 더이상 가격이 이어지지 못하고, 현재 위치 (i)에서 기간이 멈추기 때문에, 이를 비교하는 것임
        if (prices[stack[stack.length - 1]] > prices[i]) {
          // 상승장의 가격정보들과 비교하여 현재 가격(하락장)보다 가격이 높은 경우, 꺼내어 answer에 (현재 위치 - 해당 가격의 idx)를 저장
          // 현재 가격보다 높은 가격이 하락하지 않는 기간은 현재 위치까지이므로
          const idx = stack.pop();
          answer[idx] = i - idx;
        } else {
          // stack의 마지막 가격이 현재 가격보다 작거나 같은 경우, pass
          break;
        }
      }
      stack.push(i); // 현재 주식 가격 stack에 저장 -> 다음 가격들과 비교하기 위해서 기록
    }
  }

  while (stack.length) {
    // stack에 남은 기록들이 있다면, 이들은 마지막까지 가격이 떨어지지 않은 것
    const idx = stack.pop();
    answer[idx] = prices.length - idx - 1;
  }
  return answer; // [4, 3, 1, 1, 0]
}
```
