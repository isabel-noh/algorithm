// # BOJ 1753 최단경로
// [BOJ 1753 최단경로](https://www.acmicpc.net/problem/1753)

// ## 문제
// 방향그래프가 주어지면 주어진 시작점에서 다른 모든 정점으로의 최단 경로를 구하는 프로그램을 작성하시오. 단, 모든 간선의 가중치는 10 이하의 자연수이다.

// ### 입력
// 첫째 줄에 정점의 개수 V와 간선의 개수 E가 주어진다. (1 ≤ V ≤ 20,000, 1 ≤ E ≤ 300,000) 모든 정점에는 1부터 V까지 번호가 매겨져 있다고 가정한다. 둘째 줄에는 시작 정점의 번호 K(1 ≤ K ≤ V)가 주어진다. 셋째 줄부터 E개의 줄에 걸쳐 각 간선을 나타내는 세 개의 정수 (u, v, w)가 순서대로 주어진다. 이는 u에서 v로 가는 가중치 w인 간선이 존재한다는 뜻이다. u와 v는 서로 다르며 w는 10 이하의 자연수이다. 서로 다른 두 정점 사이에 여러 개의 간선이 존재할 수도 있음에 유의한다.

// ### 출력
// 첫째 줄부터 V개의 줄에 걸쳐, i번째 줄에 i번 정점으로의 최단 경로의 경로값을 출력한다. 시작점 자신은 0으로 출력하고, 경로가 존재하지 않는 경우에는 INF를 출력하면 된다.

// #### 문제풀이
// heap을 만들지 않으면 시간 초과로 문제를 해결할 수 없는 문제였다. .. 챔!
// + 다익스트라 알고리즘을 활용한다.

const fs = require("fs");
const [a, b, ...c] = fs
  .readFileSync("./sample.txt")
  .toString()
  .trim()
  .split("\n");

//서로 다른 두 정점 사이에 여러 개의 간선이 존재할 수도 있음
const [V, E] = a.split(" ").map((num) => +num); // 정점 개수 V, 간선 개수 E // 1 ~ V까지의 정점
const K = +b; // 시작 정점
const arr = c.map((e) => e.split(" ").map((el) => +el));

// u에서 v로 가는 가중치 w인 간선
const adj = [...new Array(V + 1)].map((el) => new Array(1).fill(0));
arr.forEach((element) => {
  const [u, v, w] = element;
  if (adj[u][0] === 0) {
    adj[u] = [[v, w]];
  } else {
    adj[u].push([v, w]);
  }
});
console.log(adj);

function DijkstraAlgorithm(start, distance) {
  const queue = [[start, 0]]; // 시작점, 거리 0
  // queue에 첫번째로 확인할 값 넣기
  while (queue.length > 0) {
    const [u, w] = queue.shift();
    for (nextNode of adj[u]) {
      // 해당 문제에서 키 포인트!
      //`K에서부터 다음 노드까지의 최종 거리로 잡혀있는 것이 현재 노드까지의 거리 + 다음노드까지의 거리 보다 크다면 (즉 최단경로가 아니라면) 현재 노드까지의 거리+현재 노드에서부터 다음 노드까지의 거리를 distance에 기록하고, queue에 푸시한다.`
      if (distance[nextNode[0]] > distance[u] + nextNode[1]) {
        distance[nextNode[0]] = distance[u] + nextNode[1];
        queue.push(nextNode);
      }
    }
  }
}

// 가중치 방향 그래프
// 시작점 K에서 다른 모든 정점으로 가는 최단 경로
// 정점 1, 2, 3, 4, 5
// 자기 자신으로 가는 경우는 확인 하지 않음
const distance = [...new Array(V + 1)].fill(Infinity);
distance[K] = 0;

DijkstraAlgorithm(K, distance);

distance.shift();
for (let i = 0; i < distance.length; i++) {
  if (distance[i] === Infinity) distance[i] = "INF";
}
console.log(...distance);

// #### heapQ
// 입력으로 들어오는 데이터 개수가 많기 때문에 힙을 사용하지 않으면 시간초과가 난다.
// - 최소 힙을 구현한다.
