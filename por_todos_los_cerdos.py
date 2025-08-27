from tkinter import *
from tkinter import messagebox
import random

ventana = Tk()

ventana.title("======================julian_camilo_sanchez_triana==================")

ventana.geometry("800x670")

ventana.resizable(0,0)

ventana.config(bg="green")

bebe = PhotoImage(file="img/bebe7.png")
familia1 = PhotoImage(file = "img/familia.png")
yo = PhotoImage(file = "img/yo.png")
estrella = PhotoImage(file="img/estrella.png")
kitty= PhotoImage(file = "img/kitty.png")
nesticor= PhotoImage(file="img/nesticor.png")


def nacimiento():
    global toplevel_nacimiento
    toplevel_nacimiento = Toplevel()
    toplevel_nacimiento.title("nacimiento")
    toplevel_nacimiento.resizable(False, False)
    toplevel_nacimiento.geometry("600x300")
    toplevel_nacimiento.config(bg="yellow")

    titulo1 = Label(toplevel_nacimiento, text="veran mis datos de mi nacimiento")
    titulo1.config(bg = "white",fg="blue", font=("Helvetica", 20))
    titulo1.place(x=90,y=10)

    lb_bebe = Label(toplevel_nacimiento, image = bebe)
    lb_bebe.place(x= 260,y= 50)

    titulo2 = Label(toplevel_nacimiento, text="naci el 20 de julio de 2010" + "\n" + "vivo en sangil-santander-colombia" + "\n" + "naci en sangil y sigo viviendo en sangil")
    titulo2.config(bg = "white",fg="blue", font=("Helvetica", 20))
    titulo2.place(x=80,y=160)


def familia():
    global toplevel_familia
    toplevel_familia = Toplevel()
    toplevel_familia.title("familia")
    toplevel_familia.resizable(False, False)
    toplevel_familia.geometry("600x300")
    toplevel_familia.config(bg="blue")

    lb_familia = Label(toplevel_familia, image = familia1)
    lb_familia.place(x= 50,y= 50)

    titulo3 = Label(toplevel_familia, text=" vivo con mis papas, mi hermana y mis mascotas")
    titulo3.config(bg = "white",fg="blue", font=("Helvetica", 15))
    titulo3.place(x=80,y=160)

    lb_estrella = Label(toplevel_familia, image = estrella)
    lb_estrella.place(x= 200,y= 50)

    lb_kitty = Label(toplevel_familia, image = kitty)
    lb_kitty.place(x= 270,y= 50)

def educacion():
    global toplevel_educacion
    toplevel_educacion = Toplevel()
    toplevel_educacion.title("educación")
    toplevel_educacion.resizable(False, False)
    toplevel_educacion.geometry("600x500")
    toplevel_educacion.config(bg="white")
    frame_educacion = Frame(toplevel_educacion)
    frame_educacion.config(bg = "red", width= 600, height=500 )
    frame_educacion.place(x=0,y=0)

    lb_nesticor = Label(toplevel_educacion, image = nesticor)
    lb_nesticor.place(x= 50,y= 50)


def amigos():
    global toplevel_amigos
    toplevel_amigos = Toplevel()
    toplevel_amigos.title("amigos")
    toplevel_amigos.resizable(False, False)
    toplevel_amigos.geometry("600x500")
    toplevel_amigos.config(bg="white")
    frame_amigos = Frame(toplevel_amigos)
    frame_amigos.config(bg = "green", width= 600, height=500 )
    frame_amigos.place(x=0,y=0)




def hobbies():
    global toplevel_hobbies
    toplevel_hobbies = Toplevel()
    toplevel_hobbies.title("hobbies")
    toplevel_hobbies.resizable(False, False)
    toplevel_hobbies.geometry("600x500")
    toplevel_hobbies.config(bg="white")
    frame_hobbies = Frame(toplevel_hobbies)
    frame_hobbies.config(bg = "black",width= 600, height=500 )
    frame_hobbies.place(x=0,y=0)

