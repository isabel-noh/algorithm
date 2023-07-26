class Heap {
  constructor() {
    this.heap = [];
  }

  getParentIndex(i) {
    return Math.floor(i / 2);
  }

  getLeftChildIndex(i) {
    return i * 2;
  }

  getRightChildIndex(i) {
    return i * 2 + 1;
  }

  swap(idx1, idx2) {
    const temp = this.heap[idx1];
    this.heap[idx1] = this.heap[idx2];
    this.heap[idx2] = temp;
  }

  push(val) {
    this.heap[this.heap.length] = val;
    this.heapifyUp();
  }

  heapifyUp() {
    let curIdx = this.heap.length - 1;
    while (this.heap[curIdx] > this.heap[this.getParentIndex(curIdx)]) {
      this.swap(curIdx, this.getParentIndex(curIdx));
      curIdx = this.getParentIndex(curIdx);
    }
  }

  poll() {
    let maxVal = this.heap[0];
    if (maxVal === 12 || maxVal === 10 || maxVal === 8) {
      console.log("g", this.heap);
    }
    this.heap[0] = this.heap[this.heap.length - 1];
    this.heap.length--;
    this.heapifyDown();
    return maxVal;
  }

  heapifyDown() {
    let curIdx = 0;
    while (this.heap[this.getLeftChildIndex(curIdx)] !== undefined) {
      let biggerChild = this.getLeftChildIndex(curIdx);
      if (
        this.heap[this.getLeftChildIndex(curIdx)] <
        this.heap[this.getRightChildIndex(curIdx)]
      ) {
        biggerChild = this.getRightChildIndex(curIdx);
      }
      if (this.heap[curIdx] < this.heap[biggerChild]) {
        this.swap(curIdx, biggerChild);
        curIdx = biggerChild;
      } else {
        return;
      }
    }
  }
}
