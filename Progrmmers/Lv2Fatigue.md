# Programmers 완전탐색 Fatigue

[Programmers 완전탐색 Fatigue](https://school.programmers.co.kr/learn/courses/30/lessons/87946)

## 문제 설명

XX게임에는 피로도 시스템(0 이상의 정수로 표현합니다)이 있으며, 일정 피로도를 사용해서 던전을 탐험할 수 있습니다. 이때, 각 던전마다 탐험을 시작하기 위해 필요한 "최소 필요 피로도"와 던전 탐험을 마쳤을 때 소모되는 "소모 피로도"가 있습니다. "최소 필요 피로도"는 해당 던전을 탐험하기 위해 가지고 있어야 하는 최소한의 피로도를 나타내며, "소모 피로도"는 던전을 탐험한 후 소모되는 피로도를 나타냅니다. 예를 들어 "최소 필요 피로도"가 80, "소모 피로도"가 20인 던전을 탐험하기 위해서는 유저의 현재 남은 피로도는 80 이상 이어야 하며, 던전을 탐험한 후에는 피로도 20이 소모됩니다.

이 게임에는 하루에 한 번씩 탐험할 수 있는 던전이 여러개 있는데, 한 유저가 오늘 이 던전들을 최대한 많이 탐험하려 합니다. 유저의 현재 피로도 k와 각 던전별 "최소 필요 피로도", "소모 피로도"가 담긴 2차원 배열 dungeons 가 매개변수로 주어질 때, 유저가 탐험할수 있는 최대 던전 수를 return 하도록 solution 함수를 완성해주세요.

### 제한사항

k는 1 이상 5,000 이하인 자연수입니다.  
dungeons의 세로(행) 길이(즉, 던전의 개수)는 1 이상 8 이하입니다.  
dungeons의 가로(열) 길이는 2 입니다.  
dungeons의 각 행은 각 던전의 ["최소 필요 피로도", "소모 피로도"] 입니다.  
"최소 필요 피로도"는 항상 "소모 피로도"보다 크거나 같습니다.  
"최소 필요 피로도"와 "소모 피로도"는 1 이상 1,000 이하인 자연수입니다.  
서로 다른 던전의 ["최소 필요 피로도", "소모 피로도"]가 서로 같을 수 있습니다.

### 입출력 예

| k   | dungeons                  | result |
| --- | ------------------------- | ------ |
| 80  | [[80,20],[50,40],[30,10]] | 3      |

#### 문제풀이

1. 테스트 케이스 실패
   최소 필요 피로도 - 소모 피로도 순으로 내림차순 정렬하면, 최소 필요 피로도가 크면서, 소모 피로도가 작은 순으로 정렬할 수 있다고 생각하였다. 앞에서부터 가능 여부를 확인하여 문제를 풀이하였다. -> 실패

```js
function solution(k, dungeons) {
  var answer = 0;
  dungeons = dungeons.sort((a, b) => b[0] - b[1] - (a[0] - a[1])); // 최소 필요 피로도 - 소모 피로도 순으로 정렬 -> but, 예외 있어서 탈락
  for (let i = 0; i < dungeons.length; i++) {
    if (dungeons[i][0] <= k) {
      k -= dungeons[i][1]; // 던전 투어했으면 피로도에서 소모 피로도 빼주기
      answer += 1;
    }
  }
  return answer;
}
```

2. DFS로 완전탐색
   최대 던전의 수가 8개 밖에 되지 않으므로, dfs로 완전탐색하여 문제를 풀이할 수 있었다. 0번째부터 length번째까지를 시작으로 dfs로 풀이하였다. N과M 문제 풀이 방식과 비슷하다. 현재 남은 피로도가 다음 필수 피로도보다 크고, 다음 Index를 아직 방문하지 않았다면, 그 index도 가능한 것으로 간주, 방문 표시를 한 뒤 확인한다.

```js
// 최대 던전의 개수 8
function solution(k, dungeons) {
  var answer = 0;

  visited = new Array(dungeons.length).fill(0);

  function dfs(idx, fatigue, cnt) {
    // 지금 남은 피로도 >= 최소 필요 피로도
    if (answer < cnt) {
      answer = cnt;
    }
    for (let i = 0; i < dungeons.length; i++) {
      if (visited[i] === 0 && dungeons[i][0] <= fatigue) {
        visited[i] = 1;
        dfs(i, fatigue - dungeons[i][1], cnt + 1);
        visited[i] = 0;
      }
    }
  }
  for (let i = 0; i < dungeons.length; i++) {
    visited[i] = 1;
    dfs(i, k - dungeons[i][1], 1);
    visited[i] = 0;
  }
  return answer;
}
```
