print("library visit planner")
print("answer my questions and i will plan your library visit")
day = input("what day is it monday to saturday?")
weather = input("what is the weather like today? sunny, rainy, cloudy?").lower()
book = input("do you have a book to return?").lower()
print("your library visit plan for today")

if day in ("saturday", "sunday"):
    print("its a weekend, the library is closed!")
elif day == "monday" and book == "no":
    print("its monday and you have no book to return, so you can go to the library and read a book!")
    print("the library is open from 9am to 5pm!")
elif day in ("tuesday", "wednesday", "thursday") and book == "no":
    print("its a weekday and you have no book to return, so you can go to the library and read a book!")
    print("the library is open from 9am to 5pm!")
elif day == "friday" and book == "no":
    print("its friday and you have no book to return, so you can go to the library and read a book!")
    print("the library is open from 9am to 5pm!")
elif day == "monday" and book == "yes":
    print("its monday and you have a book to return, go to the library and return your book!")
    print("the library is open from 9am to 5pm!")
else:
   print("sorry, i dont know what day it is")
if weather == "sunny" and book == "yes":
    print("its a sunny day and you have a book to return, go to the library and return your book!")
elif weather == "sunny" and book == "no":
    print("it is a sunny day and you have no book to return, so you can go to the library and read a book!")
elif weather == "rainy" or weather == "cloudy":
    print("its a rainy or cloudy day, so pack a raincoat and an umbrella and go to the library!")
    print("please remember to return your book if you have one!")
print()

print("remember to return your book on time to avoid late fees!")
print("the library is a great place to read and learn new things!")
print("have a great day and enjoy your library visit!")
print("thank you for using the library visit planner!")