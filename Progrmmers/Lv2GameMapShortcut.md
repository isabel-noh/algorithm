# Programmers - DFS/BFS - 게임 맵 최단거리

[Programmers - DFS/BFS - 게임 맵 최단거리](https://school.programmers.co.kr/learn/courses/30/lessons/1844)

## 문제 설명

ROR 게임은 두 팀으로 나누어서 진행하며, 상대 팀 진영을 먼저 파괴하면 이기는 게임입니다. 따라서, 각 팀은 상대 팀 진영에 최대한 빨리 도착하는 것이 유리합니다.

지금부터 당신은 한 팀의 팀원이 되어 게임을 진행하려고 합니다.다음은 5 x 5 크기의 맵에, 당신의 캐릭터가(행: 1, 열: 1) 위치에 있고, 상대 팀 진영은(행: 5, 열: 5) 위치에 있는 경우의 예시입니다.

위 그림에서 검은색 부분은 벽으로 막혀있어 갈 수 없는 길이며, 흰색 부분은 갈 수 있는 길입니다. 캐릭터가 움직일 때는 동, 서, 남, 북 방향으로 한 칸씩 이동하며, 게임 맵을 벗어난 길은 갈 수 없습니다.  
아래 예시는 캐릭터가 상대 팀 진영으로 가는 두 가지 방법을 나타내고 있습니다.

- 첫 번째 방법은 11개의 칸을 지나서 상대 팀 진영에 도착했습니다.
- 두 번째 방법은 15개의 칸을 지나서 상대팀 진영에 도착했습니다

위 예시에서는 첫 번째 방법보다 더 빠르게 상대팀 진영에 도착하는 방법은 없으므로, 이 방법이 상대 팀 진영으로 가는 가장 빠른 방법입니다.

만약, 상대 팀이 자신의 팀 진영 주위에 벽을 세워두었다면 상대 팀 진영에 도착하지 못할 수도 있습니다.예를 들어, 다음과 같은 경우에 당신의 캐릭터는 상대 팀 진영에 도착할 수 없습니다.

게임 맵의 상태 maps가 매개변수로 주어질 때, 캐릭터가 상대 팀 진영에 도착하기 위해서 지나가야 하는 칸의 개수의 최솟값을 return 하도록 solution 함수를 완성해주세요. 단, 상대 팀 진영에 도착할 수 없을 때는 -1을 return 해주세요.

### 제한사항

- maps는 n x m 크기의 게임 맵의 상태가 들어있는 2차원 배열로, n과 m은 각각 1 이상 100 이하의 자연수입니다.
- n과 m은 서로 같을 수도, 다를 수도 있지만, n과 m이 모두 1인 경우는 입력으로 주어지지 않습니다.
- maps는 0과 1로만 이루어져 있으며, 0은 벽이 있는 자리, 1은 벽이 없는 자리를 나타냅니다.
- 처음에 캐릭터는 게임 맵의 좌측 상단인 (1, 1) 위치에 있으며, 상대방 진영은 게임 맵의 우측 하단인 (n, m) 위치에 있습니다.

#### 문제풀이

먼저 기본적으로 BFS로 풀이하였다.  
풀이하면서 고민된 부분이 있는데, visited를 하느냐 map에 직접 distance를 표시하느냐였다. map에 distance를 직접 변경하면서 길을 찾은 경우에는 시간초과가 발생했다. 문제를 풀지 못했다는 거다. 하지만 visited에 방문 여부만 표시하고 queue에 distance를 들고 다닌 경에는 문제를 해결했다. 정확한 이유는 찾지 못했지만 아무래도 for문에서 같은 값`maps[n_x][n_y] === 1`을 바라보는데, 여기에서 계산이 엉기는 것 같다. map은 여러 방법의 dfs가 돌면서 위치를 확인해야하기 때문에 차라리 visited를 직접 변경하면서 distance를 표기해주는 방법도 있다.

```js
// visited를 직접 변경하면서 distance를 표기해주는 방법
const visited = [...new Array(you[0] + 1)].map((el) =>
  new Array(you[1] + 1).fill(0)
);
function bfs(x, y) {
  const queue = [[x, y]];
  visited[x][y] = 1;
  while (queue.length > 0) {
    const [cur_x, cur_y] = queue.shift();
    for (dir of direction) {
      const [x, y] = dir;
      const n_x = cur_x + x;
      const n_y = cur_y + y;
      if (
        0 <= n_x &&
        n_x <= you[0] &&
        0 <= n_y &&
        n_y <= you[1] &&
        maps[n_x][n_y] === 1 &&
        visited[n_x][n_y] === 0
      ) {
        visited[n_x][n_y] = visited[cur_x][cur_y] + 1;
        if (n_x === you[0] && n_y === you[1]) return visited[n_x][n_y];
        queue.push([n_x, n_y]);
      }
    }
  }
  return -1;
}
answer = bfs(0, 0);
return answer;
```

```js
function solution(maps) {
  var answer = 0;
  let you_x = maps.length - 1;
  let you_y = maps[0].length - 1;
  const direction = [
    [0, 1], // 오른쪽
    [1, 0], // 아래쪽
    [0, -1], // 왼쪽
    [-1, 0], // 위쪽
  ];
  const visited = [...new Array(you_x + 1)].map((el) =>
    new Array(you_y + 1).fill(0)
  );
  function bfs(x, y, d) {
    const queue = [[x, y, d]];
    visited[x][y] = 1;
    while (queue.length > 0) {
      const [cur_x, cur_y, distance] = queue.shift();
      for (dir of direction) {
        const [x, y] = dir;
        const n_x = cur_x + x;
        const n_y = cur_y + y;
        if (
          0 <= n_x &&
          n_x <= you[0] &&
          0 <= n_y &&
          n_y <= you[1] &&
          maps[n_x][n_y] === 1 &&
          visited[n_x][n_y] === 0
        ) {
          visited[n_x][n_y] = 1;
          if (n_x === you_x && n_y === you_y) return distance + 2;
          queue.push([n_x, n_y, distance + 1]);
        }
      }
    }
    return -1;
  }
  answer = bfs(0, 0, 0);
  return answer;
}

solution([
  [1, 0, 1, 1, 1],
  [1, 0, 1, 0, 1],
  [1, 0, 1, 1, 1],
  [1, 1, 1, 0, 1],
  [0, 0, 0, 0, 1],
]);
solution([
  [1, 1, 1, 1, 1],
  [1, 0, 1, 0, 1],
  [1, 1, 1, 1, 1],
  [1, 0, 1, 0, 1],
  [1, 1, 1, 1, 1],
]);
solution([
  [1, 0, 1, 1, 1],
  [0, 0, 1, 1, 1],
  [1, 1, 1, 1, 1],
  [1, 1, 1, 0, 0],
  [1, 1, 1, 0, 1],
]);
```
