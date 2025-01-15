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

        def change_page(page, e):
            pass

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
                        expand=True,
                        content=ft.NavigationRail(
                            # bgcolor=ft.colors.BLUE_GREY_900,
                            bgcolor=ft.colors.BLUE_GREY_800,
                            expand=True,
                            on_change=self.change_page,
                            selected_index=0,
                            indicator_color=self.color_teal_2,
                            destinations=[
                                ft.NavigationRailDestination(
                                    icon = ft.icons.HOME,
                                    label_content=ft.Text("INICIO", size=8)
                                ),
                                ft.NavigationRailDestination(
                                    icon = ft.icons.POINT_OF_SALE_SHARP,
                                    label_content=ft.Text("VENTAS", size=8),
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
                    ),
                ]
            )
        )

        # ***** AREA DE CAPTURA DE INSUMOS / ICONO HOME *****

        self.home = ft.Container(
            col=11.25,
            bgcolor=ft.colors.BLUE_GREY_800,
            border_radius=5,
            expand=True,
            content=ft.Column(
                expand=True, 
                controls=[
                    ft.Container(
                        padding=ft.Padding(top=5, bottom=0, left=10, right=25),
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
                        margin=ft.Margin(top=0, bottom=0, left=45, right=50),
                        # expand=True,
                        # bgcolor="pink",
                        content=ft.ResponsiveRow(
                            controls=[
                                ft.Container(
                                    # bgcolor="black",
                                    expand=True,
                                    col=4,
                                    content=ft.Container(
                                        # bgcolor="blue",
                                        # margin=10,
                                        content=ft.Column(
                                            horizontal_alignment="center",
                                            controls=[
                                                ft.Container(
                                                    alignment=ft.alignment.center,
                                                    # bgcolor="pink",
                                                    # border_radius=20,
                                                    width=180,
                                                    # height=30,
                                                    content=ft.Text("VASOS CHICOS", color="#ff1765", weight=ft.FontWeight.BOLD, size=15)
                                                ),
                                                ft.Container(
                                                    # bgcolor=self.color_teal_2,
                                                    # border=ft.border.all(width=5, color=self.color_teal_2),
                                                    padding=ft.padding.symmetric(horizontal=15, vertical=0),
                                                    # border_radius=10,
                                                    content=ft.Column(
                                                        controls=[
                                                            ft.Container(
                                                                alignment=ft.alignment.center,
                                                                # bgcolor=self.color_teal_2,
                                                                border_radius=20,
                                                                content=ft.ResponsiveRow(
                                                                    # alignment=ft.MainAxisAlignment.CENTER,
                                                                    # vertical_alignment="center",
                                                                    controls=[
                                                                        ft.Container(
                                                                            alignment=ft.alignment.center,
                                                                            col=4,
                                                                            # bgcolor="yellow",
                                                                            content=ft.Text("Tapas", color="white"),
                                                                        ),
                                                                        ft.Container(
                                                                            alignment=ft.alignment.center,
                                                                            col=4,
                                                                            # bgcolor="yellow",
                                                                            content=ft.Text("Vasos", color="white"),
                                                                        ),
                                                                        ft.Container(
                                                                            alignment=ft.alignment.center,
                                                                            col=4,
                                                                            # bgcolor="yellow",
                                                                            content=ft.Text("Venta", color="white"),
                                                                        ),
                                                                    ]
                                                                )
                                                            ),
                                                            ft.Container(
                                                                alignment=ft.alignment.center,
                                                                # bgcolor=self.color_teal_2,
                                                                border_radius=20,
                                                                content=ft.ResponsiveRow(
                                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                                    vertical_alignment="center",
                                                                    controls=[
                                                                        ft.Container(
                                                                            padding=2,
                                                                            alignment=ft.alignment.center,
                                                                            col=4,
                                                                            # bgcolor="yellow",
                                                                            content=ft.Container(
                                                                                bgcolor=self.color_teal_2,
                                                                                padding=2.5,
                                                                                border_radius=5,
                                                                                content=ft.TextField(height=30, width=80, color="black", text_size=13, text_align="center", label="Iniciales", label_style=ft.TextStyle(color="#545454", size=10), content_padding=3, bgcolor="white", cursor_height=18, cursor_color="#747474", focused_border_color="black", focused_border_width=2),
                                                                            ),
                                                                        ),
                                                                        ft.Container(
                                                                            padding=2,
                                                                            alignment=ft.alignment.center,
                                                                            col=4,
                                                                            # bgcolor="yellow",
                                                                            content=ft.Container(
                                                                                bgcolor=self.color_teal_2,
                                                                                padding=2.5,
                                                                                border_radius=5,
                                                                                content=ft.TextField(height=30, width=80, color="black", text_size=13, text_align="center", label="Iniciales", label_style=ft.TextStyle(color="#545454", size=10), content_padding=3, bgcolor="white", cursor_height=18, cursor_color="#747474", focused_border_color="black", focused_border_width=2),
                                                                            ),
                                                                        ),
                                                                        ft.Container(
                                                                            padding=2,
                                                                            alignment=ft.alignment.center,
                                                                            col=4,
                                                                            # bgcolor="yellow",
                                                                            content=ft.Container(
                                                                                bgcolor=self.color_teal_2,
                                                                                padding=2.5,
                                                                                border_radius=5,
                                                                                content=ft.TextField(height=30, width=80, color="#dc0000", text_size=15, text_align="center", label="Sin Vender", label_style=ft.TextStyle(color="#545454", size=10), content_padding=2, bgcolor="white", cursor_height=18, cursor_color="#747474", focused_border_color="black", focused_border_width=1.5, read_only=True),
                                                                            ),
                                                                        ),
                                                                    ]
                                                                )
                                                            ),
                                                            ft.Container(
                                                                alignment=ft.alignment.center,
                                                                # bgcolor=self.color_teal_2,
                                                                border_radius=20,
                                                                content=ft.ResponsiveRow(
                                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                                    vertical_alignment="center",
                                                                    controls=[
                                                                        ft.Container(
                                                                            padding=2,
                                                                            alignment=ft.alignment.center,
                                                                            col=4,
                                                                            # bgcolor="yellow",
                                                                            content=ft.Container(
                                                                                bgcolor=self.color_teal_2,
                                                                                padding=2.5,
                                                                                border_radius=5,
                                                                                content=ft.TextField(height=30, width=80, color="black", text_size=13, text_align="center", label="Finales", label_style=ft.TextStyle(color="#545454", size=10), content_padding=3, bgcolor="white", cursor_height=18, cursor_color="#747474", focused_border_color="black", focused_border_width=2),
                                                                            ),
                                                                        ),
                                                                        ft.Container(
                                                                            padding=2,
                                                                            alignment=ft.alignment.center,
                                                                            col=4,
                                                                            # bgcolor="yellow",
                                                                            content=ft.Container(
                                                                                bgcolor=self.color_teal_2,
                                                                                padding=2.5,
                                                                                border_radius=5,
                                                                                content=ft.TextField(height=30, width=80, color="black", text_size=13, text_align="center", label="Finales", label_style=ft.TextStyle(color="#545454", size=10), content_padding=3, bgcolor="white", cursor_height=18, cursor_color="#747474", focused_border_color="black", focused_border_width=2),
                                                                            ),
                                                                        ),
                                                                        ft.Container(
                                                                            padding=2,
                                                                            alignment=ft.alignment.center,
                                                                            col=4,
                                                                            # bgcolor="yellow",
                                                                            content=ft.Container(
                                                                                bgcolor=self.color_teal_2,
                                                                                padding=2.5,
                                                                                border_radius=5,
                                                                                content=ft.TextField(height=30, width=80, color="#dc0000", text_size=15, text_align="center", label="Vendidos", label_style=ft.TextStyle(color="#545454", size=10), content_padding=2, bgcolor="white", cursor_height=18, cursor_color="#747474", focused_border_color="black", focused_border_width=1.5, prefix_text="  $", prefix_style=ft.TextStyle(color="black", size=13), read_only=True),
                                                                            ),
                                                                        ),
                                                                        
                                                                    ]
                                                                )
                                                            ),
                                                            ft.Container(
                                                                alignment=ft.alignment.center,
                                                                # bgcolor=self.color_teal_2,
                                                                border_radius=20,
                                                                content=ft.ResponsiveRow(
                                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                                    vertical_alignment="center",
                                                                    controls=[
                                                                        ft.Container(
                                                                            padding=2,
                                                                            alignment=ft.alignment.center,
                                                                            col=4,
                                                                            # bgcolor="yellow",
                                                                            content=ft.Container(
                                                                                bgcolor=self.color_teal_2,
                                                                                padding=2.5,
                                                                                border_radius=5,
                                                                                content=ft.TextField(height=30, width=80, color="black", text_size=13, text_align="center", label="Diferencia", label_style=ft.TextStyle(color="#545454", size=10), content_padding=3, bgcolor="white", cursor_height=18, cursor_color="#747474", focused_border_color="black", focused_border_width=2, read_only=True),
                                                                            ),
                                                                        ),
                                                                        ft.Container(
                                                                            padding=2,
                                                                            alignment=ft.alignment.center,
                                                                            col=4,
                                                                            # bgcolor="yellow",
                                                                            content=ft.Container(
                                                                                bgcolor=self.color_teal_2,
                                                                                padding=2.5,
                                                                                border_radius=5,
                                                                                content=ft.TextField(height=30, width=80, color="black", text_size=13, text_align="center", label="Diferencia", label_style=ft.TextStyle(color="#545454", size=10), content_padding=3, bgcolor="white", cursor_height=18, cursor_color="#747474", focused_border_color="black", focused_border_width=2, read_only=True),
                                                                            ),
                                                                        ),
                                                                        ft.Container(
                                                                            padding=2,
                                                                            alignment=ft.alignment.center,
                                                                            col=4,
                                                                            # bgcolor="yellow",
                                                                            content=ft.Container(
                                                                                bgcolor="#f00000",
                                                                                padding=2.5,
                                                                                border_radius=5,
                                                                                content=ft.TextField(height=30, width=80, color="#dc0000", text_size=15, text_align="center", label="Venta Total", label_style=ft.TextStyle(color="#545454", size=10), content_padding=2, bgcolor="white", cursor_height=18, cursor_color="#747474", focused_border_color="black", focused_border_width=1.5, prefix_text="  $", prefix_style=ft.TextStyle(color="black", size=13), read_only=True),
                                                                            ),
                                                                        ),
                                                                        
                                                                    ]
                                                                )
                                                            ),
                                                        ]
                                                    )
                                                )
                                            ]
                                        )
                                    )
                                ),
                                ft.Container(
                                    # bgcolor="black",
                                    expand=True,
                                    col=4,
                                    content=ft.Container(
                                        # bgcolor="blue",
                                        # margin=10,
                                        content=ft.Column(
                                            horizontal_alignment="center",
                                            controls=[
                                                ft.Container(
                                                    alignment=ft.alignment.center,
                                                    # bgcolor="pink",
                                                    # border_radius=20,
                                                    width=180,
                                                    # height=30,
                                                    content=ft.Text("VASOS MEDIANOS", color="#ff1765", weight=ft.FontWeight.BOLD, size=15)
                                                ),
                                                ft.Container(
                                                    # bgcolor=self.color_teal_2,
                                                    # border=ft.border.all(width=5, color=self.color_teal_2),
                                                    padding=ft.padding.symmetric(horizontal=15, vertical=0),
                                                    border_radius=10,
                                                    content=ft.Column(
                                                        controls=[
                                                            ft.Container(
                                                                alignment=ft.alignment.center,
                                                                # bgcolor=self.color_teal_2,
                                                                border_radius=20,
                                                                content=ft.ResponsiveRow(
                                                                    # alignment=ft.MainAxisAlignment.CENTER,
                                                                    # vertical_alignment="center",
                                                                    controls=[
                                                                        ft.Container(
                                                                            alignment=ft.alignment.center,
                                                                            col=4,
                                                                            # bgcolor="yellow",
                                                                            content=ft.Text("Tapas", color="white"),
                                                                        ),
                                                                        ft.Container(
                                                                            alignment=ft.alignment.center,
                                                                            col=4,
                                                                            # bgcolor="yellow",
                                                                            content=ft.Text("Vasos", color="white"),
                                                                        ),
                                                                        ft.Container(
                                                                            alignment=ft.alignment.center,
                                                                            col=4,
                                                                            # bgcolor="yellow",
                                                                            content=ft.Text("Venta", color="white"),
                                                                        ),
                                                                    ]
                                                                )
                                                            ),
                                                            ft.Container(
                                                                alignment=ft.alignment.center,
                                                                # bgcolor=self.color_teal_2,
                                                                border_radius=20,
                                                                content=ft.ResponsiveRow(
                                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                                    vertical_alignment="center",
                                                                    controls=[
                                                                        ft.Container(
                                                                            padding=2,
                                                                            alignment=ft.alignment.center,
                                                                            col=4,
                                                                            # bgcolor="yellow",
                                                                            content=ft.Container(
                                                                                bgcolor=self.color_teal_2,
                                                                                padding=2.5,
                                                                                border_radius=5,
                                                                                content=ft.TextField(height=30, width=80, color="black", text_size=13, text_align="center", label="Iniciales", label_style=ft.TextStyle(color="#545454", size=10), content_padding=3, bgcolor="white", cursor_height=18, cursor_color="#747474", focused_border_color="black", focused_border_width=2),
                                                                            ),
                                                                        ),
                                                                        ft.Container(
                                                                            padding=2,
                                                                            alignment=ft.alignment.center,
                                                                            col=4,
                                                                            # bgcolor="yellow",
                                                                            content=ft.Container(
                                                                                bgcolor=self.color_teal_2,
                                                                                padding=2.5,
                                                                                border_radius=5,
                                                                                content=ft.TextField(height=30, width=80, color="black", text_size=13, text_align="center", label="Iniciales", label_style=ft.TextStyle(color="#545454", size=10), content_padding=3, bgcolor="white", cursor_height=18, cursor_color="#747474", focused_border_color="black", focused_border_width=2),
                                                                            ),
                                                                        ),
                                                                        ft.Container(
                                                                            padding=2,
                                                                            alignment=ft.alignment.center,
                                                                            col=4,
                                                                            # bgcolor="yellow",
                                                                            content=ft.Container(
                                                                                bgcolor=self.color_teal_2,
                                                                                padding=2.5,
                                                                                border_radius=5,
                                                                                content=ft.TextField(height=30, width=80, color="#dc0000", text_size=15, text_align="center", label="Sin Vender", label_style=ft.TextStyle(color="#545454", size=10), content_padding=2, bgcolor="white", cursor_height=18, cursor_color="#747474", focused_border_color="black", focused_border_width=1.5, read_only=True),
                                                                            ),
                                                                        ),
                                                                    ]
                                                                )
                                                            ),
                                                            ft.Container(
                                                                alignment=ft.alignment.center,
                                                                # bgcolor=self.color_teal_2,
                                                                border_radius=20,
                                                                content=ft.ResponsiveRow(
                                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                                    vertical_alignment="center",
                                                                    controls=[
                                                                        ft.Container(
                                                                            padding=2,
                                                                            alignment=ft.alignment.center,
                                                                            col=4,
                                                                            # bgcolor="yellow",
                                                                            content=ft.Container(
                                                                                bgcolor=self.color_teal_2,
                                                                                padding=2.5,
                                                                                border_radius=5,
                                                                                content=ft.TextField(height=30, width=80, color="black", text_size=13, text_align="center", label="Finales", label_style=ft.TextStyle(color="#545454", size=10), content_padding=3, bgcolor="white", cursor_height=18, cursor_color="#747474", focused_border_color="black", focused_border_width=2),
                                                                            ),
                                                                        ),
                                                                        ft.Container(
                                                                            padding=2,
                                                                            alignment=ft.alignment.center,
                                                                            col=4,
                                                                            # bgcolor="yellow",
                                                                            content=ft.Container(
                                                                                bgcolor=self.color_teal_2,
                                                                                padding=2.5,
                                                                                border_radius=5,
                                                                                content=ft.TextField(height=30, width=80, color="black", text_size=13, text_align="center", label="Finales", label_style=ft.TextStyle(color="#545454", size=10), content_padding=3, bgcolor="white", cursor_height=18, cursor_color="#747474", focused_border_color="black", focused_border_width=2),
                                                                            ),
                                                                        ),
                                                                        ft.Container(
                                                                            padding=2,
                                                                            alignment=ft.alignment.center,
                                                                            col=4,
                                                                            # bgcolor="yellow",
                                                                            content=ft.Container(
                                                                                bgcolor=self.color_teal_2,
                                                                                padding=2.5,
                                                                                border_radius=5,
                                                                                content=ft.TextField(height=30, width=80, color="#dc0000", text_size=15, text_align="center", label="Vendidos", label_style=ft.TextStyle(color="#545454", size=10), content_padding=2, bgcolor="white", cursor_height=18, cursor_color="#747474", focused_border_color="black", focused_border_width=1.5, prefix_text="  $", prefix_style=ft.TextStyle(color="black", size=13), read_only=True),
                                                                            ),
                                                                        ),
                                                                        
                                                                    ]
                                                                )
                                                            ),
                                                            ft.Container(
                                                                alignment=ft.alignment.center,
                                                                # bgcolor=self.color_teal_2,
                                                                border_radius=20,
                                                                content=ft.ResponsiveRow(
                                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                                    vertical_alignment="center",
                                                                    controls=[
                                                                        ft.Container(
                                                                            # padding=6,
                                                                            alignment=ft.alignment.center,
                                                                            col=4,
                                                                            # bgcolor="yellow",
                                                                            content=ft.Container(
                                                                                bgcolor=self.color_teal_2,
                                                                                padding=2.5,
                                                                                border_radius=5,
                                                                                content=ft.TextField(height=30, width=80, color="black", text_size=13, text_align="center", label="Diferencia", label_style=ft.TextStyle(color="#545454", size=10), content_padding=3, bgcolor="white", cursor_height=18, cursor_color="#747474", focused_border_color="black", focused_border_width=2, read_only=True),
                                                                            ),
                                                                        ),
                                                                        ft.Container(
                                                                            # padding=6,
                                                                            alignment=ft.alignment.center,
                                                                            col=4,
                                                                            # bgcolor="yellow",
                                                                            content=ft.Container(
                                                                                bgcolor=self.color_teal_2,
                                                                                padding=2.5,
                                                                                border_radius=5,
                                                                                content=ft.TextField(height=30, width=80, color="black", text_size=13, text_align="center", label="Diferencia", label_style=ft.TextStyle(color="#545454", size=10), content_padding=3, bgcolor="white", cursor_height=18, cursor_color="#747474", focused_border_color="black", focused_border_width=2, read_only=True),
                                                                            ),
                                                                        ),
                                                                        ft.Container(
                                                                            # padding=6,
                                                                            alignment=ft.alignment.center,
                                                                            col=4,
                                                                            # bgcolor="yellow",
                                                                            content=ft.Container(
                                                                                bgcolor="#f00000",
                                                                                padding=2.5,
                                                                                border_radius=5,
                                                                                content=ft.TextField(height=30, width=80, color="#dc0000", text_size=15, text_align="center", label="Venta Total", label_style=ft.TextStyle(color="#545454", size=10), content_padding=2, bgcolor="white", cursor_height=18, cursor_color="#747474", focused_border_color="black", focused_border_width=1.5, prefix_text="  $", prefix_style=ft.TextStyle(color="black", size=13), read_only=True),
                                                                            ),
                                                                        ),
                                                                        
                                                                    ]
                                                                )
                                                            ),
                                                        ]
                                                    )
                                                )
                                            ]
                                        )
                                    )
                                ),
                                ft.Container(
                                    # bgcolor="black",
                                    expand=True,
                                    col=4,
                                    content=ft.Container(
                                        # bgcolor="blue",
                                        # margin=10,
                                        content=ft.Column(
                                            horizontal_alignment="center",
                                            controls=[
                                                ft.Container(
                                                    alignment=ft.alignment.center,
                                                    # bgcolor="pink",
                                                    # border_radius=20,
                                                    width=180,
                                                    # height=30,
                                                    content=ft.Text("VASOS GRANDES", color="#ff1765", weight=ft.FontWeight.BOLD, size=15)
                                                ),
                                                ft.Container(
                                                    # bgcolor=self.color_teal_2,
                                                    # border=ft.border.all(width=5, color=self.color_teal_2),
                                                    padding=ft.padding.symmetric(horizontal=15, vertical=0),
                                                    border_radius=10,
                                                    content=ft.Column(
                                                        controls=[
                                                            ft.Container(
                                                                alignment=ft.alignment.center,
                                                                # bgcolor=self.color_teal_2,
                                                                border_radius=20,
                                                                content=ft.ResponsiveRow(
                                                                    # alignment=ft.MainAxisAlignment.CENTER,
                                                                    # vertical_alignment="center",
                                                                    controls=[
                                                                        ft.Container(
                                                                            alignment=ft.alignment.center,
                                                                            col=4,
                                                                            # bgcolor="yellow",
                                                                            content=ft.Text("Tapas", color="white"),
                                                                        ),
                                                                        ft.Container(
                                                                            alignment=ft.alignment.center,
                                                                            col=4,
                                                                            # bgcolor="yellow",
                                                                            content=ft.Text("Vasos", color="white"),
                                                                        ),
                                                                        ft.Container(
                                                                            alignment=ft.alignment.center,
                                                                            col=4,
                                                                            # bgcolor="yellow",
                                                                            content=ft.Text("Venta", color="white"),
                                                                        ),
                                                                    ]
                                                                )
                                                            ),
                                                            ft.Container(
                                                                alignment=ft.alignment.center,
                                                                # bgcolor=self.color_teal_2,
                                                                border_radius=20,
                                                                content=ft.ResponsiveRow(
                                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                                    vertical_alignment="center",
                                                                    controls=[
                                                                        ft.Container(
                                                                            # padding=6,
                                                                            alignment=ft.alignment.center,
                                                                            col=4,
                                                                            # bgcolor="yellow",
                                                                            content=ft.Container(
                                                                                bgcolor=self.color_teal_2,
                                                                                padding=2.5,
                                                                                border_radius=5,
                                                                                content=ft.TextField(height=30, width=80, color="black", text_size=13, text_align="center", label="Iniciales", label_style=ft.TextStyle(color="#545454", size=10), content_padding=3, bgcolor="white", cursor_height=18, cursor_color="#747474", focused_border_color="black", focused_border_width=2),
                                                                            ),
                                                                        ),
                                                                        ft.Container(
                                                                            # padding=6,
                                                                            alignment=ft.alignment.center,
                                                                            col=4,
                                                                            # bgcolor="yellow",
                                                                            content=ft.Container(
                                                                                bgcolor=self.color_teal_2,
                                                                                padding=2.5,
                                                                                border_radius=5,
                                                                                content=ft.TextField(height=30, width=80, color="black", text_size=13, text_align="center", label="Iniciales", label_style=ft.TextStyle(color="#545454", size=10), content_padding=3, bgcolor="white", cursor_height=18, cursor_color="#747474", focused_border_color="black", focused_border_width=2),
                                                                            ),
                                                                        ),
                                                                        ft.Container(
                                                                            # padding=6,
                                                                            alignment=ft.alignment.center,
                                                                            col=4,
                                                                            # bgcolor="yellow",
                                                                            content=ft.Container(
                                                                                bgcolor=self.color_teal_2,
                                                                                padding=2.5,
                                                                                border_radius=5,
                                                                                content=ft.TextField(height=30, width=80, color="#dc0000", text_size=15, text_align="center", label="Sin Vender", label_style=ft.TextStyle(color="#545454", size=10), content_padding=2, bgcolor="white", cursor_height=18, cursor_color="#747474", focused_border_color="black", focused_border_width=1.5, read_only=True),
                                                                            ),
                                                                        ),
                                                                    ]
                                                                )
                                                            ),
                                                            ft.Container(
                                                                alignment=ft.alignment.center,
                                                                # bgcolor=self.color_teal_2,
                                                                border_radius=20,
                                                                content=ft.ResponsiveRow(
                                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                                    vertical_alignment="center",
                                                                    controls=[
                                                                        ft.Container(
                                                                            # padding=6,
                                                                            alignment=ft.alignment.center,
                                                                            col=4,
                                                                            # bgcolor="yellow",
                                                                            content=ft.Container(
                                                                                bgcolor=self.color_teal_2,
                                                                                padding=2.5,
                                                                                border_radius=5,
                                                                                content=ft.TextField(height=30, width=80, color="black", text_size=13, text_align="center", label="Finales", label_style=ft.TextStyle(color="#545454", size=10), content_padding=3, bgcolor="white", cursor_height=18, cursor_color="#747474", focused_border_color="black", focused_border_width=2),
                                                                            ),
                                                                        ),
                                                                        ft.Container(
                                                                            # padding=6,
                                                                            alignment=ft.alignment.center,
                                                                            col=4,
                                                                            # bgcolor="yellow",
                                                                            content=ft.Container(
                                                                                bgcolor=self.color_teal_2,
                                                                                padding=2.5,
                                                                                border_radius=5,
                                                                                content=ft.TextField(height=30, width=80, color="black", text_size=13, text_align="center", label="Finales", label_style=ft.TextStyle(color="#545454", size=10), content_padding=3, bgcolor="white", cursor_height=18, cursor_color="#747474", focused_border_color="black", focused_border_width=2),
                                                                            ),
                                                                        ),
                                                                        ft.Container(
                                                                            # padding=6,
                                                                            alignment=ft.alignment.center,
                                                                            col=4,
                                                                            # bgcolor="yellow",
                                                                            content=ft.Container(
                                                                                bgcolor=self.color_teal_2,
                                                                                padding=2.5,
                                                                                border_radius=5,
                                                                                content=ft.TextField(height=30, width=80, color="#dc0000", text_size=15, text_align="center", label="Vendidos", label_style=ft.TextStyle(color="#545454", size=10), content_padding=2, bgcolor="white", cursor_height=18, cursor_color="#747474", focused_border_color="black", focused_border_width=1.5, prefix_text="  $", prefix_style=ft.TextStyle(color="black", size=13), read_only=True),
                                                                            ),
                                                                        ),
                                                                        
                                                                    ]
                                                                )
                                                            ),
                                                            ft.Container(
                                                                alignment=ft.alignment.center,
                                                                # bgcolor=self.color_teal_2,
                                                                border_radius=20,
                                                                content=ft.ResponsiveRow(
                                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                                    vertical_alignment="center",
                                                                    controls=[
                                                                        ft.Container(
                                                                            # padding=6,
                                                                            alignment=ft.alignment.center,
                                                                            col=4,
                                                                            # bgcolor="yellow",
                                                                            content=ft.Container(
                                                                                bgcolor=self.color_teal_2,
                                                                                padding=2.5,
                                                                                border_radius=5,
                                                                                content=ft.TextField(height=30, width=80, color="black", text_size=13, text_align="center", label="Diferencia", label_style=ft.TextStyle(color="#545454", size=10), content_padding=3, bgcolor="white", cursor_height=18, cursor_color="#747474", focused_border_color="black", focused_border_width=2, read_only=True),
                                                                            ),
                                                                        ),
                                                                        ft.Container(
                                                                            # padding=6,
                                                                            alignment=ft.alignment.center,
                                                                            col=4,
                                                                            # bgcolor="yellow",
                                                                            content=ft.Container(
                                                                                bgcolor=self.color_teal_2,
                                                                                padding=2.5,
                                                                                border_radius=5,
                                                                                content=ft.TextField(height=30, width=80, color="black", text_size=13, text_align="center", label="Diferencia", label_style=ft.TextStyle(color="#545454", size=10), content_padding=3, bgcolor="white", cursor_height=18, cursor_color="#747474", focused_border_color="black", focused_border_width=2, read_only=True),
                                                                            ),
                                                                        ),
                                                                        ft.Container(
                                                                            # padding=6,
                                                                            alignment=ft.alignment.center,
                                                                            col=4,
                                                                            # bgcolor="yellow",
                                                                            content=ft.Container(
                                                                                bgcolor="#f00000",
                                                                                padding=2.5,
                                                                                border_radius=5,
                                                                                content=ft.TextField(height=30, width=80, color="#dc0000", text_size=15, text_align="center", label="Venta Total", label_style=ft.TextStyle(color="#545454", size=10), content_padding=2, bgcolor="white", cursor_height=18, cursor_color="#747474", focused_border_color="black", focused_border_width=1.5, prefix_text="  $", prefix_style=ft.TextStyle(color="black", size=13), read_only=True),
                                                                            ),
                                                                        ),
                                                                        
                                                                    ]
                                                                )
                                                            ),
                                                        ]
                                                    )
                                                )
                                            ]
                                        )
                                    )
                                ),
                                
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
                        expand=True,
                        alignment=ft.alignment.center,
                        # bgcolor="pink",
                        margin=ft.Margin(top=0, bottom=0, left=50, right=50),
                        border_radius=15,
                        padding=ft.Padding(top=0, bottom=5, left=5, right=10),
                        content=ft.Column(
                            scroll="auto",
                            horizontal_alignment="center",
                            expand=True,
                            controls=[
                                ft.ResponsiveRow(
                                    controls=[
                                        ft.Container(
                                            padding=2,
                                            alignment=ft.alignment.center,
                                            # bgcolor="black",
                                            content=ft.Column(
                                                expand=True,
                                                controls=[
                                                    ft.ResponsiveRow(
                                                        controls=[
                                                            ft.Container(
                                                                alignment=ft.alignment.center,
                                                                # bgcolor="yellow",
                                                                col=12,
                                                                content=ft.Text("FRUTA", color="#ff1765", weight=ft.FontWeight.BOLD, size=16)
                                                            ),
                                                        ]
                                                    )
                                                ]
                                            )
                                        ),
                                        ft.Container(
                                            alignment=ft.alignment.center,
                                            padding=ft.Padding(top=10, bottom=10, left=55, right=65),
                                            # bgcolor="black",
                                            content=ft.Column(
                                                controls=[
                                                    ft.ResponsiveRow(
                                                        controls=[
                                                            ft.Column(
                                                                col=12,
                                                                controls=[
                                                                    ft.ResponsiveRow(
                                                                        vertical_alignment="center",
                                                                        spacing=50,
                                                                        controls=[
                                                                            ft.Container(
                                                                                alignment=ft.alignment.center,
                                                                                col=2,
                                                                                bgcolor=self.color_teal,
                                                                                border_radius=15,
                                                                                padding=3,
                                                                                content=ft.Text("Fresa", color="black")
                                                                            ),
                                                                            ft.Container(
                                                                                # alignment=ft.alignment.center,
                                                                                col=2,
                                                                                bgcolor=self.color_teal_2,
                                                                                padding=2.5,
                                                                                border_radius=5,
                                                                                content=ft.TextField(height=30, width=50, color="black", text_size=13, text_align="center", label="Picada Inicial", label_style=ft.TextStyle(color="#545454", size=10), content_padding=3, bgcolor="white", cursor_height=18, cursor_color="#747474", focused_border_color="black", focused_border_width=2, hint_text="Botes", hint_style=ft.TextStyle(color="#DADADA", size=10)),
                                                                            ),
                                                                            ft.Container(
                                                                                # alignment=ft.alignment.center,
                                                                                col=2,
                                                                                bgcolor=self.color_teal_2,
                                                                                padding=2.5,
                                                                                border_radius=5,
                                                                                content=ft.TextField(height=30, width=50, color="black", text_size=13, text_align="center", label="Picada Final", label_style=ft.TextStyle(color="#545454", size=10), content_padding=3, bgcolor="white", cursor_height=18, cursor_color="#747474", focused_border_color="black", focused_border_width=2, hint_text="Botes", hint_style=ft.TextStyle(color="#DADADA", size=10)),
                                                                            ),
                                                                            ft.Container(
                                                                                # alignment=ft.alignment.center,
                                                                                col=2,
                                                                                bgcolor=self.color_teal_2,
                                                                                padding=2.5,
                                                                                border_radius=5,
                                                                                content=ft.TextField(height=30, width=50, color="black", text_size=13, text_align="center", label="Entera Inicial", label_style=ft.TextStyle(color="#545454", size=10), content_padding=3, bgcolor="white", cursor_height=18, cursor_color="#747474", focused_border_color="black", focused_border_width=2, hint_text="Botes", hint_style=ft.TextStyle(color="#DADADA", size=10)),
                                                                            ),
                                                                            ft.Container(
                                                                                # alignment=ft.alignment.center,
                                                                                col=2,
                                                                                bgcolor=self.color_teal_2,
                                                                                padding=2.5,
                                                                                border_radius=5,
                                                                                content=ft.TextField(height=30, width=50, color="black", text_size=13, text_align="center", label="Entera Final", label_style=ft.TextStyle(color="#545454", size=10), content_padding=3, bgcolor="white", cursor_height=18, cursor_color="#747474", focused_border_color="black", focused_border_width=2, hint_text="Botes", hint_style=ft.TextStyle(color="#DADADA", size=10)),
                                                                            ),
                                                                            ft.Container(
                                                                                # alignment=ft.alignment.center,
                                                                                col=2,
                                                                                bgcolor="#f00000",
                                                                                padding=2.5,
                                                                                border_radius=5,
                                                                                content=ft.TextField(height=30, width=50, color="black", text_size=13, text_align="center", label="Vendida", label_style=ft.TextStyle(color="#545454", size=10), content_padding=3, bgcolor="white", cursor_height=18, cursor_color="#747474", focused_border_color="black", focused_border_width=2, hint_text="Botes", hint_style=ft.TextStyle(color="#DADADA", size=10)),
                                                                            ),
                                                                        ]
                                                                    ),
                                                                    ft.ResponsiveRow(
                                                                        vertical_alignment="center",
                                                                        spacing=50,
                                                                        controls=[
                                                                            ft.Container(
                                                                                alignment=ft.alignment.center,
                                                                                col=2,
                                                                                bgcolor=self.color_teal,
                                                                                border_radius=15,
                                                                                padding=3,
                                                                                content=ft.Text("Uva", color="black")
                                                                            ),
                                                                            ft.Container(
                                                                                # alignment=ft.alignment.center,
                                                                                col=2,
                                                                                bgcolor=self.color_teal_2,
                                                                                padding=2.5,
                                                                                border_radius=5,
                                                                                content=ft.TextField(height=30, width=50, color="black", text_size=13, text_align="center", label="Picada Inicial", label_style=ft.TextStyle(color="#545454", size=10), content_padding=3, bgcolor="white", cursor_height=18, cursor_color="#747474", focused_border_color="black", focused_border_width=2, hint_text="Botes", hint_style=ft.TextStyle(color="#DADADA", size=10)),
                                                                            ),
                                                                            ft.Container(
                                                                                # alignment=ft.alignment.center,
                                                                                col=2,
                                                                                bgcolor=self.color_teal_2,
                                                                                padding=2.5,
                                                                                border_radius=5,
                                                                                content=ft.TextField(height=30, width=50, color="black", text_size=13, text_align="center", label="Picada Final", label_style=ft.TextStyle(color="#545454", size=10), content_padding=3, bgcolor="white", cursor_height=18, cursor_color="#747474", focused_border_color="black", focused_border_width=2, hint_text="Botes", hint_style=ft.TextStyle(color="#DADADA", size=10)),
                                                                            ),
                                                                            ft.Container(
                                                                                # alignment=ft.alignment.center,
                                                                                col=2,
                                                                                bgcolor=self.color_teal_2,
                                                                                padding=2.5,
                                                                                border_radius=5,
                                                                                content=ft.TextField(height=30, width=50, color="black", text_size=13, text_align="center", label="Entera Inicial", label_style=ft.TextStyle(color="#545454", size=10), content_padding=3, bgcolor="white", cursor_height=18, cursor_color="#747474", focused_border_color="black", focused_border_width=2, hint_text="Botes", hint_style=ft.TextStyle(color="#DADADA", size=10)),
                                                                            ),
                                                                            ft.Container(
                                                                                # alignment=ft.alignment.center,
                                                                                col=2,
                                                                                bgcolor=self.color_teal_2,
                                                                                padding=2.5,
                                                                                border_radius=5,
                                                                                content=ft.TextField(height=30, width=50, color="black", text_size=13, text_align="center", label="Entera Final", label_style=ft.TextStyle(color="#545454", size=10), content_padding=3, bgcolor="white", cursor_height=18, cursor_color="#747474", focused_border_color="black", focused_border_width=2, hint_text="Botes", hint_style=ft.TextStyle(color="#DADADA", size=10)),
                                                                            ),
                                                                            ft.Container(
                                                                                # alignment=ft.alignment.center,
                                                                                col=2,
                                                                                bgcolor="#f00000",
                                                                                padding=2.5,
                                                                                border_radius=5,
                                                                                content=ft.TextField(height=30, width=50, color="black", text_size=13, text_align="center", label="Vendida", label_style=ft.TextStyle(color="#545454", size=10), content_padding=3, bgcolor="white", cursor_height=18, cursor_color="#747474", focused_border_color="black", focused_border_width=2, hint_text="Botes", hint_style=ft.TextStyle(color="#DADADA", size=10)),
                                                                            ),
                                                                        ]
                                                                    ),
                                                                ]
                                                            ),
                                                        ]
                                                    ),
                                                ]
                                            )
                                        ),
                                        ft.Container(
                                            padding=2,
                                            alignment=ft.alignment.center,
                                            # bgcolor="blue",
                                            content=ft.Column(
                                                expand=True,
                                                controls=[
                                                    ft.ResponsiveRow(
                                                        controls=[
                                                            ft.Container(
                                                                alignment=ft.alignment.center,
                                                                # bgcolor="yellow",
                                                                col=12,
                                                                content=ft.Text("CREMAS", color="#ff1765", weight=ft.FontWeight.BOLD, size=16)
                                                            ),
                                                        ]
                                                    ),
                                                    ft.Container(
                                                        alignment=ft.alignment.center,
                                                        # bgcolor="black",
                                                        content=ft.Column(
                                                            controls=[
                                                                ft.ResponsiveRow(
                                                                    controls=[
                                                                        ft.Column(
                                                                            col=4,
                                                                            controls=[
                                                                                ft.ResponsiveRow(
                                                                                    controls=[
                                                                                        ft.Container(
                                                                                            alignment=ft.alignment.center,
                                                                                            content=ft.Column(
                                                                                                controls=[
                                                                                                    ft.Container(
                                                                                                        # bgcolor="blue",
                                                                                                        content=ft.Text("Crema Original")
                                                                                                    )
                                                                                                ]
                                                                                            )
                                                                                        ),
                                                                                    ]
                                                                                ),
                                                                                ft.Container(
                                                                                    margin=ft.margin.symmetric(horizontal=20, vertical=0),
                                                                                    content=ft.Column(
                                                                                        controls=[
                                                                                            ft.ResponsiveRow(
                                                                                                alignment=ft.MainAxisAlignment.CENTER,
                                                                                                spacing=20,
                                                                                                vertical_alignment="center",
                                                                                                controls=[
                                                                                                    ft.Container(
                                                                                                        col=4,
                                                                                                        content=ft.ResponsiveRow(
                                                                                                            controls=[
                                                                                                                ft.Container(
                                                                                                                    bgcolor=self.color_teal_2,
                                                                                                                    padding=2.5,
                                                                                                                    border_radius=5,
                                                                                                                    content=ft.TextField(height=30, width=50, color="black", text_size=13, text_align="center", label="Inicial", label_style=ft.TextStyle(color="#545454", size=10), content_padding=3, bgcolor="white", cursor_height=18, cursor_color="#747474", focused_border_color="black", focused_border_width=2, hint_text="Botes", hint_style=ft.TextStyle(color="#DADADA", size=10)),
                                                                                                                )
                                                                                                            ]
                                                                                                        )
                                                                                                    ),
                                                                                                    ft.Container(
                                                                                                        col=4,
                                                                                                        content=ft.ResponsiveRow(
                                                                                                            controls=[
                                                                                                                ft.Container(
                                                                                                                    bgcolor=self.color_teal_2,
                                                                                                                    padding=2.5,
                                                                                                                    border_radius=5,
                                                                                                                    content=ft.TextField(height=30, width=50, color="black", text_size=13, text_align="center", label="Final", label_style=ft.TextStyle(color="#545454", size=10), content_padding=3, bgcolor="white", cursor_height=18, cursor_color="#747474", focused_border_color="black", focused_border_width=2, hint_text="Botes", hint_style=ft.TextStyle(color="#DADADA", size=10)),
                                                                                                                )
                                                                                                            ]
                                                                                                        )
                                                                                                    ),
                                                                                                    ft.Container(
                                                                                                        col=4,
                                                                                                        content=ft.ResponsiveRow(
                                                                                                            controls=[
                                                                                                                ft.Container(
                                                                                                                    bgcolor="#f00000",
                                                                                                                    padding=2.5,
                                                                                                                    border_radius=5,
                                                                                                                    content=ft.TextField(height=30, width=50, color="black", text_size=13, text_align="center", label="Vendidos", label_style=ft.TextStyle(color="#545454", size=10), content_padding=3, bgcolor="white", cursor_height=18, cursor_color="#747474", focused_border_color="black", focused_border_width=2, hint_text="Botes", hint_style=ft.TextStyle(color="#DADADA", size=10)),
                                                                                                                )
                                                                                                            ]
                                                                                                        )
                                                                                                    ),
                                                                                                ]
                                                                                            )
                                                                                        ]
                                                                                    )
                                                                                )
                                                                            ]
                                                                        ),
                                                                        ft.Column(
                                                                            col=4,
                                                                            controls=[
                                                                                ft.ResponsiveRow(
                                                                                    controls=[
                                                                                        ft.Container(
                                                                                            # bgcolor="black",
                                                                                            alignment=ft.alignment.center,
                                                                                            content=ft.Column(
                                                                                                controls=[
                                                                                                    ft.Container(
                                                                                                        # bgcolor="blue",
                                                                                                        content=ft.Text("Crema de Chocolate")
                                                                                                    )
                                                                                                ]
                                                                                            )
                                                                                        ),
                                                                                    ]
                                                                                ),
                                                                                ft.Container(
                                                                                    margin=ft.margin.symmetric(horizontal=20, vertical=0),
                                                                                    content=ft.Column(
                                                                                        controls=[
                                                                                            ft.ResponsiveRow(
                                                                                                alignment=ft.MainAxisAlignment.CENTER,
                                                                                                spacing=20,
                                                                                                vertical_alignment="center",
                                                                                                controls=[
                                                                                                    ft.Container(
                                                                                                        col=4,
                                                                                                        content=ft.ResponsiveRow(
                                                                                                            controls=[
                                                                                                                ft.Container(
                                                                                                                    bgcolor=self.color_teal_2,
                                                                                                                    padding=2.5,
                                                                                                                    border_radius=5,
                                                                                                                    content=ft.TextField(height=30, width=50, color="black", text_size=13, text_align="center", label="Inicial", label_style=ft.TextStyle(color="#545454", size=10), content_padding=3, bgcolor="white", cursor_height=18, cursor_color="#747474", focused_border_color="black", focused_border_width=2, hint_text="Botes", hint_style=ft.TextStyle(color="#DADADA", size=10)),
                                                                                                                )
                                                                                                            ]
                                                                                                        )
                                                                                                    ),
                                                                                                    ft.Container(
                                                                                                        col=4,
                                                                                                        content=ft.ResponsiveRow(
                                                                                                            controls=[
                                                                                                                ft.Container(
                                                                                                                    bgcolor=self.color_teal_2,
                                                                                                                    padding=2.5,
                                                                                                                    border_radius=5,
                                                                                                                    content=ft.TextField(height=30, width=50, color="black", text_size=13, text_align="center", label="Final", label_style=ft.TextStyle(color="#545454", size=10), content_padding=3, bgcolor="white", cursor_height=18, cursor_color="#747474", focused_border_color="black", focused_border_width=2, hint_text="Botes", hint_style=ft.TextStyle(color="#DADADA", size=10)),
                                                                                                                )
                                                                                                            ]
                                                                                                        )
                                                                                                    ),
                                                                                                    ft.Container(
                                                                                                        col=4,
                                                                                                        content=ft.ResponsiveRow(
                                                                                                            controls=[
                                                                                                                ft.Container(
                                                                                                                    bgcolor="#f00000",
                                                                                                                    padding=2.5,
                                                                                                                    border_radius=5,
                                                                                                                    content=ft.TextField(height=30, width=50, color="black", text_size=13, text_align="center", label="Vendidos", label_style=ft.TextStyle(color="#545454", size=10), content_padding=3, bgcolor="white", cursor_height=18, cursor_color="#747474", focused_border_color="black", focused_border_width=2, hint_text="Botes", hint_style=ft.TextStyle(color="#DADADA", size=10)),
                                                                                                                )
                                                                                                            ]
                                                                                                        )
                                                                                                    ),
                                                                                                ]
                                                                                            )
                                                                                        ]
                                                                                    )
                                                                                )
                                                                            ]
                                                                        ),
                                                                        ft.Column(
                                                                            col=4,
                                                                            controls=[
                                                                                ft.ResponsiveRow(
                                                                                    controls=[
                                                                                        ft.Container(
                                                                                            # bgcolor="black",
                                                                                            alignment=ft.alignment.center,
                                                                                            content=ft.Column(
                                                                                                controls=[
                                                                                                    ft.Container(
                                                                                                        # bgcolor="blue",
                                                                                                        content=ft.Text("Crema de Cafe")
                                                                                                    )
                                                                                                ]
                                                                                            )
                                                                                        ),
                                                                                    ]
                                                                                ),
                                                                                ft.Container(
                                                                                    margin=ft.margin.symmetric(horizontal=20, vertical=0),
                                                                                    content=ft.Column(
                                                                                        controls=[
                                                                                            ft.ResponsiveRow(
                                                                                                alignment=ft.MainAxisAlignment.CENTER,
                                                                                                spacing=20,
                                                                                                vertical_alignment="center",
                                                                                                controls=[
                                                                                                    ft.Container(
                                                                                                        col=4,
                                                                                                        content=ft.ResponsiveRow(
                                                                                                            controls=[
                                                                                                                ft.Container(
                                                                                                                    bgcolor=self.color_teal_2,
                                                                                                                    padding=2.5,
                                                                                                                    border_radius=5,
                                                                                                                    content=ft.TextField(height=30, width=50, color="black", text_size=13, text_align="center", label="Inicial", label_style=ft.TextStyle(color="#545454", size=10), content_padding=3, bgcolor="white", cursor_height=18, cursor_color="#747474", focused_border_color="black", focused_border_width=2, hint_text="Botes", hint_style=ft.TextStyle(color="#DADADA", size=10)),
                                                                                                                )
                                                                                                            ]
                                                                                                        )
                                                                                                    ),
                                                                                                    ft.Container(
                                                                                                        col=4,
                                                                                                        content=ft.ResponsiveRow(
                                                                                                            controls=[
                                                                                                                ft.Container(
                                                                                                                    bgcolor=self.color_teal_2,
                                                                                                                    padding=2.5,
                                                                                                                    border_radius=5,
                                                                                                                    content=ft.TextField(height=30, width=50, color="black", text_size=13, text_align="center", label="Final", label_style=ft.TextStyle(color="#545454", size=10), content_padding=3, bgcolor="white", cursor_height=18, cursor_color="#747474", focused_border_color="black", focused_border_width=2, hint_text="Botes", hint_style=ft.TextStyle(color="#DADADA", size=10)),
                                                                                                                )
                                                                                                            ]
                                                                                                        )
                                                                                                    ),
                                                                                                    ft.Container(
                                                                                                        col=4,
                                                                                                        content=ft.ResponsiveRow(
                                                                                                            controls=[
                                                                                                                ft.Container(
                                                                                                                    bgcolor="#f00000",
                                                                                                                    padding=2.5,
                                                                                                                    border_radius=5,
                                                                                                                    content=ft.TextField(height=30, width=50, color="black", text_size=13, text_align="center", label="Vendidos", label_style=ft.TextStyle(color="#545454", size=10), content_padding=3, bgcolor="white", cursor_height=18, cursor_color="#747474", focused_border_color="black", focused_border_width=2, hint_text="Botes", hint_style=ft.TextStyle(color="#DADADA", size=10)),
                                                                                                                )
                                                                                                            ]
                                                                                                        )
                                                                                                    ),
                                                                                                ]
                                                                                            )
                                                                                        ]
                                                                                    )
                                                                                )
                                                                            ]
                                                                        ),
                                                                    ]
                                                                ),
                                                            ]
                                                        )
                                                    ),
                                                ]
                                            )
                                        ),
                                    ]
                                )
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
                        # bgcolor="pink",
                        margin=ft.Margin(top=0, bottom=0, left=25, right=50),
                        border_radius=15,
                        padding=ft.Padding(top=5, bottom=5, left=5, right=10),
                        content=ft.ResponsiveRow(
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            vertical_alignment="center",
                            controls=[
                                ft.Container(
                                    col={"md":6, "lg":2.3},
                                    width=150,
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
                                                        # horizontal_alignment="start",
                                                        controls=[
                                                            ft.Text(value="$5"),
                                                            ft.Text(value="$10"),
                                                        ]
                                                    ),
                                                    ft.Column(
                                                        horizontal_alignment="start",
                                                        controls=[
                                                            ft.TextField(value="", width=50, height=25, content_padding=0, text_align="center", bgcolor="white"),
                                                            ft.TextField(value="", width=50, height=25, content_padding=0, text_align="center", bgcolor="white"),
                                                        ]
                                                    )
                                                ]
                                            )
                                        ]
                                    )
                                ),
                                ft.Container(
                                    col={"md":6, "lg":2.3},
                                    width=160,
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
                                                        horizontal_alignment="center",
                                                        controls=[
                                                            ft.Text(value="$20"),
                                                            ft.Text(value="$35"),
                                                        ]
                                                    ),
                                                    ft.Column(
                                                        horizontal_alignment="center",
                                                        controls=[
                                                            ft.TextField(value="", width=50, height=25, content_padding=0, text_align="center", bgcolor="white"),
                                                            ft.TextField(value="", width=50, height=25, content_padding=0, text_align="center", bgcolor="white"),
                                                        ]
                                                    ),
                                                ]
                                            )
                                        ]
                                    )
                                ),
                                ft.Container(
                                    col={"md":6, "lg":2.3},
                                    width=250,
                                    alignment=ft.alignment.center,
                                    # bgcolor="blue",
                                    content=ft.Column(
                                        horizontal_alignment="center",
                                        controls=[
                                            ft.Text(value="Transferencias"),
                                            ft.Container(
                                                padding=ft.padding.only(left=14),
                                                content=ft.Row(
                                                    alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                                                    controls=[
                                                        ft.Column(
                                                            # horizontal_alignment="center",
                                                            controls=[
                                                                ft.Text(value="No. Transferencias"),
                                                                ft.Text(value="Monto Total"),
                                                            ]
                                                        ),
                                                        ft.Column(
                                                            horizontal_alignment="center",
                                                            controls=[
                                                                ft.TextField(value="", width=50, height=25, content_padding=0, text_align="center", bgcolor="white"),
                                                                ft.Container(
                                                                    margin=ft.margin.only(right=18),
                                                                    content=ft.Row(
                                                                        controls=[
                                                                            ft.Text(value="$"),
                                                                            ft.TextField(value="", width=50, height=25, content_padding=0, text_align="center", bgcolor="white"),
                                                                        ]
                                                                    )
                                                                )
                                                            ]
                                                        ),
                                                    ]
                                                )
                                            )
                                        ]
                                    )
                                ),
                                ft.Container(
                                    col={"md":6, "lg":2.3},
                                    width=250,
                                    # bgcolor="blue",
                                    content=ft.Column(
                                        horizontal_alignment="center",
                                        controls=[
                                            ft.Text(value="Gastos / Retiros"),
                                            ft.Container(
                                                padding=ft.padding.only(left=12),
                                                content=ft.Row(
                                                alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                                                    controls=[
                                                        ft.Column(
                                                            controls=[
                                                                ft.Text(value="No. Gastos / Retiros"),
                                                                ft.Text(value="Monto Total"),
                                                            ]
                                                        ),
                                                        ft.Column(
                                                            horizontal_alignment="center",
                                                            controls=[
                                                                ft.TextField(value="", width=50, height=25, content_padding=0, text_align="center", bgcolor="white"),
                                                                ft.Container(
                                                                    margin=ft.margin.only(right=18),
                                                                    content=ft.Row(
                                                                        controls=[
                                                                            ft.Text(value="$"),
                                                                            ft.TextField(value="", width=50, height=25, content_padding=0, text_align="center", bgcolor="white"),
                                                                        ]
                                                                    )
                                                                )
                                                            ]
                                                        ),
                                                    ]
                                                )
                                            )
                                        ]
                                    )
                                ),
                                ft.Container(
                                    col={"md":6, "lg":2.3},
                                    # bgcolor="blue",
                                    width=200,
                                    content=ft.Column(
                                        horizontal_alignment="center",
                                        controls=[
                                            ft.Column(
                                                controls=[
                                                    ft.Text("Balance")
                                                ]
                                            ),
                                            ft.Row(
                                                alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                                                controls=[
                                                    ft.Column(
                                                        controls=[
                                                            ft.Text("Diferencia"),
                                                            ft.Text("Total día PV")
                                                        ]
                                                    ),
                                                    ft.Column(
                                                        horizontal_alignment="center",
                                                        controls=[
                                                            ft.Container(
                                                                padding=ft.padding.only(left=16),
                                                                content=ft.Row(
                                                                    controls=[
                                                                        ft.TextField(value="", width=50, height=25, content_padding=0, text_align="center", bgcolor="white"),
                                                                    ]
                                                                )
                                                            ),
                                                            ft.Container(
                                                                # margin=ft.margin.only(right=18),
                                                                content=ft.Row(
                                                                    controls=[
                                                                        ft.Text(value="$"),
                                                                        ft.TextField(value="", width=50, height=25, content_padding=0, text_align="center", bgcolor="white"),
                                                                    ]
                                                                )
                                                            )
                                                        ]
                                                    ),
                                                ]
                                            ),
                                        ]
                                    )
                                )
                                
                            ]
                        )
                    )
                ]
            )
        )

        # ***** AREA DE CAPTURA DE VENTAS / ICONO VENTAS *****

        self.sales = ft.Container(
            col=11.25,
            bgcolor=self.color_teal_2,
            expand=True,
            content=ft.Column(
                expand=True,
                controls=[
                    ft.ResponsiveRow(
                        alignment=ft.MainAxisAlignment.CENTER,
                        vertical_alignment="center",
                        controls=[
                            ft.Column(
                                controls=[
                                    ft.Container(
                                        col=12,
                                        content=ft.TextField(value="PRUEBA", text_size=100, text_align="center")
                                    )
                                ]
                            )
                        ]
                    )
                ]
            )
        )

        self.pages_containers = [self.home, self.sales]

        self.container_1 = ft.Container(self.pages_containers[0], expand=True)

        # ***** FILA PRINCIPAL DE LA PAGINA (ABARCA TODA LA VENTANA Y ES DONDE SE PONE CADA UNA DE LAS SECCIONES QUE VAN A VERSE EN LA PAGINA) *****

        self.main_pages = ft.ResponsiveRow(
            controls=[
                self.navigation_bar,
                self.home,
            ]
            
        )

        self.sales_container = ft.ResponsiveRow(
            controls=[
                self.navigation_bar,
                self.sales,
            ]
        )

    def change_page(self, e):
        index = e.control.selected_index
        self.container_1.content = self.pages_containers[index]
        print(index)


    # ***** FUNCTION CONSTRUCTORA (NO ME QUEDA CLARO PARA QUE Y PORQUE SE HACE, TENGO QUE INVESTIGAR A FONDO) *****

    def build(self):
        return self.main_pages

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


# ***** Web Mode *****
# ft.app(target=main, view=ft.WEB_BROWSER)

# ***** Desktop Mode *****
ft.app(target=main)