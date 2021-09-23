from tkinter import * 
from tkinter import Canvas, Frame, Label, filedialog, Text
from typing import overload 

root = Tk()
apps = []

root.resizable(False, False)

#choosing files function
def file():
    filename = filedialog.askopenfilename(initialdir="../Downloads/", title="Select File", 
    filetypes=(("Images","*.jpg png jpeg raw svg heic docx"), ("All Files", "*.*")))

    apps.append(filename)
    print(filename)

    for app in apps:
        fileLabel = Label(frame, text=app, bg="#6495ed",fg="#fff",padx=80, pady=5,)
        fileLabel.place(relx=0.01, rely=.25)

#choosing file destination to save
def saveFiles():
    savename = filedialog.askopenfilename(initialdir="../Downloads/", title="Select File", 
    filetypes=(("Select Folder","*.*"), ("All Files", "*.*")))


# main-ground-frame
canvas = Canvas(root, width=500,height=250, bg="#87ceeb").pack()

frame = Frame(root, bg="#87ceeb", height=435, width=455)
frame.place(relx=0.05, rely=0.1)

title = Label(root, bg="#0892d0",fg="#fff", text="PDF Converter", padx=200)
title.place(relx=0.007, rely=0.007)


#foreground-frame
header = Label(frame, text="Change your Images & Word.docx to PDF",font=("Arial", 20), bg="#87ceeb", fg="#1c2841")
header.place(relx=.08, rely=.05)

chooseFile = Button(frame, text="Choose File", padx=70, pady=5, command=file)
chooseFile.place(relx=.01, rely=.15)

fileLabel = Label(frame, text="/example/path/files", bg="#6495ed",fg="#fff",padx=162, pady=5)
fileLabel.place(relx=0.01, rely=.25)

savePath = Button(frame, text="Choose Destination to Save", padx=25, pady=5, command=saveFiles)
savePath.place(relx=.5, rely=.15)

convert = Button(frame, text="Convert", padx=197, pady=5)
convert.place(relx=.01, rely=.35)









root.mainloop()