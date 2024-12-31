grade = int(input("Enter Your Grade: "))
name = input(" Please Input Your Name: ")

if grade >= 90:
    grade = "Excellent"
    print ( f"{name} your Grade is {grade}. Great Job!")
elif grade == 70 <= 89:
    grade = "Satisfactory"
    print ( f"{name} your Grade is {grade}. Pretty good!")
else: 
    grade <= 69
    grade = "Needs Improvement"
    print ( f"{name} your Grade {grade}. Contact me for assistance.")