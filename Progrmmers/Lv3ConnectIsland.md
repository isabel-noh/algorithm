# Programmers - Greedy - 섬 연결하기

[Programmers - Greedy - 섬 연결하기](https://school.programmers.co.kr/learn/courses/30/lessons/42861)

## 문제 설명

n개의 섬 사이에 다리를 건설하는 비용(costs)이 주어질 때, 최소의 비용으로 모든 섬이 서로 통행 가능하도록 만들 때 필요한 최소 비용을 return 하도록 solution을 완성하세요.

다리를 여러 번 건너더라도, 도달할 수만 있으면 통행 가능하다고 봅니다. 예를 들어 A 섬과 B 섬 사이에 다리가 있고, B 섬과 C 섬 사이에 다리가 있으면 A 섬과 C 섬은 서로 통행 가능합니다.

### 제한사항

- 섬의 개수 n은 1 이상 100 이하입니다.
- costs의 길이는 ((n-1) \* n) / 2이하입니다.
- 임의의 i에 대해, costs[i][0] 와 costs[i] [1]에는 다리가 연결되는 두 섬의 번호가 들어있고, costs[i] [2]에는 이 두 섬을 연결하는 다리를 건설할 때 드는 비용입니다.
- 같은 연결은 두 번 주어지지 않습니다. 또한 순서가 바뀌더라도 같은 연결로 봅니다. 즉 0과 1 사이를 연결하는 비용이 주어졌을 때, 1과 0의 비용이 주어지지 않습니다.
- 모든 섬 사이의 다리 건설 비용이 주어지지 않습니다. 이 경우, 두 섬 사이의 건설이 불가능한 것으로 봅니다.
- 연결할 수 없는 섬은 주어지지 않습니다. -> 모든 섬은 연결됨

#### 문제풀이

bfs로 풀이하려했지만 틀림  
최소산장트리 MST로 해결할 수 있음  
연결할 수 없는 섬이 없으며, 모든 섬이 연결됨 -> 간선의 수는 그래프에 있는 노드의 수 - 1과 같다  
최소 비용의 간선은 총 n-1개를 선택하여야 함

크루스칼 알고리즘  
-> 주어진 간선들의 `가중치`를 보고 사이클 여부를 체크하면서 항상 최대/최소 가중치만 선택  
크루스칼 알고리즘에서는 `Union-Find`를 사용함  
-> 여러 개의 노드가 있을 때 선택된 두 개의 노드가 현재 같은 그래프에 있는지를 판별

**Kruskal Algorithm**
간선을 거리가 짧은 순서대로 그래프에 포함시키기
a. 간선을 거리가 짧은 순으로 asc 정렬하기
b. 사이클이 생기는지 확인 → 사이클이 생기면 그래프에 포함 ❌

**Union-Find**
-> 여러 개의 노드가 있을 때 선택된 두 개의 노드가 현재 같은 그래프에 있는지를 판별
-> unionParent(), getParent(), isSameParent()

```js
function getParent(conn, child) {
  const parent = conn[child];
  if (parent === child) return child;
  return (conn[child] = getParent(conn, conn[parent])); // 재귀 함수
}
function unionParent(conn, cur, target) {
  const p1 = getParent(conn, cur);
  const p2 = getParent(conn, target);
  // 더 작은 쪽으로 부모를 합침
  if (p1 < p2) return (conn[p2] = p1);
  else return (conn[p1] = p2);
}
function isSameParent(conn, a, b) {
  const p1 = getParent(conn, a);
  const p2 = getParent(conn, b);
  if (p1 === p2) return true;
  else return false;
}

function solution(n, costs) {
  // costs: n개의 섬 사이에 다리를 건설하는 비용
  var answer = 0; // 모든 섬이 서로 통행 가능하도록 만들 때 필요한 최소 비용
  const sorted = costs.sort((a, b) => a[2] - b[2]); // 최소 비용 순으로 정렬
  let connection = Array.from({ length: n }, (_, idx) => idx);
  const graph = [];
  for (let i = 0; i < sorted.length; i++) {
    // graph에 추가
    if (!isSameParent(connection, sorted[i][0], sorted[i][1])) {
      // 부모가 다르면 -> 연결안되어있는거임
      graph.push(sorted[i]);
      unionParent(connection, sorted[i][0], sorted[i][1]);
    }
  }
  return graph.reduce((acc, cur) => acc + cur[2], 0);
}

solution(4, [
  [0, 1, 1],
  [0, 2, 2],
  [1, 2, 5],
  [1, 3, 1],
  [2, 3, 8],
]);
```

// bfs로 풀이하려했지만 틀림
// 최소산장트리 MST로 해결할 수 있음
// 연결할 수 없는 섬이 없으며, 모든 섬이 연결됨 -> 간선의 수는 그래프에 있는 노드의 수 - 1과 같다
// 최소 비용의 간선은 총 n-1개를 선택하여야 함

// 크루스칼 알고리즘
// -> 주어진 간선들의 `가중치`를 보고 사이클 여부를 체크하면서 항상 최대/최소 가중치만 선택
// 크루스칼 알고리즘에서는 `Union-Find`를 사용함
// -> 여러 개의 노드가 있을 때 선택된 두 개의 노드가 현재 같은 그래프에 있는지를 판별
