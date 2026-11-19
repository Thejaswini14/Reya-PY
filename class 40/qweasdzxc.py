# Step 1: Import everything from tkinter, import messagebox from tkinter for popups, and import Image and ImageTk from PIL to load images.

# Step 2: Create the main window using root = Tk(), then set its title, background color, and size.

# Step 3: Load "app_img.jpg" with Image.open(), resize it to (300, 300), and convert it with ImageTk.PhotoImage() so it can be shown in a Label.

# Step 4: Add a welcome label below the image with a greeting message.

# Step 5: Define a function msg() that shows a messagebox.showinfo() popup asking if the user wants to calculate denominations, then calls topwin() if they click OK.

# Step 6: Create a button with the text "Let's get started!" and command=msg, then place it near the bottom of the window.

# Step 7: Define a function topwin() to open a new Toplevel window for the calculator.

# Step 8: Inside topwin(), set the new window's title, background color, and size.

# Step 9: Add a label asking the user to "Enter total amount" and an Entry box for typing it.

# Step 10: Add a heading label plus labels and Entry boxes (t1, t2, t3) to display the denomination counts for 2000, 500, and 100.

# Step 11: Inside topwin(), define a nested function calculator() that tries to convert the entered amount to an integer.

# Step 12: Inside calculator(), use // and % repeatedly to find the number of 2000, 500, and 100 notes, then clear and insert the results into t1, t2, and t3.

# Step 13: Inside calculator(), if the input isn't a valid number, show an error popup using messagebox.showerror().

# Step 14: Create a "Calculate" button with command=calculator, then place every widget in the top window using .place().

# Step 15: Start the event loop for the top window using top.mainloop(), then the main GUI event loop using root.mainloop().



from tkinter import *
from tkinter import messagebox 
from PIL import image,ImageTk
root = Tk()
root.geometry("700x500")
upload = image.open("/Users/teju/Downloads/top-view-notebooks-calculator_23-2149103982.png")
size = upload.resize((300, 300)) 
image = ImageTk.PhotoImage(size)
label = Label(root, image=image, text= "welcome to the calculater programe!")
label.place(x=123, y=456)
def msg():
    msgb = messagebox.showinfo("alert!!")
    if msgb == "ok":
btn = Button(root,text="Let's get started!")
