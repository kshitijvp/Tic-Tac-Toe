import tkinter as tk
from tkinter import messagebox

root=tk.Tk()

width=500
height=600

root.state('zoomed')

root.title('Tic Tac Toe')

winner=False
chance=True
point=0

def Disable_button():
    button_1.config(state=tk.DISABLED)
    button_2.config(state=tk.DISABLED)
    button_3.config(state=tk.DISABLED)
    button_4.config(state=tk.DISABLED)
    button_5.config(state=tk.DISABLED)
    button_6.config(state=tk.DISABLED)
    button_7.config(state=tk.DISABLED)
    button_8.config(state=tk.DISABLED)
    button_9.config(state=tk.DISABLED)

def checkifwon():
    global winner
    global point
    winner = False

    if button_1["text"] == "X" and button_2["text"] == "X" and button_3["text"] == "X" :
        button_1.config(bg="red")
        button_2.config(bg="red")
        button_3.config(bg="red")
        winner=True
        messagebox.showinfo("Game Over" , "X won!!")
        Disable_button()

    elif button_4["text"] == "X" and button_5["text"] == "X" and button_6["text"] == "X" :
        button_4.config(bg="red")
        button_5.config(bg="red")
        button_6.config(bg="red")
        winner=True
        messagebox.showinfo("Game Over" , "X won!!")
        Disable_button()

    elif button_7["text"] == "X" and button_8["text"] == "X" and button_9["text"] == "X" :
        button_7.config(bg="red")
        button_8.config(bg="red")
        button_9.config(bg="red")
        winner=True
        messagebox.showinfo("Game Over" , "X won!!")
        Disable_button()

    elif button_1["text"] == "X" and button_4["text"] == "X" and button_7["text"] == "X" :
        button_1.config(bg="red")
        button_4.config(bg="red")
        button_7.config(bg="red")
        winner=True
        messagebox.showinfo("Game Over" , "X won!!")
        Disable_button()

    elif button_3["text"] == "X" and button_6["text"] == "X" and button_9["text"] == "X" :
        button_3.config(bg="red")
        button_6.config(bg="red")
        button_9.config(bg="red")
        winner=True
        messagebox.showinfo("Game Over" , "X won!!")
        Disable_button()

    elif button_2["text"] == "X" and button_5["text"] == "X" and button_8["text"] == "X" :
        button_2.config(bg="red")
        button_5.config(bg="red")
        button_8.config(bg="red")
        winner=True
        messagebox.showinfo("Game Over" , "X won!!")
        Disable_button()

    elif button_1["text"] == "X" and button_5["text"] == "X" and button_9["text"] == "X" :
        button_1.config(bg="red")
        button_5.config(bg="red")
        button_9.config(bg="red")
        winner=True
        messagebox.showinfo("Game Over" , "X won!!")
        Disable_button()

    elif button_3["text"] == "X" and button_5["text"] == "X" and button_7["text"] == "X" :
        button_3.config(bg="red")
        button_5.config(bg="red")
        button_7.config(bg="red")
        winner=True
        messagebox.showinfo("Game Over" , "X won!!")
        Disable_button()

    elif button_1["text"] == "X" and button_2["text"] == "X" and button_3["text"] == "X" :
        button_1.config(bg="red")
        button_2.config(bg="red")
        button_3.config(bg="red")
        winner=True
        messagebox.showinfo("Game Over" , "X won!!")
        Disable_button()

    elif button_4["text"] == "X" and button_5["text"] == "X" and button_6["text"] == "X" :
        button_4.config(bg="red")
        button_5.config(bg="red")
        button_6.config(bg="red")
        winner=True
        messagebox.showinfo("Game Over" , "X won!!")
        Disable_button()

    elif button_7["text"] == "X" and button_8["text"] == "X" and button_9["text"] == "X" :
        button_7.config(bg="red")
        button_8.config(bg="red")
        button_9.config(bg="red")
        winner=True
        messagebox.showinfo("Game Over" , "X won!!")
        Disable_button()

    elif button_1["text"] == "X" and button_4["text"] == "X" and button_7["text"] == "X" :
        button_1.config(bg="red")
        button_4.config(bg="red")
        button_7.config(bg="red")
        winner=True
        messagebox.showinfo("Game Over" , "X won!!")
        Disable_button()

    elif button_3["text"] == "X" and button_6["text"] == "X" and button_9["text"] == "X" :
        button_3.config(bg="red")
        button_6.config(bg="red")
        button_9.config(bg="red")
        winner=True
        messagebox.showinfo("Game Over" , "X won!!")
        Disable_button()

    elif button_2["text"] == "X" and button_5["text"] == "X" and button_8["text"] == "X" :
        button_2.config(bg="red")
        button_5.config(bg="red")
        button_8.config(bg="red")
        winner=True
        messagebox.showinfo("Game Over" , "X won!!")
        Disable_button()

    elif button_1["text"] == "X" and button_5["text"] == "X" and button_9["text"] == "X" :
        button_1.config(bg="red")
        button_5.config(bg="red")
        button_9.config(bg="red")
        winner=True
        messagebox.showinfo("Game Over" , "X won!!")
        Disable_button()

    elif button_3["text"] == "X" and button_5["text"] == "X" and button_7["text"] == "X" :
        button_3.config(bg="red")
        button_5.config(bg="red")
        button_7.config(bg="red")
        winner=True
        messagebox.showinfo("Game Over" , "X won!!")
        Disable_button()
