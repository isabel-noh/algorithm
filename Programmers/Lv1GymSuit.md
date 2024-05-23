# Programmers 그리디 체육복

[Programmers 그리디 체육복](https://school.programmers.co.kr/learn/courses/30/lessons/42862)

## 문제 설명

점심시간에 도둑이 들어, 일부 학생이 체육복을 도난당했습니다. 다행히 여벌 체육복이 있는 학생이 이들에게 체육복을 빌려주려 합니다. 학생들의 번호는 체격 순으로 매겨져 있어, 바로 앞번호의 학생이나 바로 뒷번호의 학생에게만 체육복을 빌려줄 수 있습니다. 예를 들어, 4번 학생은 3번 학생이나 5번 학생에게만 체육복을 빌려줄 수 있습니다. 체육복이 없으면 수업을 들을 수 없기 때문에 체육복을 적절히 빌려 최대한 많은 학생이 체육수업을 들어야 합니다.

전체 학생의 수 n, 체육복을 도난당한 학생들의 번호가 담긴 배열 lost, 여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 reserve가 매개변수로 주어질 때, 체육수업을 들을 수 있는 학생의 최댓값을 return 하도록 solution 함수를 작성해주세요.

### 제한사항

전체 학생의 수는 2명 이상 30명 이하입니다.
체육복을 도난당한 학생의 수는 1명 이상 n명 이하이고 중복되는 번호는 없습니다.
여벌의 체육복을 가져온 학생의 수는 1명 이상 n명 이하이고 중복되는 번호는 없습니다.
여벌 체육복이 있는 학생만 다른 학생에게 체육복을 빌려줄 수 있습니다.
여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있습니다. 이때 이 학생은 체육복을 하나만 도난당했다고 가정하며, 남은 체육복이 하나이기에 다른 학생에게는 체육복을 빌려줄 수 없습니다.

### 입출력 예

    | n | lost | reserve |return|
    |--|--|--|--|

|5 |[2, 4] |[1, 3, 5] |5|
|5 |[2, 4] |[3] 4|
|3 |[3]| [1]| 2|

#### 문제풀이

1. 앞에서부터 차례대로 확인한 경우와 뒤에서부터 확인하는 경우를 비교하여 더 큰 값을 출력하는 방식  
   체육복을 앞의 애가 먼저 가져가면 뒤에 애중에서 못가져가는 애가 있다고 생각하여, 위의 방식  
   으로 풀었으나, 헛수고~
   -> [2, 0, 0, 0, 2]의 경우, 위 방식으로 문제를 풀이하면, [1, 1, 0, 0, 2] 혹은 [2, 0, 0, 1, 1]로 체육복이 배분됨.  
    하지만 사실은 [1, 1, 0, 1, 1]의 경우처럼 4명이 체육복을 가질 수 있음.

```js
function solution(n, lost, reserve) {
  var answer = 0;
  const students = Array(n).fill(1);
  for (const l of lost) {
    students[l - 1] = 0;
  }
  for (const r of reserve) {
    students[r - 1] += 1;
  }
  const reverseStudents = [...students];
  let left = 0;
  for (let i = 0; i < students.length; i++) {
    if (students[i] > 1) {
      left = 1;
    } else if (students[i] === 0 && left >= 1) {
      left = 0;
      students[i] = 1;
      students[i - 1] -= 1;
    } else if (students[i] === 1) {
      left = 0;
    }
  }
  for (let i = reverseStudents.length - 1; i > -1; i--) {
    if (reverseStudents[i] > 1) {
      left = 1;
    } else if (reverseStudents[i] === 0 && left >= 1) {
      left = 0;
      reverseStudents[i] = 1;
      reverseStudents[i + 1] -= 1;
    } else if (reverseStudents[i] === 1) {
      left = 0;
    }
  }
  let answer2 = 0;
  for (let i = 0; i < students.length; i++) {
    if (students[i] > 0) {
      answer++;
    }
  }
  for (let i = 0; i < reverseStudents.length; i++) {
    if (reverseStudents[i] > 0) {
      answer2++;
    }
  }
  return Math.max(answer, answer2);
}
```

2. 앞에서부터 풀되, 체육복이 없는 경우, 앞뒤 학생모두 확인
   현재 체육복이 없고, 앞의 학생 혹은 뒤의 학생이 체육복을 가진 경우, 배열에서 체크해주는 방식으로 풀이하였다.

```js
function solution(n, lost, reserve) {
  var answer = 0;
  const students = Array(n).fill(1);
  for (const l of lost) {
    students[l - 1] = 0;
  }
  for (const r of reserve) {
    students[r - 1] += 1;
  }
  for (let i = 0; i < students.length; i++) {
    if (students[i] === 0 && i > 0 && students[i - 1] > 1) {
      students[i] = 1;
      students[i - 1] -= 1;
    } else if (
      students[i] === 0 &&
      i < students.length - 1 &&
      students[i + 1] > 1
    ) {
      students[i] = 1;
      students[i + 1] -= 1;
    }
  }

  for (let i = 0; i < students.length; i++) {
    if (students[i] > 0) {
      answer++;
    }
  }
  return answer;
}
```
