import flet as ft

class UI(ft.UserControl):
    def __init__(self, page):
        super().__init__(expand=True)

        self.color_teal = "teal"

        self.mode_switch = ft.Switch(
            tooltip="Modo Nocturno",
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
                        # alignment=ft.alignment.center,
                        expand=True,
                        # content=ft.Column(
                        #     horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        #     alignment=ft.MainAxisAlignment.START,
                        #     controls=[
                        #         ft.IconButton(
                        #             icon=ft.icons.HOME,
                        #             icon_color="#555555",
                        #             tooltip="Cuenta",
                        #         ),
                        #         ft.IconButton(
                        #             icon=ft.icons.POINT_OF_SALE_SHARP,
                        #             icon_color="white",
                        #             tooltip="Configuración"
                        #         ),
                        #         ft.IconButton(
                        #             icon=ft.icons.ACCOUNT_TREE_ROUNDED,
                        #             icon_color="white",
                        #             tooltip="Configuración"
                        #         ),
                        #         ft.IconButton(
                        #             icon=ft.icons.INVENTORY,
                        #             icon_color="white",
                        #             tooltip="Configuración"
                        #         ),
                        #     ]
                        # )
                        content=ft.NavigationRail(
                            bgcolor=self.color_teal,
                            expand=True,
                            selected_index=0,
                            destinations=[
                                ft.NavigationRailDestination(
                                    icon = ft.icons.HOME,
                                    label_content=ft.Text("INICIO", size=8)
                                ),
                                ft.NavigationRailDestination(
                                    icon = ft.icons.POINT_OF_SALE_SHARP,
                                    label_content=ft.Text("VENTAS", size=8)
                                ),
                                ft.NavigationRailDestination(
                                    icon = ft.icons.ACCOUNT_TREE_ROUNDED,
                                    label_content=ft.Text("PUNTOS", size=8),
                                ),
                                ft.NavigationRailDestination(
                                    icon = ft.icons.INVENTORY,
                                    label_content=ft.Text("STOCK", size=8)
                                )
                            ]
                        )
                    ),
                    ft.Container(
                        # alignment=ft.alignment.center,
                        expand=True,
                        content=ft.Column(
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            alignment=ft.MainAxisAlignment.END,
                            controls=[
                                ft.IconButton(
                                    icon=ft.icons.ACCOUNT_CIRCLE_SHARP,
                                    icon_color="white",
                                    tooltip="Cuenta"
                                ),
                                ft.IconButton(
                                    icon=ft.icons.SETTINGS,
                                    icon_color="white",
                                    tooltip="Configuración"
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
                        height=30,
                        bgcolor=self.color_teal,
                        border_radius=15,
                        content=ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                                controls=[
                                ft.Text(value="FRESA, UVA Y CREMAS", color="black")
                            ]
                        ),
                    ),
                    ft.Row(
                            controls=[
                                ft.Container(
                                    margin=ft.margin.only(bottom=10),
                                    padding=ft.padding.only(left=30),
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
                                    # margin=ft.margin.only(bottom=0),
                                    padding=ft.padding.only(left=35),
                                    expand=True,
                                    content=ft.Column(
                                        controls=[
                                            ft.TextField(value="", bgcolor="pink", width=100, height=20, text_size=15, text_align="center", content_padding=ft.padding.only(0), color="black", border_color="pink"),
                                            ft.TextField(value="", bgcolor="pink", width=100, height=20, text_size=15, text_align="center", content_padding=ft.padding.only(0), color="black", border_color="pink"),
                                            ft.TextField(value="", bgcolor="pink", width=100, height=20, text_size=15, text_align="center", content_padding=ft.padding.only(0), color="black", border_color="pink"),
                                            ft.TextField(value="", bgcolor="pink", width=100, height=20, text_size=15, text_align="center", content_padding=ft.padding.only(0), color="black", border_color="pink"),
                                            ft.TextField(value="", bgcolor="pink", width=100, height=20, text_size=15, text_align="center", content_padding=ft.padding.only(0), color="black", border_color="pink")
                                        ]
                                    ),
                                ),
                            ]
                        ),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                         controls=[
                            ft.FilledButton("Capturar", bgcolor="white", width=100, color="black")
                        ]
                    ),

                    ft.Container(
                        alignment=ft.alignment.center,
                        margin=ft.margin.only(top=6),
                        height=30,
                        bgcolor=self.color_teal,
                        border_radius=15,
                        content=ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                                controls=[
                                ft.Text(value="TOPPINGS", color="black")
                            ]
                        ),
                    ),
                    ft.Row(
                        expand=True,
                        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                        controls=[
                            ft.Container(
                                # bgcolor="red",
                                content=ft.Column(
                                    alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                                    controls=[
                                        ft.Text(value="Almendra", color="white", size=13),
                                        ft.Text(value="Canela", color="white", size=13),
                                        ft.Text(value="Chispa Ch", color="white", size=13),
                                        ft.Text(value="Coco Rayado", color="white", size=13),
                                        ft.Text(value="Gotita Ch", color="white", size=13),
                                        ft.Text(value="Kranky", color="white", size=13),
                                        ft.Text(value="Luneta Ch", color="white", size=13),
                                        ft.Text(value="Mazapan", color="white", size=13),
                                        ft.Text(value="Oreo", color="white", size=13),
                                    ]
                                )
                            ),
                            ft.Container(
                                # bgcolor="red",
                                content=ft.Column(
                                    alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                                    controls=[
                                        ft.TextField(value="", bgcolor="pink", width=50, height=18, text_size=12, text_align="center", color="black", border_color="pink", content_padding=ft.padding.only(0)),
                                        ft.TextField(value="", bgcolor="pink", width=50, height=18, text_size=12, text_align="center", color="black", border_color="pink", content_padding=ft.padding.only(0)),
                                        ft.TextField(value="", bgcolor="pink", width=50, height=18, text_size=12, text_align="center", color="black", border_color="pink", content_padding=ft.padding.only(0)),
                                        ft.TextField(value="", bgcolor="pink", width=50, height=18, text_size=12, text_align="center", color="black", border_color="pink", content_padding=ft.padding.only(0)),
                                        ft.TextField(value="", bgcolor="pink", width=50, height=18, text_size=12, text_align="center", color="black", border_color="pink", content_padding=ft.padding.only(0)),
                                        ft.TextField(value="", bgcolor="pink", width=50, height=18, text_size=12, text_align="center", color="black", border_color="pink", content_padding=ft.padding.only(0)),
                                        ft.TextField(value="", bgcolor="pink", width=50, height=18, text_size=12, text_align="center", color="black", border_color="pink", content_padding=ft.padding.only(0)),
                                        ft.TextField(value="", bgcolor="pink", width=50, height=18, text_size=12, text_align="center", color="black", border_color="pink", content_padding=ft.padding.only(0)),
                                        ft.TextField(value="", bgcolor="pink", width=50, height=18, text_size=12, text_align="center", color="black", border_color="pink", content_padding=ft.padding.only(0))
                                    ]
                                )
                            ),
                            ft.Container(
                                # bgcolor="black",
                                content=ft.Column(
                                    alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                                    controls=[
                                        ft.Text(value="Bombon", color="white", size=13),
                                        ft.Text(value="Chispa Arc", color="white", size=13),
                                        ft.Text(value="Chocoreta", color="white", size=13),
                                        ft.Text(value="Emperador", color="white", size=13),
                                        ft.Text(value="Granola", color="white", size=13),
                                        ft.Text(value="Luneta Yog", color="white", size=13),
                                        ft.Text(value="Nuez Gr", color="white", size=13),
                                        ft.Text(value="Panditas", color="white", size=13),
                                    ]
                                )
                            ),
                            ft.Container(
                                # bgcolor="black",
                                content=ft.Column(
                                    alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                                    controls=[
                                        ft.TextField(value="", bgcolor="pink", width=50, height=18, text_size=12, text_align="center", color="black", border_color="pink", content_padding=ft.padding.symmetric),
                                        ft.TextField(value="", bgcolor="pink", width=50, height=18, text_size=12, text_align="center", color="black", border_color="pink", content_padding=ft.padding.symmetric),
                                        ft.TextField(value="", bgcolor="pink", width=50, height=18, text_size=12, text_align="center", color="black", border_color="pink", content_padding=ft.padding.symmetric),
                                        ft.TextField(value="", bgcolor="pink", width=50, height=18, text_size=12, text_align="center", color="black", border_color="pink", content_padding=ft.padding.symmetric),
                                        ft.TextField(value="", bgcolor="pink", width=50, height=18, text_size=12, text_align="center", color="black", border_color="pink", content_padding=ft.padding.symmetric),
                                        ft.TextField(value="", bgcolor="pink", width=50, height=18, text_size=12, text_align="center", color="black", border_color="pink", content_padding=ft.padding.symmetric),
                                        ft.TextField(value="", bgcolor="pink", width=50, height=18, text_size=12, text_align="center", color="black", border_color="pink", content_padding=ft.padding.symmetric),
                                        ft.TextField(value="", bgcolor="pink", width=50, height=18, text_size=12, text_align="center", color="black", border_color="pink", content_padding=ft.padding.symmetric)
                                    ]
                                )
                            ),
                        ]
                    ),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                         controls=[
                            ft.Container(
                                content=ft.FilledButton("Capturar", bgcolor="white", width=100, color="black")
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
            #bgcolor=self.color_teal,
            #border_radius=10,
            content=ft.Column(
                controls=[
                    ft.Container(
                        height=30,
                        bgcolor=self.color_teal,
                        border_radius=15,
                        content=ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                                controls=[
                                ft.Text(value="REPORTES", color="black")
                            ]
                        ),
                    ),
                    ft.Container(
                        #height=20,
                        content=ft.Row(
                            alignment=ft.MainAxisAlignment.SPACE_EVENLY
                            ,
                                controls=[
                                ft.Container(
                                    padding=ft.padding.only(right=15),
                                    content=ft.Row(
                                        controls=[
                                            ft.Text(value="Entrada", color="white"),
                                            ft.Checkbox()
                                        ]
                                    )
                                ),
                                ft.Container(
                                    padding=ft.padding.only(left=15),
                                    content=ft.Row(
                                        controls=[
                                            ft.Checkbox(),
                                            ft.Text(value="Salida", color="white")
                                        ]
                                    )
                                )
                            ]
                        ),
                    ),
                    ft.Container(
                        bgcolor="red",
                        border_radius=5,
                        expand=True,
                        content=ft.Column(
                            #expand=True,
                            alignment=ft.MainAxisAlignment.CENTER,
                                controls=[
                                ft.TextField(value="", bgcolor="white"),
                            ]
                        ),
                    ),
                    ft.Container(
                        bgcolor="black",
                        border_radius=5,
                        expand=True,
                        padding=5,
                        content=ft.Column(
                            expand=True,
                            alignment=ft.MainAxisAlignment.CENTER,
                                controls=[
                                ft.TextField(value="", bgcolor="white")
                            ]
                        ),
                    ),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                         controls=[
                            ft.Container(
                                content=ft.FilledButton("Generar archivo de reporte", bgcolor="white", width=250, color="black")
                            )
                        ]
                    ),
                ]
            )
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
    page.window_min_height = 620
    page.window_min_width = 680
    page.window_max_height = 620
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


# Web Mode
# ft.app(target=main, view=ft.WEB_BROWSER)

# Desktop Mode
ft.app(target=main)