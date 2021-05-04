from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk
from tkinter.filedialog import askopenfilenames
from PIL import Image, ImageTk
from threading import Thread

def resize():
    global image, photo
    while True:
        if photo.size[0] > 790 or photo.size[1] > 500:
            photo = photo.resize((round(photo.size[0] * 0.9),
                                  round(photo.size[1] * 0.9)))
        if photo.size[0] <= 790 and photo.size[1] <= 500:
            break

def set_image():
    global image, photo
    lblImage['image'] = ''
    lblText['text'] = ''
    try:
        photo = Image.open(paths[img_no])
        resize()
        image = ImageTk.PhotoImage(photo)
        lblImage['image'] = image
        lblText['text'] = paths[img_no].split('/')[-1]
    except IndexError:
        pass
    except:
        lblText['text'] = 'File not supported'

def thread1():
    Thread(target=select_image).start()

def thread2():
    Thread(target=clear).start()

def thread3():
    Thread(target=prev_image).start()

def thread4():
    Thread(target=next_image).start()

def select_image():
    temp_paths = askopenfilenames(initialdir='./', title='Select files',
                                  filetypes=(('All files', ('*.jpg', '*.jpeg', '*.png', '*.ico')), ))

    for i in range(len(temp_paths)):
        paths.append(temp_paths[i])

    set_image()

def clear():
    global img_no
    paths.clear()
    lblText['text'] = 'Add photos to browse'
    lblImage['image'] = ''
    img_no = 0

def prev_image():
    global img_no
    try:
        if len(paths) != 0 and img_no > 0:
            img_no -= 1
            set_image()
    except:
        pass

def next_image():
    global img_no
    try:
        if len(paths) != 0 and img_no < len(paths)-1:
            img_no += 1
            set_image()
    except:
        pass

root = ThemedTk(theme='arc')
root.title('Photos')
root.geometry('800x600+230+30')
root.minsize(800, 600)
root.iconbitmap('./res/icon.ico')
root.config(bg='white')

# Variables
img_no = 0
paths = []

# Frames
photo_frame = LabelFrame(root, borderwidth=10, bg='white')
photo_frame.pack(expand=True, fill='both')

btn_frame = Frame(root, bg='white')
btn_frame.pack(side=BOTTOM, pady=10)

# Label for image
lblText = Label(photo_frame, text='Add photos to browse', bg='white', font=('arial', 10, 'bold'))
lblText.pack()

lblImage = Label(photo_frame, bg='white')
lblImage.pack(expand=True, fill='both')

btnAdd = ttk.Button(btn_frame, text='Add', width=10, command=thread1)
btnAdd.grid(row=0, column=0, padx=5)

btnClear = ttk.Button(btn_frame, text='Clear', width=10, command=thread2)
btnClear.grid(row=0, column=1, padx=5)

btnBack = ttk.Button(btn_frame, text='Back', width=10, command=thread3)
btnBack.grid(row=0, column=2, padx=5)

btnNext = ttk.Button(btn_frame, text='Next', width=10, command=thread4)
btnNext.grid(row=0, column=3, padx=5)

root.mainloop()
