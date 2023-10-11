function solution(numbers) {
  const buckets = []; // 9999까지 이므로, 10000개짜리 사이즈의 버킷 생성

  for (const n of numbers) {
    const s = String(n),
      l = s.length;
    let j = "";
    for (let i = 0; i < 4; i++) {
      j += s[l > i ? i : i % l];
    }
    console.log(j);
    // 위 과정을 거치면 3은 3333, 34은 3434, 30은 3030이 됨
    // 왜 3을 3333으로 만들고, 30를 3030으로 만드는지가 포인트.. 이렇게 하면 3이 30보다 앞으로 오게 됨

    j = 9999 - j; // 뒤에서부터 정렬하기 위해서 9999-j를 해줌

    buckets[j] = buckets[j] ? buckets[j] + s : s; // 9999-j번째에 값을 넣어줌. 이미 값이 있는 경우 (9999와 9와 같은 경우, 같은 자리에 같은 이미 값이 있을 수 있음), 해당 값에 s를 합쳐줌, 어차피 나중에 answer에서 합쳐줄꺼니까 상관없음 -> '9999', '9' => '99999'
  }
}
solution([3, 30, 34, 5, 9, 9999]);
