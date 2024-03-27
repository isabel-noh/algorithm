function solution(n, computers) {
  var network = 0;
  const visited = [...new Array(n)].fill(0);

  function dfs(x) {
    for (let i = 0; i < n; i++) {
      if (computers[x][i] === 1 && visited[i] === 0) {
        visited[i] = 1;
        dfs(i);
      }
    }
  }
  for (let i = 0; i < n; i++) {
    if (visited[i] !== 1) {
      visited[i] = 1;
      dfs(i);
      network++;
    }
  }
  return network;
}

solution(3, [
  [1, 1, 0],
  [1, 1, 0],
  [0, 0, 1],
]);
solution(3, [
  [1, 1, 0],
  [1, 1, 1],
  [0, 1, 1],
]);
