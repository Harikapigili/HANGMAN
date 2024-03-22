import time
name=input("what is your name?")
print("Hello" +name+ "Time to play Hangman")
time.sleep(1)
print("start guessing.....")
time.sleep(0.5)
word=("qwerty")
guesses=' '
turns=10
while turns>0:
    failed=0
for char in word:
    if char in guesses:
        print(char,end="")
    else:
        print("_",end",")
    failed+=1
if failed==0:
    print("you won")
    break 
guesses+=guesses
if guesses not in word:
    turn-=1
print("wrong")
print("you have",+turns+"more guesses")
if turns==0:
    print("you lose")