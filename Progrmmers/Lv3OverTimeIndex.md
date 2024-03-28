# Programmers - 야근 지수

[Programmers - 야근 지수](https://school.programmers.co.kr/learn/courses/30/lessons/12927)

## 문제 설명

회사원 Demi는 가끔은 야근을 하는데요, 야근을 하면 야근 피로도가 쌓입니다. 야근 피로도는 야근을 시작한 시점에서 남은 일의 작업량을 제곱하여 더한 값입니다. Demi는 N시간 동안 야근 피로도를 최소화하도록 일할 겁니다.Demi가 1시간 동안 작업량 1만큼을 처리할 수 있다고 할 때, 퇴근까지 남은 N 시간과 각 일에 대한 작업량 works에 대해 야근 피로도를 최소화한 값을 리턴하는 함수 solution을 완성해주세요.

### 제한 사항

- works는 길이 1 이상, 20,000 이하인 배열입니다.
- works의 원소는 50000 이하인 자연수입니다.
- n은 1,000,000 이하인 자연수입니다.

```js
function solution(n, works) {
  var answer = 0;
  // 남은 작업량**2

  // 총 남은 작업의 양이 내가 할 수 있는 작업 시간보다 적으면 바로 리턴
  const sum = works.reduce((acc, cur) => acc + cur, 0);
  if (sum <= n) return answer;

  const sorted = [...works].sort((a, b) => a - b);
  // 평탄화
  while (n) {
    const max = sorted[sorted.length - 1];
    for (let i = sorted.length - 1; i >= 0; i--) {
      // 뒤에서부터 보면서 젤 큰 값에서 max보다 크거나 같으면 -1 ,
      // 어떻게 max보다 크거나 같은 값이 나올 수 있느냐? [3, 3, 3]와 같은 배열이 있을 때, 3에서 먼저 1을 빼면 [3, 3, 2]가 되고 arr[1]은 max보다 큰 상황이 된다. 즉, 처음에 max랑 값이 같은 것들을 처리하기 위함
      // 한바퀴 for문 다돌면 어차피 정렬된 채로 하향평준화 된 상태일테니 n이 0이 될 때까지 반복
      if (sorted[i] >= max) {
        sorted[i] -= 1;
        n -= 1;
      }
      if (n === 0) break;
    }
  }
  answer = sorted.reduce((acc, cum) => acc + cum ** 2, 0);
  return answer;
}
```
