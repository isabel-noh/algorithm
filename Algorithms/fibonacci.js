function fibonacci(idx) {
  if (idx <= 2) {
    return 1;
  }
  return fibonacci(idx - 1) + fibonacci(idx - 2);
}
fibonacci(5);
for (let i = 0; i < 10; i++) {
  console.log(fibonacci(i));
}
