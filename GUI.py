import tkinter
from tkinter import *
import tkinter.messagebox as ms

# making a main window for the GUI
root = tkinter.Tk()
root.title("My GUI")
root.geometry("800x420")

# Making a Toplevel window it doesn't need any main window
# top = Toplevel()
# top.title("My top")
# top.geometry("644x432")

# Functions for assigning commands to the widgets

def buttonCommand():
    msg = 'Hello this is my message to you'
    msgVar = Message(root,text=msg)
    msgVar.config(bg="red",fg="white")
    msgVar.pack(anchor='ne')

def newCommand():
   msg = 'Main window button clicked'
   ms.showinfo("Message info",msg)

def Menu():
   msg = ms.askquestion("Feedback","Are you a boy")
   if msg == "yes":
      ms.showinfo("Info","Ok got it!! you're a boy")
   else:
      ms.showinfo("Info","Ok got it!! you're a girl")

def help():
   ms.showinfo("Help","This is made by purushotam")

def rating_us():
   var = ms.askquestion("Rate us","Did you liked our site?")
   if var == "yes":
      ms.showinfo("Rate us","Thanks for your good feedback")
   else:
      ms.showinfo("Rate us","Thanks for feedback, we will try our best for your service")

# Adding widgets to our main and top window

# Label for adding text on window
label = tkinter.Label(text="Label number 1",fg="red",font="arial 15 italic").pack()

# Button with commands
Button(root, text="Click me...",command=newCommand,activebackground='black',activeforeground="white").pack(anchor='s')

# Button for top window
Button(root,text="Print message",command=buttonCommand,bg="grey",activebackground="black",activeforeground="grey").pack()

# Taking input from user as entry (Used in login pages, signin
# g up)
text = tkinter.Entry(root,textvariable=StringVar).pack(anchor='w',pady=12)   

# Choose options by ticking
box = tkinter.Checkbutton(root,text="Tick this").pack(anchor='w') 

# For choosing one option from multiple options
tkinter.Radiobutton(root,text="Male",value=0).pack(anchor='w')
tkinter.Radiobutton(root,text="Female",value=1).pack(anchor='w') 
tkinter.Radiobutton(root,text="Don't want to tell",value=2).pack(anchor='w')

# Creating scrollbar but ain't working
s_bar = Scrollbar(root)
s_bar.pack(side=RIGHT)
lst = Listbox(root,yscrollcommand=s_bar.set)  #creating a list of items

# Adding items to the list
i = 1
while i != 1000:
    lst.insert(END,'number- '+str(i))
    lst.pack(side=RIGHT,fill=Y)
    i += 1
s_bar.config(command=lst.yview)

# Creating a scale
scale = Scale(root,from_=0,to=50,orient=VERTICAL).pack(side=LEFT)  



#creating menu and submenu
mainmenu = tkinter.Menu(root)
m1 = tkinter.Menu(mainmenu,tearoff=0)
m1.add_command(label="SubMenu1", command=Menu)
m1.add_command(label="SubMenu2", command=Menu)
m1.add_command(label="SubMenu3", command=Menu)
mainmenu.add_cascade(label="Mainmenu",menu=m1)
root.config(menu=mainmenu)

m2 = tkinter.Menu(mainmenu,tearoff=0) 
m2.add_command(label="SubMenu4")
m2.add_command(label="SubMenu5")
m2.add_command(label="SubMenu6")
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Second Menu",menu=m2)

h = tkinter.Menu(mainmenu,tearoff=0)
h.add_command(label="About",command=help)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Help",menu=h)

about = tkinter.Menu(mainmenu,tearoff=0)
about.add_command(label="Rate us",command=rating_us)
mainmenu.add_cascade(label="About",menu=about)
root.config(menu=mainmenu)
about.add_command(label="Exit",command=quit)

root.mainloop()     # Mainloop for making GUI