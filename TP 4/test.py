import tkinter as tk


def export_canvas_to_ps(canvas, filename):
    canvas.postscript(file=filename, colormode="color")


root = tk.Tk()

# Create the main canvas
main_canvas = tk.Canvas(root, width=400, height=300, bg="white")
main_canvas.pack()

# Create an embedded canvas inside the main canvas
embedded_canvas = tk.Canvas(main_canvas, width=200, height=150, bg="lightgray")
embedded_canvas.pack()

# Draw something on the embedded canvas
embedded_canvas.create_rectangle(10, 10, 190, 140, fill="blue")

# Run the Tkinter main loop (important for postscript export)
root.update()

# Export the entire canvas (including embedded canvases) to a postscript file
export_canvas_to_ps(main_canvas, "output.ps")

root.mainloop()
