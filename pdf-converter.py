from tkinter import *
from tkinter import filedialog

window = Tk()
window.resizable(False, False)
window.geometry("600x400")
window.title("PDF Converter")
window.config(background="#6495ed")

paths = []
files = []

#file chosing function 
def chooseFile():
    filename = filedialog.askopenfilename(initialdir="../", title="Select File :", 
    filetypes=(("Available Files","*.jpg png jpeg raw svg heic docx"), ("All Files", "*.*")))

    files.append(filename)
    print(filename)

    for file in files:
        

def savePath():
    # spath = filedialog.askopenfilename(initialdir="../user/", title="Save To :", 
    # path =(("Choose Destination","/"), ("All Files", "/")))

    spath = filedialog.askdirectory()

    paths.append(spath)
    print(spath)

    for path in paths:
        destination = Label(canvas, 
                                text="Save to: " + spath, 
                                bg="#2f4a7c", 
                                fg="#fff", 
                                border=5,
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

savePath = Button(canvas, 
                        text="Save Destination",
                        bg='white', fg='black',
                        padx=35,
                        pady=5,
                        command=savePath
                        )
savePath.place(relx=0.025, rely=0.3)

#Labels 




window.mainloop()