def horario():
    global toplevel_horario
    toplevel_horario = Toplevel()
    toplevel_horario.title("horario")
    toplevel_horario.resizable(False, False)
    toplevel_horario.geometry("600x500")
    toplevel_horario.config(bg="white")
    frame_horario = Frame(toplevel_horario)
    frame_horario.config(bg = "grey",width= 600, height=500 )
    frame_horario.place(x=0,y=0)

def preparacion():
    global toplevel_preparacion
    toplevel_preparacion = Toplevel()
    toplevel_preparacion.title("preparacion para el icfes 11")
    toplevel_preparacion.resizable(False, False)
    toplevel_preparacion.geometry("600x500")
    toplevel_preparacion.config(bg="white")
    frame_preparacion = Frame(toplevel_preparacion)
    frame_preparacion.config(bg="cyan",width= 600, height=500 )
    frame_preparacion.place(x=0,y=0)

def proyecto():
    global toplevel_proyecto
    toplevel_proyecto = Toplevel()
    toplevel_proyecto.title("proyecto de vida")
    toplevel_proyecto.resizable(False, False)
    toplevel_proyecto.geometry("600x500")
    toplevel_proyecto.config(bg="white")
    frame_proyecto = Frame(toplevel_proyecto)
    frame_proyecto.config(bg="gold",width= 600, height=500 )
    frame_proyecto.place(x=0,y=0)

def salud():
    global toplevel_salud
    toplevel_salud = Toplevel()
    toplevel_salud.title("mi salud :V")
    toplevel_salud.resizable(False, False)
    toplevel_salud.geometry("600x500")
    toplevel_salud.config(bg="white")
    frame_salud = Frame(toplevel_salud)
    frame_salud.config(bg="red",width= 600, height=500 )
    frame_salud.place(x=0,y=0)

def libre():
    global toplevel_libre
    toplevel_libre = Toplevel()
    toplevel_libre.title("tema libre")
    toplevel_libre.resizable(False, False)
    toplevel_libre.geometry("600x500")
    toplevel_libre.config(bg="white")
    frame_libre = Frame(toplevel_libre)
    frame_libre.config(bg="purple",width= 600, height=500 )
    frame_libre.place(x=0,y=0)  

frame1 = Frame(ventana)
frame1.config(bg="yellow",width=780, height=200)
frame1.place(x=10,y=10)

frame2 = Frame(ventana)
frame2.config(bg="blue", width=780, height=200)
frame2.place(x=10,y=230)

frame3 = Frame(ventana)
frame3.config(bg="red", width=780, height=200)
frame3.place(x=10,y=450)



bt_nacimiento = Button(ventana,text="nacimiento", command=nacimiento)    
bt_nacimiento.place(x=20, y=460, width=100, height=30)

bt_familia = Button(ventana,text="familia", command=familia)    
bt_familia.place(x=130, y=460, width=100, height=30)

bt_educacion = Button(ventana, text="educacion", command= educacion)
bt_educacion.place(x=240, y=460, width=100, height=30)

bt_amigos = Button(ventana, text="amigos", command=amigos)
bt_amigos.place(x=350, y=460, width=100, height=30)

bt_hobbies = Button(ventana,text="hobbies", command=hobbies)    
bt_hobbies.place(x=460, y=460, width=100, height=30)

bt_horario= Button(ventana,text="horario", command=horario)    
bt_horario.place(x=570, y=460, width=100, height=30)

bt_preparacion = Button(ventana, text="preparacion", command= preparacion)
bt_preparacion.place(x=680, y=460, width=100, height=30)

bt_proyecto = Button(ventana, text="proyecto", command=proyecto)
bt_proyecto.place(x=240, y=500, width=100, height=30)

bt_salud = Button(ventana, text="salud", command=salud)
bt_salud.place(x=350, y=500, width=100, height=30)

bt_libre = Button(ventana, text="libre", command=libre)
bt_libre.place(x=460, y=500, width=100, height=30)

ventana.mainloop()
