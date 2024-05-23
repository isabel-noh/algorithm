# Programmers Stack / Queue Process

[Programmers Stack/Queue Process](https://school.programmers.co.kr/learn/courses/30/lessons/42587)

## 문제 설명

운영체제의 역할 중 하나는 컴퓨터 시스템의 자원을 효율적으로 관리하는 것입니다. 이 문제에서는 운영체제가 다음 규칙에 따라 프로세스를 관리할 경우 특정 프로세스가 몇 번째로 실행되는지 알아내면 됩니다.

|1. 실행 대기 큐(Queue)에서 대기중인 프로세스 하나를 꺼냅니다.
|2. 큐에 대기중인 프로세스 중 우선순위가 더 높은 프로세스가 있다면 방금 꺼낸 프로세스를 다시 큐에 넣습니다.
|3. 만약 그런 프로세스가 없다면 방금 꺼낸 프로세스를 실행합니다.
| 3.1 한 번 실행한 프로세스는 다시 큐에 넣지 않고 그대로 종료됩니다.

예를 들어 프로세스 4개 [A, B, C, D]가 순서대로 실행 대기 큐에 들어있고, 우선순위가 [2, 1, 3, 2]라면 [C, D, A, B] 순으로 실행하게 됩니다.

현재 실행 대기 큐(Queue)에 있는 프로세스의 중요도가 순서대로 담긴 배열 priorities와, 몇 번째로 실행되는지 알고싶은 프로세스의 위치를 알려주는 location이 매개변수로 주어질 때, 해당 프로세스가 몇 번째로 실행되는지 return 하도록 solution 함수를 작성해주세요.

### 제한사항

- priorities의 길이는 1 이상 100 이하입니다.˜
  - priorities의 원소는 1 이상 9 이하의 정수입니다.
  - priorities의 원소는 우선순위를 나타내며 숫자가 클 수록 우선순위가 높습니다.
- location은 0 이상 (대기 큐에 있는 프로세스 수 - 1) 이하의 값을 가집니다.
  - priorities의 가장 앞에 있으면 0, 두 번째에 있으면 1 … 과 같이 표현합니다.

### 입출력 예

| priorities         | location | return |
| ------------------ | -------- | ------ |
| [2, 1, 3, 2]       | 2        | 1      |
| [1, 1, 9, 1, 1, 1] | 0        | 5      |

#### 문제풀이

queue를 활용하여 풀이하였다.  
maxPriority : 현재 남아있는 해야되는 일들 중에서 제일 높은 우선순위를 나타낸다. 제일 높은 우선순위를 처리하면 maxPriority는 그다음 우선순위로 바뀐다.  
execute : 업무를 실행할 때 그 업무의 index를 저장할 배열  
queue : 남은 업무들의 리스트로 queue 형식으로 저장되어, 0번째 값부터 처리된다.  
index : 처음 업무들이 들어왔을 때의 순서를 저장한 리스트

queue에 저장된 업무들이 모두 처리될 때까지 while문을 반복할 것이다.  
queue의 업무들은 0번째부터 pop되어 처리될지 다음에 처리될지 결정된다. 해당 업무의 priority가 max보다 적다면 queue의 맨뒤로 다시 push된다.  
max우선순위와 해당 업무의 우선순위가 일치한다면, 이는 제일 우선순위가 높은 업무로 처리했다는 의미로 execute로 해당 업무의 index를 보낸다. 만약 해당 업무의 index가 우리가 확인하고자하는 idx와 동일하다면 execute배열의 길이, 즉 해당 업무의 순번이 answer가 된다.  
그렇지 않다면, 계속 while문을 이어가되, maxPriority는 이제 현재 업무가 빠진 상태의 queue에서의 priority중 제일 높은 숫자가 된다.

이것을 반복하다보면, 모든 업무가 정해진 순서대로 처리가 되어 execute로 옮겨지게되고, execute에서 우리가 찾고자하는 idx의 index + 1을 찾으면 그것이 idx가 처리된 순서이다.

```js
function solution(priorities, idx) {
  var answer = 0;
  let maxPriority = Math.max(...priorities);

  const execute = [];
  const queue = [...priorities];
  const index = [];
  for (let i = 0; i < priorities.length; i++) {
    index.push(i);
  }
  while (queue.length) {
    const p = queue.shift();
    const i = index.shift();
    if (p === maxPriority) {
      execute.push(i);
      if (i === idx) {
        answer = execute.length;
        return answer;
      }
      maxPriority = Math.max(...queue);
    } else {
      queue.push(p);
      index.push(i);
    }
  }
  answer = execute.indexOf(idx) + 1;
  return answer;
}
solution([2, 1, 3, 2], 2);
solution([1, 1, 9, 1, 1, 1], 0);
```
