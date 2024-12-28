from tkinter import *

window = Tk()
window.title('Prueba')
window.geometry('720x480')
# icon = PhotoImage(file='FresaIconoVentana.png')
# window.iconphoto(True, icon)

label = Label(text='Prueba_1',
              fg='white',
              font=('Arial', '15', 'bold'),
              bg='#222222',
              relief='flat',
              border=10,
              padx=50,
              pady=10)
label.pack()

label_2 = Label(text='Prueba_2', relief='groove', width=30)
label_2.pack()
label_3 = Label(text='Prueba_3', relief='raised', height=5)
label_3.pack()
label_4 = Label(text='Prueba_4', relief='ridge')
label_4.pack()
label_5 = Label(text='Prueba_5', relief='solid')
label_5.pack()
label_6 = Label(text='Prueba_6', relief='sunken')
label_6.pack()

aumento = 0

def conteo():
    global aumento
    aumento += 1
    label_boton.config(text=aumento)

boton = Button(text='Prueba click', bg='#f86c21', fg='black')
boton.config(font=('Ink Free', 50, 'bold'))
boton.config(activebackground='#222222')
boton.config(activeforeground='white')
boton.config(command=conteo)
boton.config(state=ACTIVE)
label_boton = Label(text='Presione el boton!!!')
label_boton.pack()
boton.pack()
# Hay otras tres configuraciones importantes que son 'image': con la cual puedes cargar una imagen para darle algun estilo mas al boton y esta se carga de la misma manera que la de la ventana, mediante la creacion de una variable que sea igual a PhotoImage(file='ruta_imagen') y despues con la configuracion en el boton (boton.config(image='nombre variable que almacena la imagen sin las comillas')), la otra configuracion es 'compound': que nos sirve para posicionar la imagen (esto resulta util si en el boton, label etc tenemos tanto texto como imagen y no queremos que uno tape al otro). Este acepta los valores de top, bottom, left y right entre comillas y por ultimo la tercera es el metodo 'state': con este activas o desactivas el boton (no deja de aparecer en la ventana, solo no puedes interactuar con el). Acepta los valores ACTIVE/DISABLED, tal cual en mayusculas y sin comillas

window.mainloop()