from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
WHITE = "#ffffff"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


# ---------------------------- SELECT Image ------------------------------- #
def add_image():
    global pop
    pop = Toplevel(window)
    pop.title("upload image")
    pop.geometry("150x150")
    pop.config(bg='white')

    computer = Button(pop, text="From computer", command=browse_button)
    computer.grid(column=0, row=0)
    Google = Button(pop, text="From Google Drive")
    Google.grid(column=0, row=1)
    drop_box = Button(pop, text="DropBox")
    drop_box.grid(column=0, row=2)

image=None

def browse_button():
    # Allow user to select a directory and store it in global var
    # called folder_path
    global image
    file_path = filedialog.askopenfilename()

    if file_path:
        image = Image.open(file_path)

        # create the image object, and save it so that it
        # won't get deleted by the garbage collector
        canvas.image_tk = ImageTk.PhotoImage(image)

        # configure the canvas item to use this image
        canvas.itemconfigure(image_id, image=canvas.image_tk)


# ---------------------------- Drag function ------------------------------- #
def move(e):
    global image
    canvas.image_tk = ImageTk.PhotoImage(image)
    image_id = canvas.create_image(e.x, e.y,image=canvas.image_tk)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Water mark app")

window.minsize()
window.config(bg="#000000", pady=10, padx=10)
back = Button(text="<Back")
back.grid(column=0, row=0)
add_images = Button(text="ADD IMAGES", command=add_image)
add_images.grid(column=1, row=0)
clear = Button(text='clear')
add_logo = Button(text="Add Logo")
add_logo.grid(column=2, row=0)
next_step = Button(text="Next Step>")
next_step.grid(column=3, row=0)
water_make_images = Button(text="Water Mark Images")
drag_drop = Label(text="Drag or drop Images")
drag_drop.grid(row=2, column=1, columnspan=2)
select = Button(text="Select Images")
select.grid(row=3, column=1, columnspan=2)

canvas = Canvas(height=500, width=500)
canvas.bind('<B1-Motion>', move)
image_id = canvas.create_image(0, 0, anchor="nw")
canvas.grid(row=4, column=1)

# canvas = Canvas(width=500, height=300, bg=WHITE, highlightthickness=0)
#
# timer_text = canvas.create_text(10, 10, text="00:00", fill="black", font=(FONT_NAME, 35, "bold"))
# canvas.grid(column=0, row=0)

window.mainloop()
