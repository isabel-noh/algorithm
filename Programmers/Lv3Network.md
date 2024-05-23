# Programmers - DFS / BFS - Network

[Programmers - DFS / BFS - Network](https://school.programmers.co.kr/learn/courses/30/lessons/43162)

## 문제 설명

네트워크란 컴퓨터 상호 간에 정보를 교환할 수 있도록 연결된 형태를 의미합니다. 예를 들어, 컴퓨터 A와 컴퓨터 B가 직접적으로 연결되어있고, 컴퓨터 B와 컴퓨터 C가 직접적으로 연결되어 있을 때 컴퓨터 A와 컴퓨터 C도 간접적으로 연결되어 정보를 교환할 수 있습니다. 따라서 컴퓨터 A, B, C는 모두 같은 네트워크 상에 있다고 할 수 있습니다.

컴퓨터의 개수 n, 연결에 대한 정보가 담긴 2차원 배열 computers가 매개변수로 주어질 때, 네트워크의 개수를 return 하도록 solution 함수를 작성하시오.

### 제한사항

- 컴퓨터의 개수 n은 1 이상 200 이하인 자연수입니다.
- 각 컴퓨터는 0부터 n-1인 정수로 표현합니다.
- i번 컴퓨터와 j번 컴퓨터가 연결되어 있으면 computers[i][j]를 1로 표현합니다.
- computer[i][i]는 항상 1입니다.

#### 문제풀이

전형적인 DFS로 풀이한 문제이다.
n 사이즈의 visited 배열을 생성해준다. 0, 1로 표시하며, 확인한, 즉 연결된 node라면 1로 아직 연결되지 않은 node라면 0으로 표시된다.
0부터 n까지 dfs로 연결되었는지를 확인한다. 만약 index가 visited에서 아직 0이라면 연결되지 않은 node이므로 dfs를 통해 어디까지 연결되었는지 확인한다.  
만약 dfs를 모두 1번 돌면 네트워크 1개가 연결되어있다는 의미로 answer을 1더해준다.

dfs내부에 대해서 보자.  
확인할 인덱스 i를 받는다.  
먼저 visited 배열에 i를 확인했다는 표식으로 1로 표시한다.  
그다음 0부터 n까지 돌면서 i와 연결되어있는(`computers[i][idx] === 1`) 노드들을 확인한다. 연결되어있지만 본인과 동일한 i일 경우, 확인하지 않고, 또 이미 확인한 node의 경우에는 확인하지 않는다. (`visited[idx] === 0`)

```js
function solution1(n, computers) {
  let answer = 0;
  const visited = [...new Array(n)].fill(0);
  function dfs(i) {
    visited[i] = 1;
    for (let idx = 0; idx < n; idx++) {
      if (computers[i][idx] === 1 && idx !== i && visited[idx] === 0) {
        dfs(idx);
      }
    }
  }
  for (let index = 0; index < n; index++) {
    if (visited[index] === 0) {
      dfs(index);
      answer++;
    }
  }
  return answer;
}

solution1(3, [
  [1, 1, 0],
  [1, 1, 0],
  [0, 0, 1],
]);
solution1(3, [
  [1, 1, 0],
  [1, 1, 1],
  [0, 1, 1],
]);
```
