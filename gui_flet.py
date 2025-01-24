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

        # ***** VARIABLES SISTEMA *****

        # ***** Variables sucursales *****

        self.glorieta = ft.Radio(value="cofradia3", label="Glorieta", label_style=ft.TextStyle(size=12), visual_density=ft.VisualDensity.STANDARD, fill_color={
                ft.ControlState.DEFAULT: ft.Colors.PINK,
                ft.ControlState.SELECTED: ft.Colors.GREEN,
            }
        )

        self.sanmiguel = ft.Radio(value="sanmiguel", label="San Miguel", label_style=ft.TextStyle(size=12), visual_density=ft.VisualDensity.STANDARD, fill_color={
                ft.ControlState.DEFAULT: ft.Colors.PINK,
                ft.ControlState.SELECTED: ft.Colors.GREEN,
            }
        )

        self.vips = ft.Radio(value="vips", label="Vips", label_style=ft.TextStyle(size=12), visual_density=ft.VisualDensity.STANDARD, fill_color={
                ft.ControlState.DEFAULT: ft.Colors.PINK,
                ft.ControlState.SELECTED: ft.Colors.GREEN,
            }
        )

        self. cofradia2 = ft.Radio(value="cofradia2", label="Cofradía 2", label_style=ft.TextStyle(size=12), visual_density=ft.VisualDensity.STANDARD, fill_color={
                ft.ControlState.DEFAULT: ft.Colors.PINK,
                ft.ControlState.SELECTED: ft.Colors.GREEN,
            }
        )

        self.ensuenos = ft.Radio(value="ensueños", label="Ensueños", label_style=ft.TextStyle(size=12), visual_density=ft.VisualDensity.STANDARD, fill_color={
                ft.ControlState.DEFAULT: ft.Colors.PINK,
                ft.ControlState.SELECTED: ft.Colors.GREEN,
            }
        )

        self.operagua = ft.Radio(value="operagua", label="Operagua", label_style=ft.TextStyle(size=12), visual_density=ft.VisualDensity.STANDARD, fill_color={
                ft.ControlState.DEFAULT: ft.Colors.PINK,
                ft.ControlState.SELECTED: ft.Colors.GREEN,
            }
        )

        self.sanantonio = ft.Radio(value="sanantonio", label="San Antonio", label_style=ft.TextStyle(size=12), visual_density=ft.VisualDensity.STANDARD, fill_color={
                ft.ControlState.DEFAULT: ft.Colors.PINK,
                ft.ControlState.SELECTED: ft.Colors.GREEN,
            }
        )

        self.lapiedad = ft.Radio(value="lapiedad", label="La Piedad", label_style=ft.TextStyle(size=12), visual_density=ft.VisualDensity.STANDARD, fill_color={
                ft.ControlState.DEFAULT: ft.Colors.PINK,
                ft.ControlState.SELECTED: ft.Colors.GREEN,
            }
        )

        self.pdv = ft.RadioGroup(
            on_change=self.pdv_selection,
            content=ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                expand=True,
                controls=[
                    self.glorieta,
                    self.sanmiguel,
                    self.vips,
                    self.cofradia2,
                    self.ensuenos,
                    self.operagua,
                    self.sanantonio,
                    self.lapiedad 
                ]
            )
        )

        # ***** Variables Vasos Chicos *****

        self.vcti = ft.TextField(height=30, width=80, color="black", text_size=13, text_align="center", label="Iniciales", label_style=ft.TextStyle(color="#545454", size=10), content_padding=3, bgcolor="white", cursor_height=18, cursor_color="#747474", focused_border_color="black", focused_border_width=2, on_change=self.valor_vcti)
        

        self.vctf = ft.TextField(height=30, width=80, color="black", text_size=13, text_align="center", label="Finales", label_style=ft.TextStyle(color="#545454", size=10), content_padding=3, bgcolor="white", cursor_height=18, cursor_color="#747474", focused_border_color="black", focused_border_width=2, on_change=self.valor_vctf)
        

        self.tcdif = ft.TextField(height=30, width=80, color="black", text_size=13, text_align="center", label="Diferencia", label_style=ft.TextStyle(color="#545454", size=10), content_padding=3, bgcolor="white", cursor_height=18, cursor_color="#747474", focused_border_color="black", focused_border_width=2, read_only=True, value="")

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
            alignment=ft.alignment.center,
            padding=ft.Padding(top=0, bottom=5, left=0, right=0),
            col=12,
            bgcolor=ft.colors.BLUE_GREY_800,
            border_radius=5,
            expand=True,
            content=ft.Column(
                expand=True, 
                controls=[
                    ft.Container(
                        padding=ft.Padding(top=5, bottom=0, left=10, right=25),
                        # bgcolor="black",
                        content=self.pdv
                    ),
                    ft.Container(
                        margin=ft.Margin(right=15, left=15, top=0, bottom=0),
                        bgcolor=self.color_teal,
                        height=2,
                        border_radius=2.5
                    ),
                    ft.Container(
                        alignment=ft.alignment.center,
                        margin=ft.Margin(top=0, bottom=0, left=45, right=50),
                        padding=ft.Padding(top=5, bottom=5, left=0, right=0),
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
                                                            ft.Container(# Vasos Chicos
                                                                alignment=ft.alignment.center,
                                                                # bgcolor=self.color_teal_2,
                                                                # border_radius=20,
                                                                content=ft.ResponsiveRow(
                                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                                    vertical_alignment="center",
                                                                    controls=[
                                                                        ft.Container(# Vasos Chicos
                                                                            padding=2,
                                                                            alignment=ft.alignment.center,
                                                                            col=4,
                                                                            # bgcolor="yellow",
                                                                            content=ft.Container( # Vasos Chicos
                                                                                bgcolor=self.color_teal_2,
                                                                                padding=2.5,
                                                                                border_radius=5,
                                                                                content=self.vcti
                                                                            )
                                                                        ),
                                                                        ft.Container(# Vasos Chicos
                                                                            padding=2,
                                                                            alignment=ft.alignment.center,
                                                                            col=4,
                                                                            # bgcolor="yellow",
                                                                            content=ft.Container(# Vasos Chicos
                                                                                bgcolor=self.color_teal_2,
                                                                                padding=2.5,
                                                                                border_radius=5,
                                                                                content=ft.TextField(height=30, width=80, color="black", text_size=13, text_align="center", label="Iniciales", label_style=ft.TextStyle(color="#545454", size=10), content_padding=3, bgcolor="white", cursor_height=18, cursor_color="#747474", focused_border_color="black", focused_border_width=2),
                                                                            ),
                                                                        ),
                                                                        ft.Container(# Vasos Chicos
                                                                            padding=2,
                                                                            alignment=ft.alignment.center,
                                                                            col=4,
                                                                            # bgcolor="yellow",
                                                                            content=ft.Container(# Vasos Chicos
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
                                                                # border_radius=20,
                                                                content=ft.ResponsiveRow(
                                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                                    vertical_alignment="center",
                                                                    controls=[
                                                                        ft.Container(# Vasos Chicos
                                                                            padding=2,
                                                                            alignment=ft.alignment.center,
                                                                            col=4,
                                                                            # bgcolor="yellow",
                                                                            content=ft.Container(# Vasos Chicos
                                                                                bgcolor=self.color_teal_2,
                                                                                padding=2.5,
                                                                                border_radius=5,
                                                                                content=self.vctf
                                                                            ),
                                                                        ),
                                                                        ft.Container(# Vasos Chicos
                                                                            padding=2,
                                                                            alignment=ft.alignment.center,
                                                                            col=4,
                                                                            # bgcolor="yellow",
                                                                            content=ft.Container(# Vasos Chicos
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
                                                                            content=ft.Container(# Vasos Chicos
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
                                                                # border_radius=20,
                                                                content=ft.ResponsiveRow(
                                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                                    vertical_alignment="center",
                                                                    controls=[
                                                                        ft.Container(# Vasos Chicos
                                                                            padding=2,
                                                                            alignment=ft.alignment.center,
                                                                            col=4,
                                                                            # bgcolor="yellow",
                                                                            content=ft.Container(# Vasos Chicos
                                                                                bgcolor=self.color_teal_2,
                                                                                padding=2.5,
                                                                                border_radius=5,
                                                                                content=self.tcdif
                                                                            ),
                                                                        ),
                                                                        ft.Container(# Vasos Chicos
                                                                            padding=2,
                                                                            alignment=ft.alignment.center,
                                                                            col=4,
                                                                            # bgcolor="yellow",
                                                                            content=ft.Container(# Vasos Chicos
                                                                                bgcolor=self.color_teal_2,
                                                                                padding=2.5,
                                                                                border_radius=5,
                                                                                content=ft.TextField(height=30, width=80, color="black", text_size=13, text_align="center", label="Diferencia", label_style=ft.TextStyle(color="#545454", size=10), content_padding=3, bgcolor="white", cursor_height=18, cursor_color="#747474", focused_border_color="black", focused_border_width=2, read_only=True),
                                                                            ),
                                                                        ),
                                                                        ft.Container(# Vasos Chicos
                                                                            padding=2,
                                                                            alignment=ft.alignment.center,
                                                                            col=4,
                                                                            # bgcolor="yellow",
                                                                            content=ft.Container(# Vasos Chicos
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
                                                                # border_radius=20,
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
                                                                # border_radius=20,
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
                                                                # border_radius=20,
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
                                                                # border_radius=20,
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
                                                                # border_radius=20,
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
                                                                # border_radius=20,
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
                        alignment=ft.alignment.center,
                        # bgcolor="pink",
                        margin=ft.Margin(top=0, bottom=0, left=50, right=50),
                        padding=ft.Padding(top=0, bottom=0, left=5, right=10),
                        border_radius=15,
                        content=ft.Column(
                            scroll=ft.ScrollMode.AUTO,
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            horizontal_alignment="center",
                            controls=[
                                ft.ResponsiveRow(
                                    vertical_alignment="center",
                                    controls=[
                                        ft.Container(
                                            padding=2,
                                            alignment=ft.alignment.center,
                                            # bgcolor="black",
                                            content=ft.Column(
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
                                            padding=ft.Padding(top=5, bottom=5, left=55, right=65),
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
                                            # bgcolor="black",
                                            content=ft.Column(
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
                                                    )
                                                ]
                                            )
                                        ),
                                        ft.Container(
                                            padding=2,
                                            alignment=ft.alignment.center,
                                            # bgcolor="blue",
                                            content=ft.Column(
                                                alignment=ft.MainAxisAlignment.CENTER,
                                                horizontal_alignment="center",
                                                controls=[
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
                        padding=ft.Padding(top=3, bottom=5, left=5, right=10),
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
            col=12,
            bgcolor=ft.colors.BLUE_GREY_800,
            border_radius=10,
            content=ft.Container(
                margin=10,
                # bgcolor="pink",
                content=ft.Column(
                    controls=[
                        ft.ResponsiveRow(
                            controls=[
                                ft.Column(
                                    col=12,
                                    horizontal_alignment="center",
                                    controls=[
                                        ft.Container(
                                            padding=10,
                                            # bgcolor="black",
                                            content=ft.Text("VENTAS Y REPORTES", size=30, color="#ff1765", weight=ft.FontWeight.BOLD)
                                        )
                                    ]
                                ),
                                ft.Column(
                                    col=12,
                                    controls=[
                                        ft.Container(
                                            margin=ft.Margin(right=15, left=15, top=0, bottom=0),
                                            bgcolor=self.color_teal,
                                            height=2,
                                            border_radius=2.5
                                        ),
                                    ]
                                ),
                                ft.Column(
                                    col=12,
                                    controls=[
                                        ft.Container(
                                            # bgcolor="pink",
                                            margin=ft.margin.only(top=20),
                                            padding=ft.padding.symmetric(horizontal=50, vertical=0),
                                            content=ft.ResponsiveRow(
                                                spacing=50,
                                                alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                                                vertical_alignment="center",
                                                controls=[
                                                    ft.Container(
                                                        col=3,
                                                        alignment=ft.alignment.center,
                                                        # bgcolor="black",
                                                        content=ft.Dropdown(
                                                            bgcolor="black",
                                                            color="white",
                                                            fill_color="#555555",
                                                            # fill_color=self.color_teal,
                                                            filled=True,
                                                            label_style=ft.TextStyle(color="white"),
                                                            border_color=self.color_teal,
                                                            border_width=1.5,
                                                            focused_border_color=self.color_teal_2,
                                                            focused_border_width=3,
                                                            label="Ventas / Reportes",
                                                            hint_text="Selecciona una opción",
                                                            options=[
                                                                ft.dropdown.Option("Ventas"),
                                                                ft.dropdown.Option("Reportes"),
                                                            ]
                                                        )
                                                    ),
                                                    ft.Container(
                                                        col=3,
                                                        alignment=ft.alignment.center,
                                                        # bgcolor="black",
                                                        content=ft.Dropdown(
                                                            bgcolor="black",
                                                            color="white",
                                                            fill_color="#555555",
                                                            # fill_color=self.color_teal,
                                                            filled=True,
                                                            label_style=ft.TextStyle(color="white"),
                                                            border_color=self.color_teal,
                                                            border_width=1.5,
                                                            focused_border_color=self.color_teal_2,
                                                            focused_border_width=3,
                                                            label="Dia",
                                                            hint_text="Selecciona el día",
                                                            options=[
                                                                ft.dropdown.Option("1"),
                                                                ft.dropdown.Option("2"),
                                                                ft.dropdown.Option("3"),
                                                                ft.dropdown.Option("4"),
                                                                ft.dropdown.Option("5"),
                                                                ft.dropdown.Option("6"),
                                                                ft.dropdown.Option("7"),
                                                                ft.dropdown.Option("8"),
                                                                ft.dropdown.Option("9"),
                                                                ft.dropdown.Option("10"),
                                                                ft.dropdown.Option("11"),
                                                                ft.dropdown.Option("12"),
                                                                ft.dropdown.Option("13"),
                                                                ft.dropdown.Option("14"),
                                                                ft.dropdown.Option("15"),
                                                                ft.dropdown.Option("16"),
                                                                ft.dropdown.Option("17"),
                                                                ft.dropdown.Option("18"),
                                                                ft.dropdown.Option("19"),
                                                                ft.dropdown.Option("20"),
                                                                ft.dropdown.Option("21"),
                                                                ft.dropdown.Option("22"),
                                                                ft.dropdown.Option("23"),
                                                                ft.dropdown.Option("24"),
                                                                ft.dropdown.Option("25"),
                                                                ft.dropdown.Option("26"),
                                                                ft.dropdown.Option("27"),
                                                                ft.dropdown.Option("28"),
                                                                ft.dropdown.Option("29"),
                                                                ft.dropdown.Option("30"),
                                                                ft.dropdown.Option("31"),
                                                            ]
                                                        )
                                                    ),
                                                    ft.Container(
                                                        col=3,
                                                        alignment=ft.alignment.center,
                                                        # bgcolor="black",
                                                        content=ft.Dropdown(
                                                            bgcolor="black",
                                                            color="white",
                                                            fill_color="#555555",
                                                            # fill_color=self.color_teal,
                                                            filled=True,
                                                            label_style=ft.TextStyle(color="white"),
                                                            border_color=self.color_teal,
                                                            border_width=1.5,
                                                            focused_border_color=self.color_teal_2,
                                                            focused_border_width=3,
                                                            label="Mes",
                                                            hint_text="Selecciona el Mes",
                                                            options=[
                                                                ft.dropdown.Option("Enero"),
                                                                ft.dropdown.Option("Febrero"),
                                                                ft.dropdown.Option("Marzo"),
                                                                ft.dropdown.Option("Abril"),
                                                                ft.dropdown.Option("Mayo"),
                                                                ft.dropdown.Option("Junio"),
                                                                ft.dropdown.Option("Julio"),
                                                                ft.dropdown.Option("Agosto"),
                                                                ft.dropdown.Option("Septiembre"),
                                                                ft.dropdown.Option("Octubre"),
                                                                ft.dropdown.Option("Noviembre"),
                                                                ft.dropdown.Option("Diciembre"),
                                                            ]
                                                        )
                                                    ),
                                                    ft.Container(
                                                        col=3,
                                                        padding=5,
                                                        # border_radius=5,
                                                        alignment=ft.alignment.center,
                                                        # bgcolor=self.color_teal,
                                                        content=ft.Dropdown(
                                                            bgcolor="black",
                                                            color="white",
                                                            fill_color="#555555",
                                                            # fill_color=self.color_teal,
                                                            filled=True,
                                                            label="Año",
                                                            label_style=ft.TextStyle(color="white"),
                                                            border_color=self.color_teal,
                                                            border_width=1.5,
                                                            focused_border_color=self.color_teal_2,
                                                            focused_border_width=3,
                                                            hint_text="Selecciona el Año",
                                                            options=[
                                                                ft.dropdown.Option("2024"),
                                                                ft.dropdown.Option("2025"),
                                                            ]
                                                        )
                                                    ),
                                                ]
                                            )
                                        )
                                    ]
                                ),
                            ]
                        ),
                        ft.Column(
                            expand=True,
                            controls=[
                                ft.Container(
                                    margin=ft.margin.symmetric(horizontal=80, vertical=0),
                                    # bgcolor="black",
                                    expand=True,
                                    content=ft.ResponsiveRow(
                                        controls=[
                                            ft.Container(
                                                padding=20,
                                                alignment=ft.alignment.center,
                                                col=4,
                                                # bgcolor=self.color_teal,
                                                content=ft.Container(
                                                    bgcolor=self.color_teal,
                                                    alignment=ft.alignment.center,
                                                    border_radius=5,
                                                    padding=4,
                                                    content=ft.TextField(bgcolor="white", multiline=True, min_lines=20, )
                                                )
                                            ),
                                            ft.Container(
                                                col=4,
                                                # bgcolor="black",
                                                content=ft.Column(
                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                    horizontal_alignment="center",
                                                    controls=[
                                                        ft.Container(
                                                            # bgcolor=self.color_teal,
                                                            # border_radius=10,
                                                            # padding=20,
                                                            content=ft.Column(
                                                                alignment=ft.MainAxisAlignment.CENTER,
                                                                horizontal_alignment="center",
                                                                controls=[
                                                                    ft.Container(
                                                                        alignment=ft.alignment.center,
                                                                        padding=15,
                                                                        content=ft.ElevatedButton(text="Cargar Archivo", bgcolor=self.color_teal, color="black", icon=ft.Icons.ADD),
                                                                    ),
                                                                    ft.Container(
                                                                        alignment=ft.alignment.center,
                                                                        padding=15,
                                                                        content=ft.ElevatedButton(text="Exportar Archivo", bgcolor=self.color_teal, color="black", icon=ft.Icons.UPLOAD),
                                                                    ),
                                                                    ft.Container(
                                                                        alignment=ft.alignment.center,
                                                                        padding=15,
                                                                        content=ft.ElevatedButton(text="Borrar Archivo", bgcolor=self.color_teal, color="black", icon=ft.Icons.DELETE),
                                                                    ),
                                                                    ft.Container(
                                                                        alignment=ft.alignment.center,
                                                                        padding=15,
                                                                        content=ft.ElevatedButton(text="Limpiar Campos", bgcolor=self.color_teal, color="black", icon=ft.Icons.CLEAR_ALL),
                                                                    ),
                                                                ]
                                                            )
                                                        )
                                                    ]
                                                )
                                            ),
                                            ft.Container(
                                                padding=20,
                                                alignment=ft.alignment.center,
                                                col=4,
                                                # bgcolor=self.color_teal,
                                                content=ft.Container(
                                                    bgcolor=self.color_teal,
                                                    alignment=ft.alignment.center,
                                                    border_radius=5,
                                                    padding=4,
                                                    content=ft.TextField(bgcolor="white", multiline=True, min_lines=20)
                                                )
                                            ),
                                        ]
                                    )
                                )
                            ]
                        )
                    ]
                )
            )
        )

        # ***** Paginas de los respectivos elementos laterales encerrados en una lista para el control de estas con los elementos laterales *****

        self.pages_containers = [self.home, self.sales]

        # ***** Seleccion de la pagina a mostrar mediante el index relacionado con el NavigationRail *****

        self.main_container = ft.Container(content=self.pages_containers[0], expand=True)

        # ***** Variable principal encargada de almacenar las diferentes paginas relacionadas con los elementos laterales *****

        self.pages = ft.Container(
            col=11.25,
            expand=True,
            content=ft.Column(
                controls=[
                    self.main_container
                ]
            )
        )

        # ***** FILA PRINCIPAL DE LA PAGINA (ABARCA TODA LA VENTANA Y ES DONDE SE PONE CADA UNA DE LAS SECCIONES QUE VAN A VERSE EN LA PAGINA) *****

        self.main_pages = ft.ResponsiveRow(
            controls=[
                self.navigation_bar,
                self.pages,
            ]
            
        )

        # self.sales_container = ft.ResponsiveRow(
        #     controls=[
        #         self.navigation_bar,
        #         self.sales,
        #     ]
        # )

    def valor_vcti(self, e):
        self.num_vcti = int(self.vcti.value)
        print(self.num_vcti)
        print(type(self.num_vcti))
        self.update()

    def valor_vctf(self, e):
        self.num_vctf = int(self.vctf.value)
        print(self.num_vctf)
        print(type(self.num_vctf))
        self.num_tcdif = self.num_vcti - self.num_vctf
        print(self.num_tcdif)
        print(type(self.num_tcdif))
        self.tcdif.value = self.num_tcdif
        self.update()

    def pdv_selection(self, e):
        print(f"La sucursal seleccionada es: {e.control.value}")

        if e.control.value == "cofradia3":
            print("Sucursal Glorieta")

    def change_page(self, e):
        index = e.control.selected_index
        self.main_container.content = self.pages_containers[index]
        self.update()
        print(index)


    # ***** FUNCTION CONSTRUCTORA (NO ME QUEDA CLARO PARA QUE Y PORQUE SE HACE, TENGO QUE INVESTIGAR A FONDO) *****

    def build(self):
        return self.main_pages

# ***** FUNCIÓN PRINCIPAL PARA CREAR LA VENTANA PRINCIPAL DE NUESTRO PROGRAMA O APP CON ALGUNAS CONFIGURACIONES EN ELLA COMO ALINEACION EN HORIZONTAL, COLOR DE FONDO, MEDIDA MINIMA EN ALTO Y ANCHO, TEMA PREDETERMINADO Y TÍTULO *****

def main(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
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