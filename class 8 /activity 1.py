print("welcome to the best child made vehicle selector program")
print("there is two types of vehicles you can choose from:")
print("1) car 🚗")
print("2) bike yamaha 🏍️/ scooter = ather 🛵")
vehicle = int(input("please enter your choice of vehicle (1 or 2): "))

if vehicle == 1:
    print("there is three types of cars you can choose from:")
    print("1) ferrari 🏎️")
    print("2) lamborghini 🏎️")
    print("3) tesla 🚙")
    car = int(input("please enter your choice of car (1, 2 or 3): "))
    if car == 1:
        print("ferrari is a good choice, it is a fast car and has a good design")
    elif car == 2:
        print("lamborghini is a good racing car, but it is not a good choice for daily use")
    elif car == 3:
        print("tesla is a nice car, it does no harm the environment and it is spacious inside")
    else:
        print("invalid choice, please choose a valid car")
elif vehicle == 2:
    print("there is two types of bikes you can choose from:")
    print("1) motorbike yamaha 🏍️")
    print("2) scooter ather 🛵")
    bike = int(input("please enter you choice of bike (1 or 2): "))
    if bike == 1:
        print("yamaha is a good choice, it is a fast bike and it is good for long rides")
    elif bike == 2:
        print("ather is a good choice, it is a good bike for daily use and it is good for short rides")
    else:
        print("invalid choice, please choose a valid bike")
else:
    print("invalid choice, please choose a vehicle in the range of 1 to 2")
    
