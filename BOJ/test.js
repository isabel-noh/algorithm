const ba = [
  [1, 2, 3],
  [1, 2, 3],
  [1, 2, 3],
];

const b = ba.map((el) => [...el]);

b[0][0] = true;
console.log(b, ba);
