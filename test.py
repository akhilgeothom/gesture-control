import image
from PIL import ImageTk,Image
import tkinter

image_list = ['gifs/1.gif', 'gifs/2.gif', 'gifs/3.gif', 'gifs/4.gif', 'gifs/5.gif']
text_list = ['apple', 'bird', 'cat', 'lol', 'rofl']
current = 0

def move(delta):
    global current, image_list
    if not (0 <= current + delta < len(image_list)):
        tkMessageBox.showinfo('End', 'No more image.')
        return
    current += delta

    curImg = Image.open(image_list[current])
    curPhoto = ImageTk.PhotoImage(curImg)
    
    try:
        prevImg = Image.open(image_list[current-1])
        prevPhoto = ImageTk.PhotoImage(prevImg)
    except:
        print("left-most image");
    try:
        nextImg = Image.open(image_list[current+1])
        nextPhoto = ImageTk.PhotoImage(nextImg)
    except:
        print("right-most image");

    label['text'] = text_list[current]
    label['image'] = photo
    label.photo = photo


root = tkinter.Tk()

label = tkinter.Label(root, compound=tkinter.TOP)
label.pack()

frame = tkinter.Frame(root)
frame.pack()

tkinter.Button(frame, text='Previous picture', command=lambda: move(-1)).pack(side=tkinter.LEFT)
tkinter.Button(frame, text='Next picture', command=lambda: move(+1)).pack(side=tkinter.LEFT)
tkinter.Button(frame, text='Quit', command=root.quit).pack(side=tkinter.LEFT)

move(0)

root.mainloop()