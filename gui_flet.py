import flet as ft

class UI(ft.UserControl):
    def __init__(self, page):
        super().__init__(expand=True)

        self.color_teal = "teal"

        self.mode_switch = ft.Switch(
            value=True,
            # thumb_color="black",
            thumb_icon={
                ft.MaterialState.DEFAULT: ft.icons.DARK_MODE,
                ft.MaterialState.SELECTED: ft.icons.DARK_MODE
            }
        )

        # self.top_bar = ft.Container(
        #     bgcolor=self.color_teal,
        #     content=ft.Row()
        # )

        # self.menu_inicio = ft.Container(
        #     bgcolor=self.color_teal,
        #     content=ft.Row()
        # )

        self.navigation_bar = ft.Container(
            col=1,
            bgcolor=self.color_teal,
            border_radius=10,
            content=ft.Column(
                controls=[
                    ft.Container(
                        alignment=ft.alignment.center,
                        expand=True,
                        content=ft.NavigationRail(
                            bgcolor="black",
                            expand=True,
                            selected_index=0,
                            destinations=[
                                ft.NavigationDestination(
                                    icon = ft.icons.HOME,
                                ),
                                ft.NavigationDestination(
                                    icon = ft.icons.ACCOUNT_TREE_ROUNDED
                                ),
                                ft.NavigationDestination(
                                    icon = ft.icons.LOCATION_ON_OUTLINED
                                ),
                                ft.NavigationDestination(
                                    icon = ft.icons.CALENDAR_MONTH_SHARP
                                )
                            ]
                        )
                    ),
                    ft.Container(
                        alignment=ft.alignment.center,
                        expand=True,
                        content=ft.Column(
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            alignment=ft.MainAxisAlignment.END,
                            controls=[
                                ft.IconButton(
                                    icon=ft.icons.ACCOUNT_CIRCLE_SHARP
                                ),
                                ft.IconButton(
                                    icon=ft.icons.SETTINGS
                                ),
                                self.mode_switch
                            ]
                        )
                    )
                ]
            )
        )

        self.insumos = ft.Container(
            col=6,
            bgcolor=self.color_teal,
            border_radius=10,
            content=ft.Column()
        )

        self.view_report = ft.Container(
            col=5,
            bgcolor=self.color_teal,
            border_radius=10,
            content=ft.Column()
        )

        self.gral_container = ft.ResponsiveRow(
            
            controls=[
                self.navigation_bar,
                self.insumos,
                self.view_report
            ]
            
        )

    def build(self):
        return self.gral_container

# Función principal para crear la ventana principal de nuestro programa o app con algunas configuraciones en ella como alineacion en horizontal, color de fondo, medida minima en alto y ancho, tema predeterminado y título

def main(page: ft.Page):
    # page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = ft.colors.BLUE_GREY_900
    page.window_min_height = 580
    page.window_min_width = 580
    page.window_max_height = 580
    page.window_max_width = 820
    page.theme_mode = ft.ThemeMode.SYSTEM
    page.title = "Gestor de Insumos"
    page.add(UI(page))

    # Functions

    

    # Widgets

    # themeText = ft.Text("Modo Claro", size= 13, color="cyan")
    # # themeButton = ft.IconButton(ft.icons.SUNNY, icon_color="yellow", tooltip="Modo Claro", focus_color="red", on_click=tema_Claro, icon_size=20)
    # switchTheme = ft.Switch(
    #     value=True,
    #     thumb_color="black",
    #     inactive_thumb_color="yellow",
    #     thumb_icon={
    #         ft.MaterialState.DEFAULT: ft.icons.DARK_MODE,
    #         ft.MaterialState.SELECTED: ft.icons.LIGHT_MODE
    #     }
    # )

    # filaCambioTema = ft.Row(
    #     controls=[themeText, switchTheme],
    #     alignment=ft.MainAxisAlignment.END
    # )
    # page.add(filaCambioTema)





ft.app(main)