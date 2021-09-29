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
    print(filepath)
    filename = os.path.basename(filepath)

    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.svg')):
        print(filename)
        global filelogo
        filelogo = PhotoImage(file="media/image1.png")
        
        global imgpreview 
        imgpreview = Label(canvas,
                                text=filename,
                                bg="#2f4a7c",
                                fg="#fff",
                                image=filelogo,
                                compound=TOP,
                                )
        imgpreview.place(relx=0.60, rely=0.18)
    else:
        filelogo = PhotoImage(file="media/file.png")

    # for file in files:
        global fpreview 
        fpreview = Label(canvas,
                                text=filename,
                                bg="#2f4a7c",
                                fg="#fff",
                                image=filelogo,
                                compound=TOP,
                                )
        fpreview.place(relx=0.56, rely=0.2)

        #delete selected file
    def dfile():
        fpreview.destroy(),imgpreview.destroy()
#save pdf name as 
    def saveAs():
        global pop 
        pop = Toplevel(window)
        pop.title("Save File Name")
        pop.geometry("250x150")
        pop.config(bg="#6495ed")

        fname = Label(pop,
                        text="What do you wanna name your file? ", 
                        bg="#6495ed", fg="#fff"
                        )
        fname.pack()
       
    global delete
    delete = Button(canvas, 
                            text="Delete Selected File",
                            bg="#2f4a7c",
                            fg="#000",
                            command=dfile,
                            padx=20
                        )
    delete.place(relx=0.40, rely=0.75)
    

    global save_as
    save_as = Button(canvas, 
                            text="Drag And Drop",
                            bg="#2f4a7c",
                            fg="#000",
                            padx=30,
                            command=saveAs
                        )
    save_as.place(relx=0.70, rely=0.75)
    
    preview.destroy()

#image to pdf function 

def img2pdf():
    with open(f'{spath}/{dir}.pdf',"wb") as f:
        f.write(img2pdf.convert(filepath))

#save to path function
def savePath():
    global spath
    spath = filedialog.askdirectory()

    paths.append(spath)
    print(spath)

    for path in paths:
        destination = Label(canvas, 
                                text="Save to : " + spath, 
                                bg="#2f4a7c", 
                                fg="#fff", 
                                padx=5,
                                image=saveTo,
                                compound=LEFT
                            )
        destination.place(rely=0.85, relx=0.01)

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
                height=170,
                )
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

