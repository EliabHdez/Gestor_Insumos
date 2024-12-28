import flet as ft

def main(page: ft.Page):
    page.horizontal_alignment = "CENTER"
    page.title = "Gestor de Insumos"
    titulo = ft.Text("Gestor Entrada / Salida de Insumos", size=50, bgcolor="#222222", color="white")
    # titulo.bgcolor = 'red'
    # titulo.size = 50
    page.add(titulo)

ft.app(main)