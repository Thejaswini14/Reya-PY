print("answer my questions and i will plan your day")
day = input("what day is it today?")
weather = input("what is the weather like today? sunny, rainy, cloudy?")
homework = input("have you finished your homework? yes or no?").lower()
print("your plan for today")
print('='*30)
if day in ("saturday", "sunday"):
    print("its a weekend enjoy you day!")
elif day == "monday":
    print("its monday, time to start the week!")
elif day in ("tuesday", "wednesday", "thursday"):
    print("its a weekday, keep going!")
elif day == "friday":
    print(" yay its friday, the weekend is almost here!")
else:
    print("sorry, i dont know what day it is")
if weather == "sunny" and homework == "yes":
    print("its a sunny day and you have finished your homework, go outside and enjoy the sun!")
elif weather == "sunny" and homework == "no":
    print("it is a sunny day but you have not done your homework, so you should do your homework first then go out to play!")
elif weather == "rainy" or weather == "cloudy":
    print("its a rainy or cloudy day, so pack a raincoat and an umbrella and go outside!")
elif not(homework == "yes"):
    print("please finish your homework first")
elif weather == "rainy" and homework == "no":
    print("best plan stay inside and finish your homework!")
print()