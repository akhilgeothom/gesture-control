from tkinter import *
from PIL import Image, ImageTk

root = Tk()

def Click():

    image = Image.open("gifs/1.gif")
    photo = ImageTk.PhotoImage(image)

    label = Label(root,image=photo)
    label.image = photo # keep a reference!
    label.pack()



image = Image.open("gifs/2.gif")
photo = ImageTk.PhotoImage(image)
label = Label(root,image=photo)

label.image = photo # keep a reference!
label.pack()


labelframe = LabelFrame(root)
labelframe.pack(fill="both", expand="yes")


left = Label(labelframe)

button=Button(labelframe, padx = 5, pady = 5, text="Next",command = Click)
button.pack(side = RIGHT)


R1 = Radiobutton(labelframe, text="Choice 1", value=1)
R1.pack(side = LEFT)

R2 = Radiobutton(labelframe, text="Choice 2",  value=2)
R2.pack(side = LEFT)


left.pack()
root.mainloop()