# Step 1: Import everything from tkinter, plus askopenfilename and asksaveasfilename from tkinter.filedialog.

# Step 2: Create the main window with Tk(), set its title and 600x500 size, and configure the grid to expand.

# Step 3: Define open_file(): call askopenfilename() to choose a file, returning early if nothing was chosen.

# Step 4: Inside open_file(), clear the editor with delete(1.0, END), read the file, then insert its text with insert(END, text).

# Step 5: Update the window's title to show the newly opened file's path.

# Step 6: Define save_file(): call asksaveasfilename() to choose a save location, returning early if nothing was chosen.

# Step 7: Inside save_file(), get the editor's current text with get(1.0, END), then write it to the chosen file.

# Step 8: Update the window's title again to show the newly saved file's path.

# Step 9: Create the Text widget, the button frame, and an Open and a Save As button, wiring each button's command to its matching function.

# Step 10: Arrange everything with grid(), then call window.mainloop() to start the application.





from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
window = Tk()
window.geometry("600x500")
def open_file():
    file_path = askopenfilename(filetypes= [("Text file", "*.txt"),("all files", "*.*")])
    if not file_path:
        return
    text_edit.delete(1.0, END)
    with open(file_path,"r") as inputfile: 
        text = inputfile.read()
        text_edit.insert(END, text)
        inputfile.close()
    window.title(file_path)
def save_file():
    file_path = asksaveasfilename(defaultextension= "txt",filetypes= [("Text file", "*.txt"),("all files", "*.*")])
    if not file_path:
        return
    text_edit.delete(1.0, END)
    with open(file_path,"w") as outputfile: 
        text = outputfile.read()
        text_edit.insert(END, text)
        outputfile.close()
    window.title(file_path)
text_edit = Text(window)
buttons = Frame(window,relief= RAISED, bd = 3)
btn_open = Button(buttons, text="open", command= open_file)    
btn_save = Button(buttons, text="save as", command= save_file)
btn_open.grid(row=0, column=0, sticky="ew")
btn_save.grid(row=1, column=0, sticky="ew")
buttons.grid(row=0, column=1, sticky="ns")
text_edit.grid(row=0, column=1, sticky="nsew")
window.mainloop()

