# Programmers - DP - N으로 표현

[Programmers - DP - N으로 표현](https://school.programmers.co.kr/learn/courses/30/lessons/42895)

## 문제 설명

아래와 같이 5와 사칙연산만으로 12를 표현할 수 있습니다.

12 = 5 + 5 + (5 / 5) + (5 / 5)
12 = 55 / 5 + 5 / 5
12 = (55 + 5) / 5

5를 사용한 횟수는 각각 6,5,4 입니다. 그리고 이중 가장 작은 경우는 4입니다.
이처럼 숫자 N과 number가 주어질 때, N과 사칙연산만 사용해서 표현 할 수 있는 방법 중 N 사용횟수의 최솟값을 return 하도록 solution 함수를 작성하세요.

### 제한사항

- N은 1 이상 9 이하입니다.
- number는 1 이상 32,000 이하입니다.
- 수식에는 괄호와 사칙연산만 가능하며 나누기 연산에서 나머지는 무시합니다.
- 최솟값이 8보다 크면 -1을 return 합니다.

#### 문제 해설

[짱어려움...]  
N을 가지고 활용할 수 있는 경우는 5가지이다. 사칙연산 그리고 NN처럼 붙여쓰기. 그리고 사용횟수가 8번이 넘어가면 안되는 것으로 간주하고 -1을 리턴한다.

1. dp 배열을 9칸짜리로 생성한다. (8칸이어도 상관없음, 어차피 0칸은 사용 안 하니까) - 사용횟수 8까지만 고려하므로  
   N = 5인 경우, dp[2]에는 N이 2번 쓰이는 결과인 [55, 10, 0, 1, 25]가 저장된다.
2. 각 dp[i]에는 N이 i번 사용되었을 때 가능한 모든 경우의 수를 넣어주게 된다. 어차피 N은 9까지 사용되므로, 최대의 경우를 보자면 N이 1개 -> 1, 2개 -> 5, 3개 -> 25 (중복을 고려하지 않음), 4개 -> 125 ..., 9개 -> 5^8 개가 된다.  
   dp[8]칸짜리를 만들고, 각 칸에는 index만큼 N이 사용된 경우를 모두 저장해준다.
3. 중복되는 수가 생길 수 있으므로, 배열의 내부인 dp[i]는 Set으로 설정해주어 중복된 값이 들어가지 않도록 한다.
4. N이 i번 붙어있는 경우, 즉 NN, NNN, NNNN, ..., NNNNNNNN 과 같은 형태로도 사용되는 경우가 있으므로 각 dp[i]-Set에 추가해준다.
   ```js
   for (let i = 0; i <= 8; i++) {
     dp[i] = new Set(); // 중복 삭제
     dp[i].add(Number(String(N).repeat(i)));
   }
   ```
5. 여기서부터가 진짜 문제다.
6. N이 3번 사용되는 경우는 어떻게 될까?
   1. dp[2]에는 N이 2번 사용된 경우들이 들어있다. [55, 10, 0, 1, 25]
   2. 여기에다가 각각 사칙연산을 한 것들이 들어간다. [ 60, 50, 11, 275, 15, 5, 2, 50, 5, -5, 0, 0, 6, -4, 0, 5, 30, 20, 125, 5 ]
   3. 중복을 제외하면, [ 60, 50, 11, 275, 15, 5, 2, -5, 0, 6, -4, 30, 20, 125 ] 이 되고, 거기에 원래 기존에 있던 [ 555 ]가 추가된다.
   4. 이걸 잘 생각해보면 dp[1]에 있는 값 1개와 dp[2]에 있는 값 한 개를 사용하면 그게 바로 N이 3개인 경우가 된다는 것이다.

다시 정리해보면,

7.  dp[1]은 N을 1회 사용한 값들이 들어가야 하는데 이는 N 하나로 유일하다.  
    dp[2]는 N을 1회 사용한 값, 즉 dp[1]의 값 중 두 개를 연산하여 만들 수 있다.  
    dp[3]은 dp[1]의 값 중 하나와 dp[2]의 값 중 하나를 연산하여 만들 수 있다.  
    dp[4]는 dp[1]의 값 중 하나와 dp[3]의 값 중 하나를 연산하거나, dp[2]의 값 중 두 개를 연산하여 만들 수 있다.  
    즉 dp[n]은 dp[1]의 값 중 하나와 dp[n - 1]의 값 중 하나를 연산하거나, dp[2]의 값 중 하나와 dp[n - 2]의 값 중 하나를 연산하거나, .... , dp[n - 1]의 값 중 하나와 dp[1]의 값 중 하나를 연산하여 만들 수 있다.

```js
function solution(N, number) {
  // N으로 number만들기
  var answer = 0;
  if (N === number) return 1;
  const dp = new Array(9); // 9칸짜리 dp // 각 칸에는 N을 i번 활용한 값들의 가능한 예시가 모두 들어간다
  for (let i = 0; i <= 8; i++) {
    dp[i] = new Set(); // 중복 삭제
    dp[i].add(Number(String(N).repeat(i)));
  }
  // dp[i]를 구하는 경우,
  for (let i = 1; i <= 8; i++) {
    // dp[i]부터 dp[i-1]까지를 확인
    for (let j = 1; j < i; j++) {
      // dp[1]과 dp[j-1]을 확인, dp[2]와 dp[j-2]를 확인 ,,,
      // i가 4라면 j는 0, 1, 2, 3 -> N을 (1,3)번 쓰는 경우, N을 (2,2)번 쓰는 경우를 확인, N을 (3,1)번 쓰는 경우를 확인
      for (const val1 of dp[j]) {
        for (const val2 of dp[i - j]) {
          dp[i].add(val2 + val1);
          dp[i].add(val2 - val1);
          dp[i].add(Math.floor(val2 / val1));
          dp[i].add(val2 * val1);
        }
      }
      if (dp[i].has(number)) return i;
    }
  }

  return -1;
}

solution(5, 12);
solution(2, 11);
```