print("welcome to the holiday planner program")
print("there is two types of holidays you can choose from:")
print("1) beach holiday 🏖️")
print("2) mountain holiday 🏔️")
holiday = int(input("please enter your choice of holiday (1 or 2): "))
print("1) beach holiday 🏖️")
print("2) mountain holiday 🏔️") 
if holiday == 1:
    print("there is three types of beach holidays you can choose from:")
    print("1) caicos 🏝️")
    print("2) hawaii 🌺")
    print("3) goa 🏝️")
    beach = int(input("please enter your choice of beach holiday (1, 2 or 3): "))
    if beach == 1:
        print("caicos is a good choice, it is a beautiful island and has soft white sand beaches and clear blue water")
    elif beach == 2:
        print("hawaii is a good choice, it is a beautiful island and has a good coconuts and beaches and has a good weather")
    elif beach == 3:
        print("goa is a good choice, it is a beautiful island and has activities like water sports")
    else:
        print("invalid choice, please choose a valid beach holiday")
elif holiday == 2:
    print("there is two types of mountain holidays you can choose from:")
    print("1) swiss alps 🏔️")
    print("2) himalayas 🏔️")
    mountain = int(input("please enter your choice of mountain holiday (1 or 2): "))
    if mountain == 1:
        print("swiss alps is a good choice, it is a beautiful mountain and has skiing and snowboarding activities")
    elif mountain == 2:
        print("himalayas is a good choice, it is a beautiful mountain and you can also do trekking and camping activities")
    else:
        print("invalid choice, please choose a valid mountain holiday")
else:
    print("invalid choice, please choose a holiday in the range of 1 to 2") 
