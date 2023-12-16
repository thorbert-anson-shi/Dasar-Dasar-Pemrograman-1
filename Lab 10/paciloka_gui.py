from tkinter import *
from tkinter import messagebox


# Create a GUI class inherited from tk.Tk()
class MyGUI(Tk):
    def __init__(self, master: Tk) -> None:
        # Dictionary of hotels and their information
        self.hotels_dict = {
            "hotel1": [10, 250000, "kode_hotel_1"],
            "hotel2": [12, 500000, "kode_hotel_2"],
            "hotel3": [10, 7500000, "kode_hotel_3"],
            "hotel4": [1, 1000000, "kode_hotel_4"],
            "hotel5": [10, 900000, "kode_hotel_5"],
            "hotel6": [10, 6000000, "kode_hotel_6"],
        }
        self.master = master

        # Lack of master.geometry() allows window to dynamically resize based on size of hotels_dict

        # Initialize program window
        master.title("This my title")
        master.configure(bg="lightblue")

        # Prevent the window from being resizable
        master.resizable(0, 0)
        master.config(padx=30, pady=30)

        # Call homepage method to create GUI
        self.homepage()

    def homepage(self):
        """
        Creates a frame of subframes which contain the information on each hotel,
        then creates another frame for user input
        """
        self.hotel_frame = Frame(
            self.master,
            highlightbackground="black",
            highlightthickness=2,
            bg="lightgreen",
            pady=10,
        )
        # The lack of self.obj.pack_propagate(0) allows the frame to fit to the size
        # of the objects within said frame.
        self.hotel_frame.pack(anchor="n")  # Anchor object to top-middle

        # Create a frame for each hotel in hotels_dict
        for hotel in self.hotels_dict:
            # Create a temporary frame to add to the superframe
            temp_frame = Frame(
                self.hotel_frame,
                highlightbackground="black",
                highlightthickness=1,
            )

            # For each detail about the hotel, add it to the temporary frame
            hotel_name = Label(temp_frame, text=f"Nama hotel\t: {hotel}")
            hotel_name.grid(row=0, sticky="w")

            hotel_rprice = Label(
                temp_frame, text=f"Harga per kamar\t: {self.hotels_dict[hotel][1]}"
            )
            hotel_rprice.grid(row=1, sticky="w")

            hotel_avail_rooms = Label(
                temp_frame, text=f"Kamar tersedia\t: {self.hotels_dict[hotel][0]}"
            )
            hotel_avail_rooms.grid(row=2, sticky="w")

            # After all the data has been loaded, pack the temp_frame to the superframe
            temp_frame.pack(side=TOP, anchor="center", padx=10, pady=5)

        # Frame for user input
        self.input_frame = Frame(
            self.master,
            highlightbackground="black",
            highlightthickness=2,
            bg="#bfe7ff",
            padx=44,
            pady=20,
        )
        self.input_frame.pack()

        # Create user input fields and their respective labels
        self.uname_tag = Label(self.input_frame, text="Nama pengguna:", bg="#bfe7ff")
        self.uname_tag.pack()

        self.user_name = StringVar()
        self.uname_field = Entry(self.input_frame, textvariable=self.user_name)
        self.uname_field.pack()

        self.hname_tag = Label(self.input_frame, text="Nama hotel:", bg="#bfe7ff")
        self.hname_tag.pack()

        self.hotel_name = StringVar()
        self.hname_field = Entry(self.input_frame, textvariable=self.hotel_name)
        self.hname_field.pack(expand=True)

        self.room_tag = Label(self.input_frame, text="Banyak kamar:", bg="#bfe7ff")
        self.room_tag.pack()

        self.room_amt = IntVar()
        self.amt_field = Entry(self.input_frame, textvariable=self.room_amt)
        self.amt_field.pack()

        # Submit button runs self.booking()
        self.submit_button = Button(
            self.input_frame, text="Submit reservation", command=self.booking
        )
        self.submit_button.pack()

        # Runs sys.exit() on press of exit button
        self.exit_button = Button(self.input_frame, text="Exit", command=exit)
        self.exit_button.pack()

    def booking(self):
        """
        Does all the input validation and modifies data in the hotels_dict
        appropriately
        """
        # Retrieve all the data provided from the Entry() objects
        uname = self.user_name.get()
        hname = self.hotel_name.get()
        try:
            room_amt = self.room_amt.get()
        # TKinter throws a TclError when the input provided can't be converted into their respective types
        except TclError:
            messagebox.showwarning(
                "Invalid input", "Input banyak kamar harus berupa bilangan bulat!"
            )
            return

        # Check if hotel name is in the hotels_dict
        if hname not in self.hotels_dict:
            messagebox.showwarning(
                "Hotel not found", f"Hotel dengan nama {hname} tidak ditemukan!"
            )
            return

        # Do not let user book fewer than 1 hotel room
        if room_amt <= 0:
            messagebox.showwarning(
                "Invalid room amount",
                "Banyak kamar yang di-booking tidak boleh lebih kecil dari 1!",
            )
            return

        # Do not let user overbook rooms in hotel
        avail_rooms = self.hotels_dict[hname][0]
        if room_amt > avail_rooms:
            messagebox.showwarning(
                "Insufficient rooms",
                f"Hotel {hname} hanya memiliki {avail_rooms} kamar tersisa!",
            )
            return

        # Decrement number of available rooms if all conditions are met
        self.hotels_dict[hname][0] -= room_amt
        rprice = self.hotels_dict[hname][1]
        total_cost = room_amt * rprice
        messagebox.showinfo(
            "Booking successful!",
            f"Booking berhasil! Pesanan untuk {uname} di hotel {hname} sebanyak {room_amt} kamar!\nTotal biaya: {total_cost}\nNomor tiket: {self.hotels_dict[hname][-1]}/{self.hotels_dict[hname][0]}/{uname[:3]}",
        )
        # Destroy the hotel and input frames so we can rewrite them on a clean empty frame
        self.hotel_frame.destroy()
        self.input_frame.destroy()

        self.homepage()


def main():
    root = Tk()
    my_gui = MyGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
