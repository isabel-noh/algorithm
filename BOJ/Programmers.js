function solution(s) {
  var answer = []
  const arr = s.slice(2, s.length - 2)
  let a = []
  let temp = []
  let stack = []
  for (let i = 0; i < arr.length; i++) {
    // string을 전체를 돌아본다.
    if (arr[i] === '{') {
      // 여는 괄호일 경우 스택에 넣어줌
      stack.push(arr[i])
    } else if (arr[i] === '}') {
      // 닫는 괄호일 경우, 닫는 괄호는 버리고, 콤마가 나올 때까지는 한 숫자이므로 a에 push, 그다음 여는 괄호 나올 때까지 stack에서 pop하여 number()해주고 a에 push. 여는 괄호가 나오면 버리고, 다음 string 확인
      let number = ''
      while (stack[stack.length - 1] !== '{') {
        // 숫자일 경우 처리를 해줘야함!
        t = stack.pop()
        console.log(stack, number)

        if (t === ',') {
          console.log(number)
          temp.push(Number(number))
          number = ''
        }
        number = t + number
      }
      t = stack.pop()
      a.push(temp)
      temp = []
    } else if (arr[i] === ',') {
      // 콤마는 stack에 넣어줌
      stack.push(arr[i])
    } else if (arr[i] === ' ') {
      // 띄어쓰기는 버림
      continue
    } else {
      // 숫자일 경우 stack에 push
      stack.push(arr[i])
    }
  }
  for (let i = 0; i < a.length; i++) {
    for (let j = 0; j < a[i].length; j++) {
      if (!answer.includes(a[i][j])) {
        answer.push(a[i][j])
      }
    }
  }
  console.log(a)
  console.log(answer)
  return answer
}

const s = '"{{1,2,3},{2,1},{1,2,4,3},{2}}"'
solution(s)
