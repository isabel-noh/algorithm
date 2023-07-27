function check(info, query) {
  let flag = true;
  for (condition of query) {
    if (flag === false) {
      return false;
    }
    if (!isNaN(parseInt(condition))) {
      if (Number(condition) > Number(info[info.length - 1])) {
        flag = false;
      }
    } else {
      if (!info.includes(condition)) {
        flag = false;
      }
    }
  }
  if (flag === false) {
    return false;
  }
  return true;
}
function solution(info, query) {
  var answer = [];
  const infoArr = info.map((el) => el.split(" "));
  const queryArr = query.map((el) =>
    el.split(" ").filter((v) => v !== "and" && v !== "-")
  );
  for (const iterator of queryArr) {
    let candidate = 0;
    for (const item of infoArr) {
      if (check(item, iterator)) {
        candidate++;
      }
    }
    answer.push(candidate);
  }
  return answer;
}
