from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import os, sys, subprocess
from typing import Sized
from PIL import ImageTk, Image
import fnmatch
import img2pdf
import PyPDF2
from fpdf import FPDF

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
    filetypes=(("Available Files","*.jpg png jpeg raw svg heic docx txt"), ("All Files", "*.*")))

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

#files to pdf
def filetopdf():
    if not spath:
        # messagebox.showerror("Note That!", "You must choose path to save a file")
        filedialog.asksaveasfilename
    nn = entry.get()
    global name 
    name = nn
    if(filename.lower().endswith(('.png', '.jpg', '.jpeg', '.svg'))):
        imgtopdf()
    if(filename.lower().endswith('.txt')):
        txtTopdf()
    

#img to pdf function 
def imgtopdf():
        with open(f"{spath}/{name}.pdf","wb") as f:
            print(f"{spath}/{name}")
            f.write(img2pdf.convert(filepath))
        if(name!=""):
            complete()
        else:
            warning()


#text file to pdf 
def txtTopdf(): 
    txtpdf = FPDF()
    txtpdf.add_page()
    file = open(filepath, "rb")
    for text in file:
        if len(text) <= 20:
            txtpdf.setfont("Arial", "B",size=18)
            txtpdf.cell(w=200,h=10,txt=text,ln=1,align="C")
        else:
            txtpdf.setfont("Arial",size=15)
            txtpdf.multi_cell(w=0,h=10,txt=text,align="L")
    txtpdf.output(f"{spath}/{name}.pdf")
    if(name!=""):
        complete()


#alert messages 
def complete():
    messagebox.showinfo("ALl Set","Congrats! Your PDF is ready")
def warning():
    messagebox.showwarning("All Set!","Your PDF was saved without a name!")

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
                        command=filetopdf
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

