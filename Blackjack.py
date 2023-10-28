import random

def deal_card():
    '''Give random card.'''
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    return random.choice(cards)


def calculate_score(cards):
   # score=0
   # for j in cards:
   #    score+=j
   score= sum(cards)   # or by sum function direct
   if score==21 :
       return 0
   if 11 in cards and score>21:
      cards.remove(11)
      cards.append(1)
    #cards.replace(11,1)
   
   return score   

def compare(user_score,computer_score):
   if user_score==computer_score:
        return "draw"
   elif computer_score==0:
       return "lose"
   elif user_score==0:
       return "win"
   elif user_score>21:
       return "u went over and lose"
   elif computer_score>21:
       "u win opponent went over"
   elif user_score>computer_score:
       return "u win"
   else:
       return "u lose"    
def play_game():
   isg=True
   user_card=[]
   computer_card=[]

   for i in range(2):
         user_card.append(deal_card())#by me 
         computer_card.append(deal_card())
         # new_card=deal_card()#by angela yu
         # user_card.append(new_card)
         # computer_card.append(new_card)


   while isg:
      user_score=calculate_score(user_card)
      computer_score=calculate_score(computer_card)
      print(user_card)
      print(f"computer first card is:{computer_card[0]}")
      # print(computer_card)  


      print(f" user score is:{calculate_score(user_card)}")
      print(f"computer score is:{ calculate_score(computer_card)}")
      # print(calculate_score(computer_card))

      if calculate_score(user_card)==0 or calculate_score(computer_card)==0 or calculate_score(user_card)>21:
         print("Game Ends!")
         isg=False
      else:
         answer=input("Enter yes to continue and no to stop").lower()
         if answer=="yes":
            user_card.append(deal_card())
         else:
            print("Game Ends!")
            isg=False
   while calculate_score(computer_card)!=0 and calculate_score(computer_card)<17:
      computer_card.append(deal_card())
      calculate_score(computer_card)
   print(f"ur final score:{user_score} and computer final score:{computer_score}")
   print(compare(user_score=user_score,computer_score=computer_score))
         
while input("DO u want to play game?")=="y":
    play_game()
    
    
    
     
            
       
        

   
        
    

    