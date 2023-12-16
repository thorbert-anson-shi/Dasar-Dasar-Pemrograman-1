# from tkinter import *

# class MyGUI:
#     def __init__(self, master) -> None:
#         self.master = master
#         master.geometry("100x250")
#         master.title("Lmao wut")
#         self.label = Label(master, text = "here's some text")
#         self.label.pack()
#         self.greet_button = Button(master, text="Helow")
#         self.greet_button.pack()
#         self.bye_button = Button(master, text="baibai", command=master.destroy)
#         self.bye_button.pack()

# window = Tk()
# myGUI = MyGUI(window)
# window.mainloop()

# from tkinter import *

# class Penghitung:
#     def __init__(self, master):
#         self.master = master
#         master.title("Penghitung")
#         master.geometry("300x100")
#         self.hitungan = 0
#         self.label = Label(master, text=self.hitungan)
#         self.label.pack()
#         self.tambah_button = Button(master, text="Tambah", command=self.tambah, bg="#00FF00")
#         self.tambah_button.pack()
#         self.kurang_button = Button(master, text="Kurang", command=self.kurang, bg="#FF0000")
#         self.kurang_button.pack()
#         self.tambah_10_button = Button(master, text="Tambah 10", command=self.add10, bg="#0000ff")
#         self.tambah_10_button.pack()

#     def tambah(self):
#         self.hitungan += 1
#         self.label["text"] = self.hitungan

#     def kurang(self):
#         self.hitungan -= 1
#         self.label["text"] = self.hitungan

#     def add10(self):
#         self.hitungan += 10
#         self.label["text"] = self.hitungan

# root = Tk()
# penghitung = Penghitung(root)
# root.mainloop()

import tkinter as tk
from tkinter.messagebox import showinfo

class DaftarMhs:
    daftar_mhs = []
    def __init__(self, master) -> None:
        self.master = master
        master.geometry("300x300")
        master.title("Daftar Mahasiswa")

        self.label = tk.Label(master, text="Masukkan nama mahasiswa")
        self.label.pack()
        self.name = tk.StringVar()
        self.field_name = tk.Entry(master, textvariable=self.name, width=100)
        self.field_name.pack()
        self.submit_button = tk.Button(master, command=self.show_list)

    def show_list(self):
        window = tk.Toplevel-[[[[[[[[-[-]]]]]]]]]