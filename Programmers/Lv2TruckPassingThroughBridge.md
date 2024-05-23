# Programmers Stack / Queue TruckPassingThroughBridge

[Programmers Stack / Queue TruckPassingThroughBridge](https://school.programmers.co.kr/learn/courses/30/lessons/42583)

## 문제 설명

트럭 여러 대가 강을 가로지르는 일차선 다리를 정해진 순으로 건너려 합니다. 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 알아내야 합니다. 다리에는 트럭이 최대 bridge_length대 올라갈 수 있으며, 다리는 weight 이하까지의 무게를 견딜 수 있습니다. 단, 다리에 완전히 오르지 않은 트럭의 무게는 무시합니다.

예를 들어, 트럭 2대가 올라갈 수 있고 무게를 10kg까지 견디는 다리가 있습니다. 무게가 [7, 4, 5, 6]kg인 트럭이 순서대로 최단 시간 안에 다리를 건너려면 다음과 같이 건너야 합니다.

| 경과 시간 | 다리를 지난 트럭 | 다리를 건너는 트럭 | 대기 트럭 |
| --------- | ---------------- | ------------------ | --------- |
| 0         | []               | []                 | [7,4,5,6] |
| 1~2       | []               | [7]                | [4,5,6]   |
| 3         | [7]              | [4]                | [5,6]     |
| 4         | [7]              | [4,5]              | [6]       |
| 5         | [7,4]            | [5]                | [6]       |
| 6~7       | [7,4,5]          | [6]                | []        |
| 8         | [7,4,5,6]        | []                 | []        |

따라서, 모든 트럭이 다리를 지나려면 최소 8초가 걸립니다.

solution 함수의 매개변수로 다리에 올라갈 수 있는 트럭 수 bridge_length, 다리가 견딜 수 있는 무게 weight, 트럭 별 무게 truck_weights가 주어집니다. 이때 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 return 하도록 solution 함수를 완성하세요.

### 제한 조건

- bridge_length는 1 이상 10,000 이하입니다. // 이중for문 안됨
- weight는 1 이상 10,000 이하입니다.
- truck_weights의 길이는 1 이상 10,000 이하입니다.
- 모든 트럭의 무게는 1 이상 weight 이하입니다.

#### 문제풀이

truck들과 bridge에 건너고 있는 트럭들의 리스트를 queue로 두고 풀이하여, 앞에서부터 뒤로 확인하도록 하였다.  
아직 건너지 못한 트럭(trucksQueue)들과 다리 위의 트럭(bridge)들의 리스트에 한대라도 있다면 계속 while문을 반복하는 것이다.
여기에서 answer은 모든 트럭이 다리를 건너는 데 걸리는 총 시간이다.

1. 다리 위에 트럭이 없다면 trucksQueue의 맨 앞의 트럭을 bridge 배열로 이동시킨다 `enqueue`. 여기에서 bridge의 각 트럭들은 [트럭의 무게, 트럭이 다리를 건너고 있는 기간]으로 기록된다. 여기에서 `트럭이 다리를 건너고 있는 기간`은 매 while 문 반복마다 1씩 추가된다.
2. 만약 다리에 트럭이 한 대 이상 있고, 이 트럭들의 총 무게 + 지금 출발할지 말지 고민중인 트럭의 무게 가 weight(다리가 견딜 수 있는 무게)보다 낮다면 트럭 한 대를 출발시킨다 `enqueue`.
3. 그렇지 않다면 버스를 출발시키지 않는다.
4. 다리 위에 있는 트럭들의 `트럭이 다리를 건너고 있는 기간`을 1씩 늘리고, 맨 앞 트럭이 다리의 길이와 동일하다면 다리를 다 건넌 것으로 생각하고 bridge에서 `dequeue`해준다.

매 while문은 1시간이 흐른 것이므로 answer을 1씩 추가해준다.

```js
function sum(arr) {
  let result = 0;
  for (const a of arr) {
    result += a[0];
  }
  return result;
}
function solution(bridge_length, weight, truck_weights) {
  var answer = 1;
  const trucksQueue = [...truck_weights];
  const bridge = [];

  while (trucksQueue.length || bridge.length) {
    if (bridge.length === 0) {
      const truck = trucksQueue.shift();
      // 다리에 트럭이 없으면 트럭 출발
      bridge.push([truck, 0]);
    } else if (sum(bridge) + trucksQueue[0] <= weight) {
      // 다리에 있는 트럭들의 무게의 합이 weight보다 작거나 같으면 트럭 출발
      const truck = trucksQueue.shift();
      bridge.push([truck, 0]);
    }
    for (let i = 0; i < bridge.length; i++) {
      bridge[i][1] = bridge[i][1] + 1;
    }
    if (bridge[0][1] === bridge_length) {
      bridge.shift();
    }
    answer++;
  }

  return answer;
}
```
