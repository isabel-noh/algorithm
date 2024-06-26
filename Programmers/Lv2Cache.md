# Programmers - LRU - 캐시

### 문제 설명

캐시  
지도개발팀에서 근무하는 제이지는 지도에서 도시 이름을 검색하면 해당 도시와 관련된 맛집 게시물들을 데이터베이스에서 읽어 보여주는 서비스를 개발하고 있다.  
이 프로그램의 테스팅 업무를 담당하고 있는 어피치는 서비스를 오픈하기 전 각 로직에 대한 성능 측정을 수행하였는데, 제이지가 작성한 부분 중 데이터베이스에서 게시물을 가져오는 부분의 실행시간이 너무 오래 걸린다는 것을 알게 되었다.  
어피치는 제이지에게 해당 로직을 개선하라고 닦달하기 시작하였고, 제이지는 DB 캐시를 적용하여 성능 개선을 시도하고 있지만 캐시 크기를 얼마로 해야 효율적인지 몰라 난감한 상황이다.

어피치에게 시달리는 제이지를 도와, DB 캐시를 적용할 때 캐시 크기에 따른 실행시간 측정 프로그램을 작성하시오.

### 입력 형식

캐시 크기(cacheSize)와 도시이름 배열(cities)을 입력받는다.  
cacheSize는 정수이며, 범위는 0 ≦ cacheSize ≦ 30 이다.  
cities는 도시 이름으로 이뤄진 문자열 배열로, 최대 도시 수는 100,000개이다.  
각 도시 이름은 공백, 숫자, 특수문자 등이 없는 영문자로 구성되며, 대소문자 구분을 하지 않는다. 도시 이름은 최대 20자로 이루어져 있다.

### 출력 형식

입력된 도시이름 배열을 순서대로 처리할 때, "총 실행시간"을 출력한다.

### 조건

- 캐시 교체 알고리즘은 LRU(Least Recently Used)를 사용한다.
- cache hit일 경우 실행시간은 1이다.
- cache miss일 경우 실행시간은 5이다.

### 문제 분석 & 알고리즘 설계

cities를 찾는 데 걸리는 실행시간을 구하는 문제이다.  
cacheSize만큼 캐시에 값을 저장할 수 있다.  
cacheSize가 0 이라면 캐시에 어떤 값도 저장할 수 없다.  
캐시에 값이 이미 있다면, 해당 그 인덱스의 값을 삭제해주고, 캐시의 맨 마지막에 해당 값을 다시 넣어준다.  
캐시에 값이 없다면 0번째 값, 즉 가장 마지막에 쓰여진 값 LRU를 삭제하고, 캐시의 맨 마지막에 해당 값을 넣어준다.

### 코드

```js
function solution(cacheSize, cities) {
  var answer = 0;
  const cacheHit = 1;
  const cacheMiss = 5;
  const cache = Array(cacheSize);

  cities.forEach((el) => {
    const city = el.toLowerCase();

    if (!cacheSize) return cacheMiss * cities.length; // cacheSize가 0일 때 따로 처리

    if (cache.includes(city)) {
      //있을 때
      answer += cacheHit;
      cache.splice(cache.indexOf(city), 1);
      cache.push(city);
    } else {
      // 없을 때
      answer += cacheMiss;
      cache.shift();
      cache.push(city);
    }
  });
  console.log(answer);
  return answer;
}
```
