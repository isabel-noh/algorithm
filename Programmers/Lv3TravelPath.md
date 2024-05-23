# Programmers - DFS/BFS - 여행경로

[Programmers - DFS/BFS - 여행경로](https://school.programmers.co.kr/learn/courses/30/lessons/43164)

## 문제 설명

주어진 항공권을 모두 이용하여 여행경로를 짜려고 합니다. 항상 "ICN" 공항에서 출발합니다.

항공권 정보가 담긴 2차원 배열 tickets가 매개변수로 주어질 때, 방문하는 공항 경로를 배열에 담아 return 하도록 solution 함수를 작성해주세요.

### 제한사항

- 모든 공항은 알파벳 대문자 3글자로 이루어집니다.
- 주어진 공항 수는 3개 이상 10,000개 이하입니다.
- tickets의 각 행 [a, b]는 a 공항에서 b 공항으로 가는 항공권이 있다는 의미입니다.
- 주어진 항공권은 모두 사용해야 합니다.
- 만일 가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로를 return 합니다.
- 모든 도시를 방문할 수 없는 경우는 주어지지 않습니다.

### 문제 분석 요약

DFS 혹은 BFS로 경로를 찾는 문제이다.
경로가 가능한 것이 2개 이상이라면 destination의 알파벳이 먼저 앞서는 경로를 선택한다.  
모든 도시를 방문하지 못하는 경우의 루트는 선택되지 않는다.

1. 처음에는 지나갈 수 있는 destination node 리스트를 찾는 문제인줄 알아서 bfs로 풀이했다.
2. 하지만 가능한 경로를 모두 탐색해야 하고, 결과물로써 받아들일 수 없는 경우의 return도 나올 수 있기 때문에 백트래킹으로 풀고자 했다.

### 알고리즘 설계

DFS를 활용한 백트래킹  
경로별 visited 필요. 0이 없으면 dfs 종료

### 코드

```js
function solution(tickets) {
  var answer = [];
  const new_tickets = [...tickets].sort((a, b) => a[1].localeCompare(b[1]));
  const visited = new Array(tickets.length).fill(0);

  function bfs(idx) {
    const queue = [idx];
    visited[idx] = 1;
    while (queue.length) {
      const index = queue.shift();
      const [s, d] = new_tickets[index];
      answer.push(d);
      visited[index] = 1;
      if (!visited.includes(0)) return;

      for (let i = 0; i < new_tickets.length; i++) {
        if (visited[i] === 0 && new_tickets[i][0] === d) {
          queue.push(i);
          break;
        }
      }
    }
  }

  for (let i = 0; i < tickets.length; i++) {
    const [a, b] = new_tickets[i];
    if (a === "ICN" && visited[i] === 0) {
      answer.push(a);
      bfs(i);
    }
  }
  return answer;
}

solution([
  ["ICN", "JFK"],
  ["HND", "IAD"],
  ["JFK", "HND"],
]);
solution([
  ["ICN", "SFO"],
  ["ICN", "ATL"],
  ["SFO", "ATL"],
  ["ATL", "ICN"],
  ["ATL", "SFO"],
]);
```

### 시간 복잡도

정렬의 시간 복잡도는 O(nlogn)  
DFS 시간 복잡도 -> O(n\*n!)

### 틀린 이유

1. 만일 가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로를 return 합니다. -> flag를 활용해서 한 번 알파벳 순서대로 탐색을 한 경우에 성공한 이력이 있으면, 그 뒤의 가능한 경로는 확인하지 않도록 수정하였다.

2. [AAA, BBB], [AAA, CCC], [CCC, AAA] 가 있다고 쳤을때, 처음 BFS로 풀이했을 때에는 AAA -> BBB 하고 끝이 나버렸다. 그렇게 되지 않고, AAA -> CCC -> AAA -> BBB 되도록 하기 위해서 가능한 점으로 다시 돌아가는 백트래킹을 선택하여 수정하였다.

```js
function solution(tickets) {
  var answer = [];
  const new_tickets = [...tickets].sort((a, b) => a[1].localeCompare(b[1]));
  let flag = false;

  function dfs(idx, visited, arr) {
    const [s, d] = new_tickets[idx];
    visited[idx] = 1;

    if (!visited.includes(0)) {
      answer = [...arr];
      flag = true;
      return;
    }

    for (let i = 0; i < new_tickets.length; i++) {
      if (visited[i] === 0 && d === new_tickets[i][0]) {
        const new_arr = [...arr, new_tickets[i][1]];
        dfs(i, visited, new_arr);
      }
    }
  }
  console.log(new_tickets);
  for (let i = 0; i < tickets.length; i++) {
    const [a, b] = new_tickets[i];
    if (a === "ICN" && flag === false) {
      const visitedRoute = new Array(tickets.length).fill(0);
      visitedRoute[i] = 1;
      dfs(i, visitedRoute, [new_tickets[i][0], new_tickets[i][1]]);
    }
  }
  console.log(answer);
  return answer;
}
```

3. testcase 1번만 틀림 ->
   이 문제를 재귀 호출을 이용한 백트래킹 기법으로 풀었다면 마찬가지로 함수를 호출하면서 사용한 항공권을, 함수가 반환될 때에는 다시 사용하지 않은 항공권으로 되돌려야 합니다.

```js
function solution(tickets) {
  var answer = [];
  const new_tickets = [...tickets].sort((a, b) => a[1].localeCompare(b[1]));
  var flag = false;

  function dfs(idx, visited, arr) {
    const [s, d] = new_tickets[idx];
    visited[idx] = 1;
    if (!visited.includes(0) && flag !== true) {
      flag = true;
      answer = [...arr];
      return;
    }

    for (let i = 0; i < new_tickets.length; i++) {
      if (visited[i] === 0 && d === new_tickets[i][0]) {
        const new_arr = [...arr, new_tickets[i][1]];
        dfs(i, visited, new_arr);
        visited[i] = 0;
      }
    }
  }
  for (let i = 0; i < tickets.length; i++) {
    const [a, b] = new_tickets[i];
    if (a === "ICN" && flag === false) {
      const visitedRoute = new Array(tickets.length).fill(0);
      visitedRoute[i] = 1;
      dfs(i, visitedRoute, [a, b]);
    }
  }
  console.log(answer);
  return answer;
}
```

### 틀린 부분 수정 or 다른 풀이

```js
for (let i = 0; i < new_tickets.length; i++) {
  if (visited[i] === 0 && d === new_tickets[i][0]) {
    const new_arr = [...arr, new_tickets[i][1]];
    dfs(i, visited, new_arr);
    visited[i] = 0; // 여기에서 불가능했던 루트라면, 다시 visited에서 i를 방문하지 않은 것으로 처리하여 이후에 사용할 수 있도록 해주어야 했다.
  }
}
```

---

#### 다른 풀이

너무 간단하게 풀이한 DFS가 있어서 가져와 본다.

```js
function solution(tickets) {
  let answer = [];
  const result = [];
  const visited = [];

  tickets.sort(); // JS에서 sort()함수는 기본적으로 문자열을 오름차순 정렬 .. 핵어이없음!

  const len = tickets.length;
  const dfs = (str, count) => {
    // count : 티켓 사용 수
    result.push(str);

    if (count === len) {
      // 티켓 사용 수와 티켓 장수가 같으면 return
      answer = result;
      return true;
    }

    for (let i = 0; i < len; i++) {
      if (!visited[i] && tickets[i][0] === str) {
        // i 티켓은 사용하지 않았고, 사용할 티켓의 출발지와 현재 위치가 같으면 재귀 들어감
        visited[i] = true;

        if (dfs(tickets[i][1], count + 1)) return true;

        visited[i] = false; // 내 코드와 마찬가지로 dfs에서 불가능한 루트로 확인 되었을 경우, visited[i]를 false처리 해준다. *중요*
      }
    }
    result.pop(); // 방문하지 않았기 때문에 마지막 result에 넣었던 destination은 꺼내어준다.

    return false;
  };

  dfs("ICN", 0);

  return answer;
}
```

### 느낀점 or 기억할정보

- 재귀로 풀이하면 JS에서는 overflow되어서 에러날 확률이 높다. 이후에는 stack으로 풀이해보자.
- spelling 가나다라 순 비교
  - a[1].localeCompare(b[1])
- `sort()` : 기본적으로 문자열을 오름차순 정렬
- 백트래킹으로 풀이할 때 가능하지 않은 루트의 경우 visited[i]에서 false로 다시 표시해주는 것은 아주 중요하다.
