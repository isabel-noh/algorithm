class ListNode {
  constructor(data) {
    this.node = data;
    this.nextNode = null;
  }
}
class LinkedList {
  constructor(head = null) {
    this.head = head;
  }
  size() {
    let count = 0;
    let cur = this.head;
    if (cur) {
      count++;
    }
    while (cur.nextNode !== null) {
      cur = cur.nextNode;
      count++;
    }
    return count;
  }
  clear() {
    this.head = null;
  }
  getLast() {
    let cur = this.head;
    while (cur.nextNode !== null) {
      cur = cur.nextNode;
    }
    return cur.node;
  }
  getFirst() {
    let cur = this.head;
    return this.head.node;
  }
  addFirstNode(data) {
    const node = new ListNode(data);
    node.nextNode = this.head;
    this.head = node;
  }
  addLastNode(data) {
    const node = new ListNode(data);
    let currentNode = this.head;
    while (currentNode.nextNode) {
      currentNode = currentNode.nextNode;
    }
    currentNode.nextNode = node;
  }
  addAtIdx(index, data) {
    if (index < this.size() && index > 0) {
      const node = new ListNode(data);
      let idx = 0;
      let curNode = this.head;
      if (index === 0) {
        this.addFirstNode(data);
      } else {
        console.log("add");
        while (idx !== index - 1) {
          curNode = curNode.nextNode;
          idx++;
        }
        //index랑 idx랑 같아지면, 이전 노드의 nextNode에 나를 넣고, 나의 nextNode를 다음 node로
        if (curNode.nextNode) {
          node.nextNode = curNode.nextNode;
        }
        curNode.nextNode = node;
      }
    }
  }
}

const node1 = new ListNode(1);
const node2 = new ListNode(2);
node1.nextNode = node2; // 노드 간 연결
const linkedList = new LinkedList(node1); // 맨 앞의 노드인 node1이 head로 들어감
console.log(linkedList.size());
console.log(linkedList.getLast());
console.log(linkedList.getFirst());
linkedList.addFirstNode(3);
linkedList.addLastNode(4);
linkedList.addAtIdx(2, 6);
console.dir(linkedList, { depth: null });
