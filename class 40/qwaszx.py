# Step 1: Import everything from tkinter to create the GUI.

# Step 2: Create the main window using root = Tk(), then set its size and title with root.geometry("400x300") and root.title("main").

# Step 3: Define a function topwin() to open a new Toplevel window.

# Step 4: Inside topwin(), create the new window with top = Toplevel(), then set its size and title with top.geometry("180x100") and top.title("toplevel").

# Step 5: Add a Label to the top window with the text "This is toplevel window", then display it using l2.pack().

# Step 6: Start the event loop for the top window using top.mainloop(), so it stays open.

# Step 7: Create a Label l in the main window with the text "This is root window".

# Step 8: Create a Button btn with the text "click here to open another window" and command=topwin, so clicking it opens the new window.

# Step 9: Arrange the main window's widgets using l.pack() and btn.pack().

# Step 10: Start the main GUI event loop using root.mainloop(), so the main window stays open and responds to user actions.



from tkinter import *
root = Tk()
root.geometry("400x300")
root.title("main")
def topwin():
    top = Toplevel()
    top.geometry("180x100")
    top.title("toplevel")
    lbl = Label(top, text="This is the toplevel window")
    lbl.pack()
    top.mainloop()
lbl2 = Label(root, text="This is root window")
btn = Button(root, text="click here to open another window", command=topwin)
lbl2.pack()
btn.pack()
root.mainloop()
