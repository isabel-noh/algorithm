# The Perfect Cow

[The Perfect Cow](https://www.acmicpc.net/problem/6108)

### 문제

For the 39th year in a row, Farmer John was named "Dairy Farmer of the Year". The Dairy Association wants him to exhibit his most perfect cow at the upcoming Cow Convention in Herbster, Wisconsin on the frigid shores of Lake Superior.

FJ keeps up with scientific literature and knows that beauty is actually a trend toward the average rather than the existence of some superior trait. Thus, he wants to find his most average cow and share her beauty with the other Dairy Farmers during the weekend of revelry and partying at the convention.

Happily, each of the N\*N cows (2 <= N <= 99; N odd) has her beauty rating (1 <= R_ij <= 1,000) inscribed on a tag in her ear, just like in this picture.

Cows aren't so good at math, so FJ lines them up into an N x N square. He asks them to find the median cow in each row (the median cow is the one whose beauty number is bigger than or equal to half the cows in her group and also smaller than or equal to half the cows in her group -- the middle number of the group). From those N medians, FJ then finds the median of those numbers and brings that cow to the convention.

Given a set of N x N cows, find the beauty index of the most perfect (average) cow.

### 입력

Line 1: A single integer: N
Lines 2..N+1: Line i+1 contains N space-separated integers that are the N beauty indices for row i of the cow square

### 출력

Line 1: A single integer that is the index of the most perfect cow as described in the task.

### 문제 해석

소들은 각자의 미적 점수가 있고, 이들의 평균을 구하고 싶다.
각 행에서의 중간 값을 찾고, 그 둘 중에서 다시 중간값을 찾는다 .

### 코드

```js
const fs = require("fs");
const [n, ...input] = fs.readFileSync("./sample.txt").toString().split("\n");
const midIndex = Math.floor(+n / 2);
let arr = [];
for (let i = 0; i < +n; i++) {
  const a = input[i]
    .split(" ")
    .map(Number)
    .sort((a, b) => a - b);
  const mid = a[midIndex];
  arr.push(mid);
}
arr = arr.sort((a, b) => a - b);
console.log(arr[midIndex]);
```
