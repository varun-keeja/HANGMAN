import random
from logo import logo
from words import word_list
from replit import clear
print(logo)
print("Welcome To HANGMAN!")
chosen_word= random.choice(word_list)
print(f"You have got {len(chosen_word)} letter word.")
import stage
lives=6
endgame=False
display=[]
for i in chosen_word:
    display+="_"
while not endgame:
    guess=input("Guess the Letter!\n")

    clear()
    
    if guess in display:
        print(f"you have already chose letter {guess}")

    for i in range(len(chosen_word)):
        letter=chosen_word[i]
        if letter==guess:
            display[i]=letter
    print(f"{''.join(display)}")
    
    if guess not in chosen_word:
        lives-=1
        print(stage.stages[lives])
        print(f"oops! Now you have got {lives} lives.")
        if lives==3:
            bi=[]
            hint=input("Do you want hint type 'yes' or 'no' \n")
            if hint=="yes":
                if len(chosen_word)==4:
                    print(f"2 letters in your word are {chosen_word[0]+chosen_word[2]}")
                if len(chosen_word)>4:
                    print(f"3 letters in your word are {chosen_word[0]+chosen_word[2]+chosen_word[4]}")
            else:
                pass
        if lives==0:
            endgame=True
            print("Oops!, You lose")
            print(f"your word was {chosen_word}")
    if "_" not in display:
        endgame=True
        print("You win")
