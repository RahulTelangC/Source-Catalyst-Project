from tkinter import *
from PIL import Image,ImageTk
from random import randint

root = Tk()
root.title("Rock Paper Sissor")
root.configure(background="#9b59b6")

rock_img = ImageTk.PhotoImage(Image.open("Rock -user.png"))
paper_img = ImageTk.PhotoImage(Image.open("Paper -user.png"))
scissor_img = ImageTk.PhotoImage(Image.open("Scissor -user.png"))
rock_img_comp = ImageTk.PhotoImage(Image.open("Rock.png"))
paper_img_comp = ImageTk.PhotoImage(Image.open("Paper.png"))
scissor_img_comp = ImageTk.PhotoImage(Image.open("Scissor.png"))

#insert picture
user_label =Label(root, image=scissor_img, bg="#9b59b6")
comp_label =Label(root, image=scissor_img_comp, bg="#9b59b6")
comp_label.grid(row=1, column=0)
user_label.grid(row=1, column=4)

#scores
player_score = Label(root, text=0,font=100,bg="#9b59b6",fg="white")
comp_score = Label(root, text=0,font=100,bg="#9b59b6",fg="white")
comp_score.grid(row=1,column=1)
player_score.grid(row=1,column=3)

#indicaters
user_indicator =Label(root,font=50,text="USER",bg="#9b59b6",fg="white")
comp_indicator =Label(root,font=50,text="COMPUTER",bg="#9b59b6",fg="white")
user_indicator.grid(row=0,column=3)
comp_indicator.grid(row=0,column=1)

#messages
msg =Label(root, font=50,bg="#9b59b6",fg="white")
msg.grid(row=3,column=2)

#update message
def updateMessage(x):
    msg['text'] = x

#update user score
def updateUserScore():
    score = int(player_score["text"])
    score += 1
    player_score["text"] = str(score)

#update comp score
def updateCompScore():
    score = int(comp_score["text"])
    score += 1
    comp_score["text"] = str(score)

#chech winner
def checkWin(player,computer):
    if player == computer:
        updateMessage("its a Tie!!")
    elif player == "rock":
        if computer == "paper":
            updateMessage("You loose")
            updateCompScore()
        else:
            updateMessage("You Win!!")
            updateUserScore()
    elif player == "paper":
        if computer == "scissor":
            updateMessage("You loose")
            updateCompScore()
        else:
            updateMessage("You Win!!")
    elif player == "scissor":
        if computer == "rock":
            updateMessage("You loose")
            updateCompScore()
        else:
            updateMessage("You Win!!")
            updateUserScore()
    else:
        pass


#update choices

choices = ["rock","paper","scissor"]
def updateChoice(x):

#for computer
    comp_choice = choices[randint(0,2)]
    if comp_choice == "rock":
        comp_label.configure(image=rock_img_comp)
    elif comp_choice =="paper":
        comp_label.configure(image=paper_img_comp)
    else:
        comp_label.configure(image=scissor_img_comp)




#for user
    if x=="rock":
        user_label.configure(image=rock_img)
    elif x=="paper":
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scissor_img)

    checkWin(x,comp_choice)

#buttons
rock = Button(root,width=20,height=2,text="ROCK",bg="#FF3E4D",fg="white",command= lambda:updateChoice("rock")).grid(row=2,column=1)
paper = Button(root,width=20,height=2,text="PAPER",bg="#FAD02E",fg="white",command= lambda:updateChoice("paper")).grid(row=2,column=2)
scissor = Button(root,width=20,height=2,text="SCISSOR",bg="#0ABDE3",fg="white",command= lambda:updateChoice("scissor")).grid(row=2,column=3)





root.mainloop()