# Step 1: Import everything from tkinter and create the main window with a title and 400x400 size.

# Step 2: Create a Frame to organize the form, and three Labels for Full Name, Email Id, and Enter Password.

# Step 3: Create three Entry widgets - name_entry, email_entry, and pass_entry with show="*" for the hidden password.

# Step 4: Define display(): read name_entry.get(), build a greeting message, and insert it into a Text widget named textbox.

# Step 5: Create the textbox itself and a Button labeled "Create Account" with command=display.

# Step 6: Place every widget - the frame, labels, entries, button, and textbox - at its own exact x, y position.

# Step 7: Call root.mainloop() to keep the login window open and responsive.

from tkinter import *
root = Tk()
root.title("Login Form")
root.geometry("400x400")
frame = Frame(root, width=400, height=400)
lbl1 = Label(frame, text="Full Name")
lbl2 = Label(frame, text="Email Id")
lbl3 = Label(frame, text="Enter Password")
name_entry = Entry(frame, width=30)
email_entry = Entry(frame, width=30)
pass_entry = Entry(frame, width=30, show="*")
def display():
    name = name_entry.get()
    greeting = f"Hello {name}, your account has been created successfully!"
    textbox.insert(END, greeting)
textbox = Text(root, height=4, width=40)
btn = Button(root, text="login", command=display)
frame.place(x=0, y=0)
lbl1.place(x=50, y=50)
lbl2.place(x=50, y=100)
lbl3.place(x=50, y=150)
name_entry.place(x=150, y=50)
email_entry.place(x=150, y=100)
pass_entry.place(x=150, y=150)
btn.place(x=150, y=200)
textbox.place(x=50, y=250)
root.mainloop()
