#from ImageRecog import ImageRecognition
import tkinter as tk


class Button_Window:
    def __init__(self, title, starttext = "hello", endtext = "world") -> None:
        #self.model = ImageRecognition()
        self.win = tk.Tk()
        self.win.geometry("500x500")
        self.win.title(title)
        self.end_text = endtext
        self.label = tk.Label(self.win, text=starttext)
        self.button = tk.Button(self.win, command=self.button_click, text="this is button")
        self.drawing = tk.Canvas(self.win, height=280, width=280, background="white")
        self.drawing.bind('<B1-Motion>', self.draw_line)
        self.label.pack()
        self.button.pack()
        self.drawing.pack()
    def show(self):
        self.win.mainloop()
    def button_click(self):
        pass
        
    def draw_line(self, event):
        x1, y1, x2, y2 = ( event.x - 3 ),( event.y - 3 ), ( event.x + 3 ),( event.y + 3 )
        self.drawing.create_line(x1,y1,x2,y2,fill="black")

    
a = Button_Window("Boris")
a.show()
