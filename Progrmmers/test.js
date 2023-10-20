let unionFinds = [];
const find = (a) => {
  if (unionFinds[a] < 0) {
    return a;
  }
  unionFinds[a] = find(unionFinds[a]);
  return unionFinds[a];
};

const merge = (a, b) => {
  const fa = find(a);
  const fb = find(b);
  if (fa === fb) return;

  unionFinds[fa] += unionFinds[fb];
  unionFinds[fb] = fa;
};

function solution(n, wires) {
  let result = Infinity;
  const N = wires.length;

  for (let node = 0; node < N; node++) {
    unionFinds = new Array(n + 1).fill(-1);
    console.log("unionFinds", unionFinds);
    const graph = wires.filter((_, i) => i != node); // 줄 끊기
    console.log(graph);

    for (const [v, w] of graph) merge(v, w);
    console.log(unionFinds);

    const [a, b] = unionFinds.slice(1).filter((v) => v < 0);
    console.log("a,b", a, b);
    result = Math.min(result, Math.abs(a - b));
  }
  return result;
}

solution(9, [
  [1, 3],
  [2, 3],
  [3, 4],
  [4, 5],
  [4, 6],
  [4, 7],
  [7, 8],
  [7, 9],
]);