#--------------------------------------------------------------------------------------------
    if button_1["text"] == "O" and button_2["text"] == "O" and button_3["text"] == "O" :
        button_1.config(bg="red")
        button_2.config(bg="red")
        button_3.config(bg="red")
        winner=True
        messagebox.showinfo("Game Over" , "O won!!")
        Disable_button()

    elif button_4["text"] == "O" and button_5["text"] == "O" and button_6["text"] == "O" :
        button_4.config(bg="red")
        button_5.config(bg="red")
        button_6.config(bg="red")
        winner=True
        messagebox.showinfo("Game Over" , "O won!!")
        Disable_button()

    elif button_7["text"] == "O" and button_8["text"] == "O" and button_9["text"] == "O" :
        button_7.config(bg="red")
        button_8.config(bg="red")
        button_9.config(bg="red")
        winner=True
        messagebox.showinfo("Game Over" , "O won!!")
        Disable_button()

    elif button_1["text"] == "O" and button_4["text"] == "O" and button_7["text"] == "O" :
        button_1.config(bg="red")
        button_4.config(bg="red")
        button_7.config(bg="red")
        winner=True
        messagebox.showinfo("Game Over" , "O won!!")
        Disable_button()

    elif button_3["text"] == "O" and button_6["text"] == "O" and button_9["text"] == "O" :
        button_3.config(bg="red")
        button_6.config(bg="red")
        button_9.config(bg="red")
        winner=True
        messagebox.showinfo("Game Over" , "O won!!")
        Disable_button()

    elif button_2["text"] == "O" and button_5["text"] == "O" and button_8["text"] == "O" :
        button_2.config(bg="red")
        button_5.config(bg="red")
        button_8.config(bg="red")
        winner=True
        messagebox.showinfo("Game Over" , "O won!!")
        Disable_button

    elif button_1["text"] == "O" and button_5["text"] == "O" and button_9["text"] == "O" :
        button_1.config(bg="red")
        button_5.config(bg="red")
        button_9.config(bg="red")
        winner=True
        messagebox.showinfo("Game Over" , "O won!!")
        Disable_button()

    elif button_3["text"] == "O" and button_5["text"] == "O" and button_7["text"] == "O" :
        button_3.config(bg="red")
        button_5.config(bg="red")
        button_7.config(bg="red")
        winner=True
        messagebox.showinfo("Game Over" , "O won!!")
        Disable_button()

    elif button_1["text"] == "O" and button_2["text"] == "O" and button_3["text"] == "O" :
        button_1.config(bg="red")
        button_2.config(bg="red")
        button_3.config(bg="red")
        winner=True
        messagebox.showinfo("Game Over" , "O won!!")
        Disable_button()

    elif button_4["text"] == "O" and button_5["text"] == "O" and button_6["text"] == "O" :
        button_4.config(bg="red")
        button_5.config(bg="red")
        button_6.config(bg="red")
        winner=True
        messagebox.showinfo("Game Over" , "O won!!")
        Disable_button()

    elif button_7["text"] == "O" and button_8["text"] == "O" and button_9["text"] == "O" :
        button_7.config(bg="red")
        button_8.config(bg="red")
        button_9.config(bg="red")
        winner=True
        messagebox.showinfo("Game Over" , "O won!!")
        Disable_button()

    elif button_1["text"] == "O" and button_4["text"] == "O" and button_7["text"] == "O" :
        button_1.config(bg="red")
        button_4.config(bg="red")
        button_7.config(bg="red")
        winner=True
        messagebox.showinfo("Game Over" , "O won!!")
        Disable_button()

    elif button_3["text"] == "O" and button_6["text"] == "O" and button_9["text"] == "O" :
        button_3.config(bg="red")
        button_6.config(bg="red")
        button_9.config(bg="red")
        winner=True
        messagebox.showinfo("Game Over" , "0 won!!")
        Disable_button()

    elif button_2["text"] == "O" and button_5["text"] == "O" and button_8["text"] == "O" :
        button_2.config(bg="red")
        button_5.config(bg="red")
        button_8.config(bg="red")
        winner=True
        messagebox.showinfo("Game Over" , "O won!!")
        Disable_button()

    elif button_1["text"] == "O" and button_5["text"] == "O" and button_9["text"] == "O" :
        button_1.config(bg="red")
        button_5.config(bg="red")
        button_9.config(bg="red")
        winner=True
        messagebox.showinfo("Game Over" , "O won!!")
        Disable_button()

    elif button_3["text"] == "O" and button_5["text"] == "O" and button_7["text"] == "O" :
        button_3.config(bg="red")
        button_5.config(bg="red")
        button_7.config(bg="red")
        winner=True
        messagebox.showinfo("Game Over" , "O won!!")
        Disable_button()

    print(winner, point)
    if point==9 and winner==False:
        tk.messagebox.showinfo("Game Over" , "It is a tie \n No one won")
        Disable_button()
 
