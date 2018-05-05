from tkinter import *
from ReLeniter import relenite


"""Function called by Run button. Calls relenite function from ReLeniter to convert input text to relenited output."""
def run_app():
    instring = boxstring.get()
    outstring = Label(app,
                      text=relenite(instring),
                      font=('Times New Roman', 12, 'bold'),
                      anchor=NW,
                      justify='left',
                      width=129,
                      height=1,
                      bd=5,
                      bg='light gray').pack()


"""Intended to clear output text. Currently closes window"""
def clear_all():
    app.destroy()


"""Abandoned button which creates a blank line instead of relenited text."""
# def new_line():
#     outstring = Label(app,
#                       text="",
#                       font=('Times New Roman', 12, 'bold'),
#                       anchor=NW,
#                       justify='left',
#                       width=129,
#                       height=1,
#                       bd=5,
#                       bg='light gray').pack()


"""Sets up the GUI: Titles it, Sets its variable name as app, sizes it."""
app = Tk()
app.title("ReLeniter")
app.geometry('1200x500')

"""Sets the variable name for the input text box."""
boxstring = StringVar()

"""Abandoned attempt to introduce a scroll bar."""
# scroll = Scrollbar(app)
# scroll.pack(side=RIGHT, fill=Y)

"""Creates the Input Text label and box, Run button, Clear button, and Output Text box,"""
inlabel = Label(app,
                text='Input Text Here:',
                font=('Times New Roman', 14, 'bold'),
                anchor=SW,
                justify='left',
                width=106,
                height=2).pack()
inbox = Entry(app,
              textvariable=boxstring,
              font=('Times New Roman', 12),
              justify='left',
              width=145,
              bd=5,
              bg='powder blue').pack()
runbutton = Button(app,
                   text='ReLenite',
                   font=('Times New Roman', 14, 'bold'),
                   command=run_app,
                   height=1,
                   bd=5).pack()
clearbutton = Button(app,
                   text='Clear All',
                   font=('Times New Roman', 14),
                   command=clear_all,
                   height=1,
                   bd=5).pack()

"""Original attempt at a clear button. Instead inserts a blank line."""
# newline = Button(app,
#                    text='New Line',
#                    font=('Times New Roman', 14),
#                    command=new_line,
#                    height=1,
#                    bd=5).pack()

"""Defines outstring variable outside of defined functions. Necessary during testing.
   Inserts blank gray box by default before relenited text content."""
# outstring = Label(app,
#                   text="",
#                   font=('Times New Roman', 12, 'bold'),
#                   anchor=NW,
#                   justify='left',
#                   width=129,
#                   height=1,
#                   bd=5,
#                   bg='light gray').pack()

app.mainloop()
