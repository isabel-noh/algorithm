const fs = require("fs");
const input = fs.readFileSync("./a.txt").toString().trim().split("\n");

for (let i = 0; i < input.length - 1; i++) {
  const [name, age, weight] = input[i].split(" ");
  if (age > 17 || weight >= 80) {
    console.log(name + " Senior");
  } else {
    console.log(name + " Junior");
  }
}
