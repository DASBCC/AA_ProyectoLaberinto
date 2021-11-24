from tkinter import *
from PIL import Image, ImageTk
from fitnes import Generaciones

#VENTANA PRINCIPAL
ventana = Tk()
ventana.geometry("700x720")
ventana.title("Proyecto: Laberinto")
ventana.resizable(False,False)
ventana.config(background="#212227")
titulo = Label(text = "Proyecto Laberinto", font = "Arial 20", bg = "#212227", fg = "white")
titulo.pack(pady = 10)

canvas = Canvas(width=400, height=300, bg='white')
canvas.pack(expand=YES, fill=BOTH)

#FUNCIONES

def ejecutarAlgoritmo():

    kGeneraciones = entradaGeneraciones.get()
    cantIndividuos = entradaIndividuos.get()
    laberinto = seleccionCB.get()

    Generaciones(kGeneraciones, cantIndividuos, laberinto)

    if laberinto == "laberinto-easy":
        imgLabG= (Image.open("laberinto-easy-Generacion.png"))
        imgLabP= (ImageTk.PhotoImage(file = "laberinto-easy-Generacion.png"))
    elif laberinto == "laberinto-medium":
        imgLabG= (Image.open("laberinto-medium-Generacion.png"))
        imgLabP= (ImageTk.PhotoImage(file = "laberinto-medium-Generacion.png"))
    elif laberinto == "laberinto-hard":
        imgLabG= (Image.open("laberinto-hard-Generacion.png"))
        imgLabP= (ImageTk.PhotoImage(file = "laberinto-hard-Generacion.png"))
    #foto = PhotoImage(file = "laberinto-easy.png")
    #foto = PhotoImage(file = "laberinto-easy.png")
    #labelFoto = Label(ventana, image = foto)
    #labelFoto.place(x = 150, y = 387)

    #canvas3 = Canvas(ventana, width = 300, height = 300)
    #canvas3.place(x = 30, y= 77)

    #img= (Image.open('laberinto-easy.png'))
    #foto = PhotoImage(file = "laberinto-easy.png")
    #labelFoto = Label(ventana, image = foto)
    #labelFoto.place(x = 150, y = 387)

    

    #Resize the Image using resize method
    resized_image= imgLabG.resize((300,300), Image.ANTIALIAS)
    new_image= ImageTk.PhotoImage(resized_image)

    #Add image to the Canvas Items
    canvasLabFinG.create_image(0,0, anchor=NW, image=new_image)
    canvasLabFinG.new_image = new_image

    canvasLabFinP.create_image(0,0, anchor=NW, image = imgLabP)
    canvasLabFinP.imgLabP = imgLabP

    boton2.config(state = 'normal')
    boton3.config(state = 'normal')
    entradaGen.config(state = 'normal')
    return

def cargarLaberinto():
    laberinto = seleccionCB.get()
    if laberinto == "laberinto-easy":
        imgLabG= (Image.open("laberinto-easy.png"))
        imgLabP= (ImageTk.PhotoImage(file = "laberinto-easy.png"))
    elif laberinto == "laberinto-medium":
        imgLabG= (Image.open("laberinto-medium.png"))
        imgLabP= (ImageTk.PhotoImage(file = "laberinto-medium.png"))
    elif laberinto == "laberinto-hard":
        imgLabG= (Image.open("laberinto-hard.png"))
        imgLabP= (ImageTk.PhotoImage(file = "laberinto-hard.png"))
    #foto = PhotoImage(file = "laberinto-easy.png")
    #foto = PhotoImage(file = "laberinto-easy.png")
    #labelFoto = Label(ventana, image = foto)
    #labelFoto.place(x = 150, y = 387)

    #canvas3 = Canvas(ventana, width = 300, height = 300)
    #canvas3.place(x = 30, y= 77)

    #img= (Image.open('laberinto-easy.png'))
    #foto = PhotoImage(file = "laberinto-easy.png")
    #labelFoto = Label(ventana, image = foto)
    #labelFoto.place(x = 150, y = 387)

    

    #Resize the Image using resize method
    resized_image= imgLabG.resize((300,300), Image.ANTIALIAS)
    new_image= ImageTk.PhotoImage(resized_image)

    #Add image to the Canvas Items
    canvasLabIniG.create_image(0,0, anchor=NW, image=new_image)
    canvasLabIniG.new_image = new_image

    canvasLabIniP.create_image(0,0, anchor=NW, image = imgLabP)
    canvasLabIniP.imgLabP = imgLabP

    boton1.config(state = 'disable')
    boton2.config(state = 'normal')
    boton3.config(state = 'normal')
    entradaGen.config(state = 'normal')
    entradaIndiv.config(state = 'normal')
    drop.config(state = 'disable')
    return

