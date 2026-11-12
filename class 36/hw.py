
from tkinter import *
from datetime import date

# Create the main window
root = Tk()
root.title("Workshop Participant Greeting")
root.geometry("400x300")

# Heading
heading = Label(
    root,
    text="Workshop Welcome Desk",
    fg="white",
    bg="#072F5F",
    height=2,
    width=35
)

# Participant name label
name_label = Label(
    root,
    text="Participant Name",
    bg="#3895D3"
)

# Name input
name_entry = Entry(root, width=30)

# Welcome function
def display_welcome():
    name = name_entry.get().strip()

    text_box.delete(1.0, END)

    if name == "":
        text_box.insert(END, "Please enter your name!")
        return

    greeting = "Hello " + name + "!\n"
    message = "Welcome to the workshop.\n"
    workshop_date = "Date: " + str(date.today())

    text_box.insert(END, greeting)
    text_box.insert(END, message)
    text_box.insert(END, workshop_date)

# Output text box
text_box = Text(root, height=4, width=40)

# Check-in button
welcome_button = Button(
    root,
    text="Check In",
    command=display_welcome,
    height=1,
    bg="#1261A0",
    fg="white"
)

# Display widgets
heading.pack(pady=10)
name_label.pack(pady=10)
name_entry.pack()
welcome_button.pack(pady=10)
text_box.pack(pady=5)

# Run application
root.mainloop()

