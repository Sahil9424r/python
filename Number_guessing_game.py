import random
print("Welcome to te number guessing Game!")
print("I'm thinking of a number between 1 and 100.")

Easy_level_turns=10
Hard_level_turns=5

def check_answer(guess,choice):
    if choice==guess:
        return "u r right"
    elif choice>guess:
        return "too low"   
    else:
        return "too high"    

def difficulty():
    level=input("Choose a difficulty:Type easy or hard").lower()
    if level=="easy":
        return Easy_level_turns
    elif level=="hard":
        return Hard_level_turns

def game():
    isg=True
    choice=random.randint(1,100)
    print(choice)
    turns=difficulty()
    print(f"u have total {turns} attempts.")
    while isg:
        guess=int(input("Make a guess:"))
        turns-=1
        print(check_answer(guess=guess,choice=choice))
        print(f"u have {turns} attempts reamaining to guess a number.")
        answer=check_answer(guess,choice)
        if answer=="u r right" :
          print("YOU WON")
          isg=False
        elif turns==0 and answer!="u r right":
         print("YOU LOSE")
         isg=False
        elif turns==0 and answer=="u r right":
            print("Correct YOU WON")
            isg=False
game()
