import pyscreenshot
import tkinter as tk


def TakeScreenShot():
    pyscreenshot.grab().save('Current-window.png')

root = tk.Tk()

canvas = tk.Canvas(root,width=300,height=300)
canvas.pack()

myButton = tk.Button(text='Take Screenshot', command=TakeScreenShot,font=10)
canvas.create_window(150,150,window=myButton) 

tk.mainloop()