def button_clicked_1():
    global chance
    global point
    
    if chance == True and button_1["text"] != "O":
        button_1["text"] = "X"
        chance=False
        point+=1
        checkifwon()

    elif chance == False and button_1["text"] != "X":
        button_1["text"] = "O"
        chance = True
        point+=1
        checkifwon()

    else:
        tk.messagebox.showerror("Error" , "That place alreeady has a letter")


def button_clicked_2():
    global chance
    global point
    
    if chance == True and button_2["text"] != "O":
        button_2["text"] = "X"
        chance=False
        point+=1
        checkifwon()

    elif chance == False and button_2["text"] != "X":
        button_2["text"] = "O"
        chance = True
        point+=1
        checkifwon()

    else:
        tk.messagebox.showerror("Error" , "That place alreeady has a letter")


def button_clicked_3():
    global chance
    global point
    
    if chance == True and button_3["text"] != "O":
        button_3["text"] = "X"
        chance=False
        point+=1
        checkifwon()

    elif chance == False and button_3["text"] != "X":
        button_3["text"] = "O"
        chance = True
        checkifwon()
        point+=1

    else:
        tk.messagebox.showerror("Error" , "That place alreeady has a letter")

def button_clicked_4():
    global chance
    global point
    
    if chance == True and button_4["text"] != "O":
        button_4["text"] = "X"
        chance=False
        point+=1
        checkifwon()

    elif chance == False and button_4["text"] != "X":
        button_4["text"] = "O"
        chance = True
        point+=1
        checkifwon()

    else:
        tk.messagebox.showerror("Error" , "That place alreeady has a letter")

def button_clicked_5():
    global chance
    global point
    
    if chance == True and button_5["text"] != "O":
        button_5["text"] = "X"
        chance=False
        point+=1
        checkifwon()

    elif chance == False and button_5["text"] != "X":
        button_5["text"] = "O"
        chance = True
        point+=1
        checkifwon()

    else:
        tk.messagebox.showerror("Error" , "That place alreeady has a letter")

