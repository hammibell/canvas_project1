from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk

root = Tk()
root.geometry("500x500")
root.configure(background = "light blue")
root.title("Canavs Project")

canvas = createCanvas(width = 500, height = 500, highlightbackground = "green")
canvas.pack()

color_label = Label(root, text = "Choose Color")
color_label.place(relx = 0.3, rely = 0.5, anchor = CENTER)

colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "brown", "grey", "black"]

fillcolor = colors

dropdown_colors = ttk.Combobox(root, state = "readonly", values = "fillcolor", width = 5)
dropdown_colors.place(relx = 0.35, rely = 0.5, anchor = CENTER)

startx = Label(root, text = "startx")
startx.place(relx = 0.4, rely = 0.5, anchor = CENTER)

starty = Label(root, text = "starty")
starty.place(relx = 0.45, rely = 0.5, anchor = CENTER)

endx = Label(root, text = "endx")
endx.place(relx = 0.5, rely = 0.5, anchor = CENTER)

endy = Label(root, text = "endy")
endy.place(relx = 0.55, rely = 0.5, anchor = CENTER)

directions = ["startx", "starty", "endx", "endy"]
coordinates_values = directions

coordinate_options = ttk.Combobox(root, state = "readonly", values = "coordinate_values", width = 5)
coordinate_options.place(relx = 0.6, rely = 0.5, anchor = CENTER)

root.mainloop()