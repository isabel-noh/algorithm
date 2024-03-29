// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(moves) {
  let answer = false;
  // Implement your solution here
  const directions = { "^": [0, 1], v: [0, -1], "<": [-1, 0], ">": [1, 0] }; // up, down, left, right
  const visited = [...new Array(200)].map(() => new Array(200).fill(0));
  let cur = [100, 100];

  for (let i = 0; i < moves.length; i++) {
    const dir = directions[moves[i]];
    let na = cur[0] + dir[0],
      nb = cur[1] + dir[1];
    if (visited[na][nb] === 1 && na !== 100 && nb !== 100) {
      // if visited already(which means, spot was visited over twice), but not (0, 0) -> false
      return answer;
    }
    cur = [na, nb]; // move current position
    visited[na][nb] = 1; // mark as visited
  }
  if (cur[0] === 100 && cur[1] === 100) {
    // if moves are all done and final current position is (0, 0) -> true
    answer = true;
  }
  return answer;
}
solution("^^^<<<<vvv>>>>");
solution("<vvv>>^^^<");
solution("<^^^>v");
solution("<<^^^^<<vv>>>>vv");
