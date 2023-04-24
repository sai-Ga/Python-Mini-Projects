from tkinter import *
from tkinter import messagebox
from random import randint


root = Tk()
root.title('Password Generator')
root.iconbitmap('key.ico')
root.geometry("500x300")


#Password Generator
def new_rand():
    pw_entry.delete(0, END)
    pw_length = int(my_entry.get())
    my_password=''
    for i in range(pw_length):
        my_password += chr(randint(33,126))
    pw_entry.insert(0, my_password)
    
#Copy to Clipboard 
def clipper():
    root.clipboard_clear()
    root.clipboard_append(pw_entry.get())
    messagebox.showinfo("Success!", "Copied to Clipboard")

#Label Frame
lf = LabelFrame(root,text='How Many Characters')
lf.pack(pady=20)

#Create Entry Box To Designate Number of Characters
my_entry = Entry(lf,font=('Helvetica',24))
my_entry.pack(padx=20,pady=20)

# Create Entry Box For Our Returned Password
pw_entry = Entry(root, text='', font=('Helvetica',24), bd=0, bg='systembuttonface')
pw_entry.pack(pady=20)

#Frame for Buttons
my_frame = Frame(root)
my_frame.pack(pady=20)

#Buttons
my_button = Button(my_frame,text= 'Generate Password', command= new_rand)
my_button.grid(row=0,column=0,padx=10)

clip_button = Button(my_frame, text='Copy to Clipboard',command= clipper)
clip_button.grid(row=0,column=1,padx=10)

root.mainloop()
