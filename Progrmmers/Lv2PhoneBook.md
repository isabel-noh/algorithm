# Programmers 해시 - 전화번호 목록

[Programmers 해시 - 전화번호 목록](https://school.programmers.co.kr/learn/courses/30/lessons/42577)

## 문제

전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 합니다.
전화번호가 다음과 같을 경우, 구조대 전화번호는 영석이의 전화번호의 접두사입니다.

구조대 : 119
박준영 : 97 674 223
지영석 : 11 9552 4421
전화번호부에 적힌 전화번호를 담은 배열 phone_book 이 solution 함수의 매개변수로 주어질 때, 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return 하도록 solution 함수를 작성해주세요.

### 제한 사항

- phone_book의 길이는 1 이상 1,000,000 이하입니다. -> 이중for문 X / O(n^2) X
- 각 전화번호의 길이는 1 이상 20 이하입니다.
- 같은 전화번호가 중복해서 들어있지 않습니다.

### 입출력 예제

| phone_book                        | return |
| --------------------------------- | ------ |
| ["119", "97674223", "1195524421"] | false  |
| ["123","456","789"]               | true   |
| ["12","123","1235","567","88"]    | false  |

#### 문제풀이

1. 시간 초과  
   제한 사항에서 100만 건의 전화번호가 들어올 수 있다고 하였으므로, O(n^2)의 풀이의 경우 시간초과가 날 가능성이 높다! -> 역시나 시초남 ...  
    이중for문은 제외하자.
   또한 phone_book을 숫자의 크기 순으로 정렬을 했는데, 사전순으로 정렬을 해야할 것이다.

```js
function solution(phone_book) {
  // 겹치는 게 있으면 false , 아니면 true return
  var answer = true;
  const arr = [...phone_book].sort((a, b) => a - b); // 해당 방법은 string의 number 값을 기준으로 정렬됨
  for (let i = 0; i < arr.length; i++) {
    for (let j = i + 1; j < arr.length; j++) {
      if (arr[i] != arr[j] && arr[j].startsWith(arr[i])) {
        answer = false;
        return answer;
      }
    }
  }
  return answer;
}
```

2. pass!  
   먼저, 숫자를 크기순으로 정렬하던 것을 사전순으로 정렬하였다. sort()함수를 그냥 쓰면 유니코드 순으로 정렬한다.  
   그러면 배열에 숫자의 크기나 길이에 상관없이 ['119', '1195524421', '97674223']와 같이 정렬된다. 즉, 어떤 두 값이 서로 접두어 관계에 있다면 앞뒤로 붙어있게 되는 것이다. a가 b의 접두어라면, 배열에서 a, b, ... 이런식으로 같이 정렬되게 된다.

   이제 정렬을 다 했으니, 앞에서부터 배열을 확인한다.  
   배열에서의 arr[i]값이 arr[i-1]로 시작한다면 (startsWith), false를 리턴하고 끝낸다.  
   그렇지 않다면, 접두어 관계가 아니므로 previous를 현재 값으로 변경해주고 다음 값을 확인한다.

```js
function solution(phone_book) {
  // 겹치는 게 있으면 false , 아니면 true return
  var answer = true;
  const arr = [...phone_book].sort(); // 사전순 정렬
  let previous = arr[0];
  for (let i = 1; i < arr.length; i++) {
    if (arr[i].startsWith(previous)) {
      return false;
    }
    previous = arr[i];
  }
  return answer;
}
```

3. 해시 활용  
   해시 문제니까 다른 사람은 해시로 어떻게 풀었나 확인해보았다.  
    table이라는 map을 선언해주고, 해당 map에 전화번호부의 전화번호들로 이루어지고, true값이 할당해준다.
   `{'119' : true, '234342' : true, '11923432' : true, }` 처럼
   자기 자신이 포함되지 않도록 string[string.length-1]까지만 잘라서 비교한다.
   각 전화번호들의 번호들을 일일히 확인한다. prefix는 전화번호를 0부터 i까지 자른 것을 의미한다.
   119의 경우 1, 11 이런식으로 진행된다.
   prefix가 table에 있다면 접두어인 것이다.

```js
function solution(phoneBook) {
  const table = {};

  for (const number of phoneBook) {
    table[number] = true;
  }

  for (const number of phoneBook) {
    for (let i = 1; i < number.length; i += 1) {
      const prefix = number.slice(0, i);
      if (table[prefix]) return false;
    }
  }

  return true;
}
```
