# Programmers 완전탐색 - 카펫

[Programmers 완전탐색 - 카펫](https://school.programmers.co.kr/learn/courses/30/lessons/42842)

## 문제 설명

Leo는 카펫을 사러 갔다가 아래 그림과 같이 중앙에는 노란색으로 칠해져 있고 테두리 1줄은 갈색으로 칠해져 있는 격자 모양 카펫을 봤습니다.

Leo는 집으로 돌아와서 아까 본 카펫의 노란색과 갈색으로 색칠된 격자의 개수는 기억했지만, 전체 카펫의 크기는 기억하지 못했습니다.

Leo가 본 카펫에서 갈색 격자의 수 brown, 노란색 격자의 수 yellow가 매개변수로 주어질 때 카펫의 가로, 세로 크기를 순서대로 배열에 담아 return 하도록 solution 함수를 작성해주세요.

### 제한사항

갈색 격자의 수 brown은 8 이상 5,000 이하인 자연수입니다.
노란색 격자의 수 yellow는 1 이상 2,000,000 이하인 자연수입니다.
카펫의 가로 길이는 세로 길이와 같거나, 세로 길이보다 깁니다.

### 입출력 예

| brown | yellow | return |
| ----- | ------ | ------ |
| 10    | 2      | [4, 3] |
| 8     | 1      | [3, 3] |
| 24    | 24     | [8, 6] |

#### 문제풀이

위 문제에서 brown은 전체 넓이의 테두리 부분, yellow는 그 안 부분이 된다. 그러므로, yellow는 `(가로 - 2) * (세로 - 2)`가 된다.
그 다음, brown과 yellow를 합하면 전체 카펫의 넓이가 나온다. 전체 넓이(totalArea)를 나눴을 때 0으로 떨어지는 나누는 수와 몫이 가능한 가로x세로 후보군이 될 것이다.

이 후보군을 굳이 1부터 N까지 다 확인해보지 않아도 된다. 1xN은 어차피 나눠질테니 2부터 확인한다. 그러면 어디까지 확인해보면 될까?  
48을 예로 들어보자. 48의 경우, 나눠지는 몫과 수를 따져보면 `2x24`, `3x16`, `4x12`, `6x8`, ... `24x2`, `48x1`이 될 것이다. 하지만 여기에서 8x6부터 48x1까지는 앞의 내용과 중복된 수들의 곱이다. `Math.sqrt(N)`, 즉 N의 제곱근까지만 확인하면 중복된 수들의 조합을 확인하지 않아도 된다. 만일 N이 어떤 수`n`의 제곱이라면 `n`이 두번 곱해지는 것이 N이 된다. 그 말인 즉슨, 1xN ,... ,nxn, ... Nx1로 nxn을 기점으로 데칼코마니가 된다는 말이다. 따라서 N의 제곱근까지만 확인하면 문제를 풀이할 수 있다.

```js
function solution(brown, yellow) {
  var answer = [];
  let width = 0,
    height = 0;
  // width >= height

  let totalArea = brown + yellow;
  for (let i = 2; i <= Math.sqrt(totalArea); i++) {
    let divide;
    if (totalArea % i === 0) {
      divide = Math.floor(totalArea / i);
    }
    if ((divide - 2) * (i - 2) === yellow) {
      width = divide;
      height = i;
    }
  }
  answer = [width, height];
  return answer;
}
solution(10, 2);
solution(8, 1);
solution(24, 24);
```
