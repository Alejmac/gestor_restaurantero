from tkinter import * 

# iniciar la pantalla
aplicacion = Tk()

#tamaño de la ventana
aplicacion.geometry('1200x630+0+0')
aplicacion.resizable(0,0)
#titulo de la ventana
aplicacion.title("Mi restaurante")
#color de la ventana
aplicacion.config(bg="burlywood4")

#configuracioin del panel superior
panel_superior = Frame(aplicacion,bd=1 ,relief= FLAT)
panel_superior.pack ( side= TOP)

#etiqueta del panel superior
etiqueta_titul = Label (panel_superior,text = 'Sistema de facturacion',fg= 'azure4',
                        font = ('Diosis' , 58 ) , bg = "burlywood4" , width= 27)
etiqueta_titul.grid(row=0, column=0)

#evitar que la app se ceirre 
aplicacion.mainloop() 