import speech_recognition as sr
from tkinter import *


def get():
    r = sr.Recognizer()
    with sr.Microphone() as s:
        print("Say something...")
        audio = r.listen(s)
        print("Done")
        try:
            speech = r.recognize_google(audio, language='en-IN')
            print("you said: " + speech)
            label_1 = Label(root, text=speech, fg='blue')
            label_1.pack()


        except Exception as e:
           label_2 = Label(root, text="Error", fg='red')
           label_2.pack()



root = Tk()

root.title("Speech Recognizer")
root.geometry('500x300')

b_1 = Button(root, text="Speak", command=get)
b_1.pack()
b_2 = Button(root, text="Exit", command=b_1.quit)
b_2.pack()

root.mainloop()


