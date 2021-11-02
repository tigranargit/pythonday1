def grade (grade1,grade2,grade3,name):
    finalgrade= (round((grade1/25*100))+round((grade2/50*100))+round((grade3)))/3
    if finalgrade > 90:
        lettergrade = "A*"
    elif finalgrade >80:
        lettergrade = "A"
    elif finalgrade >70:
        lettergrade = "B"
    elif finalgrade >60:
        lettergrade = "C"
    elif finalgrade >50:
        lettergrade = "D"
    else:
        lettergrade = "E"
    return f"{name}'s final grade is {lettergrade} or {round(finalgrade)}%"

name = input("Please, enter your full name:")
grade1 = float(input("Please, enter your homework score out of 25:"))
grade2 = float(input("Please, enter your assesment score out of 50:"))
grade3 = float(input("Please, enter your final exam score out of 100:"))
print(grade(grade1, grade2, grade3, name))