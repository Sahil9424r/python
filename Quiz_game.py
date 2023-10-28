from questionModel import Question
from data import question_data
from quizbrain import Quizbrain
question_bank=[]
for i in question_data:
    questiontext=i["text"]
    questionanswer=i["answer"]
    questions=Question(q_text=questiontext,q_answer=questionanswer)#here object is created inside list
    question_bank.append(questions)#add inside list
# print(question_bank)  
# print(question_bank[0].text)
# print(question_bank[0].answer)
# print(question_bank[1].text)
# print(question_bank[1 ].answer)
quiz=Quizbrain(question_bank)
while quiz.still_has_question():
   quiz.next_question()
print("u have completed the quiz")
print(f"Your final score was:{quiz.score}/{len(question_bank)}")
              