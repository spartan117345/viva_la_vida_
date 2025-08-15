from tkinter import *
from tkinter import messagebox
import random

ventana = Tk()

ventana.title("======================julian_camilo_sanchez_triana==================")

ventana.geometry("800x670")

ventana.resizable(0,0)

ventana.config(bg="green")

def nacimiento():
    pass

def familia():
    pass

def educacion():
    pass

def amigos():
    pass

def hobbies():
    pass

def horario():
    pass

def preparacion():
    pass

def proyecto():
    pass

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
bt_proyecto.place(x=350, y=500, width=100, height=30)

ventana.mainloop()
