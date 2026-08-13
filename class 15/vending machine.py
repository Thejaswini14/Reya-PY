print("welcome to Reya's vending machine ")
print("choose you snack or drink!")
print("accepted coins 1,5,10 or 25")
print("we have 5 types of snacks")
print("we have cheetos,doritos,lays,kurkure and hersheys")
print("we have four drinks chocolate milk,gadorade, prime and water")
cheetos = 10
doritos = 10
lays = 10
kurkure = 10
hersheys = 10
print("choose you drinks")
chocolate_milk = 5
gadorade = 5 
prime = 5
water = 5
while True:
    choice = input("chooe your snack 🍟 or drink 🍹")
    if choice == "cheetos":
       price = cheetos
       break
    elif choice == "doritos":
       price = doritos
       break
    elif choice == "lays":
       price = lays
       break
    elif choice == "kurkure":
       price = kurkure
       break 
    elif choice == "hersheys":
       price = hersheys
       break
    elif choice == "chocolate_milk":
       price = chocolate_milk
       break
    elif choice == "gadorade":
       price = gadorade
       break
    elif choice == "prime":  
       price = prime
       break
    elif choice == "water":
        price = water
        break
    else:
        print("invalid choice please choose from the above choice")
total_inserted = 0 
def change(paid, price1):
   total_change = paid - price1
   return total_change
while True:

    coin = int(input("insert a coin"))     
    if coin != 1 and coin != 5 and coin != 10 and coin != 25:
     print("Invalid coin, try again!")
     continue 
    total_inserted += coin 
    print("total_inserted so far", total_inserted )
    if total_inserted >= price:
       print("enough money inserted")
       break
change_due = change(total_inserted, price)
print("dispensing your item")
if change_due == 0:
   pass 
else:
   print("here is your change",change(total_inserted , price)) 