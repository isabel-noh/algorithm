str = list(input())
for l in range(len(str)):
    if ord(str[l]) > 97: 
        str[l] = (chr(ord(str[l])-32))
    else: 
        str[l] = (chr(ord(str[l])+32))
print(*str, sep='', end='')