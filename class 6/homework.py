print(ord('A')) 
print(ord('a'))
print(ord('0'))

print(chr(65))
print(chr(97))
print(chr(48))
 
char = input("Enter a character: ")


if type(char) is str and len(char) == 1:
    print("valid input")
else:
    print("please enter one character")



