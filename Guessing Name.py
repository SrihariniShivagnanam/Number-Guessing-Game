from tkinter import *
import random

attempts = 5

answer = random.randint(1,50)

def check_answer():
    global attempts
    global text
    attempts -= 1
    guess = int(entry_window.get())

    if  answer == guess:
        text.set("Congrats!, You Won!!")
        btn_check.pack_forget()
    elif attempts == 0:
        text.set("You are out of attempts!")
        btn_check.pack_forget()
    elif guess < answer:
        text.set("Incorrect! You have" + str(attempts) + " attempts remaining - Go Higher!!")
    elif guess > answer:
        text.set("Incorrect! You have" + str(attempts) + " attempts remaining - Go Lower!!")

    return

root = Tk()

root.title("Guess the Number")

root.geometry("500x200")

label = Label(root, text="Guess the Number from 1 to 50")
label.pack()

entry_window = Entry(root, width=50,borderwidth=5)
entry_window.pack()

btn_check = Button(root, text="Check", bg="Powder Blue", command=check_answer)
btn_check.pack()

btn_quit = Button(root, text="Quit", bg="Yellow",  command=root.destroy)
btn_quit.pack()

text = StringVar()
text.set("You have 5 attempts remaining!!")

guess_attempts = Label(root, textvariable=text)
guess_attempts.pack()

root.mainloop()