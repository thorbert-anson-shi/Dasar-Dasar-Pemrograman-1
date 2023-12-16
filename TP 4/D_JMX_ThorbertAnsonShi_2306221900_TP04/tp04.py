from tkinter import Tk, Canvas, Label, Entry, StringVar
from tkinter import messagebox


class BarcodeGenerator:
    # Determines the order of the first 6 digits following first digit
    GROUPING = {
        0: "LLLLLL",
        1: "LLGLGG",
        2: "LLGGLG",
        3: "LLGGGL",
        4: "LGLLGG",
        5: "LGGLLG",
        6: "LGGGLL",
        7: "LGLGLG",
        8: "LGLGGL",
        9: "LGGLGL",
    }

    # By knowing the L-code, we also know the G and R codes
    l_enc = {
        0: "0001101",
        1: "0011001",
        2: "0010011",
        3: "0111101",
        4: "0100011",
        5: "0110001",
        6: "0101111",
        7: "0111011",
        8: "0110111",
        9: "0001011",
    }

    r_enc = {}
    g_enc = {}

    # Fill the r_enc and g_enc dicts based on content of l_enc
    for item in l_enc.items():
        # r_enc is 1s complement of l_enc
        r_enc[item[0]] = "".join("10"[int(i)] for i in item[1])
        # g_enc is reverse of r_enc
        g_enc[item[0]] = r_enc[item[0]][::-1]

    # Initialize static properties of the program GUI
    def __init__(self, master: Tk) -> None:
        self.master = master
        self.font = ("Lucida Sans", 14, "bold")

        master.geometry("800x800")
        master.title("EAN-13 Barcode Generator")
        master.resizable(0, 0)
        master.bind("<Return>", self.enter)

        # Create interface for user input
        self.user_interaction()

    def user_interaction(self):
        """
        Method to get user input and initialize canvas.
        Used to encapsulate GUI creation process
        """
        save_label = Label(
            self.master,
            text="Save barcode to PS file [eg: EAN13.eps]",
            font=self.font,
        )
        save_label.pack()

        self.save_to = StringVar()
        save_entry = Entry(self.master, textvariable=self.save_to, font=self.font)
        save_entry.pack()

        save_label = Label(
            self.master, text="Enter code (first 12 decimal digits)", font=self.font
        )
        save_label.pack()

        self.entered_code = StringVar()
        code_entry = Entry(
            self.master,
            textvariable=self.entered_code,
            width=20,
            font=self.font,
        )
        code_entry.pack()

        # Create canvas to be exported
        # Not the canvas being used for drawing
        self.canvas = Canvas(
            self.master,
            height=450,
            width=450,
            bg="#ffffff",
            relief="groove",
            bd=4,
        )
        self.canvas.pack(padx=10, pady=10)

    # Retrieve Entry contents on enter key press
    def enter(self, event):
        self.file_name = self.save_to.get()
        self.code = self.entered_code.get()

        self.generate_barcode()

    def validate_code(self):
        """
        Make sure user input for barcode is valid.
        Success returns 1, failure returns 0
        """
        # Create new variable for ease of reading
        raw_code = self.code

        if not raw_code.isdigit():
            messagebox.showerror("Invalid Code", "EAN-13 Code must be numeric")
            return 0
        elif len(raw_code) != 12:
            messagebox.showerror("Invalid Code", "Input first 12 digits of EAN-13 Code")
            return 0

        # Used for checksum calculation
        weights = [1, 3] * 6

        # Multiply each code number with its respective weight, then sum everything up
        my_sum = sum([int(num) * weight for num, weight in zip(raw_code, weights)])

        checksum = my_sum % 10
        self.checkdigit = 10 - checksum if checksum > 0 else 0

        # Barcode includes checkdigit at very end of string
        self.processed_code = raw_code + str(self.checkdigit)

        return 1

    def validate_file(self):
        file_name = self.file_name

        if file_name == "":
            return 0

        # Make sure file name is of a valid extension
        if not file_name.endswith((".eps", ".epsf", ".epsi", ".ps")):
            messagebox.showerror(
                "File format not supported",
                "File name should end in .eps, .epsf, or .epsi",
            )
            return 0

        # Make sure file name only has one period
        if file_name.count(".") > 1:
            messagebox.showerror(
                "File name invalid", "File should only have one extension"
            )
            return 0

        return 1

    def generate_barcode(self):
        """
        Draws barcode based on input provided by self.user_interaction(),
        then exports it to the user-specified file name
        """
        if not self.validate_code():
            return 0

        if not self.validate_file():
            return 0

        # Allow for relative window sizing (not resizable)
        frame_height = self.canvas.winfo_height()
        frame_width = self.canvas.winfo_width()

        # Create subcanvas inside canvas with width and height based on main canvas
        main_canvas = Canvas(
            self.master,
            width=frame_width * 9 / 10,
            height=frame_height * 9 / 10,
            background="#ffffff",
            highlightthickness=5,
        )

        # Embed subcanvas into main canvas
        self.canvas.create_window(
            frame_width / 2, frame_height / 2, anchor="center", window=main_canvas
        )

        # For some reason doesn't work without update_idletasks()
        main_canvas.update_idletasks()

        canvas_height = main_canvas.winfo_height()
        canvas_width = main_canvas.winfo_width()

        # Create heading text in canvas
        main_canvas.create_text(
            canvas_width / 2,
            canvas_height / 5,
            anchor="s",
            justify="center",
            text="EAN-13 Barcode",
            font=self.font,
        )

        # Determines which L-G group is used based on first digit
        first_digit = int(self.processed_code[0])
        l_g_group = self.GROUPING[first_digit]

        # Find appropriate line width and height based on canvas size
        line_height = canvas_height / 4
        line_width = canvas_width / 150

        # Arbitrary positioning of barcode
        x_start = (canvas_width - 95 * line_width) / 2
        y_start = canvas_height / 3

        # Create sub-subcanvas to print the first digit
        main_canvas.create_window(
            x_start - 7 * line_width,
            y_start,
            window=InnerCanvas(main_canvas, line_height, line_width * 7, first_digit),
            anchor="nw",
        )

        # Create guard bars slightly taller than other lines
        guard_bar1 = InnerCanvas(main_canvas, line_height + 10, line_width * 3)
        main_canvas.create_window(x_start, y_start, window=guard_bar1, anchor="nw")
        guard_bar1.draw_line(line_width / 2, 0, line_width)
        guard_bar1.skip_line(line_width * (3 / 2), 0, line_width)
        guard_bar1.draw_line(line_width * (5 / 2), 0, line_width)

        # For each number in the code string, determine the corresponding l or g encoding
        for idx, l_g, num in zip(range(6), l_g_group, self.processed_code[1:7]):
            # Create InnerCanvas of width 7 to make room for 7 bits in binary pattern
            inner_canvas = InnerCanvas(main_canvas, line_height, line_width * 7, num)
            main_canvas.create_window(
                (x_start + idx * (line_width * 7)) + 3.5 * line_width,
                y_start,
                anchor="nw",
                window=inner_canvas,
            )
            num = int(num)
            # Draw binary pattern per number
            if l_g == "L":
                bin_str = self.l_enc[num]
                for pos, bit in enumerate(bin_str):
                    if bit == "1":
                        inner_canvas.draw_line(pos * line_width, 0, line_width)
                    else:
                        inner_canvas.skip_line(pos * line_width, 0, line_width)
            else:
                bin_str = self.g_enc[num]
                for pos, bit in enumerate(bin_str):
                    if bit == "1":
                        inner_canvas.draw_line(pos * line_width, 0, line_width)
                    else:
                        inner_canvas.skip_line(pos * line_width, 0, line_width)

        # Create guard bars slightly taller than other lines
        guard_bar2 = InnerCanvas(main_canvas, line_height + 10, line_width * 5)
        main_canvas.create_window(
            x_start + 46 * line_width,
            y_start,
            window=guard_bar2,
            anchor="nw",
        )
        guard_bar2.skip_line(line_width / 2, 0, line_width)
        guard_bar2.draw_line(line_width * (3 / 2), 0, line_width)
        guard_bar2.skip_line(line_width * (5 / 2), 0, line_width)
        guard_bar2.draw_line(line_width * (7 / 2), 0, line_width)
        guard_bar2.skip_line(line_width * (9 / 2), 0, line_width)

        # Create barcode for second half of code with R encoding
        for idx, num in zip(range(6), self.processed_code[7:]):
            inner_canvas = InnerCanvas(main_canvas, line_height, line_width * 7, num)
            main_canvas.create_window(
                (x_start + idx * (line_width * 7)) + 51 * line_width,
                y_start,
                anchor="nw",
                window=inner_canvas,
            )
            num = int(num)
            bin_str = self.r_enc[num]
            for pos, bit in enumerate(bin_str):
                if bit == "1":
                    inner_canvas.draw_line((pos + 1) * line_width, 0, line_width)
                else:
                    inner_canvas.skip_line((pos + 1) * line_width, 0, line_width)

        # Create guard bars slightly taller than other lines
        guard_bar3 = InnerCanvas(main_canvas, line_height + 10, line_width * 3)
        main_canvas.create_window(
            x_start + 93 * line_width,
            y_start,
            window=guard_bar3,
            anchor="nw",
        )
        guard_bar3.draw_line(line_width / 2, 0, line_width)
        guard_bar3.skip_line(line_width * (3 / 2), 0, line_width)
        guard_bar3.draw_line(line_width * (5 / 2), 0, line_width)

        # Test for check digit
        main_canvas.create_text(
            canvas_width / 2,
            canvas_height * (2 / 3),
            text=f"Check digit: {self.checkdigit}",
            font=self.font,
        )

        # Prepare canvas for exporting
        self.canvas.update_idletasks()

        # Export canvas
        self.canvas.postscript(file=self.file_name, colormode="color")


class InnerCanvas(Canvas):
    """
    Subclass of Canvas for drawing of each digit's bars, along with
    the number itself
    """

    def __init__(self, master, height, width, num=None):
        super().__init__(
            master,
            highlightthickness=0,
            borderwidth=0,
            height=height * 11 / 10,
            width=width,
            background="white",
        )
        self.canvas_height = height
        self.canvas_width = width
        self.create_text(
            self.canvas_width / 2,
            self.canvas_height,
            text=num,
            font=("Arial Black", 12, "normal"),
        )

    # Make line slightly shorter than height to accommodate number
    def draw_line(self, x, y, width):
        """Create a line at the coordinates (x,y)"""
        self.create_line(
            x,
            y,
            x,
            self.canvas_height * (9 / 10),
            width=width,
            fill="black",
        )

    def skip_line(self, x, y, width):
        """Skips a line at the coordinates (x,y)"""
        self.create_line(
            x,
            y,
            x,
            self.canvas_height * (9 / 10),
            width=width,
            fill="white",
        )


def main():
    root = Tk()
    my_gui = BarcodeGenerator(root)
    root.mainloop()


if __name__ == "__main__":
    main()
