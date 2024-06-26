# Programmers - DP - 등굣길

[Programmers - DP - 등굣길](https://school.programmers.co.kr/learn/courses/30/lessons/42898)

## 문제 설명

계속되는 폭우로 일부 지역이 물에 잠겼습니다. 물에 잠기지 않은 지역을 통해 학교를 가려고 합니다. 집에서 학교까지 가는 길은 m x n 크기의 격자모양으로 나타낼 수 있습니다.

아래 그림은 m = 4, n = 3 인 경우입니다.

가장 왼쪽 위, 즉 집이 있는 곳의 좌표는 (1, 1)로 나타내고 가장 오른쪽 아래, 즉 학교가 있는 곳의 좌표는 (m, n)으로 나타냅니다.

격자의 크기 m, n과 물이 잠긴 지역의 좌표를 담은 2차원 배열 puddles이 매개변수로 주어집니다. 오른쪽과 아래쪽으로만 움직여 집에서 학교까지 갈 수 있는 최단경로의 개수를 1,000,000,007로 나눈 나머지를 return 하도록 solution 함수를 작성해주세요.

### 제한사항

- 격자의 크기 m, n은 1 이상 100 이하인 자연수입니다.
- m과 n이 모두 1인 경우는 입력으로 주어지지 않습니다.
- 물에 잠긴 지역은 0개 이상 10개 이하입니다.
- 집과 학교가 물에 잠긴 경우는 입력으로 주어지지 않습니다.

#### 문제풀이

**모든 위치를 확인하되, 해당 위치에 올 수 있는 전 위치, 즉 board[i-1][j]와 board[i][j-1]을 바탕으로 몇가지 루트가 가능한지 확인하는 문제이다.**
목적지에 도달할 수 있는 방향은 오른쪽 ->과 아래 v 방향만 있다.  
[0,0]에서 출발한다고 했을 때, [0,1], [0,2], [0,3] 그리고, [1,0], [2,0], [3,0]으로 갈 수 있는 방법은 1가지 밖에 없다.  
만약 [1,1]로 가고자 할 경우, 2가지 방법이 있다. [0,1]을 거치는 방법과 [1,0]을 거치는 방법.  
그러면 여기서 알 수 있다. [i][j]에 가기 위해서는 [i-1][j]와 [i][j-1]에 도달하는 방법을 더한 가짓 수라는 것을.  
`왼쪽에서 접근 가능한 경로의 수 + 위에서 접근 가능한 경로의 수`

웅덩이 아래와 오른쪽은 그러면 어떻게 하지? 현재 확인하는 방향에서 이전에 웅덩이가 있었다면 (-1) 0을 더해주는 것으로 하고, 그렇지 않으면 이전 루트로 접근가능한 경로수를 더해주는 것으로 해결했다.

마지막에 destination에서 1000000007를 나눈 나머지를 구해서 값을 내고자했더니 시간 초과가 났다. 그래서 간 한칸 한 칸을 구할 때마다 1000000007를 나눠주어 해결했다.

```js
function solution(m, n, puddles) {
  var answer = 0;
  const board = [...new Array(n)].map((el) => new Array(m).fill(0));
  puddles.forEach((element) => {
    const [x, y] = element;
    board[y - 1][x - 1] = -1;
  });
  board[0][0] = 1; // 시작점
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < m; j++) {
      if (i === 0 && j === 0) continue;
      if (board[i][j] === -1) continue;
      if (j > 0) board[i][j] += board[i][j - 1] === -1 ? 0 : board[i][j - 1];
      if (i > 0) board[i][j] += board[i - 1][j] === -1 ? 0 : board[i - 1][j];
      board[i][j] %= 1000000007;
    }
  }
  //   board[n - 1][m - 1] // destination
  console.log(board);
  answer = board[n - 1][m - 1] % 1000000007;
  return answer;
}

solution(4, 3, [[2, 2]]); // 4
```
