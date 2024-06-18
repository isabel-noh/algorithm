# 정수 직사각형

[정수 직사각형](https://www.acmicpc.net/problem/9196)

### 문제

높이 h와 너비 w가 자연수인 직사각형을 정수 직사각형이라고 한다. 넓은 정수 직사각형은 w가 h보다 큰 (w>h)인 정수 직사각형이라고 한다.

넓은 정수 직사각형의 순서는 다음과 같이 정할 수 있다. 두 직사각형이 있을 때,

- 대각선의 길이가 짧은 쪽이 작다.
- 대각선의 길이가 같은 경우에는 높이가 작은 것이 작다.

넓은 정수 직사각형이 주어졌을 때, 그 직사각형보다 큰 직사각형 중 가장 작은 것을 찾는 프로그램을 작성하시오.

### 입력

입력은 여러 개의 테스트 케이스로 이루어져 있다. 테스트 케이스의 개수는 100개를 넘지 않는다. 각 테스트 케이스는 넓은 정수 직사각형의 높이와 너비 h, w이 공백으로 구분되어서 주어진다.

h와 w(>h)는 0보다 크며, 100을 넘지 않는다.

입력의 마지막 줄에는 0이 두 개 주어진다.

### 출력

각 테스트 케이스에 대해서, 입력으로 주어진 넓은 정수 직사각형보다 큰 직사각형 중 가장 작은 넓은 정수 직사각형의 높이와 너비를 출력한다. 이 값은 150을 넘지 않는다.

### 알고리즘 설계

두 가지를 기억해야한다.

1. 대각선의 길이가 짧은 쪽이 작다.
2. 대각선의 길이가 같은 경우에는 높이가 작은 것이 작다.

위 두가지는 현재 사각형과 주어진 사각형(std), 이전에 std보다 크지만 제일 작다고 생각했던 사각형과의 관계에서 비교할 때 모두 적용되어야 한다.

처음에는 기준 h보다 큰것, 기준 w보다 큰것만 고려했었지만 문제를 다시 잘 보면 h가 기준 h보다 작을 수도 있다는 것을 볼 수 있다. 따라서 h와 w 모두 1부터 확인하기로 하였다.  
또한 h는 반드시 w보다 작으며 (`h < w`), 높이와 너비는 150을 절대 넘지 않는다.

문제에서 조건을 분기하면서 해결하였다.
다음 h,w,d는 한 세트이다.
`[h, w, standard_diagonal]`  
`[smallestH, smallestW, smallestD]`  
`[i, j, new_diagonal]`

1. standard_diagonal보다 new_diagonal가 큰가?
   1. 이전에 제일 작은 줄 알았던 사각형 smallestD보다 new_diagonal의 대각선이 작은가?
      1. new_diagonal의 사각형이 제일 작은 사각형
   2. smallestD과 new_diagonal의 대각선이 같은가?
      1. smallestH보다 new_diagonal의 h가 더 작다면, new_diagonal이 제일 작은 사각형
2. standard_diagonal랑 d랑 같은가?
   1. 기준 h가 new_diagonal의 h(i)보다 작은 가? (standard_diagonal이 new_diagonal보다 작다는 의미)
      1. 이전에 제일 작은 줄 알았던 사각형 smallestD보다 new_diagonal의 대각선이 작은가?
         1. new_diagonal의 사각형이 제일 작은 사각형
      2. smallestD과 new_diagonal의 대각선이 같은가?
         1. smallestH보다 new_diagonal의 h가 더 작다면, new_diagonal이 제일 작은 사각형

### 코드

```js
const fs = require("fs");
const input = fs
  .readFileSync("./sample.txt")
  .toString()
  .split("\n")
  .map((el) => el.split(" ").map(Number));

const MAX_NUM = 150;

input.forEach((el) => {
  const [h, w] = el;
  let smallerH = 0,
    smallerW = 0,
    smallerD = 20000;

  if (h !== 0 && w !== 0) {
    const standard_diagonal = h ** 2 + w ** 2;

    for (let i = 1; i < MAX_NUM; i++) {
      for (let j = i + 1; j < MAX_NUM; j++) {
        // 왜 i+1부터 시작하냐면, w는 무조건 h보다 크니까
        if (i !== j) {
          const new_diagonal = i ** 2 + j ** 2;

          // 우리가 찾는 사각형은 대각선 길이가 standard보다는 길거나 같은 길이어야 해.
          if (standard_diagonal < new_diagonal) {
            if (new_diagonal < smallerD) {
              // 근데 이전에 확인 중이던 대각선보다는 짧아야 돼
              smallerD = new_diagonal;
              smallerH = i;
              smallerW = j;
            } else if (new_diagonal === smallerD && smallerH > i) {
              smallerH = i;
              smallerW = j;
            }
          } else if (standard_diagonal === new_diagonal && h < i) {
            // 기준 사각형이랑 대각선이 같은데, h가 더 낮다면
            if (new_diagonal < smallerD) {
              smallerD = new_diagonal;
              smallerH = i;
              smallerW = j;
            } else if (new_diagonal === smallerD && smallerH > i) {
              smallerH = i;
              smallerW = j;
            }
          }
        }
      }
    }
    console.log(smallerH + " " + smallerW);
  }
});
```

### 시간 복잡도

O(n)

### 느낀 점 / 기억할 점

조건이 많아 헷갈릴 때에는 글로 정리를 하면서 풀어보자.
