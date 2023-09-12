import random
 
words = ['MERCEDES', 'BMW', 'TOYOTA']
word=words[random.randrange(5)]
len_word=len(word)
health = 8
test=False
used_letters=""
win_word=[]
for i in range(len(word)):
    win_word+='*'
 
while len_word != 0 and health != 0:
    test = False
    while True:
        letter = input('\nENTER YOUR LETTER: ')
        if letter in used_letters or len(letter)>1:
            print('\nNO MORE THAN ONE LETTER!')
        else:
            used_letters+=letter
            break
    count=0
    for i in word:
        if letter in i:
            len_word -= 1
            test=True
            win_word[count]=letter
        count+=1
 
 
 
    if not test:
        health -= 1
        print('WRONG')
    else:
        print('RIGHT')
        print(win_word)
 
    print('YOUR HEALTH = ', health)
 
if(len_word == 0):
    print('\nYOU WIN :) -->', word.upper())
else:
    print('\nYOU LOOSE. TRY AGAIN!')