# Programmers Hash Best Album

[Programmers Hash Best Album](https://school.programmers.co.kr/learn/courses/30/lessons/42579)

## 문제 설명

스트리밍 사이트에서 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시하려 합니다. 노래는 고유 번호로 구분하며, 노래를 수록하는 기준은 다음과 같습니다.

- 속한 노래가 많이 재생된 장르를 먼저 수록합니다.
- 장르 내에서 많이 재생된 노래를 먼저 수록합니다.
- 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.  
  노래의 장르를 나타내는 문자열 배열 genres와 노래별 재생 횟수를 나타내는 정수 배열 plays가 주어질 때, 베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 return 하도록 solution 함수를 완성하세요.

### 제한사항

- genres[i]는 고유번호가 i인 노래의 장르입니다.
- plays[i]는 고유번호가 i인 노래가 재생된 횟수입니다.
- genres와 plays의 길이는 같으며, 이는 1 이상 10,000 이하입니다.
- 장르 종류는 100개 미만입니다.
- 장르에 속한 곡이 하나라면, 하나의 곡만 선택합니다.
- 모든 장르는 재생된 횟수가 다릅니다.

### 입출력 예

| genres                                          | plays                      | return       |
| ----------------------------------------------- | -------------------------- | ------------ |
| ["classic", "pop", "classic", "classic", "pop"] | [500, 600, 150, 800, 2500] | [4, 1, 3, 0] |

### 입출력 예 설명

classic 장르는 1,450회 재생되었으며, classic 노래는 다음과 같습니다.

고유 번호 3: 800회 재생  
고유 번호 0: 500회 재생  
고유 번호 2: 150회 재생  
pop 장르는 3,100회 재생되었으며, pop 노래는 다음과 같습니다.

고유 번호 4: 2,500회 재생  
고유 번호 1: 600회 재생  
따라서 pop 장르의 [4, 1]번 노래를 먼저, classic 장르의 [3, 0]번 노래를 그다음에 수록합니다.

장르 별로 가장 많이 재생된 노래를 최대 두 개까지 모아 베스트 앨범을 출시하므로 2번 노래는 수록되지 않습니다.

#### 문제풀이

노래들을 장르별로 묶어서 가장 많이 재생된 장르순으로, 그 장르 중에서 제일 많이 재생된 순으로 정렬할 필요가 있었다. 하지만 먼저 장르별로 분리하여야했다.

먼저, 장르별로 plays count와 해당 노래의 순번을 저장할 Map인 map을 생성하였다.
또한, 장르별로 재생된 수의 sum 값을 저장할 Map인 sumMap을 생성하였다.

```js
const map = new Map();
const sumMap = new Map();
for (let i = 0; i < genres.length; i++) {
  if (map.has(genres[i])) {
    map.set(genres[i], [...map.get(genres[i]), [plays[i], i]]);
    sumMap.set(genres[i], sumMap.get(genres[i]) + plays[i]);
  } else {
    map.set(genres[i], [[plays[i], i]]);
    sumMap.set(genres[i], plays[i]);
  }
}

// Map(2) {
//   'classic' => [ [ 500, 0 ], [ 150, 2 ], [ 800, 3 ] ],
//   'pop' => [ [ 600, 1 ], [ 2500, 4 ] ]
// }
// Map(2) { 'classic' => 1450, 'pop' => 3100 }
```

위의 sumMap의 entries()를 뽑아, 재생된 순으로 내림차순 정렬하고 이를 stack으로 앞에서부터 뽑아 그 장르에 해당하는 plays list를 map에서 가져온다. 이를 다시 plays의 순서에 따라 내림차순 정렬하여 index가 0, 1인 값들의 순번을 answer에 저장하여 주었다.

```js
function solution(genres, plays) {
  const answer = [];
  const map = new Map();
  const sumMap = new Map();
  for (let i = 0; i < genres.length; i++) {
    if (map.has(genres[i])) {
      map.set(genres[i], [...map.get(genres[i]), [plays[i], i]]);
      sumMap.set(genres[i], sumMap.get(genres[i]) + plays[i]);
    } else {
      map.set(genres[i], [[plays[i], i]]);
      sumMap.set(genres[i], plays[i]);
    }
  }
  const sumArr = [...sumMap.entries()].sort((a, b) => b[1] - a[1]);
  while (sumArr.length) {
    const [genre, sumGenre] = sumArr.shift();
    const genreFromMap = map.get(genre).sort((a, b) => b[0] - a[0]);
    for (let i = 0; i < genreFromMap.length; i++) {
      if (i > 1) {
        break;
      }
      answer.push(genreFromMap[i][1]);
    }
  }
  return answer;
}

solution(
  ["classic", "pop", "classic", "classic", "pop"],
  [500, 600, 150, 800, 2500]
);
```
