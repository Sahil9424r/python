class Quizbrain:
   
    def __init__(self,questionlist):
        self.questionnumber=0
        self.score=0
        self.questionlist=questionlist
    
    def still_has_question(self):
        if self.questionnumber<len(self.questionlist): #or only this line is written not neeche wali
            return True
        else :
            return False
            
    def next_question(self):
        current=self.questionlist[self.questionnumber] 
        self.questionnumber+=1
        user_answer= input(f"Q.{self.questionnumber}:{current.text} (True/False):")#s list ke nanadar object ts hai and current .text give textqueas of each object present iside list        self.check_answer(user_answer,current.answer)


    def check_answer(self,user_answer,correct_answer):
        if user_answer.lower()==correct_answer.lower():
            self.score+=1
           
            print("u r right")
           
        else:
            print("u r wrong")
        print(f"the correct answer was:{correct_answer}.")        
        print(f"ur score is :{self.score}/{self.questionnumber}.")
    

     