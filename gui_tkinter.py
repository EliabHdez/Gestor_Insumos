from tkinter import *

# Root Window

window = Tk()
window.title('Gestor de Ventas e Insumos')
icon = PhotoImage(file='FresaIconoVentana.png')
window.iconphoto(True, icon)
window.geometry("720x480")
window.config(bg='#222222')
# window.config(bg='#ff5c5c')

# Variables globales

aum_num = 0

# Funciones botones

def conteo():
    global aum_num
    aum_num += 1
    label_2.config(text=aum_num)

# Widgets

label = Label(
            text='ENTRADA Y SALIDA DE INSUMOS',
            font=('Arial', 12, 'bold'),
            bg='#ff5c5c',
            relief='groove',
            border=5,
            padx=20,
            pady=10
            )
label.pack()

boton_1 = Button(text='Conteo', bg='red', relief='raised', fg='black')
boton_1.config(command=conteo)
label_2 = Label(text='Prueba de boton. Push the red button!!!',
                bg='green',
                fg='black',
                width=30)
label_2.pack()
boton_1.pack()


window.mainloop() # Coloca una ventana en la pantalla de la computadora