function solution(left, right) {
  var answer = 0;
  for (let i = left; i <= right; i++) {
    sqr = Math.floor(Math.sqrt(i));
    if (sqr * sqr === i) {
      answer -= i;
    } else {
      answer += i;
    }
  }
  return answer;
}
solution(13, 17);