def button_clicked_6():
    global chance
    global point

    if chance == True and button_6["text"] != "O":
        button_6["text"] = "X"
        chance=False
        point+=1
        checkifwon()

    elif chance == False and button_6["text"] != "X":
        button_6["text"] = "O"
        chance = True
        point+=1
        checkifwon()

    else:
        tk.messagebox.showerror("Error" , "That place alreeady has a letter")

def button_clicked_7():
    global chance
    global point
    
    if chance == True and button_7["text"] != "O":
        button_7["text"] = "X"
        chance=False
        point+=1
        checkifwon()

    elif chance == False and button_7["text"] != "X":
        button_7["text"] = "O"
        chance = True
        point+=1
        checkifwon()

    else:
        tk.messagebox.showerror("Error" , "That place alreeady has a letter")

def button_clicked_8():
    global point
    global chance
    
    if chance == True and button_8["text"] != "O":
        button_8["text"] = "X"
        chance=False
        point+=1
        checkifwon()

    elif chance == False and button_8["text"] != "X":
        button_8["text"] = "O"
        chance = True
        point+=1
        checkifwon()

    else:
        tk.messagebox.showerror("Error" , "That place alreeady has a letter")

def button_clicked_9():
    global chance
    global point
    
    if chance == True and button_9["text"] != "O":
        button_9["text"] = "X"
        chance=False
        point+=1
        checkifwon()

    elif chance == False and button_9["text"] != "X":
        button_9["text"] = "O"
        chance = True
        point+=1
        checkifwon()

    else:
        tk.messagebox.showerror("Error" , "That place alreeady has a letter")

frame=tk.Frame(root , bg="cyan")
frame.place(relwidth=1 , relheight=1)


def reset():

    global button_1 , button_2 , button_3 , button_4 , button_5 , button_6 , button_7 , button_8 , button_9
    global chance , point 
    chance=True
    point=0


    button_1 = tk.Button(frame , bg="white", text="", command=button_clicked_1 , font=100) 
    button_1.place(relx=0.2 , rely=0.14 , relwidth=0.2 , relheight=0.2)

    button_2 = tk.Button(frame , bg="white", text="", command=button_clicked_2 , font=100)
    button_2.place(relx=0.4 , rely=0.14 , relwidth=0.2 , relheight=0.2)

    button_3 = tk.Button(frame , bg="white", text="", command=button_clicked_3 , font=100)
    button_3.place(relx=0.6 , rely=0.14 , relwidth=0.2 , relheight=0.2)

    button_4 = tk.Button(frame , bg="white", text="", command=button_clicked_4 , font=100)
    button_4.place(relx=0.2 , rely=0.337 , relwidth=0.2 , relheight=0.2)

    button_5 = tk.Button(frame , bg="white", text="", command=button_clicked_5 , font=100)
    button_5.place(relx=0.4 , rely=0.337 , relwidth=0.2 , relheight=0.2)

    button_6 = tk.Button(frame , bg="white", text="", command=button_clicked_6 , font=100)
    button_6.place(relx=0.6 , rely=0.337 , relwidth=0.2 , relheight=0.2 ) 

    button_7 = tk.Button(frame , bg="white", text="", command=button_clicked_7 , font=100)
    button_7.place(relx=0.2 , rely=0.53 , relwidth=0.2 , relheight=0.2)

    button_8 = tk.Button(frame , bg="white", text="", command=button_clicked_8 , font=100)
    button_8.place(relx=0.4 , rely=0.53 , relwidth=0.2 , relheight=0.2)

    button_9 = tk.Button(frame , bg="white", text="", command=button_clicked_9)
    button_9.place(relx=0.6 , rely=0.53 , relwidth=0.2 , relheight=0.2)


my_menu=tk.Menu(root)
root.config(menu=my_menu)

options_menu = tk.Menu(my_menu , tearoff=False)
my_menu.add_cascade(label="Options" , menu=options_menu)
options_menu.add_command(label="Reset Game" , command=reset)



reset()



root.mainloop()