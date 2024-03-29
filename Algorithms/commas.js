function comma(num) {
  let point,
    str = "";

  point = String(num).length % 3;

  while (point < String(num).length) {
    if (String(num).length % 3 !== 0) {
      str += String(num).substring(0, point);
      str += ",";
      num = Number(String(num).slice(1));
    } else {
      str += String(num).substring(0, 3);
      num = Number(String(num).slice(3));
      if (num % 1000 !== 0) {
        str += ",";
      }
    }
  }
  return str;
}

function com(n) {
  let num = n;
  return num.toLocaleString("ko-KR");
}

console.log(comma(1234567899));
console.log(com(1234567899));
