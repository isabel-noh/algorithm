# Programmers - DFS/BFS - 단어 변환

[Programmers - DFS/BFS - 단어 변환](https://school.programmers.co.kr/learn/courses/30/lessons/43163)

## 문제 설명

두 개의 단어 begin, target과 단어의 집합 words가 있습니다. 아래와 같은 규칙을 이용하여 begin에서 target으로 변환하는 가장 짧은 변환 과정을 찾으려고 합니다.

1.  한 번에 한 개의 알파벳만 바꿀 수 있습니다.
2.  words에 있는 단어로만 변환할 수 있습니다.

예를 들어 begin이 "hit", target가 "cog", words가 ["hot","dot","dog","lot","log","cog"]라면 "hit" -> "hot" -> "dot" -> "dog" -> "cog"와 같이 4단계를 거쳐 변환할 수 있습니다.

두 개의 단어 begin, target과 단어의 집합 words가 매개변수로 주어질 때, 최소 몇 단계의 과정을 거쳐 begin을 target으로 변환할 수 있는지 return 하도록 solution 함수를 작성해주세요.

### 제한사항

- 각 단어는 알파벳 소문자로만 이루어져 있습니다.
- 각 단어의 길이는 3 이상 10 이하이며 모든 단어의 길이는 같습니다.
- words에는 3개 이상 50개 이하의 단어가 있으며 중복되는 단어는 없습니다.
- begin과 target은 같지 않습니다.
- 변환할 수 없는 경우에는 0를 return 합니다.

## 문제 분석 요약

begin 단어를 한 철자씩 바꾸어서 최종 목표 target 단어로 몇 번만에 갈 수 있는지 확인하는 문제  
철자는 하나씩 바꿀 수 있지만 바꿀 수 있는 단어는 words에 한정되어 있음 -> 모든 철자를 확인할 필요가 없음

단어의 길이는 최대 10이고, 한 단어에 대해서 모든 변화 가능한 단어를 확인하는 것은 O(10\*26(영어철자)) = O(1)만큼 소요됨  
단어 변환 과정은 최대 O(N(words의 길이))이 걸림

## 알고리즘 설계

단어의 변환 과정이 모두 words 배열로 제한되어 있고, 최단 거리를 구하는 문제라고 이해하여 `BFS`로 풀이하였다.  
"hit", target가 "cog", words가 ["hot","dot","dog","lot","log","cog"]라고 했을 때, "hit" -> "hot" -> "dot" -> "dog" -> "cog"  
index로 표기하면 0 -> 1 -> 2 -> 5로 표시할 수 있다.  
queue에는 [현재 확인중인 단어, 이동 거리]를 표기해준다.  
처음에 "hit"에서 변경될 수 있는 단어는 "hot" 뿐이므로, queue에 ["hot", 1]을 넣는다.
그 다음 "hot"에서 변경될 수 있는 단어는 "dot", "lot"이다. 그러면 queue에는 [["dot", 1+1], ["lot", 1+1]]이 들어가게 된다.
같은 단어를 반복해서 확인하지 않게 하기 위해서 visited를 words 길이만큼 선언해주고, 이동하면서 방문기록을 표시하여주었다.

또한 처음부터 words리스트에 target단어가 없다면 어차피 해결하지 못하는 문제이므로 바로 0을 리턴해주도록 하여 시간을 줄일 수 있도록 하였다.

## 코드

```js
function check(w, t, l) {
  let count = 0; // 다른 철자의 개수
  for (let i = 0; i < l; i++) {
    if (w[i] === t[i]) continue;
    else count++;
    if (count > 1) break;
  }
  return count > 1 ? false : true;
}
function solution(begin, target, words) {
  var answer = 0;
  const length = begin.length;
  const visited = new Array(words.length).fill(0);
  if (!words.includes(target)) return answer; // 어차피 words 리스트에 target 문자 없으면 변환 못하는 것이므로 0 리턴
  function bfs(word) {
    const queue = [[word, 0]];
    while (queue.length > 0) {
      const [word, distance] = queue.shift();
      if (word === target) {
        answer = distance;
        break;
      }
      for (let index = 0; index < words.length; index++) {
        if (check(word, words[index], length) && visited[index] === 0) {
          queue.push([words[index], distance + 1]);
          visited[index] = 1;
        }
      }
    }
  }
  bfs(begin);
  console.log("answer", answer);
  return answer;
}

solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]);
solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]);
```

## 시간 복잡도

bfs에서 최악의 경우 모든 단어를 한 번씩 방문해야 하므로 O(N) 시간이 소요된다.  
N = words 배열의 길이

## 틀린 이유

## 틀린 부분 수정 or 다른 풀이

다른 풀이에서는 visited에 distance를 바로 표기하였다. 여기는 2차원 배열도 아니므로 그런 방식으로 간단하게 표기해도 될 것 같다.

```js
function solution(begin, target, words) {
  const visited = { [begin]: 0 };
  const queue = [begin];

  while (queue.length) {
    const cur = queue.shift();

    if (cur === target) break;

    for (const word of words) {
      if (isConnected(word, cur) && !visited[word]) {
        visited[word] = visited[cur] + 1;
        queue.push(word);
      }
    }
  }
  return visited[target] ? visited[target] : 0;
}
```

## 느낀점 or 기억할정보

간단한 bfs 문제였다. String 변환 문제가 아니라 bfs문제라는 것을 알아내는것이 관건인 것 같다.  
bfs나 dfs 문제풀이에서는 visited가 방문 했던 곳을 다시 가서 뺑뺑 돌지 않도록 하는 key라는 것을 잊지말자
