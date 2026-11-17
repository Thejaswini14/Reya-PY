# Step 1: Import everything from tkinter to create the GUI.

# Step 2: Create the main window using window = Tk().

# Step 3: Set the window's title to "Event Handler" and its size to 100x100.

# Step 4: Define a function handle_keypress(event) that receives an event object automatically and prints event.char to show which key was pressed.

# Step 5: Bind the keypress event to the window using window.bind("<Key>", handle_keypress), so every key press triggers the function.

# Step 6: Define a function handle_click(event) that also receives an event object automatically and prints a message when the button is clicked.

# Step 7: Create a Button widget with the text "Click me!" and display it using pack().

# Step 8: Bind the left mouse click event to the button using button.bind("<Button-1>", handle_click), so left-click triggers the function.

# Step 9: Start the GUI event loop using window.mainloop(), so the window stays open and responds to user actions.



from tkinter import *
window = Tk()
window.title("Event Handler")
window.geometry("100x100")
def handle_keypress(event):
    print(event.char)
window.bind("<Key>", handle_keypress)
def handle_click(event):
    print("the button was clicked!")
button = Button(text = "click me!")
button.pack()
button.bind("<Button-1>", handle_click)
window.mainloop()

