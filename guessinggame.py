from tkinter import*
import math
import tkinter.messagebox
import random

root = Tk()
root.geometry("500x500") # root.minsize(500, 500)
root.title("Guess the number game")

number = random.randint(1, 20)

def check_num():
    guess = text_guess.get()
    guess = int(guess)
    if guess > number:
        tkinter.messagebox.showinfo("Higher", "Your guess is too high")
    elif guess < number:
        tkinter.messagebox.showinfo("Lower", "Your guess is too low")
    elif guess == number:
        tkinter.messagebox.showinfo("Correct", "You guessed it correctly")



def btn_confirm():
    my_name = text_name.get()
    tkinter.messagebox.showinfo("welcome", "Well " +my_name+ " I am thinking of a number between one to twenty, guess that number")

label = Label(root, text="Welcome to our game")
label.pack()
label_name = Label(root, text="What is your name?")
label_name.place(x=50, y=50)
text_name = Entry(root, width=25)
text_name.place(x=50,y=75)

btn_ok = Button(root, text="Ok", command=btn_confirm)
btn_ok.place(x=300, y=75)
label_guess = Label(root, text="Take a guess")
label_guess.place(x=50, y=125)
text_guess = Entry(root, width=25)
text_guess.place(x=50, y=150)
btn_check = Button(root, text="Check", command=check_num)
btn_check.place(x=300, y=150 )
root.mainloop()