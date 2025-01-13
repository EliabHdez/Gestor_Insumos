import flet as ft

class UI(ft.UserControl):
    def __init__(self, page):
        super().__init__(expand=True)

        self.color_teal = "teal"

        self.top_bar = ft.Container(
            col=1,
            bgcolor=self.color_teal,
            content=ft.Column()
        )

        self.menu_inicio = ft.Container(
            col=12,
            bgcolor=self.color_teal,
            border_radius=10,
            content=ft.Column(
                controls=[
                    ft.Container(
                        expand=True,
                        content=ft.NavigationRail(
                            bgcolor="blue",
                            expand=True,
                            selected_index=0,
                            destinations=[
                                ft.Switch(
                                    # value=True,
                                    thumb_color="black",
                                    inactive_thumb_color="yellow",
                                    thumb_icon={
                                        ft.MaterialState.DEFAULT: ft.icons.DARK_MODE,
                                        ft.MaterialState.SELECTED: ft.icons.LIGHT_MODE
                                    }
                                )
                            ]
                        )
                    ),
                    ft.Container(
                        expand=True,
                        bgcolor='red',
                        content=ft.ResponsiveRow(
                            spacing=50,
                            controls=[
                                ft.Container(
                                    padding=10,
                                    col=4,
                                    expand=True,
                                    margin=10,
                                    bgcolor="yellow",
                                    content=ft.Container(
                                        bgcolor="black",
                                        # alignment=ft.alignment.center,
                                        content=ft.Column(
                                            alignment=ft.MainAxisAlignment.CENTER,
                                            horizontal_alignment="center",
                                            controls=[
                                                ft.Container(
                                                    # alignment=ft.,
                                                    bgcolor="blue",
                                                    content=ft.Text("Prueba")
                                                ),
                                                ft.Container(
                                                    bgcolor=self.color_teal,
                                                    content=ft.ResponsiveRow(
                                                        alignment=ft.MainAxisAlignment.CENTER,
                                                        vertical_alignment="center",
                                                        controls=[
                                                            ft.Container(
                                                                col=2,
                                                                bgcolor="pink",
                                                                content=ft.Text("Proof")
                                                            ),
                                                            ft.Container(
                                                                col=2,
                                                                margin=ft.margin.only(right=10),
                                                                # expand=True,
                                                                bgcolor="pink",
                                                                content=ft.TextField(value="", height=30, width=50)
                                                            ),
                                                            ft.Container(
                                                                col=2,
                                                                margin=ft.margin.only(left=10),
                                                                bgcolor="pink",
                                                                content=ft.Text("Proof")
                                                            ),
                                                            ft.Container(
                                                                col=2,
                                                                # expand=True,
                                                                bgcolor="pink",
                                                                content=ft.TextField(value="", height=30, width=50)
                                                            ),
                                                            ft.Container(
                                                                col=2,
                                                                margin=ft.margin.only(left=10),
                                                                bgcolor="pink",
                                                                content=ft.Text("Proof")
                                                            ),
                                                            ft.Container(
                                                                col=2,
                                                                # expand=True,
                                                                bgcolor="pink",
                                                                content=ft.TextField(value="", height=30, width=50)
                                                            ),
                                                        ]
                                                    )
                                                ),
                                                ft.Container(
                                                    bgcolor=self.color_teal,
                                                    content=ft.Row(
                                                        alignment=ft.MainAxisAlignment.CENTER,
                                                        controls=[
                                                            ft.Container(
                                                                bgcolor="pink",
                                                                content=ft.Text("Prueba_2")
                                                            ),
                                                            ft.Container(
                                                                margin=ft.margin.only(right=10),
                                                                # expand=True,
                                                                bgcolor="pink",
                                                                content=ft.TextField(value="", height=30, width=50)
                                                            ),
                                                            ft.Container(
                                                                margin=ft.margin.only(left=10),
                                                                bgcolor="pink",
                                                                content=ft.Text("Prueba_2")
                                                            ),
                                                            ft.Container(
                                                                # expand=True,
                                                                bgcolor="pink",
                                                                content=ft.TextField(value="", height=30, width=50)
                                                            ),
                                                        ]
                                                    )
                                                ),
                                            ]
                                        )
                                    )
                                ),
                                ft.Container(
                                    col=4,
                                    expand=True,
                                    margin=10,
                                    bgcolor="black",
                                ),
                                ft.Container(
                                    col=4,
                                    expand=True,
                                    margin=10,
                                    bgcolor="black",
                                ),
                            ]
                        ),
                    ),
                    ft.Container(
                        expand=True,
                        bgcolor='yellow'
                    ),
                    ft.Container(
                        expand=True,
                        bgcolor='black'
                    )
                ]
            )
        )

        self.navigation_bar = ft.Container(
            col=1,
            bgcolor=self.color_teal,
            border_radius=10,
            content=ft.Column()
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

        # self.gral_container = ft.ResponsiveRow(
            
        #     controls=[
        #         self.navigation_bar,
        #         self.insumos,
        #         self.view_report
        #     ]
            
        # )

        self.gral_container = ft.ResponsiveRow(
            controls=[
                self.menu_inicio,
                # self.top_bar
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
    # page.window_max_height = 580
    # page.window_max_width = 820
    page.theme_mode = ft.ThemeMode.SYSTEM
    page.title = "Gestor de Insumos"
    page.add(UI(page))

    # Functions





ft.app(main)