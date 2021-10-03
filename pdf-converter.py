from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import os, sys, subprocess
from PIL import ImageTk, Image
import fnmatch
import img2pdf
import PyPDF2


window = Tk()
window.resizable(False, False)
window.geometry("600x400")
window.title("PDF Converter")
window.config(background="#6495ed")
# pop.resizable(False, False)

paths = []
files = []

#file chosing function 
def chooseFile():
    global filepath 
    filepath = filedialog.askopenfilename(initialdir="../", title="Select File :", 
    filetypes=(("Available Files","*.jpg png jpeg raw svg heic docx"), ("All Files", "*.*")))

    files.append(filepath)
    global filename
    filename = os.path.basename(filepath)

    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.svg')):
        global imglogo
        imglogo = PhotoImage(file="media/image1.png")
        for file in files:
            selectedfile = Label(canvas,
                                text=filename,
                                bg="#fff",
                                fg="#828282",
                                image=imglogo,
                                compound=TOP , 
                                pady=5     
                            )
            selectedfile.place(relx=0.38,
                            rely=0.1,
                            width=350,
                            height=130,
                            )
    else: 
        global filelogo
        filelogo = PhotoImage(file="media/file.png")
        for file in files: 
            selectedfile = Label(canvas,
                                text=filename,
                                bg="#fff",
                                fg="#828282",
                                image=filelogo,
                                compound=TOP       
                            )
            selectedfile.place(relx=0.38,
                            rely=0.1,
                            width=350,
                            height=130,
                            )
#save pdf name as 
               
#save to path function
def savePath():
    global spath
    spath = filedialog.askdirectory()

    paths.append(spath)
    # print(spath)

    for path in paths:
        destination = Label(canvas, 
                                text="Save to : " + spath, 
                                bg="#2f4a7c", 
                                fg="#fff", 
                                padx=6.5,
                                image=saveTo,
                                compound=LEFT
                            )
        destination.place(rely=0.85, relx=0.01)

#img to pdf function 

def imgtopdf():
    nn = entry.get()
    # print(filepath)
    with open(f"{spath}/{nn}.pdf","wb") as f:
        print(f"{spath}/{nn}")
        f.write(img2pdf.convert(filepath))

#foregrounds frames 
logo = PhotoImage(file="media/logo1.png")

#header and logo
header = Label(window,
                    text="Convert Your Files To .PDF",
                    fg="#111111" ,font=("Arial", 20, 'bold'),
                    bg="#6495ed",
                    pady=5,
                    image=logo,
                    compound=TOP,
                    )
header.place(relx=0.27, rely=0.05)

#second frame
canvas = Canvas(window,
                    width=580, 
                    height=230, 
                    bg="#2f4a7c"
                    )
canvas.place(rely=0.35, relx=0.01)

#buttons
chooseFile = Button(canvas, 
                        text="Choose File",
                        bg='white', fg='black',
                        padx=50,
                        pady=5,
                        command=chooseFile
                        )
chooseFile.place(relx=0.025, rely=0.1)

saveTo = PhotoImage(file="media/saveto.png")
savePath = Button(canvas, 
                        text="Save Destination",
                        bg='white', fg='black',
                        padx=35,
                        pady=5,
                        command=savePath,
                        )
savePath.place(relx=0.025, rely=0.3)

convert = Button(canvas, 
                        text="Convert",
                        bg='white', fg='black',
                        padx=62,
                        pady=5,
                        command=imgtopdf
                        )
convert.place(relx=0.025, rely=0.5)

#Labels 
global preview
preview = Label(canvas,
                        text="Drag and Drop your files",
                        bg="#fff",
                        fg="#828282",       
                )
preview.place(relx=0.38,
                rely=0.1,
                width=350,
                height=130,
                )
newfileas = Label(canvas, 
                    text="Save File As : ", 
                    bg="#2f4a7c",
                    fg="#fff"
                    )
newfileas.place(relx=0.38, rely=0.7)

global entry
entry = Entry(width=20, background="#3a4c77", fg="#fff",border=None)
entry.place(relx=0.55, rely=0.75)


browse = Label(canvas, 
                    text="Save to : ", 
                    bg="#2f4a7c", 
                    fg="#fff", 
                    padx=5,
                    image=saveTo,
                    compound=LEFT
            )
browse.place(rely=0.85, relx=0.01)

window.mainloop()

