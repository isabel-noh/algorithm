# Programmers Heap - Disc Controller

[Programmers Heap - Disc Controller](https://school.programmers.co.kr/learn/courses/30/lessons/42627)

## 문제 설명

하드디스크는 한 번에 하나의 작업만 수행할 수 있습니다. 디스크 컨트롤러를 구현하는 방법은 여러 가지가 있습니다. 가장 일반적인 방법은 요청이 들어온 순서대로 처리하는 것입니다.

예를들어

- 0ms 시점에 3ms가 소요되는 A작업 요청
- 1ms 시점에 9ms가 소요되는 B작업 요청
- 2ms 시점에 6ms가 소요되는 C작업 요청
  와 같은 요청이 들어왔습니다. 이를 그림으로 표현하면 아래와 같습니다.

한 번에 하나의 요청만을 수행할 수 있기 때문에 각각의 작업을 요청받은 순서대로 처리하면 다음과 같이 처리 됩니다.

- A: 3ms 시점에 작업 완료 (요청에서 종료까지 : 3ms)
- B: 1ms부터 대기하다가, 3ms 시점에 작업을 시작해서 12ms 시점에 작업 완료(요청에서 종료까지 : 11ms)
- C: 2ms부터 대기하다가, 12ms 시점에 작업을 시작해서 18ms 시점에 작업 완료(요청에서 종료까지 : 16ms)
  이 때 각 작업의 요청부터 종료까지 걸린 시간의 평균은 10ms(= (3 + 11 + 16) / 3)가 됩니다.

하지만 A → C → B 순서대로 처리하면

- A: 3ms 시점에 작업 완료(요청에서 종료까지 : 3ms)
- C: 2ms부터 대기하다가, 3ms 시점에 작업을 시작해서 9ms 시점에 작업 완료(요청에서 종료까지 : 7ms)
- B: 1ms부터 대기하다가, 9ms 시점에 작업을 시작해서 18ms 시점에 작업 완료(요청에서 종료까지 : 17ms)
  이렇게 A → C → B의 순서로 처리하면 각 작업의 요청부터 종료까지 걸린 시간의 평균은 9ms(= (3 + 7 + 17) / 3)가 됩니다.

각 작업에 대해 [작업이 요청되는 시점, 작업의 소요시간]을 담은 2차원 배열 jobs가 매개변수로 주어질 때, 작업의 요청부터 종료까지 걸린 시간의 평균을 가장 줄이는 방법으로 처리하면 평균이 얼마가 되는지 return 하도록 solution 함수를 작성해주세요. (단, 소수점 이하의 수는 버립니다)

### 제한 사항

jobs의 길이는 1 이상 500 이하입니다.  
jobs의 각 행은 하나의 작업에 대한 [작업이 요청되는 시점, 작업의 소요시간] 입니다.  
각 작업에 대해 작업이 요청되는 시간은 0 이상 1,000 이하입니다.  
각 작업에 대해 작업의 소요시간은 1 이상 1,000 이하입니다.  
하드디스크가 작업을 수행하고 있지 않을 때에는 먼저 요청이 들어온 작업부터 처리합니다.

### 입출력 예

| jobs                     | return |
| ------------------------ | ------ |
| [[0, 3], [1, 9], [2, 6]] | 9      |

입출력 예 설명
문제에 주어진 예와 같습니다.

0ms 시점에 3ms 걸리는 작업 요청이 들어옵니다.  
1ms 시점에 9ms 걸리는 작업 요청이 들어옵니다.  
2ms 시점에 6ms 걸리는 작업 요청이 들어옵니다.

#### 문제풀이

먼저 최소힙을 활용하여 풀이하는 문제이다. (힙을 활용하지 않고 queue로도 풀이할 수 있다. 아래에 후록)

종료까지 걸리는 평균시간이 최소가 되기 위해서는`` 가장 짧은 실행 시간을 가진 Process를 먼처 처리`하면 된다.  
짧은 걸 먼저 처리하면, 전체적인 남아있는 대기 job들에 대해서 딜레이를 적게 발생시킨다. 먼저 처리 되는 것이 '끝날 때'까지 기다려야 하기 때문이다. 그렇기 때문에 heap을 활용하여 작업들의 소요시간을 기준으로 정렬할 수 있게 해준다.

여기에서 놓친 부분들을 나열하자면,

1. 걸리는 시간이 같은 경우? 먼저 오는 작업을 먼저 처리해야 한다. -> 이를 처리하기 위해서 처음에 input으로 jobs의 리스트가 들어올 때, 이를 jobs[i][0]인 작업 도착시간을 기준으로 정렬한다.

```js
const jobs = [...input].sort((a, b) => a[0] - b[0]);
```

2. 작업을 하다가 끝나고, 대기 중인 작업이 없는 경우, 바로 시작할 수 있는 작업을 수행해야 함
   - 4초에 작업이 끝이 났고, 다음에 있는 작업들이 [7, 2]와 [5, 3]이 있다면, [5, 3]을 먼저 처리해야 한다는 것이다.

answer : 각 작업이 진행될 때마다, 작업 소요 시간과 대기한 시간을 총합한 값
jobDoneAt : 작업이 끝난 시각
currentTime : 시간을 0부터 1초씩 더해서 시간이 흐름을 표현함 -> 지금 시간이 작업들 중에서 최소 소요 시간인 작업의 시작 시간과 일치한다면, jobs에서 빼서 heap에 넣음

먼저 언제 Heap에 넣을지를 생각해 보아야 한다. 변수 `currentTime`이 있다. 해당 변수는 `현재 시간`을 나타낸다. 현재 시간이 시작 시간에 이른 순으로 정렬되어 있는 jobs 리스트의 0번째 값, 즉 남은 작업들 중에서 현재 시간에 시작할 수 있는 작업들을 빼서 heap에 넣어준다. 만일 동일한 시간에 시작하는 업무가 여러 개 있다면 모두 heap에 들어가서 소요 시간대로 정렬될 것이다.

heap에는 현재 대기 중인 작업들이 있는 것이다. heap에 대기 중인 작업이 있고, 현재 시간이 전 업무가 끝난 시간 이후라면, 즉, 작업 중인 업무가 없다면, heap에서 대기중인 작업을 하나 꺼낸다. 이것은 지금 시간에 바로 할 수 있는 것들 중에서 제일 시간이 적게 소요되는 일일 것이다.

jobDoneAt은 새로운 작업을 진행했기 때문에, 현재 시간 + 작업의 소요 시간을 더해 업데이트해준다. answer(모든 작업의 소요 시간 + 대기 시간)은 새로운 작업이 끝난 시간 - 새로운 작업의 시작 시간을 더하여 업데이트 해준다. `새로운 작업이 끝난 시간 - 새로운 작업의 시작 시간`은 (currentTime - startTime + job)으로 `방금 진행한 업무가 대기한 시간 + 해당 업무의 소요 시간`이다.

```js
function solution(input) {
  const heap = new Heap();

  const cnt = input.length;
  let answer = 0;
  let jobDoneAt = 0;
  let currentTime = 0;

  const jobs = [...input].sort((a, b) => a[0] - b[0]);
  // 같은 소요시간이 걸리는 경우도 있을 수 있기 때문에, 더 먼저 들어오는 작업을 먼저 처리하기 위해서 정렬

  while (jobs.length || heap.heap.length) {
    // jobs나 heap에 작업이 있으면 처리 하지 않은 일이 있다는 의미이므로, 계속 반복
    while (jobs.length) {
      if (currentTime === jobs[0][0]) {
        // 지금 바로 할 수 있는 일이면 빼서 heap에 넣기
        heap.push(jobs.shift());
      } else break;
    }
    // heap에 대기중인 작업이 있고, 진행 중인 작업의 종료 시간이 현재 시간과 같거나, 현재 시간이 되기 전에 이미 작업이 종료되었다면 바로 다른 작업을 시작할 수 있음
    if (heap.heap.length && jobDoneAt <= currentTime) {
      // heap에 있는 값들 중에서 제일 작업 소요시간이 덜 걸리는 것이 지금 대기 중이거나 바로 시작할 수 있는 경우, 처리
      const [startTime, job] = heap.pop(); // 지금 바로 할 수 있는 일 중에서 제일 시간이 적게 소요되는 일이 나오게 될 것
      jobDoneAt = currentTime + job; // 현재의 작업이 끝나는 시간 = 현재 업무를 시작하는 현재 시간 + 작업 소요 시간;
      answer += jobDoneAt - startTime;
    }
    currentTime++; // 시간이 흘러감에 따라 확인
  }

  // answer = jobDoneAt + totalWaitingTime;
  return Math.floor(answer / cnt);
}

class Heap {
  constructor() {
    this.heap = [];
  }
  getParent(idx) {
    return Math.floor((idx - 1) / 2);
  }
  getLeftChild(idx) {
    return idx * 2 + 1;
  }
  getRightChild(idx) {
    return idx * 2 + 2;
  }
  swap(idx1, idx2) {
    [this.heap[idx1], this.heap[idx2]] = [this.heap[idx2], this.heap[idx1]];
    return this.heap;
  }
  push(item) {
    this.heap.push(item);
    let cur = this.heap.length - 1;
    let parent = this.getParent(cur);
    if (this.heap.length === 1) {
      return;
    }
    // 부모와 계속 비교하면서 부모보다 더 클 때까지 자리 교체
    while (this.heap[parent] && this.heap[cur][1] < this.heap[parent][1]) {
      this.swap(cur, parent);
      cur = parent;
      parent = this.getParent(cur);
    }
  }
  pop() {
    // 아무것도 없을 때
    if (this.heap.length === 0) {
      return null;
    }
    // 자식이 없는 경우,
    if (this.heap.length === 1) {
      return this.heap.pop();
    }
    // 자식이 있는 경우,
    const value = this.heap[0];
    this.heap[0] = this.heap[this.heap.length - 1];
    this.heap.pop();

    let cur = 0;
    let leftChild = this.getLeftChild(cur);
    let rightChild = this.getRightChild(cur);

    while (
      (this.heap[leftChild] && this.heap[cur][1] > this.heap[leftChild][1]) ||
      (this.heap[rightChild] && this.heap[cur][1] > this.heap[rightChild][1])
    ) {
      if (
        // 오른쪽 자식이 있고(오른쪽 자식이 있다면 왼쪽 자식도 당연히 있음), 왼쪽 자식이 오른쪽 자식보다 큰 경우, 오른쪽 자식과 current의 값을 변경한다(더 작은 쪽과 swap)
        this.heap[rightChild] &&
        this.heap[leftChild][1] > this.heap[rightChild][1]
      ) {
        this.swap(rightChild, cur);
        cur = rightChild;
        rightChild = this.getRightChild(cur);
        leftChild = this.getLeftChild(cur); // 오른쪽과 swap하였어도, 왼쪽도 업데이트 해주어야 함
      } else {
        this.swap(leftChild, cur);
        cur = leftChild;
        rightChild = this.getRightChild(cur);
        leftChild = this.getLeftChild(cur); // 왼쪽과 swap하였어도, 오른쪽도 업데이트 해주어야 함
      }
    }
    return value;
  }
}
```

#### heap을 사용하지 않은 풀이

heap 대신 queue와 sort를 활용한 풀이이다. 내용은 동일하다.

```js
function solution(jobs) {
    var answer = 0;
    let index = 0;
    let now = 0;
    let sum = 0;
    const length = jobs.length;

    jobs.sort((a, b) => a[0]- b[0]);

    const waiting = [];

    while (index < jobs.length || waiting.length > 0) {
        if (index < jobs.length && now >= jobs[index][0]) {
            waiting.push(jobs[index]);
            index += 1;

            waiting.sort((a, b) => a[1] - b[1]); // minHeap 대신 queue에서 a[1], 즉 작업의 소요시간을 기준으로 다시 오름차순으로 정렬
            continue;
        }
        if (!waiting.length) {
            now = jobs[index][0];
        } else {
            const first = waiting.shift();
            sum += now - first[0] + first[1];

            now += first[1];
        }
    }

    answer = Math.floor(sum / length);
```
