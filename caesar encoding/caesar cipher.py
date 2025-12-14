# encoding...

word=input()
k=int(input())
word1=""
for i in range(len(word)):
    word1+=chr(ord(word[i])+k)

print(word1)

#decoding...
word=input()
k=int(input())
word1=""
for i in range(len(word)):
    word1+=chr(ord(word[i])-k)

print(word1)


