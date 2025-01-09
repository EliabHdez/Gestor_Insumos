import flet as ft

class UI(ft.UserControl):
    def __init__(self, page):
        super().__init__(expand=True)

        # self.color_teal = "teal"
        self.color_teal = "#04d59c"
        self.color_teal_2 = "#11b78a"

        self.mode_switch = ft.Switch(
            adaptive=True,
            tooltip="Modo Nocturno",
            value=True,
            thumb_color="#222222",
            active_track_color=ft.Colors.CYAN,
            # active_color="red",
            inactive_thumb_color=ft.Colors.BLUE,
            inactive_track_color=ft.Colors.BLUE_GREY_500,
            thumb_icon={
                ft.MaterialState.HOVERED: ft.icons.DARK_MODE_SHARP,
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

        #  ***** BARRA DE NAVEGACION LATERAL IZQUIERDA *****

        self.navigation_bar = ft.Container(
            col=.7,
            # bgcolor=self.color_teal,
            bgcolor=ft.colors.BLUE_GREY_800,
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
                            # bgcolor=ft.colors.BLUE_GREY_900,
                            bgcolor=ft.colors.BLUE_GREY_800,
                            expand=True,
                            selected_index=0,
                            indicator_color=self.color_teal_2,
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
                        margin=ft.margin.only(bottom=3),
                        alignment=ft.alignment.center,
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

        # LINEA ESTETICA DIVISORIA ENTRE LA BARRA DE NAVEGACION LATERAL Y EL AREA DE LA DERECHA

        # self.div_line = ft.Container(
        #     # margin=ft.margin.symmetric(vertical=10),
        #     # padding=10,
        #     col=.2,
        #     # height=620,
        #     # bgcolor=self.color_teal,
        #     # border_radius=5,
        #     content=ft.Container(
        #         width=1,
        #         # margin=ft.margin.symmetric(vertical=10),
        #         # height=620,
        #         bgcolor=self.color_teal,
        #         border_radius=5,
        #         content=ft.Column(
        #             expand=True
        #         )
        #     )
        # )

        # ***** AREA DE CAPTURA DE DATOS *****

        self.gestion = ft.Container(
            col=11.25,
            bgcolor=ft.colors.BLUE_GREY_800,
            border_radius=5,
            expand=True,
            content=ft.Column(
                expand=True, 
                controls=[
                    ft.Container(
                        padding=ft.Padding(top=5, bottom=5, left=10, right=25),
                        # bgcolor="black",
                        content=ft.Row(
                            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                            expand=True,
                            controls=[
                                ft.Radio(value="cofradia3", label="Glorieta", label_style=ft.TextStyle(size=12), visual_density=ft.VisualDensity.STANDARD, fill_color={
                                    ft.ControlState.DEFAULT: ft.Colors.PINK,
                                    ft.ControlState.SELECTED: ft.Colors.GREEN,
                                }),
                            ft.Radio(value="sanmiguel", label="San Miguel", label_style=ft.TextStyle(size=12), visual_density=ft.VisualDensity.STANDARD, fill_color={
                                    ft.ControlState.DEFAULT: ft.Colors.PINK,
                                    ft.ControlState.SELECTED: ft.Colors.GREEN,
                                }),
                            ft.Radio(value="vips", label="Vips", label_style=ft.TextStyle(size=12), visual_density=ft.VisualDensity.STANDARD, fill_color={
                                    ft.ControlState.DEFAULT: ft.Colors.PINK,
                                    ft.ControlState.SELECTED: ft.Colors.GREEN,
                                }),
                            ft.Radio(value="cofradia2", label="Cofradía 2", label_style=ft.TextStyle(size=12), visual_density=ft.VisualDensity.STANDARD, fill_color={
                                    ft.ControlState.DEFAULT: ft.Colors.PINK,
                                    ft.ControlState.SELECTED: ft.Colors.GREEN,
                                }),
                            ft.Radio(value="ensueños", label="Ensueños", label_style=ft.TextStyle(size=12), visual_density=ft.VisualDensity.STANDARD, fill_color={
                                    ft.ControlState.DEFAULT: ft.Colors.PINK,
                                    ft.ControlState.SELECTED: ft.Colors.GREEN,
                                }),
                            ft.Radio(value="operagua", label="Operagua", label_style=ft.TextStyle(size=12), visual_density=ft.VisualDensity.STANDARD, fill_color={
                                    ft.ControlState.DEFAULT: ft.Colors.PINK,
                                    ft.ControlState.SELECTED: ft.Colors.GREEN,
                                }),
                            ft.Radio(value="sanantonio", label="San Antonio", label_style=ft.TextStyle(size=12), visual_density=ft.VisualDensity.STANDARD, fill_color={
                                    ft.ControlState.DEFAULT: ft.Colors.PINK,
                                    ft.ControlState.SELECTED: ft.Colors.GREEN,
                                }),
                            ft.Radio(value="lapiedad", label="La Piedad", label_style=ft.TextStyle(size=12), visual_density=ft.VisualDensity.STANDARD, fill_color={
                                    ft.ControlState.DEFAULT: ft.Colors.PINK,
                                    ft.ControlState.SELECTED: ft.Colors.GREEN,
                                })
                            ]
                        )
                    ),
                    ft.Container(
                        margin=ft.Margin(right=15, left=15, top=0, bottom=0),
                        bgcolor=self.color_teal,
                        height=2,
                        border_radius=2.5
                    ),
                    ft.Container(
                        bgcolor="pink",
                        margin=ft.Margin(top=0, bottom=0, left=50, right=50),
                        border_radius=15,
                        padding=ft.Padding(top=5, bottom=5, left=5, right=10),
                        content=ft.Column(
                            controls=[
                                ft.Container(
                                    margin=ft.Margin(top=0, bottom=0, left=50, right=50),
                                    # bgcolor="pink",
                                    # border_radius=10,
                                    expand=True,
                                    content=ft.Row(
                                        expand=True,
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        controls=[
                                            ft.Text(value="VASOS CHICOS", size=20, color="black")
                                        ]
                                    )
                                ),
                                ft.Container(
                                    alignment=ft.alignment.center,
                                    # bgcolor="yellow",
                                    expand=True,
                                    content=ft.Row(
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        controls=[
                                            ft.Container(
                                                # bgcolor="red",
                                                margin=ft.margin.only(right=30),
                                                content=ft.Row(
                                                    controls=[
                                                        ft.Text(value="Vasos Iniciales"),
                                                        ft.TextField(value="", height=20, width=50, text_size=12, content_padding=5, text_align="center", bgcolor="white", color="black"),
                                                        ft.Text(value="Tapas Iniciales"),
                                                        ft.TextField(value="", height=20, width=50, text_size=12, content_padding=5, text_align="center", bgcolor="white", color="black"),
                                                        ft.Text(value="Vasos Finales"),
                                                        ft.TextField(value="", height=20, width=50, text_size=12, content_padding=5, text_align="center", bgcolor="white", color="black"),
                                                        ft.Text(value="Tapas Finales"),
                                                        ft.TextField(value="", height=20, width=50, text_size=12, content_padding=5, text_align="center", bgcolor="white", color="black"),
                                                    ]
                                                ),
                                            ),
                                            ft.Container(
                                                margin=ft.margin.only(left=30),
                                                # bgcolor="blue",
                                                content=ft.Row(
                                                    controls=[
                                                        ft.Text(value="Vendidos", size=17),
                                                        ft.TextField(value="", height=25, width=60, text_size=20, content_padding=3, text_align="center", bgcolor="white", color="red"),
                                                        ft.Text(value="Total Venta", size=17),
                                                        ft.Text(value="$",size=15),
                                                        ft.TextField(value="", height=25, width=80, text_size=20, content_padding=3, text_align="center", bgcolor="white", color="red"),
                                                    ]
                                                ),
                                            ),
                                        ]
                                    )
                                )
                            ]
                        )
                    ),
                    ft.Container(
                        bgcolor="pink",
                        margin=ft.Margin(top=0, bottom=0, left=50, right=50),
                        border_radius=15,
                        padding=ft.Padding(top=5, bottom=5, left=5, right=10),
                        content=ft.Column(
                            controls=[
                                ft.Container(
                                    margin=ft.Margin(top=0, bottom=0, left=50, right=50),
                                    bgcolor="pink",
                                    border_radius=10,
                                    expand=True,
                                    content=ft.Row(
                                        expand=True,
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        controls=[
                                            ft.Text(value="VASOS MEDIANOS", size=20, color="black")
                                        ]
                                    )
                                ),
                                ft.Container(
                                    alignment=ft.alignment.center,
                                    # bgcolor="yellow",
                                    expand=True,
                                    content=ft.Row(
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        controls=[
                                            ft.Container(
                                                # bgcolor="red",
                                                margin=ft.margin.only(right=30),
                                                content=ft.Row(
                                                    controls=[
                                                        ft.Text(value="Vasos Iniciales"),
                                                        ft.TextField(value="", height=20, width=50, text_size=12, content_padding=5, text_align="center", bgcolor="white", color="black"),
                                                        ft.Text(value="Tapas Iniciales"),
                                                        ft.TextField(value="", height=20, width=50, text_size=12, content_padding=5, text_align="center", bgcolor="white", color="black"),
                                                        ft.Text(value="Vasos Finales"),
                                                        ft.TextField(value="", height=20, width=50, text_size=12, content_padding=5, text_align="center", bgcolor="white", color="black"),
                                                        ft.Text(value="Tapas Finales"),
                                                        ft.TextField(value="", height=20, width=50, text_size=12, content_padding=5, text_align="center", bgcolor="white", color="black"),
                                                    ]
                                                ),
                                            ),
                                            ft.Container(
                                                margin=ft.margin.only(left=30),
                                                # bgcolor="blue",
                                                content=ft.Row(
                                                    controls=[
                                                        ft.Text(value="Vendidos", size=17),
                                                        ft.TextField(value="", height=25, width=60, text_size=20, content_padding=3, text_align="center", bgcolor="white", color="red"),
                                                        ft.Text(value="Total Venta", size=17),
                                                        ft.Text(value="$",size=15),
                                                        ft.TextField(value="", height=25, width=80, text_size=20, content_padding=3, text_align="center", bgcolor="white", color="red"),
                                                    ]
                                                ),
                                            ),
                                        ]
                                    )
                                )
                            ]
                        )
                    ),
                    ft.Container(
                        bgcolor="pink",
                        margin=ft.Margin(top=0, bottom=0, left=50, right=50),
                        border_radius=15,
                        padding=ft.Padding(top=5, bottom=5, left=5, right=10),
                        content=ft.Column(
                            controls=[
                                ft.Container(
                                    margin=ft.Margin(top=0, bottom=0, left=50, right=50),
                                    bgcolor="pink",
                                    border_radius=10,
                                    expand=True,
                                    content=ft.Row(
                                        expand=True,
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        controls=[
                                            ft.Text(value="VASOS GRANDES", size=20, color="black")
                                        ]
                                    )
                                ),
                                ft.Container(
                                    alignment=ft.alignment.center,
                                    # bgcolor="yellow",
                                    expand=True,
                                    content=ft.Row(
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        controls=[
                                            ft.Container(
                                                # bgcolor="red",
                                                margin=ft.margin.only(right=30),
                                                content=ft.Row(
                                                    controls=[
                                                        ft.Text(value="Vasos Iniciales"),
                                                        ft.TextField(value="", height=20, width=50, text_size=12, content_padding=5, text_align="center", bgcolor="white", color="black"),
                                                        ft.Text(value="Tapas Iniciales"),
                                                        ft.TextField(value="", height=20, width=50, text_size=12, content_padding=5, text_align="center", bgcolor="white", color="black"),
                                                        ft.Text(value="Vasos Finales"),
                                                        ft.TextField(value="", height=20, width=50, text_size=12, content_padding=5, text_align="center", bgcolor="white", color="black"),
                                                        ft.Text(value="Tapas Finales"),
                                                        ft.TextField(value="", height=20, width=50, text_size=12, content_padding=5, text_align="center", bgcolor="white", color="black"),
                                                    ]
                                                ),
                                            ),
                                            ft.Container(
                                                margin=ft.margin.only(left=30),
                                                # bgcolor="blue",
                                                content=ft.Row(
                                                    controls=[
                                                        ft.Text(value="Vendidos", size=17),
                                                        ft.TextField(value="", height=25, width=60, text_size=20, content_padding=3, text_align="center", bgcolor="white", color="red"),
                                                        ft.Text(value="Total Venta", size=17),
                                                        ft.Text(value="$",size=15),
                                                        ft.TextField(value="", height=25, width=80, text_size=20, content_padding=3, text_align="center", bgcolor="white", color="red"),
                                                    ]
                                                ),
                                            ),
                                        ]
                                    )
                                )
                            ]
                        )
                    ),
                    ft.Container(
                        bgcolor="pink",
                        margin=ft.Margin(top=0, bottom=0, left=50, right=50),
                        border_radius=15,
                        padding=ft.Padding(top=5, bottom=5, left=5, right=10),
                    ),
                    ft.Container(
                        bgcolor="pink",
                        margin=ft.Margin(top=0, bottom=0, left=50, right=50),
                        border_radius=15,
                        padding=ft.Padding(top=5, bottom=5, left=5, right=10),
                        content=ft.Row(
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            controls=[
                                ft.Container(
                                    width=200,
                                    alignment=ft.alignment.center,
                                    # bgcolor="blue",
                                    content=ft.Column(
                                        horizontal_alignment="center",
                                        controls=[
                                            ft.Text(value="Topping(s) Extra"),
                                            ft.Row(
                                                alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                                                controls=[
                                                    ft.Column(
                                                        controls=[
                                                            ft.Column(
                                                                horizontal_alignment="center",
                                                                controls=[
                                                                    ft.Text(value="$5"),
                                                                    ft.TextField(value="", width=50, height=25, content_padding=0, text_align="center", bgcolor="white"),
                                                                ]
                                                            )
                                                        ]
                                                    ),
                                                    ft.Column(
                                                        controls=[
                                                            ft.Column(
                                                                horizontal_alignment="center",
                                                                controls=[
                                                                    ft.Text(value="$10"),
                                                                    ft.TextField(value="", width=50, height=25, content_padding=0, text_align="center", bgcolor="white"),
                                                                ]
                                                            )
                                                        ]
                                                    )
                                                ]
                                            )
                                        ]
                                    )
                                ),
                                ft.Container(
                                    width=210,
                                    alignment=ft.alignment.center,
                                    # bgcolor="blue",
                                    content=ft.Column(
                                        horizontal_alignment="center",
                                        controls=[
                                            ft.Text(value="Servicios a Domicilio"),
                                            ft.Row(
                                                alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                                                controls=[
                                                    ft.Column(
                                                        controls=[
                                                            ft.Column(
                                                                horizontal_alignment="center",
                                                                controls=[
                                                                    ft.Text(value="$20"),
                                                                    ft.TextField(value="", width=50, height=25, content_padding=0, text_align="center", bgcolor="white"),
                                                                ]
                                                            )
                                                        ]
                                                    ),
                                                    ft.Column(
                                                        controls=[
                                                            ft.Column(
                                                                horizontal_alignment="center",
                                                                controls=[
                                                                    ft.Text(value="$35"),
                                                                    ft.TextField(value="", width=50, height=25, content_padding=0, text_align="center", bgcolor="white"),
                                                                ]
                                                            )
                                                        ]
                                                    )
                                                ]
                                            )
                                        ]
                                    )
                                ),
                                ft.Container(
                                    width=330,
                                    alignment=ft.alignment.center,
                                    # bgcolor="blue",
                                    content=ft.Column(
                                        horizontal_alignment="center",
                                        controls=[
                                            ft.Text(value="Transferencias"),
                                            ft.Row(
                                                alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                                                controls=[
                                                    ft.Column(
                                                        controls=[
                                                            ft.Container(
                                                                width=200,
                                                                # alignment=ft.alignment.center,
                                                                content=ft.Column(
                                                                    horizontal_alignment="center",
                                                                    controls=[
                                                                        ft.Text(value="No. de Transferencias"),
                                                                        ft.TextField(value="", width=50, height=25, content_padding=0, text_align="center", bgcolor="white"),
                                                                ]
                                                            )
                                                            )
                                                        ]
                                                    ),
                                                    ft.Column(
                                                        controls=[
                                                            ft.Container(
                                                                width=130,
                                                                # bgcolor="blue",
                                                                alignment=ft.alignment.center,
                                                                content=ft.Column(
                                                                horizontal_alignment="center",
                                                                controls=[
                                                                    ft.Text(value="Monto"),
                                                                    ft.Row(
                                                                        alignment=ft.MainAxisAlignment.START,
                                                                        controls=[
                                                                            ft.Container(
                                                                                margin=ft.margin.only(left=23),
                                                                                # bgcolor="yellow",
                                                                                alignment=ft.alignment.center,
                                                                                content=ft.Row(
                                                                                    alignment=ft.CrossAxisAlignment.CENTER,
                                                                                    controls=[
                                                                                        ft.Text(value="$"),
                                                                                        ft.TextField(value="", width=50, height=25, content_padding=0, text_align="center", bgcolor="white")
                                                                                    ]
                                                                                ),
                                                                            )
                                                                        ]
                                                                    )
                                                                ]
                                                            )
                                                            )
                                                        ]
                                                    )
                                                ]
                                            )
                                        ]
                                    )
                                ),
                                ft.Container(
                                    width=280,
                                    alignment=ft.alignment.center,
                                    # bgcolor="blue",
                                    content=ft.Column(
                                        horizontal_alignment="center",
                                        controls=[
                                            ft.Text(value="Gastos"),
                                            ft.Row(
                                                alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                                                controls=[
                                                    ft.Column(
                                                        controls=[
                                                            ft.Column(
                                                                horizontal_alignment="center",
                                                                controls=[
                                                                    ft.Text(value="No. Gastos"),
                                                                    ft.TextField(value="", width=50, height=25, content_padding=0, text_align="center", bgcolor="white"),
                                                                ]
                                                            )
                                                        ]
                                                    ),
                                                    ft.Column(
                                                        controls=[
                                                            ft.Column(
                                                                horizontal_alignment="center",
                                                                controls=[
                                                                    ft.Text(value="Monto"),
                                                                    ft.Row(
                                                                        alignment=ft.MainAxisAlignment.START,
                                                                        controls=[
                                                                            ft.Container(
                                                                                margin=ft.margin.only(right=15),
                                                                                # bgcolor="yellow",
                                                                                alignment=ft.alignment.center,
                                                                                content=ft.Row(
                                                                                    alignment=ft.CrossAxisAlignment.CENTER,
                                                                                    controls=[
                                                                                        ft.Text(value="$"),
                                                                                        ft.TextField(value="", width=50, height=25, content_padding=0, text_align="center", bgcolor="white")
                                                                                    ]
                                                                                ),
                                                                            )
                                                                        ]
                                                                    )
                                                                ]
                                                            )
                                                        ]
                                                    )
                                                ]
                                            )
                                        ]
                                    )
                                ),
                            ]
                        )
                    )
                ]
            )
        )

        # self.insumos = ft.Container(
        #     col=6,
        #     #bgcolor=self.color_teal,
        #     #border_radius=10,
        #     content=ft.Column(
        #         controls=[
        #             ft.Container(
        #                 height=30,
        #                 # bgcolor=self.color_teal,
        #                 border_radius=15,
        #                 content=ft.Row(
        #                     alignment=ft.MainAxisAlignment.CENTER,
        #                         controls=[
        #                         ft.Text(value="<<<<< FRESA, UVA Y CREMAS >>>>>", color="white")
        #                     ]
        #                 ),
        #             ),
        #             ft.Row(
        #                 alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        #                 controls=[
        #                     ft.Container(
        #                         margin=ft.margin.only(bottom=10),
        #                         padding=ft.padding.only(left=32),
        #                         content=ft.Column(
        #                             controls=[
        #                                 ft.Text(value="Fresa", color="white"),
        #                                 ft.Text(value="Uva", color="white"),
        #                                 ft.Text(value="Crema Original", color="white"),
        #                                 ft.Text(value="Crema Chocolate", color="white"),
        #                                 ft.Text(value="Crema Cafe", color="white"),
        #                             ]
        #                         ),
        #                     ),
        #                     ft.Container(
        #                         padding=ft.padding.only(right=32),
        #                         content=ft.Column(
        #                             controls=[
        #                                 ft.TextField(value="", bgcolor="pink", width=100, height=20, text_size=15, text_align="center", content_padding=ft.padding.only(0), color="black", border_color="pink"),
        #                                 ft.TextField(value="", bgcolor="pink", width=100, height=20, text_size=15, text_align="center", content_padding=ft.padding.only(0), color="black", border_color="pink"),
        #                                 ft.TextField(value="", bgcolor="pink", width=100, height=20, text_size=15, text_align="center", content_padding=ft.padding.only(0), color="black", border_color="pink"),
        #                                 ft.TextField(value="", bgcolor="pink", width=100, height=20, text_size=15, text_align="center", content_padding=ft.padding.only(0), color="black", border_color="pink"),
        #                                 ft.TextField(value="", bgcolor="pink", width=100, height=20, text_size=15, text_align="center", content_padding=ft.padding.only(0), color="black", border_color="pink")
        #                             ]
        #                         ),
        #                     ),
        #                 ]
        #             ),
        #             ft.Row(
        #                 alignment=ft.MainAxisAlignment.CENTER,
        #                  controls=[
        #                     ft.FilledButton("Capturar", bgcolor="white", width=100, color="black")
        #                 ]
        #             ),

        #             ft.Container(
        #                 alignment=ft.alignment.center,
        #                 margin=ft.margin.only(top=6),
        #                 height=30,
        #                 # bgcolor=self.color_teal,
        #                 border_radius=15,
        #                 content=ft.Row(
        #                     alignment=ft.MainAxisAlignment.CENTER,
        #                         controls=[
        #                         ft.Text(value="<<<<< TOPPINGS >>>>>", color="white")
        #                     ]
        #                 ),
        #             ),
        #             ft.Row(
        #                 expand=True,
        #                 alignment=ft.MainAxisAlignment.SPACE_EVENLY,
        #                 controls=[
        #                     ft.Container(
        #                         # bgcolor="red",
        #                         content=ft.Column(
        #                             alignment=ft.MainAxisAlignment.SPACE_EVENLY,
        #                             controls=[
        #                                 ft.Text(value="Almendra", color="white", size=13),
        #                                 ft.Text(value="Canela", color="white", size=13),
        #                                 ft.Text(value="Chispa Ch", color="white", size=13),
        #                                 ft.Text(value="Coco Rayado", color="white", size=13),
        #                                 ft.Text(value="Gotita Ch", color="white", size=13),
        #                                 ft.Text(value="Kranky", color="white", size=13),
        #                                 ft.Text(value="Luneta Ch", color="white", size=13),
        #                                 ft.Text(value="Mazapan", color="white", size=13),
        #                                 ft.Text(value="Oreo", color="white", size=13),
        #                             ]
        #                         )
        #                     ),
        #                     ft.Container(
        #                         # bgcolor="red",
        #                         content=ft.Column(
        #                             alignment=ft.MainAxisAlignment.SPACE_EVENLY,
        #                             controls=[
        #                                 ft.TextField(value="", bgcolor="pink", width=50, height=18, text_size=12, text_align="center", color="black", border_color="pink", content_padding=ft.padding.only(0)),
        #                                 ft.TextField(value="", bgcolor="pink", width=50, height=18, text_size=12, text_align="center", color="black", border_color="pink", content_padding=ft.padding.only(0)),
        #                                 ft.TextField(value="", bgcolor="pink", width=50, height=18, text_size=12, text_align="center", color="black", border_color="pink", content_padding=ft.padding.only(0)),
        #                                 ft.TextField(value="", bgcolor="pink", width=50, height=18, text_size=12, text_align="center", color="black", border_color="pink", content_padding=ft.padding.only(0)),
        #                                 ft.TextField(value="", bgcolor="pink", width=50, height=18, text_size=12, text_align="center", color="black", border_color="pink", content_padding=ft.padding.only(0)),
        #                                 ft.TextField(value="", bgcolor="pink", width=50, height=18, text_size=12, text_align="center", color="black", border_color="pink", content_padding=ft.padding.only(0)),
        #                                 ft.TextField(value="", bgcolor="pink", width=50, height=18, text_size=12, text_align="center", color="black", border_color="pink", content_padding=ft.padding.only(0)),
        #                                 ft.TextField(value="", bgcolor="pink", width=50, height=18, text_size=12, text_align="center", color="black", border_color="pink", content_padding=ft.padding.only(0)),
        #                                 ft.TextField(value="", bgcolor="pink", width=50, height=18, text_size=12, text_align="center", color="black", border_color="pink", content_padding=ft.padding.only(0))
        #                             ]
        #                         )
        #                     ),
        #                     ft.Container(
        #                         # bgcolor="black",
        #                         content=ft.Column(
        #                             alignment=ft.MainAxisAlignment.SPACE_EVENLY,
        #                             controls=[
        #                                 ft.Text(value="Bombon", color="white", size=13),
        #                                 ft.Text(value="Chispa Arc", color="white", size=13),
        #                                 ft.Text(value="Chocoreta", color="white", size=13),
        #                                 ft.Text(value="Emperador", color="white", size=13),
        #                                 ft.Text(value="Granola", color="white", size=13),
        #                                 ft.Text(value="Luneta Yog", color="white", size=13),
        #                                 ft.Text(value="Nuez Gr", color="white", size=13),
        #                                 ft.Text(value="Panditas", color="white", size=13),
        #                             ]
        #                         )
        #                     ),
        #                     ft.Container(
        #                         # bgcolor="black",
        #                         content=ft.Column(
        #                             alignment=ft.MainAxisAlignment.SPACE_EVENLY,
        #                             controls=[
        #                                 ft.TextField(value="", bgcolor="pink", width=50, height=18, text_size=12, text_align="center", color="black", border_color="pink", content_padding=ft.padding.symmetric),
        #                                 ft.TextField(value="", bgcolor="pink", width=50, height=18, text_size=12, text_align="center", color="black", border_color="pink", content_padding=ft.padding.symmetric),
        #                                 ft.TextField(value="", bgcolor="pink", width=50, height=18, text_size=12, text_align="center", color="black", border_color="pink", content_padding=ft.padding.symmetric),
        #                                 ft.TextField(value="", bgcolor="pink", width=50, height=18, text_size=12, text_align="center", color="black", border_color="pink", content_padding=ft.padding.symmetric),
        #                                 ft.TextField(value="", bgcolor="pink", width=50, height=18, text_size=12, text_align="center", color="black", border_color="pink", content_padding=ft.padding.symmetric),
        #                                 ft.TextField(value="", bgcolor="pink", width=50, height=18, text_size=12, text_align="center", color="black", border_color="pink", content_padding=ft.padding.symmetric),
        #                                 ft.TextField(value="", bgcolor="pink", width=50, height=18, text_size=12, text_align="center", color="black", border_color="pink", content_padding=ft.padding.symmetric),
        #                                 ft.TextField(value="", bgcolor="pink", width=50, height=18, text_size=12, text_align="center", color="black", border_color="pink", content_padding=ft.padding.symmetric)
        #                             ]
        #                         )
        #                     ),
        #                 ]
        #             ),
        #             # ft.Row(
        #             #     controls=[
        #             #         ft.Text(value="Servicios a Domicilio"),
        #             #         ft.Radio(label="$20"),
        #             #         ft.Radio(label="$35")
        #             #     ]
        #             # ),
        #             # ft.Row(
        #             #     controls=[
        #             #         ft.Text(value="Toppigs Extra"),
        #             #         ft.Radio(label="$5"),
        #             #         ft.Radio(label="$10")
        #             #     ]
        #             # ),
        #             ft.Row(
        #                 alignment=ft.MainAxisAlignment.CENTER,
        #                  controls=[
        #                     ft.Container(
        #                         content=ft.FilledButton("Capturar", bgcolor="white", width=100, color="black")
        #                     )
        #                 ]
        #             ),
        #             # ft.Container(
        #             #     expand=True,
        #             #     bgcolor="black"
                        
        #             # ),
        #         ]
        #     )
        # )

        # self.view_report = ft.Container(
        #     col=5,
        #     #bgcolor=self.color_teal,
        #     #border_radius=10,
        #     content=ft.Column(
        #         alignment=ft.MainAxisAlignment.SPACE_AROUND,
        #         controls=[
        #             ft.Container(
        #                 height=30,
        #                 # bgcolor=self.color_teal,
        #                 border_radius=15,
        #                 content=ft.Row(
        #                     alignment=ft.MainAxisAlignment.CENTER,
        #                         controls=[
        #                         ft.Text(value="----- REPORTES -----", color="pink")
        #                     ]
        #                 ),
        #             ),
        #             ft.Container(
        #                 content=ft.Row(
        #                     alignment=ft.MainAxisAlignment.SPACE_EVENLY,
        #                     controls=[
        #                         ft.Container(
        #                             content=ft.Row(
        #                                 alignment=ft.MainAxisAlignment.CENTER,
        #                                 expand=True,
        #                                 controls=[
        #                                     ft.Dropdown(
        #                                         expand=True,
        #                                         label="Punto de Venta",
        #                                         width=250,
        #                                         # height=100,
        #                                         border=ft.InputBorder.OUTLINE,
        #                                         border_radius=5,
        #                                         border_color="pink",
        #                                         border_width=.5,
        #                                         focused_border_width=2,
        #                                         text_size=12,
        #                                         padding=ft.Padding(top=0, bottom=18, left=20, right=20),
        #                                         hint_text="Selecciona PDV",
        #                                         align_label_with_hint=ft.alignment.center_left,
        #                                         options=[
        #                                             ft.dropdown.Option("Cofradia 3"),
        #                                             ft.dropdown.Option("San Miguel"),
        #                                             ft.dropdown.Option("Vips"),
        #                                             ft.dropdown.Option("Cofradia 2"),
        #                                             ft.dropdown.Option("San Antonio")
        #                                         ],
        #                                         autofocus=True
        #                                     ),
        #                                 ]
        #                             )
        #                         ),
        #                     ]  
        #                 ),
        #             ),
        #             ft.Container(
        #                 # bgcolor="red",
        #                 # expand=True,
        #                 padding=ft.padding.symmetric(horizontal=20, vertical=5),
        #                 content=ft.Column(
        #                     alignment=ft.MainAxisAlignment.START,
        #                         controls=[
        #                         ft.TextField(value="", bgcolor="white", color="black", multiline=True, min_lines=5, max_lines=8, border_color=self.color_teal, border_radius=10, border_width=3, text_size=14)
        #                     ]
        #                 ),
        #             ),
        #             ft.Container(
        #                 # bgcolor="black",
        #                 border_radius=10,
        #                 expand=True,
        #                 padding=ft.padding.symmetric(horizontal=20, vertical=5),
        #                 content=ft.Column(
        #                     alignment=ft.MainAxisAlignment.CENTER,
        #                         controls=[
        #                         ft.TextField(value="", bgcolor="white", color="black", multiline=True, min_lines=17, max_lines=20, border_color=self.color_teal, border_radius=10, border_width=3, text_size=14)
        #                     ]
        #                 ),
        #             ),
        #             ft.Row(
        #                 alignment=ft.MainAxisAlignment.CENTER,
        #                  controls=[
        #                     ft.Container(
        #                         content=ft.FilledButton("Generar Reporte", bgcolor="white", width=150, color="black")
        #                     )
        #                 ]
        #             ),
        #         ]
        #     )
        # )

        # ***** FILA PRINCIPAL DE LA PAGINA (ABARCA TODA LA VENTANA Y ES DONDE SE PONE CADA UNA DE LAS SECCIONES QUE VAN A VERSE EN LA PAGINA) *****

        self.gral_container = ft.ResponsiveRow(
            controls=[
                self.navigation_bar,
                self.gestion
                # self.div_line,
                # self.insumos,
                # self.view_report
            ]
            
        )

    # ***** FUNCTION CONSTRUCTORA (NO ME QUEDA CLARO PARA QUE Y PORQUE SE HACE, TENGO QUE INVESTIGAR A FONDO) *****

    def build(self):
        return self.gral_container

# ***** FUNCIÓN PRINCIPAL PARA CREAR LA VENTANA PRINCIPAL DE NUESTRO PROGRAMA O APP CON ALGUNAS CONFIGURACIONES EN ELLA COMO ALINEACION EN HORIZONTAL, COLOR DE FONDO, MEDIDA MINIMA EN ALTO Y ANCHO, TEMA PREDETERMINADO Y TÍTULO *****

def main(page: ft.Page):
    # page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = ft.colors.BLUE_GREY_900
    page.window_min_height = 620
    page.window_min_width = 680
    # page.window_max_height = 620
    # page.window_max_width = 1080
    page.theme_mode = ft.ThemeMode.DARK
    page.title = "Gestor"
    # page.window_resizable = False
    # page.window_opacity = .95
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