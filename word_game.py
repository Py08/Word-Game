import random
import sys

Lst_Str_Words = ['ghost','pouch','scale','cakes','cubes','horse','about','above','kings','shark','taste','cloth']
lives = 10
score = 0
print ("Welcome to 10 lives!")
print ("RULES:- A set of question marks come on the screen. They are the letters that are not guessed. You can also guess the whole word, but be careful. If you guess the whole word and it is wrong it moves on to the next word and you lose 2 lives! If you solve a word you get 1 point. You have only 10 lives per word through-out the game. 5 points to win!")
print ("(Playing in full screen is better)")
while True:
    if score == 5:
        print ("You Win!")
        sys.exit(0)
    word = random.choice(Lst_Str_Words)
    Str_Question = "?????"
    while True:
        print (Str_Question)
        ans = input("guess a letter or the whole word > ")
        if len(ans) == 5:
            if ans == word:
                print ("correct")
                score = score + 1
                #print ("Lives left: ", lives)
                print ("Your score is ", score)
                lives = 10
                break
            else:
                print ("wrong")
                lives = lives - 2
                print ("Lives left: ", lives)
                print ("Your score is: ", score)
                print ("The answer was: ", word)
                break
        elif len(ans) == 1:
            if ans in word:
                ans_index = word.index(ans)
                if ans_index == 0:
                    Str_Question = ans + Str_Question[1:]
                elif ans_index == 1:
                    Str_Question = Str_Question[0] + ans + Str_Question[2:]
                elif ans_index == 2:
                    Str_Question = Str_Question[:2] + ans + Str_Question[3:]
                elif ans_index == 3:
                    Str_Question = Str_Question[:3] + ans + Str_Question[4]
                elif ans_index == 4:
                    Str_Question = Str_Question[:4] + ans
            else:
                print ("wrong")
                lives = lives - 1
                print ("Lives left: ", lives)
        else:
            print ("Guess only one letter or whole word")
        if lives == 0:
            print ("You lose")
            sys.exit(0)
        elif score == 5:
            print ("You win")
            sys.exit(0)
        elif '?' not in Str_Question:
            score = score + 1
            print ("Your score is: ", score)
            print ("Word Solved!")
            lives = 10
            break
# By Amey Anand
# Done on: 28/01/2020
