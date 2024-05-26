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
panel_izquierdo = Frame(aplicacion ,bd = 1, relief= FLAT)
panel_izquierdo.pack(side= LEFT)

#panel costos
panel_costos = Frame (panel_izquierdo ,bd = 1, relief= FLAT)
panel_costos.pack(side=BOTTOM)

#panel costos
panel_comidas = LabelFrame(panel_izquierdo , text= "comida", font=('Dosis', 19 ,'bold' ), bd =1 ,relief= FLAT,fg= 'azure4')
panel_comidas.pack(side=LEFT)

#panel bebidas
panel_bebidads = LabelFrame(panel_izquierdo , text= "Bebidas", font=('Dosis', 19 ,'bold' ), bd =1 ,relief= FLAT,fg= 'azure4')
panel_bebidads.pack(side=LEFT)

#panel Postres
panel_Postres = LabelFrame(panel_izquierdo , text= "Postres", font=('Dosis', 19 ,'bold' ), bd =1 ,relief= FLAT,fg= 'azure4')
panel_Postres.pack(side=LEFT)

#panel derecho
panel_derecho = Frame(aplicacion, bd=1, relief= FLAT)
panel_derecho.pack(side= RIGHT)

#panel calculadora
panel_calculadora = Frame(panel_derecho,bd=1 , relief=FLAT,bg ='burlywood' )
panel_calculadora.pack()

#panel recibo
panel_recibo = Frame(panel_derecho,bd=1 , relief=FLAT,bg ='burlywood' )
panel_recibo.pack()

#panel calculadora
panel_calculadora = Frame(panel_derecho,bd=1 , relief=FLAT,bg ='burlywood' )
panel_calculadora.pack()

#panel botones
panel_botones = Frame(panel_derecho,bd=1 , relief=FLAT,bg ='burlywood' )
panel_botones.pack()

#Lista de comidas
Lista_comidas = ['pollo','cordero','salmon','merluza','kebab', 'pizza']
Lista_debida =['agua','refresco','jugo', 'cola']
Lista_postres =['helado','fruta','bro','brownies','flan']

contador = 0 
variables_comida=[]
for comida in Lista_comidas: 
    variables_comida.append('')
    variables_comida[contador]= IntVar()
    comida = Checkbutton(panel_comidas,text= comida.title(), font=('dosis', 19 , 'bold') , onvalue= 1 , offvalue = 0 )
    comida.grid(row=contador,column=0, sticky= W)
    contador+=1

#variables bebida
contador = 0 
variables_bebida=[]
for comida in Lista_debida: 
    variables_bebida.append('')
    variables_bebida[contador]= IntVar()
    bebida = Checkbutton(panel_bebidas,text= bebida.title(), font=('dosis', 19 , 'bold') , onvalue= 1 , offvalue = 0 )
    bebida.grid(row=contador,column=0, sticky= W)
    contador+=1

#evitar que la app se ceirre 
aplicacion.mainloop() 