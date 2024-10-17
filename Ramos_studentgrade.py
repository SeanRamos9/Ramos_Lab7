name = input("Enter your name: ")
section = input("Enter your section: ")
prelims_grade = float(input("Enter your prelim grade: "))
if(prelims_grade < 40 or prelims_grade > 100):
    print("invalid input")
    exit ()
midterm_grade = float(input("Enter your midterm grade: "))
if(midterm_grade < 40 or midterm_grade > 100):
    print("invalid input")
    exit()
Finals_grade = float(input("Enter your finals grade: "))
if(Finals_grade < 40 or Finals_grade > 100):
    print("invalid input")
    exit()
final = (prelims_grade * .3333) + (midterm_grade * .3333) + (Finals_grade * .3333)
print(f"your final grade is {final:.0f}")


if(final >= 99 and final <= 100):
    print("1.00")
elif(final >= 96 and final <= 98):
    print("1.25")
elif(final >= 93 and final <= 95):
    print("1.50")
elif(final >= 90  and final <= 92):
    print("1.75")
elif(final >= 87 and final <= 89):
    print("2.00")
elif(final >= 84 and final <= 86):
    print("2.25")
elif(final >= 81 and final <= 83):
    print("2.50")
elif(final >= 78 and final <= 80):
    print("2.75")
elif(final >= 75 and final <= 77):
    print("3.00")
elif(final < 75):
    print("5.0")
else:
    print("invalid input")