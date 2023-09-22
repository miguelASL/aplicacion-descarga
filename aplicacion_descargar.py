from pytube import YouTube
from tkinter import *
from tkinter import messagebox

root = Tk()

def popup():
    messagebox.showinfo("Información sobre la aplicación", "La aplicación que sirve para descargar videos de youtube: pega el enlace en el boton" )
def miguel():
    messagebox.showinfo("Informacion sobre mi","Soy miguel sarmiento")
def accion():
    enlace = videos.get()
    video = YouTube(enlace)
    descarga = video.streams.get_highest_resolution()
    descarga.download()
    
imagen = PhotoImage(file="logo_final.png")
foto = Label(root, image=imagen, bd=0)
foto.grid(row=0, column=0)

menubar = Menu(root)
root.config(menu=menubar)
helpmenu = Menu(menubar, tearoff=0)

menubar.add_cascade(label= "Para mas informacion", menu=helpmenu)
helpmenu.add_command(label ="Instrucciones de uso", command=popup)
helpmenu.add_command(label ="Instruccion sobre el creador", command=miguel)

instrucciones = Label(root, text="Debes de pegar el video de Youtube en la parte de abajo")
instrucciones.grid(row=0, column=1)

videos = Entry(root)
videos.grid(row=1, column=1)

boton = Button(root, text="Descargar", command=accion)
boton.grid(row=2, column=1)
root.mainloop()