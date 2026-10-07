def honor_rollChecker():
    grade = input("Enter your grade: ")
    days_absent = int(input("Enter the number of days absent: "))

    if days_absent > 5:
        print("You have been absent for too many days.")
    else:
        print("Your attendance is acceptable.")
    if grade >= "A":
        print("You have an excellent grade.")
    elif grade >= "B":
        print("You have a good grade.")
    elif grade >= "C":
        print("Your grade is average.")
    else:
        print("Your grade needs improvement.")
