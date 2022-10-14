import tkinter as tk

class Button_Window:
    def __init__(self, title, starttext = "hello", endtext = "world") -> None:
        self.win = tk.Tk()
        self.win.geometry("250x100")
        self.win.title(title)
        self.end_text = endtext
        self.label = tk.Label(self.win, text=starttext)
        self.button = tk.Button(self.win, command=self.button_click, text="this is button")
        self.label.pack()
        self.button.pack()
    def show(self):
        self.win.mainloop()
    def button_click(self):
        self.label.configure(text=self.end_text)

a = Button_Window("Boris")
a.show()
