from tkinter import *

class TempConverter:
    def __init__(self, master) -> None:
        self.master = master
        master.title("Temperature Converter")
        master.geometry("300x30")

        self.temperature = StringVar()
        self.temperature.set("0")

        self.temp_field = Entry(master, textvariable=self.temperature, width=20)
        self.temp_field.grid(row=0, column=0, padx=5, pady=5)
        self.temp_label = Label(master, text="°C",width=2).grid(row=0, column=1)

        self.convert_button = Button(master, text="->", command=self.convert)
        self.convert_button.grid(row=0, column=2, padx=5, pady=5)

        self.outie = Label(master, text=self.temperature.get())
        self.outie.grid(row=0, column=3, padx=5, pady=5)
        self.outie_label = Label(master, text="°F").grid(row=0, column=4)

    def convert(self):
        celsius = (float(self.temperature.get()) - 32) * 5 / 9
        self.outie['text'] = f"{celsius:.2f}"

root = Tk()
my_gui = TempConverter(root)
root.mainloop()