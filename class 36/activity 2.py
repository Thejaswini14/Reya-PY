# Step 1: Import everything from tkinter, and also import date from datetime to display today's date.

# Step 2: Create the main window using root = Tk(), then set its title and size with root.title(...) and root.geometry(...).

# Step 3: Create a Label lbl with the text "Hey There!" and its own foreground color, background color, height, and width.

# Step 4: Create a Label name_lbl asking the user for their full name.

# Step 5: Create an Entry widget name_entry as a text box for the user to type their name into.

# Step 6: Define a function display() that reads name_entry.get(), builds a greeting and welcome message, and uses a global variable named message.

# Step 7: Inside display(), insert the greeting, message, and today's date into the text box using text_box.insert(END, ...).

# Step 8: Create a Text widget text_box to display the output messages.

# Step 9: Create a Button widget btn with the text "Begin" and command=display, so clicking it calls the display() function.

# Step 10: Arrange every widget in the window - lbl, name_lbl, name_entry, btn, and text_box - using pack().

# Step 11: Start the GUI event loop using root.mainloop(), so the window stays open and responds to user actions.






from tkinter import *
from datetime import date

# Create the main window
root = Tk()
root.title("Hey There!")
root.geometry("400x300")

# Create the heading
lbl = Label(
    root,
    text="Hey There!",
    fg="white",
    bg="black",
    height=2,
    width=20
)

# Create the name label
name_lbl = Label(root, text="Enter your full name:")

# Create the name input box
name_entry = Entry(root, width=30)

# Function to display the greeting
def display():
    name = name_entry.get().strip()

    if name == "":
        text_box.insert(END, "Please enter your name!\n")
        return

    message = f"Hello {name}, welcome to the program!\n"
    text_box.insert(END, message)
    text_box.insert(END, f"Today's date: {date.today()}\n\n")

# Create the text box
text_box = Text(root, height=5, width=40)

# Create the button
btn = Button(
    root,
    text="Let's Start",
    command=display,
    bg="black",
    fg="white",
    height=2,
    width=20
)

# Place everything in the window
lbl.pack(pady=5)
name_lbl.pack(pady=5)
name_entry.pack(pady=5)
btn.pack(pady=10)
text_box.pack(pady=5)

# Run the application
root.mainloop()
