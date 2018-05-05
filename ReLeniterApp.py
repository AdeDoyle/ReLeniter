from tkinter import *
from ReLeniter import relenite

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

def clear_all():
    app.destroy()

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

app = Tk()
app.title("ReLeniter")
boxstring = StringVar()
app.geometry('1200x500')
# scroll = Scrollbar(app)
# scroll.pack(side=RIGHT, fill=Y)

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
# newline = Button(app,
#                    text='New Line',
#                    font=('Times New Roman', 14),
#                    command=new_line,
#                    height=1,
#                    bd=5).pack()
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
