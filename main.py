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

# panel izquierdo
panel_izquierdo = Frame (aplicacion ,bd = 1, relief= FLAT)
panel_izquierdo.pack(side= Left)

#panel costos
panel_costos = Frame (panel_izquierdo ,bd = 1, relief= FLAT)
panel_costos.pack(side=BOTTOM)

#panel costos
panel_comidas = LabelFrame(panel_izquierdo , Text= "comida", font=('Dosis', 19 ,'bodl' ), bd =1 ,relief= FLAT,figure= 'azure4')
panel_comidas.pack(side=LEFT)

#panel bebidas
panel_bebidads = LabelFrame(panel_izquierdo , Text= "Bebidas", font=('Dosis', 19 ,'bodl' ), bd =1 ,relief= FLAT,figure= 'azure4')
panel_bebidads.pack(side=LEFT)

#panel Postres
panel_Postres = LabelFrame(panel_izquierdo , Text= "Postres", font=('Dosis', 19 ,'bodl' ), bd =1 ,relief= FLAT,figure= 'azure4')
panel_Postres.pack(side=LEFT)

#panel derecho
panel_derecho = Frame(aplicacion, bd=1, relief= FLAT)
panel_derecho.pack(side= RIGHT)

#panel calculadora
panel_calculadora = Frame(panel_derecho,bd=1 , relief=FLAT,bg ='butlywood' )
panel_calculadora.pack()

#panel recibo
panel_recibo = Frame(panel_derecho,bd=1 , relief=FLAT,bg ='butlywood' )
panel_recibo.pack()

#panel calculadora
panel_calculadora = Frame(panel_derecho,bd=1 , relief=FLAT,bg ='butlywood' )
panel_calculadora.pack()

#panel botones
panel_botones = Frame(panel_derecho,bd=1 , relief=FLAT,bg ='butlywood' )
panel_botones.pack()

#evitar que la app se ceirre 
aplicacion.mainloop() 