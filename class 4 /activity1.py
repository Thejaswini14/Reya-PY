
temperature = int(input("enter todays temperature:"))
if temperature < 15:
    outfit = "sweater" 
    print("it is cold today")
    print("make sure you carry a ", outfit)
else:
    outfit = "t-shirt"
    print("it is warm today")
    print("make sure you wear a ", outfit)




rain = input("is it raining at your place today")
if rain =="yes":
    print("carry an umbrella")
else: 
     print("no need to carry an umbrella")



speed = int(input("what is the speed"))
if speed > 40:
    windbreaker = "yes"
    print("it is very windy today")
    print("shall i wear a windbreaker?", windbreaker)
else: 
     windbreaker = "no"
     print("the weather is calm")
     print("sall i wear a windbreaker",windbreaker)


puddles = input("are there puddles on the road?")
if puddles == "yes":
    shoes = "boots"
    print("the ground is wet wear ", shoes)
else:
     shoes = "sneakers"
     print("the ground is dry wear ", shoes)




print("---- weather outfit picker ----")
print("temprature:",temperature)
print("outfit",outfit)
print("raining",rain)
print("windbreaker",windbreaker)
print("shoes",shoes)
