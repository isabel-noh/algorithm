# Reordering the Cows

[Reordering the Cows](https://www.acmicpc.net/problem/10024)

### 문제

Farmer John's N cows (1 <= N <= 100), conveniently numbered 1..N, are standing in a row. Their ordering is described by an array A, where A(i) is the number of the cow in position i. Farmer John wants to rearrange them into a different ordering for a group photo, described by an array B, where B(i) is the number of the cow that should end up in position i.

For example, suppose the cows start out ordered as follows:

A = 5 1 4 2 3

and suppose Farmer John would like them instead to be ordered like this:

B = 2 5 3 1 4

To re-arrange themselves from the "A" ordering to the "B" ordering, the cows perform a number of "cyclic" shifts. Each of these cyclic shifts begins with a cow moving to her proper location in the "B" ordering, displacing another cow, who then moves to her proper location, displacing another cow, and so on, until eventually a cow ends up in the position initially occupied by the first cow on the cycle. For example, in the ordering above, if we start a cycle with cow 5, then cow 5 would move to position 2, displacing cow 1, who moves to position 4, displacing cow 2, who moves to position 1, ending the cycle. The cows keep performing cyclic shifts until every cow eventually ends up in her proper location in the "B" ordering. Observe that each cow participates in exactly one cyclic shift, unless she occupies the same position in the "A" and "B" orderings.

Please compute the number of different cyclic shifts, as well as the length of the longest cyclic shift, as the cows rearrange themselves.

### 입력

Line 1: The integer N.
Lines 2..1+N: Line i+1 contains the integer A(i).
Lines 2+N..1+2N: Line 1+N+i contains the integer B(i).

### 출력

Line 1: Two space-separated integers, the first giving the number of cyclic shifts and the second giving the number cows involved in the longest such shift. If there are no cyclic shifts, output -1 for the second number.

### 문제 분석

A처럼 정렬되어있는 소들을 B처럼 재정렬하기

위치 변경 cycle을 수행해야함.  
이 순회 변경은 한 소가 B의 순서에 맞게 알맞은 위치로 옮기면서 시작한다.
이 때 다른 소를 그 자리에서 빼고 자기가 들어간다. 그 빠진 소는 다른 소를 자리에서 빼고 자기가 들어가고 이런 식.
마지막 소가 첫번째 소의 자리로 갈 때 1번의 싸이클이 끝난다.

A에서 B의 정렬로 재정렬되기 위해서는 몇번의 싸이클을 돌아야하는지 계산하세요. 그리고 한 cycle에 최대 몇개의 소가 연관되어있는지도 계산해주세요.

### 앍고리즘 설꼐

이 문제에서는 변수를 여러개 사용하였기 때문에 처음에 좀 헷갈렸었다. 0번째부터 맨끝까지 확인할 것인데, 0번째에 계속 와서 확인을 해야하는지, 한번 방문하면 두번은 안봐도 되는지가 헷갈렸다.  
하지만 다시 생각해보니 한 사이클을 타면 그 사이클 내에 있는 소들이 모두 정해진 위치로 가는 것이기 때문에, 0번째를 계속 확인할 필요 없이 앞에서부터 뒤로 차례로 확인하면 되는 것이었다.

### 코드

```js
const fs = require("fs");
const input = fs
  .readFileSync("./sample.txt")
  .toString()
  .split("\n")
  .map(Number);
const N = input.shift();
const A = input.slice(0, N);
const B = input.slice(N);

let cycleCnt = 0;
let involvedCows = 0;

for (let index = 0; index < A.length; index++) {
  let startPoint = 0;
  if (A[index] !== B[index]) {
    // cycle
    startPoint = index;
    let cows = 0;
    let temp = 0;
    let cur = index;
    let value = A[index];

    while (true) {
      const idx = B.indexOf(value);
      temp = A[idx];
      A[idx] = value;
      value = temp;
      cur = idx;
      cows++;
      if (cur === startPoint) {
        involvedCows = Math.max(involvedCows, cows);
        break;
      }
    }
    cycleCnt++;
  }
}
if (cycleCnt === 0) {
  involvedCows = -1;
}
console.log(cycleCnt, involvedCows);
```

### 시간 복잡도

최대 O(N^3)

### 다른 코드

아래의 방법처럼 B를 해시맵으로 index를 찾도록 한다면 시간 복잡도를 O(N^2)로 줄일 수 있다.

```js
...
// B의 값과 인덱스를 매핑하는 해시맵 생성
const BIndexMap = new Map();
for (let i = 0; i < B.length; i++) {
  BIndexMap.set(B[i], i);
}

for (let index = 0; index < A.length; index++) {
  ...
  if (A[index] !== B[index]) {
    ...
    while (true) {
      const idx = BIndexMap.get(value); // 해시맵에서 인덱스 가져오기
      ...
    }
    cycleCnt++;
  }
}
...
console.log(cycleCnt, involvedCows);
```
