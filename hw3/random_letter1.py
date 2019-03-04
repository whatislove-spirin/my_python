wordlist = ['самовар','весна','лето']
import random
word = random.choice(wordlist)
letter = random.choice(word)
x = word.find(letter)
lword = list(word)
answer = lword[x]
lword[x] = '?'
newword = ''.join(lword)
print('Guess the word:',newword)
guessing = input('Введите букву:')
if guessing == answer:
    print('Победа!')
else: print('Увы! Попробуйте в другой раз.')
print('Слово:',word)
