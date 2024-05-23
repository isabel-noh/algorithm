# Programmers - Heap - 이중우선순위큐\*\*

[Programmers - Heap - 이중우선순위큐](https://school.programmers.co.kr/learn/courses/30/lessons/42628)

## 문제 설명

이중 우선순위 큐는 다음 연산을 할 수 있는 자료구조를 말합니다.

| 명령어 | 수신 탑(높이)                  |
| ------ | ------------------------------ |
| I 숫자 | 큐에 주어진 숫자를 삽입합니다. |
| D 1    | 큐에서 최댓값을 삭제합니다.    |
| D -1   | 큐에서 최솟값을 삭제합니다.    |

이중 우선순위 큐가 할 연산 operations가 매개변수로 주어질 때, 모든 연산을 처리한 후 큐가 비어있으면 [0,0] 비어있지 않으면 [최댓값, 최솟값]을 return 하도록 solution 함수를 구현해주세요.

### 제한사항

operations는 길이가 1 이상 1,000,000 이하인 문자열 배열입니다. // 이중 포문 안됨
operations의 원소는 큐가 수행할 연산을 나타냅니다.
원소는 “명령어 데이터” 형식으로 주어집니다.- 최댓값/최솟값을 삭제하는 연산에서 최댓값/최솟값이 둘 이상인 경우, 하나만 삭제합니다.
빈 큐에 데이터를 삭제하라는 연산이 주어질 경우, 해당 연산은 무시합니다.

### 입출력 예

| operations                                                                    | return     |
| ----------------------------------------------------------------------------- | ---------- |
| ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]                    | [0,0]      |
| ["I -45", "I 653"**, "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"] | [333, -45] |

#### 문제풀이1 - minHeap과 heap의 depth를 활용하여 풀이

처음에는 minHeap에서 max값을 찾는 방법에서 두가지 방법을 생각했다.

1. minHeap에서 자식들 중에서 큰 쪽으로 가다보면 제일 큰 값이 나오지 않을까? -> 그렇게 안 됨
2. minHeap에서 depth를 구하고, 마지막 depth에 있는 값들 중에서 max를 찾으면 되지 않을까? -> 가능함

아래 코드는 2번 방법을 활용하여 풀이한 풀이법이다.  
맨 마지막 값의 idx는 `this.heap.length - 1`이다. 마지막 노드의 부모 노드는 자식(마지막 노드)이 있기 때문에, 마지막 depth에 포함되지 않는다. `맨 마지막 노드의 부모 노드 + 1 부터 맨 마지막 노드까지의 값`들이 마지막 depth의 값들이다.
그들 중에 최대값이 있으므로, Math.max()로 마지막 depth의 최대값 maxVal을 찾고, 그 값과 heap의 마지막 노드 값과 교체한 뒤, 빼내어 삭제한다.

이번 문제로, minHeap에서 maxVal, 혹은 maxHeap에서 minVal을 pop하는 방법을 배울 수 있었다.

```js
maxPop() {
    // 가장 마지막 노드의 부모 노드 + 1 ~ 가장 마지막 노드
    const startPoint = this.getParent(this.heap.length - 1) + 1;
    const maxCandidates = this.heap.slice(startPoint);
    const maxVal = Math.max(...maxCandidates);

    // maxValue 빼고, 다시 정렬하기
    const maxValIdx = this.heap.indexOf(maxVal);
    this.swap(maxValIdx, this.heap.length - 1);
    this.heap.pop();
    return maxVal;
  }
```

```js
class MinHeap {
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
      return this.heap;
    }
    while (this.heap[parent] && this.heap[cur] < this.heap[parent]) {
      this.swap(cur, parent);
      cur = parent;
      parent = this.getParent(cur);
    }
    return this.heap;
  }
  minPop() {
    if (this.heap.length === 0) {
      return null;
    }

    if (this.heap.length === 1) {
      return this.heap.pop();
    }

    const minValue = this.heap[0];
    this.swap(0, this.heap.length - 1);
    this.heap.pop();

    let current = 0;
    let leftChild = this.getLeftChild(current);
    let rightChild = this.getRightChild(current);

    while (
      (this.heap[leftChild] && this.heap[current] > this.heap[leftChild]) ||
      (this.heap[rightChild] && this.heap[current] > this.heap[rightChild])
    ) {
      // left 자식이 더 클때
      if (
        this.heap[rightChild] &&
        this.heap[leftChild] > this.heap[rightChild]
      ) {
        this.swap(rightChild, current);
        current = rightChild;
        rightChild = this.getRightChild(current);
        leftChild = this.getLeftChild(current);
      } else {
        this.swap(leftChild, current);
        current = leftChild;
        rightChild = this.getRightChild(current);
        leftChild = this.getLeftChild(current);
      }
    }

    return minValue;
  }

  maxPop() {
    // 가장 마지막 노드의 부모 노드 + 1 ~ 가장 마지막 노드
    const startPoint = this.getParent(this.heap.length - 1) + 1;
    const maxCandidates = this.heap.slice(startPoint);
    const maxVal = Math.max(...maxCandidates);

    // maxValue 빼고, 다시 정렬하기
    const maxValIdx = this.heap.indexOf(maxVal);
    this.swap(maxValIdx, this.heap.length - 1);
    this.heap.pop();
    return maxVal;
  }
}

function solution(operations) {
  var answer = [];
  const heap = new MinHeap();

  for (const o of operations) {
    if (o[0] === "I") {
      const num = o.slice(2);
      heap.push(Number(num));
    } else if (o === "D 1") {
      // max를 어떻게 구할건지 고민해야 함. -> maxHeap 생성? 그건 아닌거 같고, 깊이로 구해서 마지막 줄을 뽑아서 max를 구하거나,,
      heap.maxPop();
    } else {
      heap.minPop();
    }
  }

  if (heap.heap.length === 0) {
    answer = [0, 0];
  } else {
    const max = heap.maxPop();
    const min = heap.minPop();
    answer = [max, min];
  }
  console.log(answer);
  return answer;
}
```

#### 문제풀이2 - heap을 사용하지 않는 풀이

아래 풀이는 heap을 만들지 않고 그냥 배열에 값을 더하고 빼는 방식으로 풀이하는 문제이다.
그냥 부르트포스 쯤 되려나

```js
function solution(operations) {
  var answer = [];
  const queue = [];
  for (const o of operations) {
    if (o[0] === "I") {
      const num = o.slice(2);
      queue.push(Number(num));
    } else if (o === "D 1") {
      // console.log(heap.maxPop());
      const maxVal = Math.max(...queue);
      const idx = queue.indexOf(maxVal);
      queue.splice(idx, 1);
    } else {
      // console.log(queue.minPop());
      const minVal = Math.min(...queue);
      const idx = queue.indexOf(minVal);
      queue.splice(idx, 1);
    }
  }
  if (queue.length === 0) {
    answer = [0, 0];
  } else {
    const maxVal = Math.max(...queue);
    const minVal = Math.min(...queue);
    answer = [maxVal, minVal];
  }
  return answer;
}
```
