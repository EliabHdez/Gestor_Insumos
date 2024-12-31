import flet as ft

# Función principal para crear la ventana principal de nuestro programa o app con algunas configuraciones en ella como alineacion en horizontal, color de fondo, medida minima en alto y ancho, tema predeterminado y título

def main(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = ft.colors.BLUE_GREY_900
    page.window_min_height = 720
    page.window_min_width = 480
    page.theme_mode = ft.ThemeMode.SYSTEM
    page.title = "Gestor de Insumos"

    # Functions

    def tema_Oscuro(e):
        page.bgcolor = ft.colors.BLUE_GREY_900
        texto_1.color = "white"
        page.add(texto_1)
        texto_2.value = "Bienvenido Efrain"
        texto_2.color = "white"
        texto_4 = ft.Text("Modo Oscuro Activado", size=10, color="white")
        page.add(texto_4)

    def tema_Claro(e):
        page.bgcolor = ft.colors.LIGHT_BLUE_400
        texto_1.color = "black"
        texto_2.value = "Programa cargado y listo! Comencemos con la captura de información..."
        texto_2.color = "black"
        themeText.value = "Modo Oscuro"
        themeText.color = "black"
        texto_4 = ft.Text("Modo Claro Activado", size=10, color="black")
        page.add(texto_4)
        
            # El siguiente codigo lo que hace es crear una nueva variable texto_3 y el texto de esta queda por debajo del boton al momento de hacer click en el elemento antes mencionado. No choca o interfiera con la variable inicial texto_3 debido a que la que se crea lo hace dentro de la funcion y por lo tanto es una variable nueva que en ningun momento entra en conflicto con la que se encuentra afuera debido a que la variable de la funcion su scope se queda dentro de la funcion

                # texto_3 = ft.Text("Modo Claro Activado", size=10, color="black")
                # page.add(texto_3)

            # Tuve que cambiar el nombre de la variable texto_3 que se creaba dentro de la función a texto_4 ya que al querer cambiar el color de la varible global texto_3 ahi si que si me generaba un problema y no ejecutaba el programa como debia al momento de hacer click en el boton, sin embargo dejo la explicación para cualquier eventualidad


            # El siguiente codigo lo que hace es cambiar los valores del texto de la variable texto_3, respetando la posición del texto en la ventana de la aplicación, es decir por encima del boton
                # texto_3.value = "Modo Claro Activado"
                # texto_3.size = 10
                # texto_3.color = "black"

    # Widgets

    themeText = ft.Text("Modo Claro", size= 13, color="cyan")
    # themeButton = ft.IconButton(ft.icons.SUNNY, icon_color="yellow", tooltip="Modo Claro", focus_color="red", on_click=tema_Claro, icon_size=20)
    switchTheme = ft.Switch(
        value=True,
        thumb_color="yellow",
        inactive_thumb_color="yellow",
        thumb_icon={
            ft.MaterialState.DEFAULT: ft.icons.DARK_MODE,
            ft.MaterialState.SELECTED: ft.icons.LIGHT_MODE
        }
    )

    filaCambioTema = ft.Row(
        controls=[themeText, switchTheme],
        alignment=ft.MainAxisAlignment.END
    )
    page.add(filaCambioTema)

    texto_1 = ft.Text("Gestor Entrada / Salida de Insumos", size=30, color="white")
    # titulo.bgcolor = 'red'
    # titulo.size = 50
    page.add(texto_1)

    texto_2 = ft.Text("Bienvenido Efrain", size=20, color="white")
    page.add(texto_2)





ft.app(main)