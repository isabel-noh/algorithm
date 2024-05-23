# Programmers - Greedy - 구명보트

[Programmers - Greedy - 구명보트](https://school.programmers.co.kr/learn/courses/30/lessons/42885)

## 문제 설명

무인도에 갇힌 사람들을 구명보트를 이용하여 구출하려고 합니다. 구명보트는 작아서 한 번에 최대 2명씩 밖에 탈 수 없고, 무게 제한도 있습니다.

예를 들어, 사람들의 몸무게가 [70kg, 50kg, 80kg, 50kg]이고 구명보트의 무게 제한이 100kg이라면 2번째 사람과 4번째 사람은 같이 탈 수 있지만 1번째 사람과 3번째 사람의 무게의 합은 150kg이므로 구명보트의 무게 제한을 초과하여 같이 탈 수 없습니다.

구명보트를 최대한 적게 사용하여 모든 사람을 구출하려고 합니다.

사람들의 몸무게를 담은 배열 people과 구명보트의 무게 제한 limit가 매개변수로 주어질 때, 모든 사람을 구출하기 위해 필요한 구명보트 개수의 최솟값을 return 하도록 solution 함수를 작성해주세요.

### 제한사항

- 무인도에 갇힌 사람은 1명 이상 50,000명 이하입니다.
- 각 사람의 몸무게는 40kg 이상 240kg 이하입니다.
- 구명보트의 무게 제한은 40kg 이상 240kg 이하입니다.
- 구명보트의 무게 제한은 항상 사람들의 몸무게 중 최댓값보다 크게 주어지므로 사람들을 구출할 수 없는 경우는 없습니다.

#### 문제풀이

해당 문제에서는 `투포인터 알고리즘`을 활용하였다.  
먼저 사람들을 무게 오름차순으로 정렬해놓고, left 변수에는 index 0을, right 변수에는 배열의 마지막 index를 정해준다.  
맨 왼쪽에는 가장 가벼운 사람이, 맨 오른쪽에는 제일 무거운 사람이 서있을 것이다.
제일 가벼운 사람과 제일 무거운 사람의 합이 limit이 넘는다면, 제일 무거운 사람은 누구랑 같이 탈 수 없는 몸무게이므로, 구명보트를 한 대 보내고 (answer++) right 인덱스를 한사람 앞으로 변경한다.  
만약 현재 기준에서 가장 가벼운 사람과 가장 무거운 사람의 합이 limit보다 작거나 같다면, 이 두명은 보트에 태울 수 있는 몸무게가 되므로, 구명보트를 한 대 보내고 (answer++) left를 뒷사람으로, right를 앞사람으로 변경한다.  
이 두 방법을 right, left가 만날 때까지 반복한다.

```js
function solution(people, limit) {
  var answer = 0;
  // 구명보트 최소값
  const pp = [...people].sort((a, b) => a - b);
  let left = 0;
  let right = pp.length - 1;
  while (left <= right) {
    if (pp[left] + pp[right] > limit) {
      answer++;
      right--;
    } else if (pp[left] + pp[right] <= limit) {
      answer++;
      left++;
      right--;
    }
  }
  return answer;
}
```
