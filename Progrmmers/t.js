function solution(players, callings) {
  var answer = [];

  const map = new Map();
  for (let i = 0; i < players.length; i++) {
    map.set(players[i], i);
  }

  for (const calling of callings) {
    const key = map.get(calling);
    map.set(calling, key - 1);
  }
  console.log(map);
  return players;
}

solution(["mumu", "soe", "poe", "kai", "mine"], ["kai", "kai", "mine", "mine"]);
