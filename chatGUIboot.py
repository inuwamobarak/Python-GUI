import ttkbootstrap as ttk

from pathlib import Path

from ttkbootstrap.icons import Emoji

from ttkbootstrap.constants import *

from tkinter import *

# GUI
root = Tk()
#root = ttk.Window(themename="superhero")

root.title("Chatbot")

BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

# Send function
def send():
	send = "User -> " + e.get()
	txt.insert(END, "\n" + send)

	user = e.get().lower()

	if (user == "hello"):
		txt.insert(END, "\n" + "Bot -> Hi there, how can I help?")

	elif (user == "hi" or user == "hii" or user == "hiiii"):
		txt.insert(END, "\n" + "Bot -> Hi there, what can I do for you?")

	elif (user == "how are you"):
		txt.insert(END, "\n" + "Bot -> fine! and you")

	elif (user == "fine" or user == "i am good" or user == "i am doing good"):
		txt.insert(END, "\n" + "Bot -> Great! how can I help you.")

	elif (user == "thanks" or user == "thank you" or user == "now its my time"):
		txt.insert(END, "\n" + "Bot -> My pleasure !")

	elif (user == "what do you sell" or user == "what kinds of items are there" or user == "have you something"):
		txt.insert(END, "\n" + "Bot -> We have coffee and tea")

	elif (user == "tell me a joke" or user == "tell me something funny" or user == "crack a funny line"):
		txt.insert(
			END, "\n" + "Bot -> What did the buffalo say when his son left for college? Bison.! ")

	elif (user == "goodbye" or user == "see you later" or user == "see yaa"):
		txt.insert(END, "\n" + "Bot -> Have a nice day!")

	else:
		txt.insert(END, "\n" + "Bot -> Sorry! I didn't understand that")

	e.delete(0, END)


e = ttk.Entry(root, bootstyle="primary", width=65)
e.pack(side=LEFT, padx=1, pady=2)

send = ttk.Button(root, text="Send", bootstyle="primary", command=send)#.grid(row=2, column=1)
send.pack(side=LEFT, padx=1, pady=2)

txt = Text(root, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=60)
txt.pack(side=RIGHT, padx=0, pady=0)

scrollbar = Scrollbar(txt)
scrollbar.place(relheight=1, relx=0.974)

root.mainloop()
