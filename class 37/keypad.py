# Step 1: Import everything from tkinter and create the main window with a title and 250x300 size.

# Step 2: Store the keypad's numbers and symbols in a 2D list named nums, one inner list per row.

# Step 3: Start an outer loop with i from 0 to 3, one pass per row.

# Step 4: Configure that row's column and row sizing with columnconfigure() and rowconfigure() so cells resize evenly.

# Step 5: Start an inner loop with j from 0 to 2, one pass per column.

# Step 6: Create a Frame with relief=SUNKEN and borderwidth=1, then place it with frame.grid(row=i, column=j).

# Step 7: Create a Label inside that frame showing nums[i][j], then pack() it with padding.

# Step 8: Call root.mainloop() to keep the keypad window open.

from tkinter import *
root = Tk()
root.title("number keypad")
root.geometry("250x300")
nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]
for i in range(4):
    root.columnconfigure(i, weight=1)
for i in range(3):
    root.rowconfigure(i, weight=1)
    root.columnconfigure(i, weight=1)
    for j in range(3):
        frame = Frame(root, relief=SUNKEN, borderwidth=1)
        frame.grid(row=i, column=j, sticky=NSEW)
        label = Label(frame, text=nums[i][j])
        label.pack(padx=10, pady=10)
root.mainloop()