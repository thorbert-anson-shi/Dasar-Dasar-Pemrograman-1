from tkinter import *

class Timer:
    def __init__(self, master) -> None:
        self.master = master
        master.title("Timer")
        master.geometry("500x500")

        self.time = IntVar()
        self.time = self.ask_time()


    def ask_time(self):
        window = Toplevel(self.master)
        time = IntVar()
        Entry(window, textvariable=time,width=40).grid(row=0,column=1)
        return time

root = Tk()
my_gui = Timer(root)
root.mainloop()