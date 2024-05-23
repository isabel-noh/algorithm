# Programmers Heap - Hotter and Hotter

[Programmers Heap - Hotter and Hotter](https://school.programmers.co.kr/learn/courses/30/lessons/42626)

## 문제 설명

매운 것을 좋아하는 Leo는 모든 음식의 스코빌 지수를 K 이상으로 만들고 싶습니다. 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 Leo는 스코빌 지수가 가장 낮은 두 개의 음식을 아래와 같이 특별한 방법으로 섞어 새로운 음식을 만듭니다.

`섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)`
Leo는 모든 음식의 스코빌 지수가 K 이상이 될 때까지 반복하여 섞습니다.
Leo가 가진 음식의 스코빌 지수를 담은 배열 scoville과 원하는 스코빌 지수 K가 주어질 때, 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 섞어야 하는 최소 횟수를 return 하도록 solution 함수를 작성해주세요.

### 제한 사항

scoville의 길이는 2 이상 1,000,000 이하입니다.
K는 0 이상 1,000,000,000 이하입니다.
scoville의 원소는 각각 0 이상 1,000,000 이하입니다.
모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우에는 -1을 return 합니다.

### 입출력 예

| scoville             | K   | return |
| -------------------- | --- | ------ |
| [1, 2, 3, 9, 10, 12] | 7   | 2      |

### 입출력 예 설명

스코빌 지수가 1인 음식과 2인 음식을 섞으면 음식의 스코빌 지수가 아래와 같이 됩니다.
새로운 음식의 스코빌 지수 = 1 + (2 \* 2) = 5
가진 음식의 스코빌 지수 = [5, 3, 9, 10, 12]

스코빌 지수가 3인 음식과 5인 음식을 섞으면 음식의 스코빌 지수가 아래와 같이 됩니다.
새로운 음식의 스코빌 지수 = 3 + (5 \* 2) = 13
가진 음식의 스코빌 지수 = [13, 9, 10, 12]

모든 음식의 스코빌 지수가 7 이상이 되었고 이때 섞은 횟수는 2회입니다.

#### 문제풀이

MinHeap을 직접 구현하여야 풀이할 수 있는 문제이다.
최소힙은 오른쪽 왼쪽 상관없이 부모노드가 자식노드보다 크기만 하면 된다. (처음에 오른쪽이 왼쪽보다 커야하는 줄 알고 헷갈렸음 )

먼저, 전체 입력값을 Heap에 push해준다. heap에 push할 때에는 값을 배열의 맨 마지막 부분에 넣어주고, 마지막 index의 값을 기준으로 부모 노드와 비교하면서 부모노드보다 더 큰 상황이 올 때까지 부모와 자식을 swap하면서 올라간다. 부모 노드가 현재 비교대상인 자식노드보다 더 크다면 값을 swap하고 비교대상을 그 부모노드의 index로 변경한다. 그렇지 않다면 멈춘다.

Heap의 첫 번째로 작은 값과 두번째로 작은 값 \* 2를 구하기 위해, heap에서 pop을 두 번하여, 제일 작은 값과 두번째 작은 값을 구한다. (매 pop마다 minHeap은 정렬된다.) 그 다음 그 값들의 합을 Push하고, heap을 재정렬한다. 이런식으로 반복하다가 heap의 길이가 1, 즉 제일 작은 값만 있고, 두 번째 값이 없는 경우가 되거나, heap의 [0]값이 K보다 커지면 위 동작을 멈춘다. 위 두 경우에서, heap[0]이 K보다 크다면 answer을, 그렇지 않다면 조건을 충족시키지 못한 경우이므로 -1을 리턴한다. (`missing point`)

위 과정에서 heap에서 pop하는 동작이 있는데, 여기가 아주 골머리~~~  
**일단 힙에서는 최소힙이든 최대힙이든 루트 노드가 항상 먼저 배출되어야 한다. 배출되고 나서 생기는 빈자리는 가장 마지막 노드, 즉 배열에서 제일 뒤에 있는 값을 가져온다. 그리고 다시 루트노드서 부터 재정렬을 실행해준다.**

1. 만약 heap에 어떤 값도 없다면 null을 리턴한다.
2. 만약 Heap의 길이가 1인 경우, 즉, 루트 노드 밖에 없는 경우라면, heap[0]을 pop하여 리턴한다.
3. 1, 2번의 경우 외로 자식 노드들이 있는 경우, 루트 노드를 메서드가 끝날 때 return하기 위해 따로 저장한다.
4. 루트 노드와 맨 마지막 노드를 교환하고, 맨 마지막 노드는 필요가 없어졌기 때문에 heap에서 pop() (배열에서의 pop을 의미)을 한다.
5. 새롭게 바뀐 루트 노드를 자식 노드들과 비교하여 재정렬한다.
6. 3번에서 저장했던 루트 노드를 리턴한다.

_재정렬_

1. 루트 노드를 자식 노드들과 비교하여 정렬할 것이기 때문에 3가지 정보가 필요하다.

- 현재 노드의 위치 : 0
- 왼쪽 자식 노드의 위치
- 오른쪽 자식 노드의 위치

2. 아래 진행될 정렬을 왼쪽 자식 노드와 오른쪽 자식 노드보다 작을 때까지 계속 반복할 것이다.
3. 주의할 점1. `왼쪽 자식 노드만 있고, 오른쪽 자식 노드는 없는 경우가 있음!`
4. 주의할 점2. `왼쪽 자식 노드도 있고, 오른쪽 자식 노드도 있는 경우, 더 작은 자식 노드와 위치를 바꾸어야 한다.`
5. 왼쪽 혹은 오른쪽 자식 노드와 위치를 바꾼 경우, current idx를 바꾼 자식 노드의 idx로 변경하고, 해당 위치로부터 다시 정렬한다.

```js
class Heap {
  constructor() {
    this.heap = [];
  }
  // 부모 idx = Math.floor(자식 idx / 2)
  getParentIdx(idx) {
    return Math.floor((idx - 1) / 2);
  }
  // 왼쪽 자식 idx = 부모 idx * 2
  getLeftChildIdx(idx) {
    return idx * 2 + 1;
  }
  // 오른쪽 자식 idx = 부모 idx * 2 + 1
  getRightChildIdx(idx) {
    return idx * 2 + 2;
  }
  swap(idx1, idx2) {
    [this.heap[idx1], this.heap[idx2]] = [this.heap[idx2], this.heap[idx1]];
  }
  push(value) {
    // 일단 마지막 노드에 들어온 값을 push하여 삽입한다. 이때 재귀적이든 반복문을 돌리든 부모노드를 확인하면서 들어온 값이 부모노드보다 작은지 큰지를 구분하여 위치를 교환을 계속 실행해주며 정렬해준다.
    this.heap.push(value);
    let current = this.heap.length - 1; // push 했기 때문에 heap 배열의 맨 뒤에 붙음
    let parent = this.getParentIdx(current);

    while (this.heap[parent] > this.heap[current]) {
      this.swap(parent, current);
      current = parent;
      parent = this.getParentIdx(current);
    }
    return this.heap;
  }
  pop() {
    // 일단 힙에서는 최소힙이든 최대힙이든 루트 노드가 항상 먼저 배출되어야 한다. 배출되고 나서 생기는 빈자리는 가장 마지막 노드, 즉 배열에서 제일 뒤에 있는 값을 가져온다. 그리고 다시 루트노드서 부터 재정렬을 실행해준다.

    // heap에 아무것도 없는 경우,
    if (this.heap.length === 0) {
      return null;
    }
    // root만 있는 경우 ,
    if (this.heap.length === 1) {
      return this.heap.pop();
    }
    const min = this.heap[0]; // min에 0번째 값 저장
    this.heap[0] = this.heap.pop(); //  마지막 값이랑 0번째 값이랑 교체

    // 정렬
    let current = 0;
    let leftChild = this.getLeftChildIdx(current);
    let rightChild = this.getRightChildIdx(current);

    while (
      (this.heap[leftChild] && this.heap[leftChild] < this.heap[current]) ||
      (this.heap[rightChild] && this.heap[rightChild] < this.heap[current])
    ) {
      // 오른쪽 왼쪽 다 있고, 왼쪽이 더 큰 경우, -> 오른쪽과 변경
      if (
        this.heap[rightChild] &&
        this.heap[rightChild] < this.heap[leftChild]
      ) {
        this.swap(rightChild, current);
        current = rightChild;
      } else {
        this.swap(leftChild, current);
        current = leftChild;
      }

      leftChild = this.getLeftChildIdx(current);
      rightChild = this.getRightChildIdx(current);
    }
    return min;
  }
}

function solution(input, K) {
  var answer = 0;
  const heap = new Heap();
  for (const item of input) {
    heap.push(item);
  }
  while (heap.heap[0] < K && heap.heap.length > 1) {
    // heap의 root가 k보다 작고, heap에 1개 이상의 데이터가 있다면 계속 할 것
    const first = heap.pop(); // 제일 작은 값과
    const second = heap.pop(); // 두번째로 작은 값을 빼내고,
    heap.push(first + second * 2); // 새로 만든 값을 push
    answer++;
  }
  // 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우에는 -1을 return 합니다. - `놓친 부분``
  if (heap.heap[0] >= K) {
    return answer;
  } else {
    return -1;
  }
}
```
