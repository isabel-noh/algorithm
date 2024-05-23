# Programmers - 완전 탐색 - 전력망을 둘로 나누기

[Programmers - 완전 탐색 - 전력망을 둘로 나누기](https://school.programmers.co.kr/learn/courses/30/lessons/86971)

## 문제 설명

n개의 송전탑이 전선을 통해 하나의 트리 형태로 연결되어 있습니다. 당신은 이 전선들 중 하나를 끊어서 현재의 전력망 네트워크를 2개로 분할하려고 합니다. 이때, 두 전력망이 갖게 되는 송전탑의 개수를 최대한 비슷하게 맞추고자 합니다.

송전탑의 개수 n, 그리고 전선 정보 wires가 매개변수로 주어집니다.전선들 중 하나를 끊어서 송전탑 개수가 가능한 비슷하도록 두 전력망으로 나누었을 때, 두 전력망이 가지고 있는 송전탑 개수의 차이(절대값)를 return 하도록 solution 함수를 완성해주세요.

### 제한사항

- n은 2 이상 100 이하인 자연수입니다.
- wires는 길이가 n-1인 정수형 2차원 배열입니다.
  - wires의 각 원소는 [v1, v2] 2개의 자연수로 이루어져 있으며, 이는 전력망의 v1번 송전탑과 v2번 송전탑이 전선으로 연결되어 있다는 것을 의미합니다.
  - 1 ≤ v1 < v2 ≤ n 입니다.
  - 전력망 네트워크가 하나의 트리 형태가 아닌 경우는 입력으로 주어지지 않습니다.

### 입출력 예

| n   | wires                                             | result |
| --- | ------------------------------------------------- | ------ |
| 9   | [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]] | 3      |
| 4   | [[1,2],[2,3],[3,4]]                               | 0      |
| 7   | [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]             | 1      |

#### 문제풀이

1.  모든 선을 끊어서 dfs로 연결되어있는 것들이 몇 개인지 확인해보기

```js
function solution(n, wires) {
  var answer = 100;
  const cntArr = [];
  for (let exceptIndex = 0; exceptIndex < wires.length; exceptIndex++) {
    const board = Array.from(Array(n + 1), () => []); // 빈 배열로 이루어진 n+1짜리 배열 만들기
    for (let i = 0; i < wires.length; i++) {
      if (i !== exceptIndex) {
        // 줄 하나씩 끊어서 dfs를 위한 adj 배열 생성
        board[wires[i][0]].push(wires[i][1]);
        board[wires[i][1]].push(wires[i][0]);
      }
    }
    const visited = Array(n + 1).fill(false);

    function dfs(idx) {
      for (let j = 0; j < board[idx].length; j++) {
        if (!visited[board[idx][j]]) {
          // 현재 노드에 연결된 노드 중 아직 방문하지 않은 노드만 방문,
          visited[board[idx][j]] = true;
          dfs(board[idx][j]);
        }
      }
    }
    for (let index = 1; index < board.length; index++) {
      if (!visited[index]) {
        visited[index] = true;
        dfs(index, 1);
        let cnt = 0;
        cnt = visited.filter((x) => x === true).length;
        // cntArr.push(Math.abs(n - cnt - cnt));
        answer = Math.min(answer, Math.abs(n - cnt - cnt));
      }
    }
  }
  // answer = Math.min(...cntArr);
  return answer;
}
```

##### TiL

- 빈 배열로 이루어진 n+1짜리 배열 만들기
  Array.from(Array(n + 1), () => []);
