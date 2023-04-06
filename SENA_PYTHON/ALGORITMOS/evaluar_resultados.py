#EVALUATE:
def evaluate(score):
    if score > 95 and score <= 100:
        print("This tasks is completed")
    elif score < 95 and score >= 70:
        print("this task needds to be completed ASAP")
    else:
        print("Asignar Plan de mejoramiento")

    
score = int(input("Please enter the score for this tasks"))
evaluate(score)
