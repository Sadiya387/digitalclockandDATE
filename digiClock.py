from tkinter import *
import time

def times():
    current_time = time.strftime("%d-%m-%y|%a:%I:%M:%S:%p ")
    clock_lbl=Label(root, font = 'berlin 50 ',bg="black",fg='light green',text= current_time)

    clock_lbl.after(200,times)
    clock_lbl.grid(column=5, row=200)


root = Tk()


root.title("Date & Digital clock")
root.resizable(False,False)
times()

root.mainloop()

