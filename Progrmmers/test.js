function solution(players, callings) {
  var answer = [];

  const playersKeyMap = new Map();
  const scoreKeyMap = new Map();
  for (let i = 0; i < players.length; i++) {
    playersKeyMap.set(players[i], i);
    scoreKeyMap.set(i, players[i]);
  }
  console.log(playersKeyMap);
  console.log(scoreKeyMap);

  for (const calling of callings) {
    const score = playersKeyMap.get(calling); // 이름 부른 사람의 지금 순위
    playersKeyMap.set(calling, score - 1);
    const formerName = scoreKeyMap.get(score - 1);
    playersKeyMap.set(formerName, score);
    scoreKeyMap.set(score - 1, calling);
    scoreKeyMap.set(score, formerName);
  }
  answer = [...scoreKeyMap.values()];
  return answer;
}

solution(["mumu", "soe", "poe", "kai", "mine"], ["kai", "kai", "mine", "mine"]);
