# Programmers - Map - 달리기 경주

[Programmers - Map - 달리기 경주](https://school.programmers.co.kr/learn/courses/30/lessons/178871)

## 문제 설명

얀에서는 매년 달리기 경주가 열립니다. 해설진들은 선수들이 자기 바로 앞의 선수를 추월할 때 추월한 선수의 이름을 부릅니다. 예를 들어 1등부터 3등까지 "mumu", "soe", "poe" 선수들이 순서대로 달리고 있을 때, 해설진이 "soe"선수를 불렀다면 2등인 "soe" 선수가 1등인 "mumu" 선수를 추월했다는 것입니다. 즉 "soe" 선수가 1등, "mumu" 선수가 2등으로 바뀝니다.

선수들의 이름이 1등부터 현재 등수 순서대로 담긴 문자열 배열 players와 해설진이 부른 이름을 담은 문자열 배열 callings가 매개변수로 주어질 때, 경주가 끝났을 때 선수들의 이름을 1등부터 등수 순서대로 배열에 담아 return 하는 solution 함수를 완성해주세요.

### 제한사항

5 ≤ players의 길이 ≤ 50,000  
players[i]는 i번째 선수의 이름을 의미합니다.  
players의 원소들은 알파벳 소문자로만 이루어져 있습니다.  
players에는 중복된 값이 들어가 있지 않습니다.  
3 ≤ players[i]의 길이 ≤ 10  
2 ≤ callings의 길이 ≤ 1,000,000  
callings는 players의 원소들로만 이루어져 있습니다.  
경주 진행중 1등인 선수의 이름은 불리지 않습니다.

### 입출력 예

| players                               | callings                       | result                                |
| ------------------------------------- | ------------------------------ | ------------------------------------- |
| ["mumu", "soe", "poe", "kai", "mine"] | ["kai", "kai", "mine", "mine"] | ["mumu", "kai", "mine", "soe", "poe"] |

#### 문제풀이

처음에는 배열에서 호출되는 이름의 indexOf를 구하여 players에서 앞의 사람과 위치를 바꾸는 것으로 하였으나, 몇몇 테스트케이스에서 시간초과가 발생하였다.
하여 문제를 Map으로 풀이하였다.

Map을 2개 생성하였다.
이 두 개의 Map은 같은 내용을 담지만 서로 key:value가 거꾸로 되어있다. Map이 두개여서 두개 모두 값을 변경해줘야하는 번거로움이 있지만, 시간은 배열에서 값을 변경하는 것보다 빠르다.

- `playersKeyMap` : 달리기 선수의 이름 : 등수
- `scoreKeyMap` : 등수 : 달리기 선수의 이름

이 두 배열에 모든 선수들의 처음 달리기 순서를 기입해준다.

```
Map(5) { 'mumu' => 0, 'soe' => 1, 'poe' => 2, 'kai' => 3, 'mine' => 4 }
Map(5) { 0 => 'mumu', 1 => 'soe', 2 => 'poe', 3 => 'kai', 4 => 'mine' }
```

선수의 이름이 불리면, playersKeyMap에서의 등수를 앞으로 당겨주고, 앞에 있는 등수의 사람의 등수를 +1해주어야 한다. 또한, scoreKeyMap에서의 등수의 사람을 서로 바꾸어 주어야 한다.  
callings의 배열을 순차적으로 돌면서, 먼저 불린 이름`calling`의 지금 순위`score`를 playersKeyMap에서 찾는다.  
playersKeyMap에서의 이름의 순위를 `score-1`하여, 앞으로 제친 것을 표기해준다.
그 다음, scoreKeyMap에서 선수의 원래 앞 등수`score-1`에 있던 사람의 이름`formerName`을 찾는다. 그 이름`formerName`을 가지고, playersKeyMap에서의 등수를 +1, 즉, `score`로 바꿔준다. playersKeyMap에서의 일은 모두 끝이 났다.  
마지막으로 scoreKeyMap에서 `score - 1 : calling`, `score : formerName`으로 바꾸어준다.

```js
function solution(players, callings) {
  var answer = [];

  const playersKeyMap = new Map();
  const scoreKeyMap = new Map();
  for (let i = 0; i < players.length; i++) {
    playersKeyMap.set(players[i], i);
    scoreKeyMap.set(i, players[i]);
  }

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
```