def reiniciarCanvas():
    canvasLabIniP.delete("all")
    canvasLabIniG.delete("all")
    canvasLabFinP.delete("all")
    canvasLabFinG.delete("all")
    boton1.config(state = 'normal')
    boton2.config(state = 'disable')
    entradaGen.config(state = 'disable')
    entradaIndiv.config(state = 'disable')
    boton3.config(state = 'disable')
    entradaIndividuos.set(0)
    entradaGeneraciones.set(0)
    drop.config(state = 'normal')
    return

#CANVAS DE LAS IMÁGENES

canvasLabIniG = Canvas(ventana, width = 300, height = 300, bg='white')
canvasLabIniG.place(x = 30, y= 77)

canvasLabIniP = Canvas(ventana, width = 50, height = 50, bg='white')
canvasLabIniP.place(x = 150, y= 387)

canvasLabFinG = Canvas(ventana, width = 300, height = 300, bg='white')
canvasLabFinG.place(x = 365, y= 77)

canvasLabFinP = Canvas(ventana, width = 50, height = 50, bg='white')
canvasLabFinP.place(x = 486, y= 387)


#BOTONES
boton1 = Button(ventana, text="Cargar laberinto", command= cargarLaberinto, width= "16", height= "2", bg= "#5FEDD5", font = "Arial 13")
boton1.place(x = 95, y = 450 )

boton2 = Button(ventana, text = "Reiniciar programa", command = reiniciarCanvas, width= "16", height= "2", bg= "#5FEDD5", font = "Arial 13")
boton2.place(x = 270, y = 450 )
boton2.config(state = "disable")

boton3 = Button(ventana, text = "Ejecutar algoritmo", command = ejecutarAlgoritmo, width= "16", height= "2", bg= "#5FEDD5", font = "Arial 13")
boton3.place(x = 445, y = 450 )
boton3.config(state = "disable")
#COMBOBOX

opciones = ["laberinto-easy", "laberinto-medium", "laberinto-hard"]

seleccionCB = StringVar()
drop = OptionMenu(ventana, seleccionCB, *opciones)
drop.pack(pady = 15)
seleccionCB.set(opciones[0])

#CAJAS DE TEXTO

entradaGeneraciones = IntVar()
entradaGen = Entry(ventana, textvariable = entradaGeneraciones, width = "5", font = ("Arial", "32"), bg= "#5FEDD5")
entradaGen.place(x = 445, y = 520)
entradaGen.config(state = 'disable')

canvas.create_text(270, 485 ,fill="black",font="Times 20 italic bold", text="Cantidad de Generaciones:")

entradaIndividuos = IntVar()
entradaIndiv = Entry(ventana, textvariable = entradaIndividuos, width = "5", font = ("Arial", "32"), bg= "#5FEDD5")
entradaIndiv.place(x = 445, y = 590)
entradaIndiv.config(state = 'disable')

canvas.create_text(270, 555 ,fill="black",font="Times 20 italic bold", text="Cantidad de Individuos:")

"""
laberinto = seleccionCB.get()

foto = PhotoImage(file = "laberinto-easy.png")
labelFoto = Label(ventana, image = foto)
labelFoto.place(x = 150, y = 387)


img= (Image.open("laberinto-easy.png"))

#Resize the Image using resize method
resized_image= img.resize((300,300), Image.ANTIALIAS)
new_image= ImageTk.PhotoImage(resized_image)

#Add image to the Canvas Items
canvas.create_image(30,20, anchor=NW, image=new_image)
"""

#LLAMADA PARA INICIAR EL PROGRAMA
ventana.mainloop()