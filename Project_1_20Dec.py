grade = int(input("Enter Your Grade: "))
name = input(" Please Input Your Name: ")

if grade >= 90:
    grade = "Excellent"
    print ( f"{name} your Grade is {grade}. Great Job!")   
elif grade >= 70:
    grade = "Satisfactory"
    print ( f"{name} your Grade is {grade}. Pretty good!")
else:
    print ( f"{name} your Grade Needs Improvement. Contact me for assistance.")