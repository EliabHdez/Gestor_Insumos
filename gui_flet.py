import flet as ft

def main(page: ft.Page):
    page.horizontal_alignment = "center"
    page.title = 'Gestor de Insumos'
    page.add(
        ft.Text("Gestor Entrada / Salida de Insumos", size=30)
        )
    page.add(
        ft.Text("Seleccione la opcion deseada")
    )

ft.app(main)