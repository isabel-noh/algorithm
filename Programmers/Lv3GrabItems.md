# Programmers - DFS / BFS - 아이템 줍기

[Programmers - DFS/BFS - 아이템 줍기](https://school.programmers.co.kr/learn/courses/30/lessons/87694)

## 문제 설명

다음과 같은 다각형 모양 지형에서 캐릭터가 아이템을 줍기 위해 이동하려 합니다.

지형은 각 변이 x축, y축과 평행한 직사각형이 겹쳐진 형태로 표현하며, 캐릭터는 이 다각형의 둘레(굵은 선)를 따라서 이동합니다.

만약 직사각형을 겹친 후 다음과 같이 중앙에 빈 공간이 생기는 경우, 다각형의 가장 바깥쪽 테두리가 캐릭터의 이동 경로가 됩니다.

단, 서로 다른 두 직사각형의 x축 좌표 또는 y축 좌표가 같은 경우는 없습니다.

즉, 위 그림처럼 서로 다른 두 직사각형이 꼭짓점에서 만나거나, 변이 겹치는 경우 등은 없습니다.

다음 그림과 같이 지형이 2개 이상으로 분리된 경우도 없습니다.

한 직사각형이 다른 직사각형 안에 완전히 포함되는 경우 또한 없습니다.

지형을 나타내는 직사각형이 담긴 2차원 배열 rectangle, 초기 캐릭터의 위치 characterX, characterY, 아이템의 위치 itemX, itemY가 solution 함수의 매개변수로 주어질 때, 캐릭터가 아이템을 줍기 위해 이동해야 하는 가장 짧은 거리를 return 하도록 solution 함수를 완성해주세요.

### 제한사항

- rectangle의 세로(행) 길이는 1 이상 4 이하입니다.
- rectangle의 원소는 각 직사각형의 [좌측 하단 x, 좌측 하단 y, 우측 상단 x, 우측 상단 y] 좌표 형태입니다.
- 직사각형을 나타내는 모든 좌표값은 1 이상 50 이하인 자연수입니다.
- 서로 다른 두 직사각형의 x축 좌표, 혹은 y축 좌표가 같은 경우는 없습니다.
- 문제에 주어진 조건에 맞는 직사각형만 입력으로 주어집니다.
- charcterX, charcterY는 1 이상 50 이하인 자연수입니다.
- 지형을 나타내는 다각형 테두리 위의 한 점이 주어집니다.
- itemX, itemY는 1 이상 50 이하인 자연수입니다.
- 지형을 나타내는 다각형 테두리 위의 한 점이 주어집니다.
- 캐릭터와 아이템의 처음 위치가 같은 경우는 없습니다.

- 전체 배점의 50%는 직사각형이 1개인 경우입니다.
- 전체 배점의 25%는 직사각형이 2개인 경우입니다.
- 전체 배점의 25%는 직사각형이 3개 또는 4개인 경우입니다.

## 문제 분석 요약

character이 item을 찾으러가는 길의 최단거리를 구하는 문제이다.
루트는 주어진 rectangle 배열에 있는 사각형들의 테두리 중 가장 바깥 테두리들끼리의 조합이라고 할 수 있다.
겹쳐지는 곳은 route로 사용할 수 없다.
먼저 테두리를 지도에 표시하고, 테두리 중 어떤 사각형의 내부에라도 해당된다면 지나갈 수 없다.

## 알고리즘 설계

테두리 = 1로 표기, 테투리 안쪽 = 0으로 표기, 테투리 바깥쪽 = -1로 표기.
지나간 길은 2로 표기

bfs로 가능한 방향을 지나가며 확인한다.
확인할 때 조건이 중요하다. 범위에 포함되는가? 테두리인가, 사각형 내부인가?

마지막에 빼먹은 조건이 있었다. 어느 지점에서 다른 지점으로 이동할 때, 길을 따라가지 않고 건너뛰는가?

## 코드

```js
function solution(rectangle, characterX, characterY, itemX, itemY) {
  var answer = 0;
  // 현재 위치가 어느 사각형에 있는지
  const current = [characterX, characterY];
  const visited = [...new Array(51)].map((el) => new Array(51).fill(-1));

  // 길 막기
  for (let i = 0; i < visited.length; i++) {
    for (let j = 0; j < visited[0].length; j++) {
      for (let r = 0; r < rectangle.length; r++) {
        const [lx, ly, rx, ry] = rectangle[r];
        // 테두리 표시
        if (
          ((ly === i || ry === i) && lx <= j && j <= rx) ||
          ((lx === j || rx === j) && ly <= i && i <= ry)
        ) {
          visited[i][j] = 1;
        }
      }
      for (let r = 0; r < rectangle.length; r++) {
        const [lx, ly, rx, ry] = rectangle[r];
        // 테두리 안쪽 표시
        if (lx < j && j < rx && ly < i && i < ry) {
          visited[i][j] = 0;
        }
      }
    }
  }
  const direction = [
    [0, 1],
    [1, 0],
    [0, -1],
    [-1, 0],
  ];
  const bfs = (location) => {
    const queue = [[...location, 0]];
    while (queue.length > 0) {
      const [cx, cy, distance] = queue.shift();
      console.log(cx, cy, distance);
      visited[cy][cx] = 2;
      if (itemX === cx && itemY === cy) return distance;
      for (let d = 0; d < direction.length; d++) {
        let nx = cx + direction[d][0];
        let ny = cy + direction[d][1];
        if (
          visited[ny][nx] === 1 &&
          nx >= 0 &&
          nx <= 51 &&
          ny >= 0 &&
          ny <= 51
        ) {
          queue.push([nx, ny, distance + 1]);
          visited[ny][nx] = 2;
        }
      }
    }
  };

  answer = bfs(current);
  return answer;
}
```

```js
function solution(rectangle, characterX, characterY, itemX, itemY) {
  var answer = 0;
  const current = [characterX * 2, characterY * 2]; // 시작 위치 * 2
  // 전체 지도에 해당하는 visited의 크기도 2배!
  const visited = [...new Array(51 * 2)].map((el) =>
    new Array(51 * 2).fill(-1)
  );

  // 길 막기
  for (let i = 0; i < visited.length; i++) {
    for (let j = 0; j < visited[0].length; j++) {
      for (let r = 0; r < rectangle.length; r++) {
        const [lx, ly, rx, ry] = rectangle[r]; // 네모의 모서리
        // 테두리 표시 1
        if (
          ((ly * 2 === i || ry * 2 === i) && lx * 2 <= j && j <= rx * 2) ||
          ((lx * 2 === j || rx * 2 === j) && ly * 2 <= i && i <= ry * 2)
        ) {
          visited[i][j] = 1;
        }
      }
      for (let r = 0; r < rectangle.length; r++) {
        const [lx, ly, rx, ry] = rectangle[r];
        // 테두리 안쪽 표시 0
        if (lx * 2 < j && j < rx * 2 && ly * 2 < i && i < ry * 2) {
          visited[i][j] = 0;
        }
      }
    }
  }
  const direction = [
    [0, 1],
    [1, 0],
    [0, -1],
    [-1, 0],
  ];
  const bfs = (location) => {
    const queue = [[...location, 0]];
    while (queue.length > 0) {
      const [cx, cy, distance] = queue.shift();
      visited[cy][cx] = 2; // 방문했다면 2
      if (itemX * 2 === cx && itemY * 2 === cy) return distance; // 아이템을 찾았다면 distance를 리턴
      for (let d = 0; d < direction.length; d++) {
        let nx = cx + direction[d][0];
        let ny = cy + direction[d][1];
        // 새로운 위치가 방문하기 전이고, 범위 안에 있다면 queue에 넣어서 확인~
        if (
          visited[ny][nx] === 1 &&
          nx >= 0 &&
          nx <= 102 &&
          ny >= 0 &&
          ny <= 102
        ) {
          queue.push([nx, ny, distance + 1]);
        }
      }
    }
  };

  answer = bfs(current);
  return answer / 2;
}

console.log(
  solution(
    [
      [1, 1, 7, 4],
      [3, 2, 5, 5],
      [4, 3, 6, 9],
      [2, 6, 8, 8],
    ],
    1,
    3,
    7,
    8
  )
);
console.log(
  solution(
    [
      [2, 2, 5, 5],
      [1, 3, 6, 4],
      [3, 1, 4, 6],
    ],
    1,
    4,
    6,
    3
  )
);
```

## 시간 복잡도

O(n^2)

- visited 배열의 크기는 2배로 설정되어 있습니다. 따라서 visited 배열을 초기화하는 부분은 O(N^2)의 시간이 소요됩니다.
- 길을 막는 부분을 계산하는 부분은 visited 배열의 모든 요소를 확인하며, 이중 반복문을 사용합니다. 이 부분의 시간 복잡도는 O(N^2)입니다.
- bfs 함수의 시간 복잡도는 전체 맵을 탐색하는 것과 관련이 있습니다. 즉, 최악의 경우에는 맵의 모든 지점을 한 번씩 방문해야 합니다. 따라서 이 부분의 시간 복잡도도 O(N^2)입니다.

## 틀린 점

중간에 [3,5]에서 [3,6]으로 갈 때, 돌아가야하는데, 처음 내가 짠 코드에서는 직진으로 그냥 가버림.
![참고 이미지](/IMG_AAF4A824E96C-1.jpeg)

### 참고한 해결 방법

너비, 거리 모든 것을 2배로 해줘서 한 칸 씩을 더 가야하는 것처럼 인식하도록 해주는 방법으로 해결하였다. 물론, 답도 2배로 나올테니 /2를 해주어야 한다.

[3,5]에서 [3,6]로 간다고 했을 때, 위의 방법을 사용한다면, [6,10]에서 [6,12]를 가야하는 것처럼 인식하게 된다. 그러면 10에서 12로 가려고 할 때, 11에서 막혀 있기 때문에 돌아서 가게 된다는 것이다.
즉, 직사각형 내부를 점프해서 가느냐, 길을 따라 가느냐를 구분하기 위한 장치인 것이다.

## 느낀점 or 기억할정보

예외에 대한 부분을 꼼꼼히 확인해보아야 할 것이다.
