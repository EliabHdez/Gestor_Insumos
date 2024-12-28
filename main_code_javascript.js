// alert("Bienvenido gordito")

// document.getElementById('start').onclick = function() {
//     let opcion = prompt('Seleccione la opción deseada\n1.- Agregar insumos\n2.- Quitar insumos')

//     if (opcion <= 0 || opcion >=3){
    //     }else if (opcion == 1){
        //         alert('"Opción invalida"')
//         alert('"Agregar insumos confirmado. De clik en "aceptar" para continuar"')
//     }else if (opcion == 2){
//         alert('"Quitar insumos confirmado. Presione "aceptar" para continuar"')
//     }else if (opcion == 'Agregar' || opcion == 'agregar' || opcion == 'AGREGAR'){
//         alert('"Agregar insumos confirmado. De clik en "aceptar" para continuar"')
//     }else if (opcion == 'Quitar' || opcion == 'quitar' || opcion == 'QUITAR'){
//         alert('"Quitar insumos confirmado. Presione "aceptar" para continuar"')
//     }

//     alert('Prueba finalizada')
// }

function comenzar() {
    opcion = prompt('Seleccione la opción deseada\n1.- Entrada insumos\n2.- Salida insumos')

    if (opcion <= 0 || opcion >=3){
        alert('"Opción invalida"')

    }else if (opcion == 1 || opcion == "E" || opcion == "e" || opcion == 'Entrada' || opcion == 'entrada' || opcion == 'ENTRADA'){
        alert('"Entrada de insumos confirmado. Da clik en "aceptar" para continuar"')
        add_product()
    
    }else if (opcion == 2 || opcion == "S" || opcion == "s" || opcion == 'Salida' || opcion == 'salida' || opcion == 'SALIDA'){
        alert('"Quitar insumos confirmado. Presione "aceptar" para continuar"')
    }
}

function add_product() {
    agregar_cantidad = prompt('Cantidad')
    agregar_producto = prompt('Insumo')
    alert(`${agregar_cantidad} ${agregar_producto} agregado`)
    prod_agregado = (agregar_cantidad) + ' ' + (agregar_producto) + '\n'
    document.getElementById('lc').value = prod_agregado
    answer = prompt('¿Desea agregar mas insumos?\n1.- Si\n2.- No')
    while (answer == 1){
        add_product()
        answer
    }
}

click_add = document.getElementById('add')
click_add.onclick = add_product

click_start = document.getElementById('start')
click_start.onclick = comenzar