print("Weclome to Grade Calculator")
chemmark = float(input("Please, enter you chemisty mark:"))
physmark = float(input("Please, enter you physics mark:"))
matmark = float(input("Please, enter you maths mark:"))
score = round((chemmark+physmark+matmark)/3, 2)
print("Your percentage score is:",score,"%")

if score > 70:
    print("You scored a grade of: A")
elif score > 60:
    print("You scored a grade of: B")
elif score > 50:
    print("You scored a grade of: C")
elif score > 40:
    print("You scored a grade of: D")
else:
    print("You failed")


