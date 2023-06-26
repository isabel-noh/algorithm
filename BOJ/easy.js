let n = 1;
const range = 10000;
const arr = Array(range + 1).fill(false);

function check(num) {
  let number = num;
  let result = num;
  for (let i = 0; i < String(num).length; i++) {
    // num을 stringfy하고 그 자리수만큼 반복
    result += number % 10; // number은 for문 돌 때마다 10으로 나눠서 한자리씩 뒤에서부터 줄어듦
    number = Math.floor(number / 10);
  }
  return result; // 매 자리수를 더한 값 + 원래 값
}

while (n <= range) {
  const res = check(n);
  arr[res] = true;
  n++;
}

for (let i = 1; i <= range; i++) {
  if (!arr[i]) {
    console.log(i);
  }
}
