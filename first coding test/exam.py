user = int(input("write a number: "))
variable = 1 
while variable <= 5:
    reya = int(input("write a number: "))
    if user == reya:
        print("you guessed it right")
        break
    else:
        print("try again")
    variable += 1