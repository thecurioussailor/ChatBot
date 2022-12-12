from tkinter import *

# GUI
root = Tk()
root.title("Chatbot")
BG_GRAY = "#ABB2B9"
BG_COLOR = "#8B063B"
TEXT_COLOR = "#EAECEE"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

# Send function
def send():
	send = "You -> " + e.get()
	txt.insert(END, "\n" + send)

	user = e.get().lower()

	if (user == "hello"):
		txt.insert(END, "\n" + "Bot -> Hi there, how can I help?")

	elif (user == "hi" or user == "hii" or user == "hiiii"):
		txt.insert(END, "\n" + "Bot -> Hi there, what can I do for you?")

	elif (user == "how are you"):
		txt.insert(END, "\n" + "Bot -> fine! and what about you")

	elif (user == "fine" or user == "i am good" or user == "i am doing good"):
		txt.insert(END, "\n" + "Bot -> Great! how can I help you.")

	elif (user == "thanks" or user == "thank you" or user == "now its my time"):
		txt.insert(END, "\n" + "Bot -> My pleasure !")

	elif (user == "what do you sell" or user == "what kinds of items are there" or user == "have you something"):
		txt.insert(END, "\n" + "Bot -> We have coffee and tea")

	elif (user == "what is your name" or user == "who are you" or user == "tell me about yourself"):
		txt.insert(END, "\n" + "Bot -> I am a bot. My name is Potter. Nice to meet you!")

	elif (user == "what are your soft skills" or user == "what is your strength"):
		txt.insert(END, "\n" + "Bot -> patience,communication,positive Thinking,creative Thinkng")	

	elif (user == "tell me a joke" or user == "tell me something funny" or user == "crack a funny line"):
		txt.insert(END, "\n" + "Bot -> What did the buffalo say when his son left for college? Bison.! ")

	elif (user == "goodbye" or user == "see you later" or user == "see yaa"):
		txt.insert(END, "\n" + "Bot -> Have a nice day!")

	elif (user == "how do you feel" or user == "what do you feel"):
		txt.insert(END, "\n" + "Bot -> It's cold outside but I don't feel anything cause I am a bot.	")


	else:
		txt.insert(END, "\n" + "Bot -> Sorry! I didn't understand that")

	e.delete(0, END)


lable1 = Label(root, bg=BG_COLOR, fg=TEXT_COLOR, text="Potter Bot", font=FONT_BOLD, pady=10, width=20, height=1).grid(
	row=0)

txt = Text(root, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=70)
txt.grid(row=1, column=0, columnspan=2)

scrollbar = Scrollbar(txt)
scrollbar.place(relheight=1, relx=0.974)

e = Entry(root, bg=BG_COLOR, fg=TEXT_COLOR , font=FONT, width=60)
e.grid(row=2, column=0)

send = Button(root, text="Send", font=FONT_BOLD, bg=BG_GRAY,width=12,height=1,
			command=send).grid(row=2, column=1)

root.mainloop()
