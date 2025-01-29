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

        # *** VARIABLES VENTANA INICIO ***

        # Variables sucursales

        self.glorieta = self.create_radio("glorieta", "Glorieta")

        self.sanmiguel = self.create_radio("sanmiguel", "San Miguel")

        self.vips = self.create_radio("vips", "vips")

        self. cofradia2 = self.create_radio("cofradia2", "Cofradía 2")

        self.ensuenos = self.create_radio("ensueños", "Ensueños")

        self.operagua = self.create_radio("operagua", "Operagua")

        self.sanantonio = self.create_radio("sanantonio", "San Antonio")

        self.lapiedad = self.create_radio("lapiedad", "La Piedad")

        self.pdv = ft.RadioGroup(
            on_change=self.pdv_selection,
            content=ft.Column(
                controls=[
                    ft.Row(
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
                ]
            )
        )

        # Variables Vasos Chicos

        # Opciones a configurar en la funcion create_textfield: Label, Color, text_Size, prefix_Text, prefix_Style, border_Color, border_Width, read_Only=False, on_Change=False

        self.tci = self.create_textfield("Iniciales", "black", 13, None, None, None, None, on_Change=self.conversion_n_capture_vc)
        self.tcf = self.create_textfield("Finales", "black", 13, None, None, None, None, on_Change=self.conversion_n_capture_vc)
        self.tcdif = self.create_textfield("Diferencia", "black", 13, None, None, None, None, read_Only=True)
        self.vci = self.create_textfield("Iniciales", "black", 13, None, None, None, None, on_Change=self.conversion_n_capture_vc)
        self.vcf = self.create_textfield("Finales", "black", 13, None, None, None, None, on_Change=self.conversion_n_capture_vc)
        self.vcdif = self.create_textfield("Diferencia", "black", 13, None, None, None, None, read_Only=True)
        self.vcsv = self.create_textfield("Sin Vender", "#dc0000", 15, None, None, None, None, read_Only=True)
        self.vcven = self.create_textfield("Vendidos", "#dc0000", 15, None, None, None, None, read_Only=True)
        self.vcvt = self.create_textfield("Venta Total", "#dc0000", 15, "  $", ft.TextStyle(color="black", size=13), "black", 1.5, read_Only=True)

        # Variables Vasos Medianos

        # Opciones a configurar en la funcion create_textfield: Label, Color, text_Size, prefix_Text, prefix_Style, border_Color, border_Width, read_Only=False, on_Change=False

        self.tmi = self.create_textfield("Iniciales", "black", 13, None, None, None, None, on_Change=self.conversion_n_capture_vm)
        self.tmf = self.create_textfield("Finales", "black", 13, None, None, None, None, on_Change=self.conversion_n_capture_vm)
        self.tmdif = self.create_textfield("Diferencia", "black", 13, None, None, None, None, read_Only=True)
        self.vmi = self.create_textfield("Iniciales", "black", 13, None, None, None, None, on_Change=self.conversion_n_capture_vm)
        self.vmf = self.create_textfield("Finales", "black", 13, None, None, None, None, on_Change=self.conversion_n_capture_vm)
        self.vmdif = self.create_textfield("Diferencia", "black", 13, None, None, None, None, read_Only=True)
        self.vmsv = self.create_textfield("Sin Vender", "#dc0000", 15, None, None, None, None, read_Only=True)
        self.vmven = self.create_textfield("Vendidos", "#dc0000", 15, None, None, None, None, read_Only=True)
        self.vmvt = self.create_textfield("Venta Total", "#dc0000", 15, "  $", ft.TextStyle(color="black", size=13), "black", 1.5, read_Only=True)

        # Variables Vasos Grandes

        # Opciones a configurar en la funcion create_textfield: Label, Color, text_Size, prefix_Text, prefix_Style, border_Color, border_Width, read_Only=False, on_Change=False

        self.tgi = self.create_textfield("Iniciales", "black", 13, None, None, None, None, on_Change=self.conversion_n_capture_vg)
        self.tgf = self.create_textfield("Finales", "black", 13, None, None, None, None, on_Change=self.conversion_n_capture_vg)
        self.tgdif = self.create_textfield("Diferencia", "black", 13, None, None, None, None, read_Only=True)
        self.vgi = self.create_textfield("Iniciales", "black", 13, None, None, None, None, on_Change=self.conversion_n_capture_vg)
        self.vgf = self.create_textfield("Finales", "black", 13, None, None, None, None, on_Change=self.conversion_n_capture_vg)
        self.vgdif = self.create_textfield("Diferencia", "black", 13, None, None, None, None, read_Only=True)
        self.vgsv = self.create_textfield("Sin Vender", "#dc0000", 15, None, None, None, None, read_Only=True)
        self.vgven = self.create_textfield("Vendidos", "#dc0000", 15, None, None, None, None, read_Only=True)
        self.vgvt = self.create_textfield("Venta Total", "#dc0000", 15, "  $", ft.TextStyle(color="black", size=13), "black", 1.5, read_Only=True)

        # ***** VARIABLES FRUTAS *****

        # Fresa

        """ self.fpi
        self.fpf
        self.fei
        self.fef
        self.fv """

        # Uva

        """ self.upi
        self.upf
        self.uei
        self.uef
        self.uv """

        # ***** VARIABLES CREMAS *****

        # Crema Original

        """ self.coi
        self.cof
        self.cov """

        # Crema Chocolate

        """ self.cchi
        self.cchf
        self.cchv """

        # Crema Cafe

        """ self.ccai
        self.ccaf
        self.ccav """
        
        # ***** VARIABLES ADICIONALES Y EXTRAS *****

        # Toppings Extras

        """ self.t5
        self.t10 """

        # Servicios a Domicilio

        """ self.sd20
        self.sd35 """

        # Transferencias

        """ self.num_tr
        self.mt_tr """

        # Gastos / Retiros

        """ self.num_gr
        self.mt_gr """

        # Balance

        """ self.dif
        self.td_pdv """

        # ***** VARIABLES VENTANA VENTAS *****

        # *** Variables Campos de texto y Botones ***

        # Campos de texto

        self.report_field = ft.TextField(bgcolor="white", multiline=True, min_lines=20)
        self.sales_field = ft.TextField(bgcolor="white", multiline=True, min_lines=20)

        # ***** BARRA DE NAVEGACION LATERAL IZQUIERDA *****

        self.navigation_bar = ft.Container(# Barra lateral de navegacion principal
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

        self.home = ft.Container(# Ventana Inicio
            alignment=ft.alignment.center,
            padding=ft.Padding(top=0, bottom=0, left=0, right=0),
            col=12,
            bgcolor=ft.colors.BLUE_GREY_800,
            border_radius=5,
            expand=True,
            content=ft.Column(
                scroll=ft.ScrollMode.AUTO,
                expand=True, 
                controls=[
                    ft.Container(# Puntos de venta
                        height=30,
                        padding=ft.Padding(top=0, bottom=0, left=10, right=25),
                        # bgcolor="#2a2a2a",
                        content=self.pdv
                    ),
                    ft.Container(# Separador de secciones
                        margin=ft.Margin(right=30, left=25, top=0, bottom=0),
                        bgcolor=self.color_teal,
                        height=2,
                        border_radius=2.5
                    ),
                    ft.Container(# Vasos
                        alignment=ft.alignment.center,
                        margin=ft.Margin(top=0, bottom=0, left=45, right=50),
                        padding=ft.Padding(top=0, bottom=0, left=0, right=0),
                        # expand=True,
                        # bgcolor="pink",
                        content=ft.ResponsiveRow(
                            controls=[
                                ft.Container( # Vasos Chicos
                                    # bgcolor="black",
                                    expand=True,
                                    col=4,
                                    content=ft.Container(# Vasos Chicos
                                        # bgcolor="blue",
                                        # margin=10,
                                        content=ft.Column(
                                            horizontal_alignment="center",
                                            controls=[
                                                ft.Container(# Vasos Chicos
                                                    alignment=ft.alignment.center,
                                                    # bgcolor="pink",
                                                    # border_radius=20,
                                                    width=180,
                                                    # height=30,
                                                    content=ft.Text("VASOS CHICOS", color="#ff1765", weight=ft.FontWeight.BOLD, size=15)
                                                ),
                                                ft.Container(# Vasos Chicos
                                                    # bgcolor=self.color_teal_2,
                                                    # border=ft.border.all(width=5, color=self.color_teal_2),
                                                    padding=ft.padding.symmetric(horizontal=15, vertical=0),
                                                    # border_radius=10,
                                                    content=ft.Column(
                                                        controls=[
                                                            ft.Container(# Vasos Chicos
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
                                                                        ft.Container(# Tapas chicas iniciales
                                                                            padding=2,
                                                                            alignment=ft.alignment.center,
                                                                            col=4,
                                                                            # bgcolor="yellow",
                                                                            content=ft.Container(
                                                                                bgcolor=self.color_teal_2,
                                                                                padding=2.5,
                                                                                border_radius=5,
                                                                                content=self.tci
                                                                            )
                                                                        ),
                                                                        ft.Container(# Vasos chicos iniciales
                                                                            padding=2,
                                                                            alignment=ft.alignment.center,
                                                                            col=4,
                                                                            # bgcolor="yellow",
                                                                            content=ft.Container(
                                                                                bgcolor=self.color_teal_2,
                                                                                padding=2.5,
                                                                                border_radius=5,
                                                                                content=self.vci
                                                                            ),
                                                                        ),
                                                                        ft.Container(# Vasos chicos sin vender
                                                                            padding=2,
                                                                            alignment=ft.alignment.center,
                                                                            col=4,
                                                                            # bgcolor="yellow",
                                                                            content=ft.Container(
                                                                                bgcolor=self.color_teal_2,
                                                                                padding=2.5,
                                                                                border_radius=5,
                                                                                content=self.vcsv
                                                                            ),
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
                                                                        ft.Container(# Tapas chicas finales
                                                                            padding=2,
                                                                            alignment=ft.alignment.center,
                                                                            col=4,
                                                                            # bgcolor="yellow",
                                                                            content=ft.Container(
                                                                                bgcolor=self.color_teal_2,
                                                                                padding=2.5,
                                                                                border_radius=5,
                                                                                content=self.tcf
                                                                            ),
                                                                        ),
                                                                        ft.Container(# Vasos chicos finales
                                                                            padding=2,
                                                                            alignment=ft.alignment.center,
                                                                            col=4,
                                                                            # bgcolor="yellow",
                                                                            content=ft.Container(# Vasos Chicos
                                                                                bgcolor=self.color_teal_2,
                                                                                padding=2.5,
                                                                                border_radius=5,
                                                                                content=self.vcf
                                                                            ),
                                                                        ),
                                                                        ft.Container(# Vasos chicos vendidos
                                                                            padding=2,
                                                                            alignment=ft.alignment.center,
                                                                            col=4,
                                                                            # bgcolor="yellow",
                                                                            content=ft.Container(
                                                                                bgcolor=self.color_teal_2,
                                                                                padding=2.5,
                                                                                border_radius=5,
                                                                                content=self.vcven
                                                                            ),
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
                                                                        ft.Container(# Diferencia tapas chicas
                                                                            padding=2,
                                                                            alignment=ft.alignment.center,
                                                                            col=4,
                                                                            # bgcolor="yellow",
                                                                            content=ft.Container(
                                                                                bgcolor=self.color_teal_2,
                                                                                padding=2.5,
                                                                                border_radius=5,
                                                                                content=self.tcdif
                                                                            ),
                                                                        ),
                                                                        ft.Container(# Diferencia vasos chicos
                                                                            padding=2,
                                                                            alignment=ft.alignment.center,
                                                                            col=4,
                                                                            # bgcolor="yellow",
                                                                            content=ft.Container(
                                                                                bgcolor=self.color_teal_2,
                                                                                padding=2.5,
                                                                                border_radius=5,
                                                                                content=self.vcdif
                                                                            ),
                                                                        ),
                                                                        ft.Container(# Venta total vasos chicos
                                                                            padding=2,
                                                                            alignment=ft.alignment.center,
                                                                            col=4,
                                                                            # bgcolor="yellow",
                                                                            content=ft.Container(
                                                                                bgcolor="#f00000",
                                                                                padding=2.5,
                                                                                border_radius=5,
                                                                                content=self.vcvt
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
                                ft.Container( # Vasos Medianos
                                    # bgcolor="black",
                                    expand=True,
                                    col=4,
                                    content=ft.Container( # Vasos Medianos
                                        # bgcolor="blue",
                                        # margin=10,
                                        content=ft.Column(
                                            horizontal_alignment="center",
                                            controls=[
                                                ft.Container( # Vasos Medianos
                                                    alignment=ft.alignment.center,
                                                    # bgcolor="pink",
                                                    # border_radius=20,
                                                    width=180,
                                                    # height=30,
                                                    content=ft.Text("VASOS MEDIANOS", color="#ff1765", weight=ft.FontWeight.BOLD, size=15)
                                                ),
                                                ft.Container( # Vasos Medianos
                                                    # bgcolor=self.color_teal_2,
                                                    # border=ft.border.all(width=5, color=self.color_teal_2),
                                                    padding=ft.padding.symmetric(horizontal=15, vertical=0),
                                                    border_radius=10,
                                                    content=ft.Column(
                                                        controls=[
                                                            ft.Container( # Vasos Medianos
                                                                alignment=ft.alignment.center,
                                                                # bgcolor=self.color_teal_2,
                                                                border_radius=20,
                                                                content=ft.ResponsiveRow(
                                                                    # alignment=ft.MainAxisAlignment.CENTER,
                                                                    # vertical_alignment="center",
                                                                    controls=[
                                                                        ft.Container(# Vasos Medianos
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
                                                            ft.Container(# Vasos Medianos
                                                                alignment=ft.alignment.center,
                                                                # bgcolor=self.color_teal_2,
                                                                # border_radius=20,
                                                                content=ft.ResponsiveRow(
                                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                                    vertical_alignment="center",
                                                                    controls=[
                                                                        ft.Container( # Tapas medianas iniciales
                                                                            padding=2,
                                                                            alignment=ft.alignment.center,
                                                                            col=4,
                                                                            # bgcolor="yellow",
                                                                            content=ft.Container(
                                                                                bgcolor=self.color_teal_2,
                                                                                padding=2.5,
                                                                                border_radius=5,
                                                                                content=self.tmi
                                                                            ),
                                                                        ),
                                                                        ft.Container( # Vasos medianos iniciales
                                                                            padding=2,
                                                                            alignment=ft.alignment.center,
                                                                            col=4,
                                                                            # bgcolor="yellow",
                                                                            content=ft.Container(
                                                                                bgcolor=self.color_teal_2,
                                                                                padding=2.5,
                                                                                border_radius=5,
                                                                                content=self.vmi
                                                                            ),
                                                                        ),
                                                                        ft.Container( # Vasos medianos sin vender
                                                                            padding=2,
                                                                            alignment=ft.alignment.center,
                                                                            col=4,
                                                                            # bgcolor="yellow",
                                                                            content=ft.Container(
                                                                                bgcolor=self.color_teal_2,
                                                                                padding=2.5,
                                                                                border_radius=5,
                                                                                content=self.vmsv
                                                                            ),
                                                                        ),
                                                                    ]
                                                                )
                                                            ),
                                                            ft.Container(# Vasos Medianos
                                                                alignment=ft.alignment.center,
                                                                # bgcolor=self.color_teal_2,
                                                                # border_radius=20,
                                                                content=ft.ResponsiveRow(
                                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                                    vertical_alignment="center",
                                                                    controls=[
                                                                        ft.Container( # Tapas medianas finales
                                                                            padding=2,
                                                                            alignment=ft.alignment.center,
                                                                            col=4,
                                                                            # bgcolor="yellow",
                                                                            content=ft.Container(
                                                                                bgcolor=self.color_teal_2,
                                                                                padding=2.5,
                                                                                border_radius=5,
                                                                                content=self.tmf
                                                                            ),
                                                                        ),
                                                                        ft.Container( # Vasos medianos finales
                                                                            padding=2,
                                                                            alignment=ft.alignment.center,
                                                                            col=4,
                                                                            # bgcolor="yellow",
                                                                            content=ft.Container(
                                                                                bgcolor=self.color_teal_2,
                                                                                padding=2.5,
                                                                                border_radius=5,
                                                                                content=self.vmf
                                                                            ),
                                                                        ),
                                                                        ft.Container( # Vasos medianos vendidos
                                                                            padding=2,
                                                                            alignment=ft.alignment.center,
                                                                            col=4,
                                                                            # bgcolor="yellow",
                                                                            content=ft.Container(
                                                                                bgcolor=self.color_teal_2,
                                                                                padding=2.5,
                                                                                border_radius=5,
                                                                                content=self.vmven
                                                                            ),
                                                                        ),
                                                                        
                                                                    ]
                                                                )
                                                            ),
                                                            ft.Container(# Vasos Medianos
                                                                alignment=ft.alignment.center,
                                                                # bgcolor=self.color_teal_2,
                                                                # border_radius=20,
                                                                content=ft.ResponsiveRow(
                                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                                    vertical_alignment="center",
                                                                    controls=[
                                                                        ft.Container( # Diferencia tapas medianas
                                                                            # padding=6,
                                                                            alignment=ft.alignment.center,
                                                                            col=4,
                                                                            # bgcolor="yellow",
                                                                            content=ft.Container(
                                                                                bgcolor=self.color_teal_2,
                                                                                padding=2.5,
                                                                                border_radius=5,
                                                                                content=self.tmdif
                                                                            ),
                                                                        ),
                                                                        ft.Container( # Diferencia vasos medianos
                                                                            # padding=6,
                                                                            alignment=ft.alignment.center,
                                                                            col=4,
                                                                            # bgcolor="yellow",
                                                                            content=ft.Container(
                                                                                bgcolor=self.color_teal_2,
                                                                                padding=2.5,
                                                                                border_radius=5,
                                                                                content=self.vmdif
                                                                            ),
                                                                        ),
                                                                        ft.Container( # Venta total vasos medianos
                                                                            # padding=6,
                                                                            alignment=ft.alignment.center,
                                                                            col=4,
                                                                            # bgcolor="yellow",
                                                                            content=ft.Container(
                                                                                bgcolor="#f00000",
                                                                                padding=2.5,
                                                                                border_radius=5,
                                                                                content=self.vmvt
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
                                ft.Container( # Vasos Grandes
                                    # bgcolor="black",
                                    expand=True,
                                    col=4,
                                    content=ft.Container( # Vasos Grandes
                                        # bgcolor="blue",
                                        # margin=10,
                                        content=ft.Column(
                                            horizontal_alignment="center",
                                            controls=[
                                                ft.Container( # Vasos Grandes
                                                    alignment=ft.alignment.center,
                                                    # bgcolor="pink",
                                                    # border_radius=20,
                                                    width=180,
                                                    # height=30,
                                                    content=ft.Text("VASOS GRANDES", color="#ff1765", weight=ft.FontWeight.BOLD, size=15)
                                                ),
                                                ft.Container( # Vasos Grandes
                                                    # bgcolor=self.color_teal_2,
                                                    # border=ft.border.all(width=5, color=self.color_teal_2),
                                                    padding=ft.padding.symmetric(horizontal=15, vertical=0),
                                                    border_radius=10,
                                                    content=ft.Column(
                                                        controls=[
                                                            ft.Container( # Vasos Grandes
                                                                alignment=ft.alignment.center,
                                                                # bgcolor=self.color_teal_2,
                                                                border_radius=20,
                                                                content=ft.ResponsiveRow(
                                                                    # alignment=ft.MainAxisAlignment.CENTER,
                                                                    # vertical_alignment="center",
                                                                    controls=[
                                                                        ft.Container( # Vasos Grandes
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
                                                            ft.Container( # Vasos Grandes
                                                                alignment=ft.alignment.center,
                                                                # bgcolor=self.color_teal_2,
                                                                # border_radius=20,
                                                                content=ft.ResponsiveRow(
                                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                                    vertical_alignment="center",
                                                                    controls=[
                                                                        ft.Container(# Tapas iniciales grandes
                                                                            # padding=6,
                                                                            alignment=ft.alignment.center,
                                                                            col=4,
                                                                            # bgcolor="yellow",
                                                                            content=ft.Container(
                                                                                bgcolor=self.color_teal_2,
                                                                                padding=2.5,
                                                                                border_radius=5,
                                                                                content=self.tgi
                                                                            ),
                                                                        ),
                                                                        ft.Container(# Vasos iniciales grandes
                                                                            # padding=6,
                                                                            alignment=ft.alignment.center,
                                                                            col=4,
                                                                            # bgcolor="yellow",
                                                                            content=ft.Container(
                                                                                bgcolor=self.color_teal_2,
                                                                                padding=2.5,
                                                                                border_radius=5,
                                                                                content=self.vgi
                                                                            ),
                                                                        ),
                                                                        ft.Container(# Vasos grandes sin vender
                                                                            # padding=6,
                                                                            alignment=ft.alignment.center,
                                                                            col=4,
                                                                            # bgcolor="yellow",
                                                                            content=ft.Container(
                                                                                bgcolor=self.color_teal_2,
                                                                                padding=2.5,
                                                                                border_radius=5,
                                                                                content=self.vgsv
                                                                            ),
                                                                        ),
                                                                    ]
                                                                )
                                                            ),
                                                            ft.Container( # Vasos Grandes
                                                                alignment=ft.alignment.center,
                                                                # bgcolor=self.color_teal_2,
                                                                # border_radius=20,
                                                                content=ft.ResponsiveRow(
                                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                                    vertical_alignment="center",
                                                                    controls=[
                                                                        ft.Container( # Vasos Grandes
                                                                            # padding=6,
                                                                            alignment=ft.alignment.center,
                                                                            col=4,
                                                                            # bgcolor="yellow",
                                                                            content=ft.Container(# Tapas grandes finales
                                                                                bgcolor=self.color_teal_2,
                                                                                padding=2.5,
                                                                                border_radius=5,
                                                                                content=self.tgf
                                                                            ),
                                                                        ),
                                                                        ft.Container( # Vasos Grandes
                                                                            # padding=6,
                                                                            alignment=ft.alignment.center,
                                                                            col=4,
                                                                            # bgcolor="yellow",
                                                                            content=ft.Container(# Vasos grandes finales
                                                                                bgcolor=self.color_teal_2,
                                                                                padding=2.5,
                                                                                border_radius=5,
                                                                                content=self.vgf
                                                                            ),
                                                                        ),
                                                                        ft.Container( # Vasos Grandes
                                                                            # padding=6,
                                                                            alignment=ft.alignment.center,
                                                                            col=4,
                                                                            # bgcolor="yellow",
                                                                            content=ft.Container(# Vasos grandes vendidos
                                                                                bgcolor=self.color_teal_2,
                                                                                padding=2.5,
                                                                                border_radius=5,
                                                                                content=self.vgven
                                                                            ),
                                                                        ),
                                                                        
                                                                    ]
                                                                )
                                                            ),
                                                            ft.Container( # Vasos Grandes
                                                                alignment=ft.alignment.center,
                                                                # bgcolor=self.color_teal_2,
                                                                # border_radius=20,
                                                                content=ft.ResponsiveRow(
                                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                                    vertical_alignment="center",
                                                                    controls=[
                                                                        ft.Container( # Vasos Grandes
                                                                            # padding=6,
                                                                            alignment=ft.alignment.center,
                                                                            col=4,
                                                                            # bgcolor="yellow",
                                                                            content=ft.Container(# Diferencia tapas grandes
                                                                                bgcolor=self.color_teal_2,
                                                                                padding=2.5,
                                                                                border_radius=5,
                                                                                content=self.tgdif
                                                                            ),
                                                                        ),
                                                                        ft.Container( # Vasos Grandes
                                                                            # padding=6,
                                                                            alignment=ft.alignment.center,
                                                                            col=4,
                                                                            # bgcolor="yellow",
                                                                            content=ft.Container(# Diferencia vasos grandes
                                                                                bgcolor=self.color_teal_2,
                                                                                padding=2.5,
                                                                                border_radius=5,
                                                                                content=self.vgdif
                                                                            ),
                                                                        ),
                                                                        ft.Container( # Vasos Grandes
                                                                            # padding=6,
                                                                            alignment=ft.alignment.center,
                                                                            col=4,
                                                                            # bgcolor="yellow",
                                                                            content=ft.Container(# Venta total vasos grandes
                                                                                bgcolor="#f00000",
                                                                                padding=2.5,
                                                                                border_radius=5,
                                                                                content=self.vgvt
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
                    ft.Container(# Separador de secciones
                        margin=ft.Margin(right=30, left=25, top=0, bottom=0),
                        bgcolor=self.color_teal,
                        height=2,
                        border_radius=2.5
                    ),
                    ft.Container(# Frutas y cremas
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
                                            alignment=ft.alignment.center,
                                            # bgcolor="black",
                                            content=ft.Column(
                                                horizontal_alignment="center",
                                                controls=[
                                                    ft.ResponsiveRow(
                                                        controls=[
                                                            ft.Container(
                                                                alignment=ft.alignment.center,
                                                                padding=ft.padding.only(right=10),
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
                                            padding=ft.Padding(top=0, bottom=0, left=55, right=65),
                                            # bgcolor="black",
                                            content=ft.Column(
                                                controls=[
                                                    ft.ResponsiveRow(
                                                        alignment=ft.MainAxisAlignment.CENTER,
                                                        vertical_alignment="center",
                                                        controls=[
                                                            ft.Container(
                                                                col=5.5,
                                                                # bgcolor="pink",
                                                                content=ft.Column(
                                                                    controls=[
                                                                        ft.Container(
                                                                            content=ft.Row(
                                                                                alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                                                                                controls=[
                                                                                    ft.Container(
                                                                                        bgcolor=self.color_teal_2,
                                                                                        padding=2.5,
                                                                                        border_radius=5,
                                                                                        content=ft.TextField(height=30, width=75, color="black", text_size=13, text_align="center", label="Picada Inicial", label_style=ft.TextStyle(color="#545454", size=10), content_padding=3, bgcolor="white", cursor_height=18, cursor_color="#747474", focused_border_color="black", focused_border_width=2, hint_text="Botes", hint_style=ft.TextStyle(color="#DADADA", size=10)),
                                                                                    ),
                                                                                    ft.Container(
                                                                                        bgcolor=self.color_teal_2,
                                                                                        padding=2.5,
                                                                                        border_radius=5,
                                                                                        content=ft.TextField(height=30, width=75, color="black", text_size=13, text_align="center", label="Picada Final", label_style=ft.TextStyle(color="#545454", size=10), content_padding=3, bgcolor="white", cursor_height=18, cursor_color="#747474", focused_border_color="black", focused_border_width=2, hint_text="Botes", hint_style=ft.TextStyle(color="#DADADA", size=10)),
                                                                                    ),
                                                                                ]
                                                                            )
                                                                        ),
                                                                        ft.Container(
                                                                            content=ft.Row(
                                                                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                                                                controls=[
                                                                                    ft.Container(
                                                                                        bgcolor="#6971ff",
                                                                                        padding=2.5,
                                                                                        border_radius=5,
                                                                                        content=ft.TextField(height=30, width=75, color="black", text_size=13, text_align="center", label="Remanente", label_style=ft.TextStyle(color="#545454", size=10), content_padding=3, bgcolor="white", cursor_height=18, cursor_color="#747474", focused_border_color="black", focused_border_width=2, hint_text="Botes", hint_style=ft.TextStyle(color="#DADADA", size=10), border_color="black", border_width=1.5),
                                                                                    ),
                                                                                    ft.Container(
                                                                                        width=100,
                                                                                        height=30,
                                                                                        alignment=ft.alignment.center,
                                                                                        content=ft.Text("Fresa", color="white", size=16),
                                                                                    ),
                                                                                    ft.Container(
                                                                                        bgcolor="#f00000",
                                                                                        padding=2.5,
                                                                                        border_radius=5,
                                                                                        content=ft.TextField(height=30, width=75, color="black", text_size=13, text_align="center", label="Vendida", label_style=ft.TextStyle(color="#545454", size=10), content_padding=3, bgcolor="white", cursor_height=18, cursor_color="#747474", focused_border_color="black", focused_border_width=2, hint_text="Botes", hint_style=ft.TextStyle(color="#DADADA", size=10), border_color="black", border_width=1.5),
                                                                                    ),
                                                                                ]
                                                                            )
                                                                        ),
                                                                        ft.Container(
                                                                            content=ft.Row(
                                                                                alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                                                                                controls=[
                                                                                    ft.Container(
                                                                                        bgcolor=self.color_teal_2,
                                                                                        padding=2.5,
                                                                                        border_radius=5,
                                                                                        content=ft.TextField(height=30, width=75, color="black", text_size=13, text_align="center", label="Entera Inicial", label_style=ft.TextStyle(color="#545454", size=10), content_padding=3, bgcolor="white", cursor_height=18, cursor_color="#747474", focused_border_color="black", focused_border_width=2, hint_text="Botes", hint_style=ft.TextStyle(color="#DADADA", size=10)),
                                                                                    ),
                                                                                    ft.Container(
                                                                                        bgcolor=self.color_teal_2,
                                                                                        padding=2.5,
                                                                                        border_radius=5,
                                                                                        content=ft.TextField(height=30, width=75, color="black", text_size=13, text_align="center", label="Entera Final", label_style=ft.TextStyle(color="#545454", size=10), content_padding=3, bgcolor="white", cursor_height=18, cursor_color="#747474", focused_border_color="black", focused_border_width=2, hint_text="Botes", hint_style=ft.TextStyle(color="#DADADA", size=10)),
                                                                                    ),
                                                                                ]
                                                                            )
                                                                        ),
                                                                    ]
                                                                )
                                                            ),
                                                            ft.Container(# Separador
                                                                col=1,
                                                                alignment=ft.alignment.center,
                                                                content=ft.Column(
                                                                    horizontal_alignment="center",
                                                                    controls=[
                                                                        ft.Container(
                                                                            bgcolor=self.color_teal,
                                                                            width=2,
                                                                            height=80,
                                                                            border_radius=2.5,
                                                                        )
                                                                    ]
                                                                )
                                                            ),
                                                            ft.Container(
                                                                col=5.5,
                                                                # bgcolor="pink",
                                                                content=ft.Column(
                                                                    controls=[
                                                                        ft.Container(
                                                                            content=ft.Row(
                                                                                alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                                                                                controls=[
                                                                                    ft.Container(
                                                                                        bgcolor=self.color_teal_2,
                                                                                        padding=2.5,
                                                                                        border_radius=5,
                                                                                        content=ft.TextField(height=30, width=70, color="black", text_size=13, text_align="center", label="Picada Inicial", label_style=ft.TextStyle(color="#545454", size=10), content_padding=3, bgcolor="white", cursor_height=18, cursor_color="#747474", focused_border_color="black", focused_border_width=2, hint_text="Botes", hint_style=ft.TextStyle(color="#DADADA", size=10)),
                                                                                    ),
                                                                                    ft.Container(
                                                                                        bgcolor=self.color_teal_2,
                                                                                        padding=2.5,
                                                                                        border_radius=5,
                                                                                        content=ft.TextField(height=30, width=70, color="black", text_size=13, text_align="center", label="Picada Final", label_style=ft.TextStyle(color="#545454", size=10), content_padding=3, bgcolor="white", cursor_height=18, cursor_color="#747474", focused_border_color="black", focused_border_width=2, hint_text="Botes", hint_style=ft.TextStyle(color="#DADADA", size=10)),
                                                                                    ),
                                                                                ]
                                                                            )
                                                                        ),
                                                                        ft.Container(
                                                                            content=ft.Row(
                                                                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                                                                controls=[
                                                                                    ft.Container(
                                                                                        bgcolor="#6971ff",
                                                                                        padding=2.5,
                                                                                        border_radius=5,
                                                                                        content=ft.TextField(height=30, width=80, color="black", text_size=13, text_align="center", label="Remanente", label_style=ft.TextStyle(color="#545454", size=10), content_padding=3, bgcolor="white", cursor_height=18, cursor_color="#747474", focused_border_color="black", focused_border_width=2, hint_text="Botes", hint_style=ft.TextStyle(color="#DADADA", size=10), border_color="black", border_width=1.5),
                                                                                    ),
                                                                                    ft.Container(
                                                                                        width=100,
                                                                                        height=30,
                                                                                        alignment=ft.alignment.center,
                                                                                        content=ft.Text("Uva", color="white", size=16),
                                                                                    ),
                                                                                    ft.Container(
                                                                                        bgcolor="#f00000",
                                                                                        padding=2.5,
                                                                                        border_radius=5,
                                                                                        content=ft.TextField(height=30, width=80, color="black", text_size=13, text_align="center", label="Vendida", label_style=ft.TextStyle(color="#545454", size=10), content_padding=3, bgcolor="white", cursor_height=18, cursor_color="#747474", focused_border_color="black", focused_border_width=2, hint_text="Botes", hint_style=ft.TextStyle(color="#DADADA", size=10), border_color="black", border_width=1.5),
                                                                                    ),
                                                                                ]
                                                                            )
                                                                        ),
                                                                        ft.Container(
                                                                            content=ft.Row(
                                                                                alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                                                                                controls=[
                                                                                    ft.Container(
                                                                                        bgcolor=self.color_teal_2,
                                                                                        padding=2.5,
                                                                                        border_radius=5,
                                                                                        content=ft.TextField(height=30, width=70, color="black", text_size=13, text_align="center", label="Entera Inicial", label_style=ft.TextStyle(color="#545454", size=10), content_padding=3, bgcolor="white", cursor_height=18, cursor_color="#747474", focused_border_color="black", focused_border_width=2, hint_text="Botes", hint_style=ft.TextStyle(color="#DADADA", size=10)),
                                                                                    ),
                                                                                    ft.Container(
                                                                                        bgcolor=self.color_teal_2,
                                                                                        padding=2.5,
                                                                                        border_radius=5,
                                                                                        content=ft.TextField(height=30, width=70, color="black", text_size=13, text_align="center", label="Entera Final", label_style=ft.TextStyle(color="#545454", size=10), content_padding=3, bgcolor="white", cursor_height=18, cursor_color="#747474", focused_border_color="black", focused_border_width=2, hint_text="Botes", hint_style=ft.TextStyle(color="#DADADA", size=10)),
                                                                                    ),
                                                                                ]
                                                                            )
                                                                        ),
                                                                    ]
                                                                )
                                                            )
                                                        ]
                                                    )
                                                ]
                                            )
                                        ),
                                        ft.Container(
                                            alignment=ft.alignment.center,
                                            padding=ft.Padding(top=0, bottom=0, left=55, right=65),
                                            # bgcolor="black",
                                            content=ft.Column(
                                                controls=[
                                                    ft.ResponsiveRow(
                                                        controls=[
                                                            ft.Container(
                                                                alignment=ft.alignment.center,
                                                                # padding=ft.padding.only(right=5),
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
                                                                                                                    content=ft.TextField(height=30, width=50, color="black", text_size=13, text_align="center", label="Vendidos", label_style=ft.TextStyle(color="#545454", size=10), content_padding=3, bgcolor="white", cursor_height=18, cursor_color="#747474", focused_border_color="black", focused_border_width=2, hint_text="Botes", hint_style=ft.TextStyle(color="#DADADA", size=10), border_color="black", border_width=1.5),
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
                                                                                                                    content=ft.TextField(height=30, width=50, color="black", text_size=13, text_align="center", label="Vendidos", label_style=ft.TextStyle(color="#545454", size=10), content_padding=3, bgcolor="white", cursor_height=18, cursor_color="#747474", focused_border_color="black", focused_border_width=2, hint_text="Botes", hint_style=ft.TextStyle(color="#DADADA", size=10), border_color="black", border_width=1.5),
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
                                                                                                                    content=ft.TextField(height=30, width=50, color="black", text_size=13, text_align="center", label="Vendidos", label_style=ft.TextStyle(color="#545454", size=10), content_padding=3, bgcolor="white", cursor_height=18, cursor_color="#747474", focused_border_color="black", focused_border_width=2, hint_text="Botes", hint_style=ft.TextStyle(color="#DADADA", size=10), border_color="black", border_width=1.5),
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
                    ft.Container(# Separador de secciones
                        margin=ft.Margin(right=30, left=25, top=0, bottom=0),
                        bgcolor=self.color_teal,
                        height=2,
                        border_radius=2.5
                    ),
                    ft.Container(# Extras y adicionales
                        expand=True,
                        # bgcolor="pink",
                        margin=ft.Margin(top=0, bottom=0, left=25, right=30),
                        border_radius=15,
                        padding=ft.Padding(top=0, bottom=0, left=2, right=12),
                        content=ft.ResponsiveRow(
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            vertical_alignment="center",
                            controls=[
                                ft.Container(
                                    col={"md":6, "lg":1.5},
                                    alignment=ft.alignment.center,
                                    # width=150,
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
                                    col={"md":6, "lg":1.8},
                                    alignment=ft.alignment.center,
                                    # width=160,
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
                                    col={"md":6, "lg":2.5},
                                    alignment=ft.alignment.center,
                                    # width=250,
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
                                    col={"md":6, "lg":2.5},
                                    # width=250,
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
                                    col={"md":6, "lg":2},
                                    # bgcolor="blue",
                                    # width=200,
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
                                                            ft.Text("Total día PDV")
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
                                ),
                                ft.Container(
                                    col={"md":6, "lg":.5},
                                    alignment=ft.alignment.center,
                                    content=ft.Column(
                                        horizontal_alignment="center",
                                        controls=[
                                            ft.Container(
                                                margin=ft.margin.only(top=3),
                                                bgcolor=self.color_teal,
                                                width=2,
                                                height=100,
                                                border_radius=2.5,
                                            )
                                        ]
                                    )
                                ),
                                ft.Container(
                                    # padding=8,
                                    # border_radius=5,
                                    # bgcolor="blue",
                                    col={"md":6, "lg":1.2},
                                    alignment=ft.alignment.center,
                                    content=ft.Column(
                                        spacing=15,
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        horizontal_alignment="center",
                                        controls=[
                                            ft.FilledButton(text="Resetear Campos", width=120, bgcolor=self.color_teal, color="#0a0a0a", style=ft.ButtonStyle(side=ft.BorderSide(1.5, color="#181818"), text_style={
                                                ft.ControlState.DEFAULT: ft.TextStyle(size=12),
                                                ft.ControlState.PRESSED: ft.TextStyle(size=6)
                                            })),
                                            ft.FilledButton(text="Generar Reporte", width=150, bgcolor=self.color_teal, color="#0a0a0a", style=ft.ButtonStyle(side=ft.BorderSide(1.5, color="#181818"), text_style={
                                                ft.ControlState.DEFAULT: ft.TextStyle(size=12),
                                                ft.ControlState.PRESSED: ft.TextStyle(size=6)
                                            }))
                                        ]
                                    )
                                )
                            ]
                        )
                    ),
                ]
            )
        )

        # ***** AREA DE CAPTURA DE VENTAS / ICONO VENTAS *****

        self.sales = ft.Container(# Ventana Ventas
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
                                ft.Column(# Titulo ventana
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
                                ft.Column(# Separador de secciones
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
                                ft.Column(# Dropdowns para fecha
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
                        ft.Column(# Campos de texto y archivos
                            expand=True,
                            controls=[
                                ft.Container(
                                    margin=ft.margin.symmetric(horizontal=80, vertical=0),
                                    # bgcolor="black",
                                    expand=True,
                                    content=ft.ResponsiveRow(
                                        controls=[
                                            ft.Container(# Campo de texto para reportes
                                                padding=20,
                                                alignment=ft.alignment.center,
                                                col=4,
                                                # bgcolor=self.color_teal,
                                                content=ft.Container(
                                                    bgcolor=self.color_teal,
                                                    alignment=ft.alignment.center,
                                                    border_radius=5,
                                                    padding=4,
                                                    content=self.report_field
                                                )
                                            ),
                                            ft.Container(# Botones interactivos para archivos
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
                                            ft.Container(# Campo de texto para ventas
                                                padding=20,
                                                alignment=ft.alignment.center,
                                                col=4,
                                                # bgcolor=self.color_teal,
                                                content=ft.Container(
                                                    bgcolor=self.color_teal,
                                                    alignment=ft.alignment.center,
                                                    border_radius=5,
                                                    padding=4,
                                                    content= self.sales_field
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


        self.sucursales = ft.Row(
            # expand=True,
            controls=[
                ft.Container(
                    expand=True,
                    bgcolor=ft.colors.BLUE_GREY_800,
                    border_radius=10,
                    content=ft.Container(
                        expand=True,
                        content=ft.Column(
                            expand=True,
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment="center",
                            controls=[
                                ft.Container(
                                    # content=ft.FilledButton(text="En proceso...", width=200, height=50, bgcolor=self.color_teal, color="black", style=ft.ButtonStyle(text_style=ft.TextStyle(size=25), alignment=ft.alignment.center))
                                    content=ft.Text("En proceso...", size=25)
                                )
                            ]
                        )
                    )
                )
            ]
        )
        # ***** Paginas de los respectivos elementos laterales encerrados en una lista para el control de estas con los elementos laterales *****

        self.pages_containers = [self.home, self.sales, self.sucursales]

        # ***** Seleccion de la pagina a mostrar mediante el index relacionado con el NavigationRail *****

        self.main_container = ft.Container(content=self.pages_containers[2], expand=True)

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

    # ***** FUNCIONES *****

    # Funcion para el manejo del cambio de ventanas mediante la barra lateral de navegacion

    def change_page(self, e):
        index = e.control.selected_index
        self.main_container.content = self.pages_containers[index]
        self.update()
        print(index)

    # ***** Funcion para el manejo de los radios boton's y la seleccion de las sucursales

    def pdv_selection(self, e):
        print(f"La sucursal seleccionada es: {e.control.value}")

        if e.control.value == "cofradia3":
            print("Sucursal Glorieta")

    # ***** Creacion de radios para sucursales *****

    def create_radio(self, value, label):
            return ft.Radio(
                value=value,
                label=label,
                label_style=ft.TextStyle(size=12),
                visual_density=ft.VisualDensity.STANDARD,
                fill_color={
                    ft.ControlState.DEFAULT: ft.Colors.PINK,
                    ft.ControlState.SELECTED: ft.Colors.GREEN,
                }
            )

    def create_textfield(self, Label, Color, text_Size, prefix_Text, prefix_Style, border_Color, border_Width, read_Only=False, on_Change=None):
        return ft.TextField(
            height=30,
            width=80,
            # color="#dc0000", # rojo
            color=Color,
            text_size=text_Size,
            text_align="center",
            label=Label,
            label_style=ft.TextStyle(color="#545454", size=10), # color = gris claro
            content_padding=3,
            bgcolor="white",
            cursor_height=18,
            cursor_color="#747474", # gris oscuro
            focused_border_color="black",
            focused_border_width=1.5,
            prefix_text=prefix_Text,
            prefix_style=prefix_Style,
            read_only=read_Only,
            border_color=border_Color,
            border_width=border_Width,
            on_change=on_Change
        )
    
    # ***** Funciones para el manejo de los campos de texto de la seccion de vasos *****

    # Vasos Chicos

    def conversion_n_capture_vc(self, e):
        try:
            self.num_tci = int(self.tci.value)
            self.num_tcf = int(self.tcf.value)
            self.num_tcdif = self.num_tci - self.num_tcf
            self.tcdif.value = self.num_tcdif
            self.num_vci = int(self.vci.value)
            self.num_vcf = int(self.vcf.value)
            self.num_vcdif = self.num_vci - self.num_vcf
            self.vcdif.value = self.num_vcdif

            self.values_columnSale_vc()
        except ValueError:
            pass
        finally:
            self.update()

    # Vasos Medianos

    def conversion_n_capture_vm(self, e):
        try:
            self.num_tmi = int(self.tmi.value)
            print(type(self.num_tmi))
            print(self.num_tmi)
            self.num_tmf = int(self.tmf.value)
            print(type(self.num_tmf))
            print(self.num_tmf)
            self.num_tmdif = self.num_tmi - self.num_tmf
            print(self.num_tmdif)
            self.tmdif.value = self.num_tmdif
            self.num_vmi = int(self.vmi.value)
            self.num_vmf = int(self.vmf.value)
            self.num_vmdif = self.num_vmi - self.num_vmf
            self.vmdif.value = self.num_vmdif

            self.values_columnSale_vm()
        except:
            pass
        finally:
            self.update()       

    # Vasos Grandes

    def conversion_n_capture_vg(self, e):
        try:
            self.num_tgi = int(self.tgi.value)
            self.num_tgf = int(self.tgf.value)
            self.num_tgdif = self.num_tgi - self.num_tgf
            self.tgdif.value = self.num_tgdif
            self.num_vgi = int(self.vgi.value)
            self.num_vgf = int(self.vgf.value)
            self.num_vgdif = self.num_vgi - self.num_vgf
            self.vgdif.value = self.num_vgdif
            self.values_columnSale_vg()
        except:
            pass
        finally:
            self.update()       

    # Vasos Chicos

    def values_columnSale_vc(self):
        self.num_vcsv = self.num_vcf
        self.vcsv.value = self.num_vcsv
        self.num_vcven = self.num_vcdif
        self.vcven.value = self.num_vcven
        self.num_vcvt = self.num_vcven * 50
        self.vcvt.value = self.num_vcvt

    # Vasos Medianos

    def values_columnSale_vm(self):
        self.num_vmsv = self.num_vmf
        self.vmsv.value = self.num_vmsv
        self.num_vmven = self.num_vmdif
        self.vmven.value = self.num_vmven
        self.num_vmvt = self.num_vmven * 70
        self.vmvt.value = self.num_vmvt

    # Vasos Grandes
    def values_columnSale_vg(self):
        self.num_vgsv = self.num_vgf
        self.vgsv.value = self.num_vgsv
        self.num_vgven = self.num_vgdif
        self.vgven.value = self.num_vgven
        self.num_vgvt = self.num_vgven * 150
        self.vgvt.value = self.num_vgvt

    # ***** FUNCTION CONSTRUCTORA (NO ME QUEDA CLARO PARA QUE Y PORQUE SE HACE, TENGO QUE INVESTIGAR A FONDO) *****

    def build(self):
        return self.main_pages

# ***** FUNCIÓN PRINCIPAL PARA CREAR LA VENTANA PRINCIPAL DE NUESTRO PROGRAMA O APP CON ALGUNAS CONFIGURACIONES EN ELLA COMO ALINEACION EN HORIZONTAL, COLOR DE FONDO, MEDIDA MINIMA EN ALTO Y ANCHO, TEMA PREDETERMINADO Y TÍTULO *****

def main(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = ft.colors.BLUE_GREY_900
    page.window_min_height = 680
    page.window_min_width = 920
    # page.window_max_height = 620
    # page.window_max_width = 1080
    page.theme_mode = ft.ThemeMode.DARK
    page.title = "Control"
    page.window.maximized = True
    page.window_resizable = True
    # page.window.icon = ft.Icon.
    # page.window_opacity = .95
    page.add(UI(page))

# ***** Web Mode *****
# ft.app(target=main, view=ft.WEB_BROWSER)

# ***** Desktop Mode *****
ft.app(target=main)