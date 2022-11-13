a, b = map(int, input().split())
baesoo = []
if b > a:
    a, b = b, a
while True:
    for i in range(2, b+1):
        if a%i == 0 and b%i==0:
            baesoo.append(i)
            a, b = a//i, b//i
            break
    else:
        break
res1 = 1
for i in baesoo:
    res1 *= i
print(res1)
print(res1 * a * b)