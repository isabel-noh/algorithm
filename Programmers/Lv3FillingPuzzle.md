# Programmers - BFS/DFS - 퍼즐 조각 채우기

[Programmers - BFS/DFS - 퍼즐 조각 채우기](https://school.programmers.co.kr/learn/courses/30/lessons/84021)

## 제한사항

- 3 ≤ game_board의 행 길이 ≤ 50
- game_board의 각 열 길이 = game_board의 행 길이
  - 즉, 게임 보드는 정사각 격자 모양입니다. - game_board의 모든 원소는 0 또는 1입니다.
  - 0은 빈칸, 1은 이미 채워진 칸을 나타냅니다.
  - 퍼즐 조각이 놓일 빈칸은 1 x 1 크기 정사각형이 최소 1개에서 최대 6개까지 연결된 형태로만 주어집니다.
- table의 행 길이 = game_board의 행 길이
- table의 각 열 길이 = table의 행 길이
  - 즉, 테이블은 game_board와 같은 크기의 정사각 격자 모양입니다.
  - table의 모든 원소는 0 또는 1입니다.
  - 0은 빈칸, 1은 조각이 놓인 칸을 나타냅니다.
  - 퍼즐 조각은 1 x 1 크기 정사각형이 최소 1개에서 최대 6개까지 연결된 형태로만 주어집니다.
- game_board에는 반드시 하나 이상의 빈칸이 있습니다.
- table에는 반드시 하나 이상의 블록이 놓여 있습니다.

## 문제 분석

주어진 게임 보드에는 빈칸이 있다. 테이블 위에는 퍼즐 조각들이 있다.  
주어진 게임 보드의 빈칸에 퍼즐을 놓는 문제이다.  
퍼즐은 돌릴 수 있다. 하지만 뒤집을 수는 없다.  
퍼즐들은 서로 인접할 수 없다.  
퍼즐은 빈 칸과 정확히 모양이 일치하는 경우에만 놓을 수 있다.  
최대한 퍼즐을 몇 칸까지 채울 수 있는지 return 하는 문제이다.

## 알고리즘 설계

for문으로 돌면서, bfs로 각 퍼즐 조각의 시작점에서부터 어디까지 가는지 확인해서 퍼즐 모양 확인하고 이것을 0,0 기준으로 당겨 가져온다. 그리고 puzzleList에 저장한다.

- missing point1. bfs에서 범위를 ni만 지정하고 nj에 대해서는 고려하지 않았다.

그 다음 game_board에서서 bfs를 통해 각 빈칸의 모양을 확인한다.  
빈 칸 모양 1개가 만들어지면, puzzle list의 각 puzzle들과 모양을 비교한다.  
일단 칸의 개수가 다르면 고려할 필요 없으므로 조건을 넣어준다.  
`check` 함수를 통해 퍼즐모양과 빈칸모양을 비교해야하는데, 여기에서 퍼즐을 돌리는 것이 관건이다.

`check` 함수에서는 stringfy로 배열을 확인해준다.

### 퍼즐 회전

여기에서 다시 `rotate` 함수에서 퍼즐을 90도로 돌려가면서 확인해준다. `rotate` 함수에서의 돌리는 부분은 다른 사람들의 코드를 참고하였다.

1. X좌표와 Y좌표를 먼저 뒤집어준다. [x, y] => [y, x]
2. y를 음수화 해준다.

```
[[1, 1, 0],
[0, 1, 0],
[0, 1, 0]]
```

라고 했을 때, 90도로 회전하는 것은 아래와 같을 것이다.

```
[[0, 0, 1],
[1, 1, 1],
[0, 0, 0]]
```

위처럼 만들기 위해서는 먼저 x=y기울기를 가지는 선이 있다고 가정하고 이를 기준으로 서로 값을 뒤집는다. (`[x, y] => [y, x]`)

```
[[0, 0, 0],
[1, 1, 1],
[0, 0, 1]]
```

그러면 이처럼 된다. 이것을 위아래로 뒤집으면 원하는 모양이 나온다. (`[y, x] => [y, -x]`)

```
[[0, 0, 1],
[1, 1, 1],
[0, 0, 0]]
```

하지만 때에 따라서 배열 바깥으로 넘어갈 수도 있기 때문에 제일 포인트를 기점으로 0,0으로 맞춰주는 작업을 하면 된다.

만약 퍼즐이 일치하면, answer에 퍼즐의 길이를 추가해주고, 이후에 중복 확인되지 않게 하기위해서 puzzleList에서 합격한 퍼즐을 삭제한다.

## 코드

```js
function solution(game_board, table) {
  var answer = 0;
  const length = game_board.length;
  let visited = [...new Array(length)].map((el) =>
    [...new Array(length)].fill(0)
  );
  const direction = [
    [0, 1],
    [1, 0],
    [0, -1],
    [-1, 0],
  ];

  // 0,0으로 맞추기
  function makeMatrix(piece) {
    // X, Y 좌표 대로 정렬하기
    piece = piece.sort((a, b) => a[1] - b[1]);
    piece = piece.sort((a, b) => a[0] - b[0]);

    const minX = piece[0][0];
    const minY = piece[0][1];

    // 왼쪽 위로 정렬
    for (let i = 0; i < piece.length; i++) {
      piece[i][0] -= minX;
      piece[i][1] -= minY;
    }
    return piece;
  }

  // 퍼즐 모양 확인
  function bfs(i, j, target, board) {
    const piece = [[i, j]];
    const queue = [[i, j]];
    visited[i][j] = 1;
    while (queue.length) {
      const [ci, cj] = queue.shift();
      for (let d = 0; d < 4; d++) {
        const ni = ci + direction[d][0],
          nj = cj + direction[d][1];
        if (
          ni >= 0 &&
          ni < length &&
          nj >= 0 &&
          nj < length &&
          visited[ni][nj] === 0 &&
          board[ni][nj] === target
        ) {
          piece.push([ni, nj]);
          queue.push([ni, nj]);
          visited[ni][nj] = 1;
        }
      }
    }
    return makeMatrix(piece);
  }

  const puzzleList = [];

  // 퍼즐 list 추출
  for (let i = 0; i < table.length; i++) {
    for (let j = 0; j < table.length; j++) {
      if (table[i][j] === 1 && visited[i][j] === 0) {
        const puzzle = bfs(i, j, 1, table);
        puzzleList.push(puzzle);
      }
    }
  }
  // _ visited 재사용을 위해 초기화 _
  visited = [...new Array(length)].map((el) => [...new Array(length)].fill(0));

  function rotate(pieces) {
    // 90도 시계 방향으로 회전
    for (let i = 0; i < pieces.length; i++) {
      let temp = 0;
      temp = pieces[i][0];
      pieces[i][0] = pieces[i][1];
      {
        temp === -0 ? (pieces[i][1] = 0) : (pieces[i][1] = -temp);
      }
    }
    const answer = makeMatrix(pieces);
    return answer;
  }

  // 퍼즐을 돌려서 blank랑 맞는지 확인
  function check(puzzle, blank) {
    const equals = (a, b) => JSON.stringify(a) === JSON.stringify(b);
    let rotatedPuzzle = [...puzzle];
    // 돌려보기
    for (let i = 0; i < 4; i++) {
      if (i === 0) {
        if (equals(makeMatrix(puzzle), blank)) {
          // 여기에서 puzzle이 정렬이 안 되어있을 줄은 몰랐다. missing point!
          return true;
        }
      } else {
        rotatedPuzzle = rotate(rotatedPuzzle);
        if (equals(rotatedPuzzle, blank)) return true;
      }
    }
    return false;
  }

  // 퍼즐 조각 회전 및 확인
  for (let i = 0; i < table.length; i++) {
    for (let j = 0; j < table.length; j++) {
      if (game_board[i][j] === 0 && visited[i][j] === 0) {
        const blank = bfs(i, j, 0, game_board); // 빈 공간 확보
        // 빈 공간과 퍼즐 확인
        for (let p = 0; p < puzzleList.length; p++) {
          if (puzzleList[p].length === blank.length) {
            const res = check(puzzleList[p], blank);
            if (res) {
              answer += blank.length;
              puzzleList.splice(p, 1); // 같은 모양의 퍼즐이 여러개 있을 수도 있다는 것을 놓쳤다. missing point!
              break;
            }
          }
        }
      }
    }
  }
  return answer;
}
```
