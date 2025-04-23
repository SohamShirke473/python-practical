from tkinter import *   
top = Tk()   
top.geometry("400x250")
Label(top, text = "Enter Student Name").place(x = 50,y = 70)   
   
#e1 = Entry(top).place(x = 200, y = 70)   
e1 = Entry(top)
e1.place(x = 200, y = 70)

Label(top, text = "Select Your Branch").place(x = 50,y = 90)   
# Variable to store selected value
selected_option = StringVar(value="None")

# Function to display the selected option
#def show_selection():
 #   label.config(text=f"Selected: {selected_option.get()}")

radio1 = Radiobutton(text="Computer Engineering", variable=selected_option, value="Computer Engineering")
radio1.place(x = 180, y = 90)

radio2 = Radiobutton(text="Information Technology", variable=selected_option, value="Information Technology",)
radio2.place(x = 310, y = 90)

games = Label(top, text = "Selct Favorite Games").place(x = 50,y = 140) 
check_var1 = IntVar()
check_var2 = IntVar()
check_var3 = IntVar()

# Define the function to show the selected checkbutton states
def show_checkbuttons():
    print(f"Checkbutton 1: {'Selected' if check_var1.get() else 'Not Selected'}")
    print(f"Checkbutton 2: {'Selected' if check_var2.get() else 'Not Selected'}")
    print(f"Checkbutton 3: {'Selected' if check_var3.get() else 'Not Selected'}")

# Create checkbuttons
check1 = Checkbutton(top, text="Cricket", variable=check_var1, command=show_checkbuttons)
check1.place(x=50, y=170)

check2 = Checkbutton(top, text="Football", variable=check_var2, command=show_checkbuttons)
check2.place(x=50, y=200)

check3 = Checkbutton(top, text="Badminton", variable=check_var3, command=show_checkbuttons)
check3.place(x=50, y=230)


def submit_action():
    name = e1.get()  # Get value from entry field
    branch = selected_option.get()
    selected_games = []
    if check_var1.get():
        selected_games.append("Cricket")
    if check_var2.get():
        selected_games.append("Football")
    if check_var3.get():
        selected_games.append("Badminton")
    
    games_text = ", ".join(selected_games) if selected_games else "None"
    result_label.config(text=f"Entered data is:\nName:{name}\nBranch:{branch}\nGames:{games_text}")  # Update label
    
  
    print("Button clicked!")
    

# Create a Submit button
submit_btn = Button(top, text="Submit", command=submit_action)

# Place the button at x,y
submit_btn.place(x=125, y=250)

result_label = Label(top, fg="blue")
result_label.place(x=70, y=310)

top.mainloop()  
