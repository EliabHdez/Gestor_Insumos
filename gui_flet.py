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
                            bgcolor=self.color_teal,
                            expand=True,
                            selected_index=0,
                            destinations=[
                                ft.NavigationDestination(
                                    icon = ft.icons.HOME,
                                ),
                                ft.NavigationDestination(
                                    icon = ft.icons.POINT_OF_SALE_SHARP
                                ),
                                ft.NavigationDestination(
                                    icon = ft.icons.ACCOUNT_TREE_ROUNDED
                                ),
                                ft.NavigationDestination(
                                    icon = ft.icons.INVENTORY
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
            #bgcolor=self.color_teal,
            #border_radius=10,
            content=ft.Column(
                controls=[
                    ft.Container(
                        bgcolor=self.color_teal,
                        border_radius=4,
                        content=ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                                controls=[
                                ft.Text(value="CONTROL DE FRESA, UVA Y CREMAS", color="black")
                            ]
                        ),
                    ),
                    ft.Row(
                            controls=[
                                ft.Container(
                                    # bgcolor="black",
                                    padding=ft.Padding(top=0, bottom=0, left=20, right=0),
                                    expand=True,
                                    content=ft.Column(
                                        controls=[
                                            ft.Text(value="Fresa", color="white"),
                                            ft.Text(value="Uva", color="white"),
                                            ft.Text(value="Crema Original", color="white"),
                                            ft.Text(value="Crema Chocolate", color="white"),
                                            ft.Text(value="Crema Cafe", color="white"),
                                        ]
                                    ),
                                ),
                                ft.Container(
                                    # bgcolor="red",
                                    padding=ft.Padding(top=0, bottom=0, left=25, right=0),
                                    expand=True,
                                    content=ft.Column(
                                        controls=[
                                            ft.TextField(value="", bgcolor="pink", width=100, height=20, text_size=13, text_align="center", content_padding=26, color="black"),
                                            ft.TextField(value="", bgcolor="pink", width=100, height=20, text_size=13, text_align="center", content_padding=26, color="black"),
                                            ft.TextField(value="", bgcolor="pink", width=100, height=20, text_size=13, text_align="center", content_padding=26, color="black"),
                                            ft.TextField(value="", bgcolor="pink", width=100, height=20, text_size=13, text_align="center", content_padding=26, color="black"),
                                            ft.TextField(value="", bgcolor="pink", width=100, height=20, text_size=13, text_align="center", content_padding=26, color="black")
                                        ]
                                    ),
                                ),
                            ]
                        ),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                         controls=[
                            ft.FilledButton("Enviar", bgcolor="pink", width=100, color="black")
                        ]
                    ),

                    ft.Container(
                        bgcolor=self.color_teal,
                        border_radius=4,
                        content=ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                                controls=[
                                ft.Text(value="TOPPINGS", color="black")
                            ]
                        ),
                    ),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                        controls=[
                            ft.Container(
                                bgcolor="red",
                                content=ft.Column(
                                    controls=[
                                        ft.Text(value="Nuez", color="white", size=10),
                                        ft.Text(value="Almendra", color="white", size=10),
                                        ft.Text(value="Oreo", color="white", size=10),
                                        ft.Text(value="Bombon", color="white", size=10),
                                        ft.Text(value="Bombon", color="white", size=10),
                                        ft.Text(value="Bombon", color="white", size=10),
                                        ft.Text(value="Bombon", color="white", size=10),
                                    ]
                                )
                            ),
                            ft.Container(
                                bgcolor="red",
                                content=ft.Column(
                                    controls=[
                                        ft.TextField(value="", bgcolor="pink", width=50, height=15, text_size=11, text_align="center", content_padding=26, color="black"),
                                        ft.TextField(value="", bgcolor="pink", width=50, height=15, text_size=11, text_align="center", content_padding=26, color="black"),
                                        ft.TextField(value="", bgcolor="pink", width=50, height=15, text_size=11, text_align="center", content_padding=26, color="black"),
                                        ft.TextField(value="", bgcolor="pink", width=50, height=15, text_size=11, text_align="center", content_padding=26, color="black"),
                                        ft.TextField(value="", bgcolor="pink", width=50, height=15, text_size=11, text_align="center", content_padding=26, color="black"),
                                        ft.TextField(value="", bgcolor="pink", width=50, height=15, text_size=11, text_align="center", content_padding=26, color="black"),
                                        ft.TextField(value="", bgcolor="pink", width=50, height=15, text_size=11, text_align="center", content_padding=26, color="black")
                                    ]
                                )
                            ),
                            ft.Container(
                                bgcolor="black",
                                content=ft.Column(
                                    controls=[
                                        ft.Text(value="Luneta", color="white", size=10),
                                        ft.Text(value="Chocoreta", color="white", size=10),
                                        ft.Text(value="Chispa Choc", color="white", size=10),
                                        ft.Text(value="Coco", color="white", size=10),
                                        ft.Text(value="Coco", color="white", size=10),
                                        ft.Text(value="Coco", color="white", size=10),
                                        ft.Text(value="Coco", color="white", size=10),
                                    ]
                                )
                            ),
                            ft.Container(
                                bgcolor="black",
                                content=ft.Column(
                                    controls=[
                                        ft.TextField(value="", bgcolor="pink", width=50, height=15, text_size=11, text_align="center", content_padding=26, color="black"),
                                        ft.TextField(value="", bgcolor="pink", width=50, height=15, text_size=11, text_align="center", content_padding=26, color="black"),
                                        ft.TextField(value="", bgcolor="pink", width=50, height=15, text_size=11, text_align="center", content_padding=26, color="black"),
                                        ft.TextField(value="", bgcolor="pink", width=50, height=15, text_size=11, text_align="center", content_padding=26, color="black"),
                                        ft.TextField(value="", bgcolor="pink", width=50, height=15, text_size=11, text_align="center", content_padding=26, color="black"),
                                        ft.TextField(value="", bgcolor="pink", width=50, height=15, text_size=11, text_align="center", content_padding=26, color="black"),
                                        ft.TextField(value="", bgcolor="pink", width=50, height=15, text_size=11, text_align="center", content_padding=26, color="black")
                                    ]
                                )
                            ),
                        ]
                    ),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                         controls=[
                            ft.Container(
                                padding=ft.Padding(top=10, bottom=0, left=0, right=0),
                                content=ft.FilledButton("Enviar", bgcolor=self.color_teal, width=100, color="black")
                            )
                        ]
                    ),
                    # ft.Container(
                    #     expand=True,
                    #     bgcolor="black"
                        
                    # ),
                ]
            )
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
    page.window_min_height = 520
    page.window_min_width = 680
    page.window_max_height = 520
    page.window_max_width = 680
    # page.window_max_height = 580
    # page.window_max_width = 820
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


# Web Mode
# ft.app(target=main, view=ft.WEB_BROWSER)

# Desktop Mode
ft.app(target=main)