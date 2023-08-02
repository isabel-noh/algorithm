const arr = new Array(5).fill();

arr.forEach((v, i, array) => (array[i] = () => i));
console.log(arr);
arr.forEach((f) => console.log(f()));
