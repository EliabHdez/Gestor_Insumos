print('"FRESAS CON CREMAS"')
print()
print('Gestor de Insumos')
print()
print('Quieres comenzar?')
print('1.- Si     2.- No     3.- Menu Principal')
print()
mensaje = 'Digite la opción deseada o escriba "Si" o "No"'
confirmacion = int(input())

while confirmacion <= 0 or confirmacion >= 4:
    print('La opción ingresada no es válida')
    print()
    mensaje = 'Digite alguna de éstas opciones:  1, 2, "Si" o "No"'
    confirmacion = input('Su respuesta: ')

while confirmacion == 2:
    print('Saliendo')
    print('.........')
    print()
    print('Cargando...')
    print('**********50%**********')
    print('**********100%**********')
    print('Entrando, por favor espere...')
    print()
    print('Quieres comenzar?')
    print('1.- Si     2.- No     3.- Menu Principal')
    print()
    mensaje = 'Digite la opción deseada o escriba "Si" o "No"'
    confirmacion = int(input())

if confirmacion == 1:
    add_1 = 'Agregar'
    delete_1 = 'Eliminar'
    print('Que deseas hacer?')
    print()
    answer_1 = input('1.- Agregar productos / insumos\n2.- Quitar productos / insumos\nIngrese su respuesta: ')
    answer_1 = int(answer_1)
    
    if answer_1 == 1:
        print()
        print(f'{add_1} confirmado')
        print('En proceso...')
    elif answer_1 == 2:
        print()
        print(f'{delete_1} confirmado')
        print('En proceso...')
    elif answer_1 == 3:
        print('Saliendo...')
    else:
        print('Opción no válida')


    

# or confirmacion != "Si" or confirmacion != "SI" or confirmacion != "si" or confirmacion != "No" or confirmacion != "NO" or confirmacion != "no"