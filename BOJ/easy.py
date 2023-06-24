word = input()
letters = [0] * 26
for w in word:
    letters[ord(w)-97] += 1
    
print(*letters, sep=' ')