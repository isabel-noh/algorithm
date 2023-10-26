function solution(word) {
  var answer = 0;
  // A E I O U
  // 길이 5 이하의 모든 단어
  // A, AA, AAA, AAAA, AAAAA, AAAAE, ... , UUUUU
  const arr = ["A", "E", "I", "O", "U"];
  for (let i = 0; i < word.length; i++) {
    if (i === 0) {
      for (let l = 0; l < 5; l++) {
        if (word[i] === arr[l]) {
          answer += 1 + 781 * l;
        }
      }
    } else if (i === 1) {
      for (let l = 0; l < 5; l++) {
        if (word[i] === arr[l]) {
          answer += 1 + 156 * l;
        }
      }
    } else if (i === 2) {
      for (let l = 0; l < 5; l++) {
        if (word[i] === arr[l]) {
          answer += 1 + 31 * l;
        }
      }
    } else if (i === 3) {
      for (let l = 0; l < 5; l++) {
        if (word[i] === arr[l]) {
          answer += 1 + 6 * l;
        }
      }
    } else if (i === 4) {
      for (let l = 0; l < 5; l++) {
        if (word[i] === arr[l]) {
          answer += 1 + 1 * l;
        }
      }
    }
  }
  console.log(answer);
  return answer;
}

solution("AAAAE");
solution("AAAE");
solution("I");
solution("EIO");
