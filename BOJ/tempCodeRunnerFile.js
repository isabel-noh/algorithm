(arr);

const check = new Array(N + 1).fill(0);
for (let i = 0; i < N - 1; i++) {
  if (musics[i] > musics[i + 1]) {
    check[i + 1] = i === 0 ? 1 : check[i] + 1;
  } else {
    check[i + 1] = i === 0 ? 0 : check[i];
  }
}
console.log(check);

for (let i = 0; i < Q; i++) {
  const [x, y] = arr[i];
  console.log(check[y - 1] - check[x - 1]);
}
