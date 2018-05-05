from tkinter import *
from ReLeniter import relenite


class Application(Frame):
    """The GUI Application"""

    def __init__(self, master):
        """Initialises the frame"""
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """Creates Widgets for Buttons and Text Input and Output"""
        self.instruction = Label(self, text = "Enter Text Here:")
        self.instruction.grid(row=0, column=0, columnspan=2, sticky=W)

        self.intext = Text(self, width=149, height=15, wrap=WORD)
        self.intext.grid(row=1, column=0, columnspan=2, sticky=W)

        self.runapp = Button(self, text = "ReLenite", command=self.reveal)
        self.runapp.grid(row=2, column=1, sticky=W)

        self.outtext = Text(self, width=149, height=15, wrap=WORD)
        self.outtext.grid(row=3, column=0, columnspan=2, sticky=W)

    def reveal(self):
        """Display output text."""
        content = self.intext.get(1.0, END)
        output = relenite(content)
        self.outtext.delete(1.0, END)
        self.outtext.insert(0.0, output)


app = Tk()
app.title("ReLeniter")
app.geometry('1200x600')
appli = Application(app)

app.mainloop()