// # BOJ 9663 N-Queen
// [BOJ 9663 N-Queen](https://www.acmicpc.net/problem/9663)

// ## 백트랙킹 알고리즘, DFS, Brute Force

// ## 문제
// N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.

// N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.

// ### 입력
// 첫째 줄에 N이 주어진다. (1 ≤ N < 15)

// ### 출력
// 첫째 줄에 퀸 N개를 서로 공격할 수 없게 놓는 경우의 수를 출력한다.

// #### 문제풀이
// 먼저 체스의 규칙을 알아야 하는데, 퀸은 가로, 세로, 대각선 8방향으로 원하는 만큼 움직일 수 있다.
// N*N의 체스판에 `N개의 퀸`을 놓으려고 하는 경우, `같은 줄에는 두 개의 퀸이 있을 수 없으므로`, 결국 한 줄에는 무조건 하나의 퀸만 존재할 수 있다. (퀸을 놓을 수 있는 방향을 선택할 때, 오른쪽 왼쪽은 볼 필요 없음)
// 대각선 상에도 둘 수 없음
// 각 퀸은 상하좌우대각선 상에서 만날 수 없음!
// 즉 N개의 퀸이 N개의 줄에 각각 한개씩 배치되어 있어야 함.

// 나는 기본적으로 2차원 배열을 당연히 생각했지만, 상하좌우에 다른 퀸을 놓을 수 없기 때문에 이는 1차원 배열로도 해당 위치들을 기록할 수 있다고 한다
// 1차원 배열의 Index를 체스판의 가로 index로 보고, 해당 index에 세로 index에 해당하는 값을 넣어주어 표시할 수 있다.

// 예를 들어 `[2, 4, 3, 1]`의 경우, chessBoard[0][1], chessBoard[1][3], chessBoard[2][2], chessBoard[3][0] 각각 자리에 퀸이 놓여있다고 판단할 수 있다.

const fs = require("fs");
const n = Number(fs.readFileSync("./sample.txt").toString().trim());
let answer = 0;

function isPromising(v, arr) {
  // 다음 줄 중에서 어디가 유망한지 확인
  for (let i = 0; i < v; i++) {
    // 지금 확인하는 노드의 가로줄과 같은 위치거나 대각선이 같은 위치이면 false!
    if (arr[v] === arr[i] || Math.abs(i - v) === Math.abs(arr[i] - arr[v])) {
      return false;
    }
  }
  return true;
}

function checkNode(row, board) {
  // 여기에서 row는 현재 세로 몇번째 줄을 확인하고 있는지 체크
  if (row === n - 1) {
    // 마지막 줄까지 잘 왔으면 성공!
    answer++;
  } else {
    // 마지막 줄이 아닌 경우,
    for (let col = 0; col < n; col++) {
      // 다음 줄에서 각 가로 칸 확인
      board[row + 1] = col;
      if (isPromising(row + 1, board)) {
        // 다음 칸이 promising하다면 다음줄 확인
        checkNode(row + 1, board);
      }
    }
  }
}

for (let i = 0; i < n; i++) {
  const chessBoard = new Array(n).fill(0);
  chessBoard[0] = i; // 세로 첫번째줄부터 n번째줄까지 확인할 것
  checkNode(0, chessBoard);
}

console.log(answer);

// #### 백트래킹
// 기본적으로는 dfs방식으로 모든 노드를 확인하다가, 각 노드에 대해서 유망한지를 판단하고, 유망하지 않다면 그 뒤는 확인하지 않고, 그 전 단계로 돌아와서 다른 노드를 확인하는 기법이다.
