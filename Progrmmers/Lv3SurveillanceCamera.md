# Programmers - Greedy - 단속카메라

[Programmers - Greedy - 단속카메라](https://school.programmers.co.kr/learn/courses/30/lessons/42884)

## 문제

고속도로를 이동하는 모든 차량이 고속도로를 이용하면서 단속용 카메라를 한 번은 만나도록 카메라를 설치하려고 합니다.

고속도로를 이동하는 차량의 경로 routes가 매개변수로 주어질 때, 모든 차량이 한 번은 단속용 카메라를 만나도록 하려면 최소 몇 대의 카메라를 설치해야 하는지를 return 하도록 solution 함수를 완성하세요.

### 제한사항

- 차량의 대수는 1대 이상 10,000대 이하입니다.
- routes에는 차량의 이동 경로가 포함되어 있으며 routes[i][0]에는 i번째 차량이 고속도로에 진입한 지점, routes[i][1]에는 i번째 차량이 고속도로에서 나간 지점이 적혀 있습니다.
- 차량의 진입/진출 지점에 카메라가 설치되어 있어도 카메라를 만난것으로 간주합니다.
- 차량의 진입 지점, 진출 지점은 -30,000 이상 30,000 이하입니다.

#### 문제풀이

Greedy  
먼저 카메라를 어떻게 최소로 설치할 수 있을지 잘 생각해보자.

- 이전 차량 진출 시점(이전 카메라 설치 위치) < 현재 차량 진입 시점
  - 카메라 1대 추가 설치
  - 최근 카메라 설치 위치 = 현재 차량의 진출 시점으로 갱신
- 이전 차량 진출 시점(이전 카메라 설치 위치) > 다음 차량 진출 시점
  - 카메라 설치 불 필요

차량의 도착지점을 기준으로 오름차순으로 정렬하였다.  
처음 시작에는 첫 차량의 도착지점에 감시카메라를 설치한다. 도착지점에 설치하는 이유는, 해당 구간을 지난 차량을 모두 감시할 수 있다. 그러면 최소 개수의 감시 카메라를 설치할 수 있다.  
직전에 설치한 감시 카메라의 위치가 현재 확인 중의 차량 경로의 밖에 있다면 감시카메를 하나 더 설치하여야 한다.

```js
function solution(routes) {
  // 한 번은 단속용 카메라를 만나도록 하려면 최소 몇 대의 카메라
  var answer = 0;
  const sorted = routes.sort((a, b) => a[1] - b[1]);
  let surveillanceCamera = 0;
  for (const route of sorted) {
    const [s, e] = route;
    if (surveillanceCamera === 0) {
      answer++;
      surveillanceCamera = e;
    } else if (s > surveillanceCamera) {
      answer++;
      surveillanceCamera = e;
    }
  }
  return answer;
}
```
