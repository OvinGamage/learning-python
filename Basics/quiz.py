questions=("What is the capital of Sri Lanka","What is the tallest mountain on earth",
           "Who invented the telephone",
           "How many elements are there in the periodic table",
           "What is the largest land animal")
options=("A.Bangkok,B.Kathmandu,C.Sri Jayawardenapura Kotte,D.Kuala Lumpur",
         "A.Mount Aconcagua,B.Mount Everest,C.Mount Kilimanjaro,d.Mount Cook",
         "A.Alexander Graham Bell,B.Mahatma Gandhi,C.Albert Einstein,D.Thomas Edison",
         "A.120,B.118,C.110,D.100",
         "A.Whale,B.Hippopotamus,C.Lion.D.Elephant")
answers=("C","B","A","B","D")
guesses=[]
question_no=0
score=0
print("TEST YOUR KNOWLEDGE!")
for question in questions:
    print("----------")
    print(question,)
    print()
    for option in options[question_no]:
        print(option,end="")
    print()
    guess=input("enter your answer(A,B,C,D):").upper()
    guesses.append(guess)

    if guess==answers[question_no]:
        print("Correct Answer")
        score+=1
        question_no+=1

    else:
        print("Wrong Answer")
        question_no+=1
print(f"You answered {score} out of {question_no} correctly")
marks=score/question_no*100
print(f"You got {marks}% of questions correct")

