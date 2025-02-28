import flet as ft
import created_Functions
import datetime as dt
from fpdf import FPDF

class UI(ft.ResponsiveRow):
    def __init__(self, page):
        super().__init__(expand=True)

        # ***** VARIABLES SISTEMA *****

        self.pdv = ""

        # self.color_teal = "teal"
        self.color_teal = "#00ebab"
        self.color_teal_2 = "#11b78a"

        # *** Variable Boton cambio de tema ***

        self.mode_switch = created_Functions.create_Boton_Switch()

        # *** Variables Iconos Inferiores Barra de Navegacion Lateral ***

        self.profiles = ft.IconButton(# Ventana Perfiles / Cuentas
            icon=ft.icons.ACCOUNT_CIRCLE_SHARP,
            icon_color="white",
            tooltip="Cuenta",
            on_click=lambda e: page.open(
                ft.CupertinoAlertDialog(
                    # title=ft.Text("Cuentas"),
                    content=ft.Text('Sección no disponible por el momento'),
                    actions=[
                        ft.CupertinoDialogAction("Ok", is_destructive_action=True, on_click=lambda e: page.close(e.control.parent))
                    ]
                ),
            )
        )

        self.configuration = ft.IconButton(# Ventana Configuraciones
            icon=ft.icons.SETTINGS,
            icon_color="white",
            tooltip="Configuraciones",
            on_click=lambda e: page.open(
                ft.AlertDialog(
                    modal=True,
                    # title=ft.Text("Cuentas"),
                    content=ft.Text('Por el momento no hay configuraciones disponibles'),
                    actions=[
                        ft.TextButton("Ok", on_click=lambda e: page.close(e.control.parent))
                    ]
                ),
            )
        )

        # *** Variables Ventana Inicio ***

        # Variables sucursales

        self.glorieta = created_Functions.create_radio("glorieta", "Glorieta")

        self.sanmiguel = created_Functions.create_radio("sanmiguel", "San Miguel")

        self.vips = created_Functions.create_radio("vips", "Vips")

        self. cofradia2 = created_Functions.create_radio("cofradia2", "Cofradía 2")

        self.ensuenos = created_Functions.create_radio("ensueños", "Ensueños")

        self.operagua = created_Functions.create_radio("operagua", "Operagua")

        self.sanantonio = created_Functions.create_radio("sanantonio", "San Antonio")

        self.lapiedad = created_Functions.create_radio("lapiedad", "La Piedad")

        self.pdv = ft.RadioGroup(# Grupo de Botones tipo Radio de las Sucursales
            on_change=self.pdv_selection,
            content=ft.Container(
                alignment=ft.alignment.center,
                padding=ft.Padding(top=2, bottom=2, left=2, right=4),
                # bgcolor="blue",
                content=ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                    # expand=True,
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
        )

        # Variables Vasos Chicos

        # Opciones a configurar en la funcion create_textfield: Label, Color="#d3d3d3", text_Size=13, border_Color="#11b78a", border_Width=None, focused_Border_Color="#00ebab", hint_Text=None, hint_Style=None, prefix_Text=None, prefix_Style=None, read_Only=False, on_Change=None

        self.tci = created_Functions.create_textfield("Iniciales", suffix_Text="Tapas Iniciales", on_Focus=created_Functions.Focus, on_Change=self.conversion_n_capture_vc)
        self.tcf = created_Functions.create_textfield("Finales", suffix_Text="Tapas Finales", on_Focus=created_Functions.Focus, on_Change=self.conversion_n_capture_vc)
        # self.tcdif = created_Functions.create_textfield("Diferencia de...", suffix_Text="Tapas", read_Only=True)
        self.vci = created_Functions.create_textfield("Iniciales", suffix_Text="Vasos Iniciales", on_Focus=created_Functions.Focus, on_Change=self.conversion_n_capture_vc)
        self.vcf = created_Functions.create_textfield("Finales", suffix_Text="Vasos Finales", on_Focus=created_Functions.Focus, on_Change=self.conversion_n_capture_vc)
        # self.vcdif = created_Functions.create_textfield("Diferencia", suffix_Text="Vasos", read_Only=True)
        # self.vcsv = created_Functions.create_textfield("Sin vender", suffix_Text="Vasos", Color="#ffffff", read_Only=True)
        self.vcven = created_Functions.create_textfield("Vendidos", Color="#fd0000", text_Size=24, label_Style=ft.TextStyle(color="#a2a2a2", size=12), suffix_Text="Vasos", suffix_Style=ft.TextStyle(color="#a2a2a2", size=12), read_Only=True)
        self.vcvt = created_Functions.create_textfield(Label="Venta Total", Color="#ffffff", text_Size=24,label_Style=ft.TextStyle(color="#a2a2a2", size=12), border_Color="#fd0000", border_Width=2, focused_Border_Color="#fd0000", prefix_Text=" $", prefix_Style=ft.TextStyle(color="#ffffff", size=12), read_Only=True)

        # Variables Vasos Medianos

        # Opciones a configurar en la funcion create_textfield: Label, Color="#d3d3d3", text_Size=13, border_Color="#11b78a", border_Width=None, focused_Border_Color="#00ebab", hint_Text=None, hint_Style=None, prefix_Text=None, prefix_Style=None, read_Only=False, on_Change=None

        self.tmi = created_Functions.create_textfield("Iniciales", suffix_Text="Tapas Iniciales", on_Focus=created_Functions.Focus, on_Change=self.conversion_n_capture_vm)
        self.tmf = created_Functions.create_textfield("Finales", suffix_Text="Tapas Finales", on_Focus=created_Functions.Focus, on_Change=self.conversion_n_capture_vm)
        # self.tmdif = created_Functions.create_textfield("Diferencia", read_Only=True)
        self.vmi = created_Functions.create_textfield("Iniciales", suffix_Text="Vasos Iniciales", on_Focus=created_Functions.Focus, on_Change=self.conversion_n_capture_vm)
        self.vmf = created_Functions.create_textfield("Finales", suffix_Text=" Vasos Finales", on_Focus=created_Functions.Focus, on_Change=self.conversion_n_capture_vm)
        # self.vmdif = created_Functions.create_textfield("Diferencia", read_Only=True)
        # self.vmsv = created_Functions.create_textfield("Sin Vender", Color="#ffffff", read_Only=True)
        self.vmven = created_Functions.create_textfield("Vendidos", Color="#fd0000", text_Size=24, label_Style=ft.TextStyle(color="#a2a2a2", size=12), suffix_Text="Vasos", suffix_Style=ft.TextStyle(color="#a2a2a2", size=12), read_Only=True)
        self.vmvt = created_Functions.create_textfield(Label="Venta Total", Color="#ffffff", text_Size=24, label_Style=ft.TextStyle(color="#a2a2a2", size=12), border_Color="#fd0000", border_Width=1.5, focused_Border_Color="#fd0000", prefix_Text=" $", prefix_Style=ft.TextStyle(color="#ffffff", size=12), read_Only=True)

        # Variables Vasos Grandes

        # Opciones a configurar en la funcion create_textfield: Label, Color="#d3d3d3", text_Size=13, border_Color="#11b78a", border_Width=None, focused_Border_Color="#00ebab", hint_Text=None, hint_Style=None, prefix_Text=None, prefix_Style=None, read_Only=False, on_Change=None

        self.tgi = created_Functions.create_textfield("Iniciales", suffix_Text="Tapas Iniciales", on_Focus=created_Functions.Focus, on_Change=self.conversion_n_capture_vg)
        self.tgf = created_Functions.create_textfield("Finales", suffix_Text="Tapas Finales", on_Focus=created_Functions.Focus, on_Change=self.conversion_n_capture_vg)
        # self.tgdif = created_Functions.create_textfield("Diferencia", read_Only=True)
        self.vgi = created_Functions.create_textfield("Iniciales", suffix_Text="Vasos Iniciales", on_Focus=created_Functions.Focus, on_Change=self.conversion_n_capture_vg)
        self.vgf = created_Functions.create_textfield("Finales", suffix_Text="Vasos Finales", on_Focus=created_Functions.Focus, on_Change=self.conversion_n_capture_vg)
        # self.vgdif = created_Functions.create_textfield("Diferencia", read_Only=True)
        # self.vgsv = created_Functions.create_textfield("Sin Vender", Color="#ffffff", read_Only=True)
        self.vgven = created_Functions.create_textfield("Vendidos", Color="#fd0000", text_Size=24, label_Style=ft.TextStyle(color="#a2a2a2", size=12), suffix_Text="Vasos", suffix_Style=ft.TextStyle(color="#a2a2a2", size=12), read_Only=True)
        self.vgvt = created_Functions.create_textfield(Label="Venta Total", Color="#ffffff", text_Size=24, label_Style=ft.TextStyle(color="#a2a2a2", size=12), border_Color="#fd0000", border_Width=1.5, focused_Border_Color="#fd0000", prefix_Text=" $", prefix_Style=ft.TextStyle(color="#ffffff", size=12), read_Only=True)

        # Variables Venta Total Vasos

        # Opciones a configurar en la funcion create_textfield: Label, Color="#d3d3d3", text_Size=13, border_Color="#11b78a", border_Width=None, focused_Border_Color="#00ebab", hint_Text=None, hint_Style=None, prefix_Text=None, prefix_Style=None, read_Only=False, on_Change=None

        self.vtv = created_Functions.create_textfield_WB("Vendidos", Color="#ffffff", text_Size=24, border_Color="#292929", border_Width=.3, focused_Border_Color="#292929", suffix_Text="Vasos ", read_Only=True)
        self.vvmt = created_Functions.create_textfield_WB(Label="Venta Total", Color="#ffffff", text_Size=24, border_Color="#292929", border_Width=.3, focused_Border_Color="#292929", prefix_Text=" $", prefix_Style=ft.TextStyle(color="#ffffff", size=12), suffix_Text="MX ", read_Only=True)

        # ***** VARIABLES FRUTAS *****

        # Opciones a configurar en la funcion create_textfield: Label, Color="#d3d3d3", text_Size=13, border_Color="#11b78a", border_Width=None, focused_Border_Color="#00ebab", hint_Text=None, hint_Style=None, prefix_Text=None, prefix_Style=None, read_Only=False, on_Change=None

        # Fresa

        # self.tgi = created_Functions.create_textfield("Iniciales", suffix_Text="Tapas Iniciales", on_Focus=created_Functions.Focus, on_Change=self.conversion_n_capture_vg)
        self.fpi = created_Functions.create_textfield("Picada Inicial", suffix_Text="Botes", on_Change=self.conversion_n_capture_fr)
        self.fpf = created_Functions.create_textfield("Picada Final", suffix_Text="Botes", on_Change=self.conversion_n_capture_fr)
        self.fei = created_Functions.create_textfield("Entera Inicial", suffix_Text="Botes", on_Change=self.conversion_n_capture_fr)
        self.fef = created_Functions.create_textfield("Entera Final", suffix_Text="Botes", on_Change=self.conversion_n_capture_fr)
        self.fv = created_Functions.create_textfield(Label="Vendidos", suffix_Text="Botes", Color="#ffffff", text_Size=22, Width=150, label_Style=ft.TextStyle(color="#a2a2a2", size=12), suffix_Style=ft.TextStyle(color="#a2a2a2", size=12), border_Color="#fd0000", border_Width=1.5, focused_Border_Color="#fd0000", read_Only=True)
        # self.fr = created_Functions.create_textfield(Label="Remanente", Color="#ffffff", text_Size=15, border_Color="#0c52ff", border_Width=1.5, focused_Border_Color="#0c52ff", hint_Text="Botes", hint_Style=ft.TextStyle(color="#5b5b5b", size=10), read_Only=True)

        # Uva

        self.upi = created_Functions.create_textfield("Picada Inicial", suffix_Text="Botes", on_Change=self.conversion_n_capture_uva)
        self.upf = created_Functions.create_textfield("Picada Final", suffix_Text="Botes", on_Change=self.conversion_n_capture_uva)
        self.uei = created_Functions.create_textfield("Entera Inicial", suffix_Text="Botes", on_Change=self.conversion_n_capture_uva)
        self.uef = created_Functions.create_textfield("Entera Final", suffix_Text="Botes", on_Change=self.conversion_n_capture_uva)
        self.uv = created_Functions.create_textfield(Label="Vendidos", suffix_Text="Botes", Color="#ffffff", text_Size=22, Width=150, label_Style=ft.TextStyle(color="#a2a2a2", size=12), suffix_Style=ft.TextStyle(color="#a2a2a2", size=12), border_Color="#fd0000", border_Width=1.5, focused_Border_Color="#fd0000",read_Only=True)
        # self.ur = created_Functions.create_textfield(Label="Remanente", Color="#ffffff", text_Size=15, border_Color="#0c52ff", border_Width=1.5, focused_Border_Color="#0c52ff", hint_Text="Botes", hint_Style=ft.TextStyle(color="#5b5b5b", size=10), read_Only=True)

        # ***** VARIABLES CREMAS *****

        # Opciones a configurar en la funcion create_textfield: Label, Color="#d3d3d3", text_Size=13, border_Color="#11b78a", border_Width=None, focused_Border_Color="#00ebab", hint_Text=None, hint_Style=None, prefix_Text=None, prefix_Style=None, read_Only=False, on_Change=None

        # Crema Original

        self.coi = created_Functions.create_textfield("Inicial", suffix_Text="Botes", on_Change=self.conversion_n_capture_co)
        self.cof = created_Functions.create_textfield("Final", suffix_Text="Botes", on_Change=self.conversion_n_capture_co)
        self.cov = created_Functions.create_textfield(Label="Vendidos", suffix_Text="Botes", Color="#ffffff", text_Size=22, Width=150, label_Style=ft.TextStyle(color="#a2a2a2", size=12), suffix_Style=ft.TextStyle(color="#a2a2a2", size=12), border_Color="#fd0000", border_Width=1.5, focused_Border_Color="#fd0000",read_Only=True)

        # Crema Chocolate

        self.cchi = created_Functions.create_textfield("Inicial", suffix_Text="Botes", on_Change=self.conversion_n_capture_co)
        self.cchf = created_Functions.create_textfield("Final", suffix_Text="Botes", on_Change=self.conversion_n_capture_co)
        self.cchv = created_Functions.create_textfield(Label="Vendidos", suffix_Text="Botes", Color="#ffffff", text_Size=22, Width=150, label_Style=ft.TextStyle(color="#a2a2a2", size=12), suffix_Style=ft.TextStyle(color="#a2a2a2", size=12), border_Color="#fd0000", border_Width=1.5, focused_Border_Color="#fd0000",read_Only=True)

        # Crema Cafe

        self.ccai = created_Functions.create_textfield("Inicial", suffix_Text="Botes", on_Change=self.conversion_n_capture_co)
        self.ccaf = created_Functions.create_textfield("Final", suffix_Text="Botes", on_Change=self.conversion_n_capture_co)
        self.ccav = created_Functions.create_textfield(Label="Vendidos", suffix_Text="Botes", Color="#ffffff", text_Size=22, Width=150, label_Style=ft.TextStyle(color="#a2a2a2", size=12), suffix_Style=ft.TextStyle(color="#a2a2a2", size=12), border_Color="#fd0000", border_Width=1.5, focused_Border_Color="#fd0000",read_Only=True)
        
        # ***** VARIABLES ADICIONALES Y EXTRAS *****

        # Opciones a configurar en la funcion create_textfield_Extras: Width, Height, Color="#d3d3d3", text_Size=12, border_Color=None, read_Only=False, on_Change=False

        # Toppings Extras

        self.t5 = created_Functions.create_textField_Extras(40, 25, on_Change=self.conversion_n_capture_tE)
        self.t10 = created_Functions.create_textField_Extras(40, 25, on_Change=self.conversion_n_capture_tE)
        self.tt = created_Functions.create_textField_Extras(55, 25, "#ffffff", 15, border_Color="#fd0000", read_Only=True)

        # Servicios a Domicilio

        self.sd25 = created_Functions.create_textField_Extras(40, 25, on_Change=self.conversion_n_capture_sD)
        self.sd35 = created_Functions.create_textField_Extras(40, 25, on_Change=self.conversion_n_capture_sD)
        self.sdt = created_Functions.create_textField_Extras(50, 25, "#ffffff", 15, border_Color="#fd0000", read_Only=True)

        # Transferencias

        self.trn = created_Functions.create_textField_Extras(50, 25)
        self.trt = created_Functions.create_textField_Extras(50, 25, "#ffffff", 15, border_Color="#fd0000")

        # Gastos / Retiros

        self.grn = created_Functions.create_textField_Extras(50, 25)
        self.grt = created_Functions.create_textField_Extras(50, 25, "#ffffff", 15, border_Color="#fd0000", on_Change=self.balance_General)

        # Balance

        self.bgi = created_Functions.create_textField_Extras(50, 25)
        self.bgd = created_Functions.create_textField_Extras(50, 25)
        self.bgt = created_Functions.create_textField_Extras(70, 25, "#ffffff", 15, border_Color="#fd0000", read_Only=True)

        # ***** VARIABLES VENTANA VENTAS *****

        # *** Variables Campos de texto y Botones ***

        # Campos de texto

        self.report_field = created_Functions.create_textField_RyV("REPORTE")
        self.sales_field = created_Functions.create_textField_RyV("EXTRAS", False)

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
                            # selected_label_text_style=ft.TextStyle(color=self.color_teal_2),
                            destinations=[
                                ft.NavigationRailDestination(
                                    icon = ft.icons.HOME,
                                    label_content=ft.Text("INICIO", size=8),
                                    selected_icon=ft.Icon(ft.icons.HOME, color="#2e2e2e")
                                ),
                                ft.NavigationRailDestination(
                                    icon = ft.icons.POINT_OF_SALE_SHARP,
                                    label_content=ft.Text("VENTAS", size=8),
                                    selected_icon=ft.Icon(ft.icons.POINT_OF_SALE_SHARP, color="#2e2e2e")
                                ),
                                ft.NavigationRailDestination(
                                    icon = ft.icons.ACCOUNT_TREE_ROUNDED,
                                    label_content=ft.Text("PDV's", size=8),
                                    selected_icon=ft.Icon(ft.icons.ACCOUNT_TREE_ROUNDED, color="#2e2e2e")
                                ),
                                ft.NavigationRailDestination(
                                    icon = ft.icons.INVENTORY,
                                    label_content=ft.Text("STOCK", size=8),
                                    selected_icon=ft.Icon(ft.icons.INVENTORY, color="#2e2e2e")
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
                                self.profiles,
                                self.configuration,
                                self.mode_switch
                            ]
                        )
                    ),
                ]
            )
        )

        self.select_Bar_Sucursales = ft.Container(# Puntos de venta
            alignment=ft.alignment.center,
            bgcolor=ft.colors.BLUE_GREY_800,
            border_radius=10,
            content=ft.Column(
                horizontal_alignment="center",
                alignment="center",
                controls=[
                    self.pdv,
                ]
            )
        )
        # ***** AREA DE CAPTURA DE INSUMOS / ICONO HOME *****

        self.home = ft.Container(# Ventana Inicio
            bgcolor=ft.colors.BLUE_GREY_800,
            # height=638,
            # width=1500,
            # padding=10,
            border_radius=8,
            clip_behavior=ft.ClipBehavior.NONE,
            # alignment=ft.alignment.center,
            content=ft.Stack(
                height=638,
                width=1500,
                # alignment="start"
                # scroll=ft.ScrollMode.AUTO,
                controls=[
                        # ft.Container(# Puntos de venta
                    #     alignment=ft.alignment.center,
                    #     # bgcolor="pink",
                    #     margin=ft.Margin(top=10, bottom=2, left=0, right=0),
                    #     padding=ft.Padding(top=0, bottom=0, left=0, right=0),
                    #     content=ft.Column(
                    #         horizontal_alignment="center",
                    #         controls=[
                    #             self.pdv,
                    #             ft.Divider(# Separador de seccion con Divider
                    #                 height=1,
                    #                 color=self.color_teal,
                    #                 thickness=3,
                    #                 # leading_indent=50,
                    #                 # trailing_indent=10
                    #             ),
                    #         ]
                    #     )
                    # ),
                    # ft.Container(# Separador de secciones
                    #     margin=ft.Margin(right=30, left=25, top=0, bottom=0),
                    #     bgcolor=self.color_teal,
                    #     height=2,
                    #     border_radius=2.5
                    # ),
                    # created_Functions.create_Bg_Containers(),
                    ft.Tabs(
                        selected_index=1,
                        label_text_style=ft.TextStyle(size=16, italic=True),
                        label_color="#08f5a9",
                        unselected_label_color="white",
                        unselected_label_text_style=ft.TextStyle(size=12, italic=False),
                        animation_duration=150,
                        scrollable=False,
                        indicator_tab_size=True,
                        indicator_color="#08f5a9",
                        # indicator_color="#ff1765",
                        # indicator_thickness=10,
                        tabs=[
                            ft.Tab(# Frutas y Cremas
                                text="Frutas y Cremas",
                                content=ft.Column(
                                    controls=[
                                        ft.Container(
                                            content=ft.ResponsiveRow(
                                                alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                                                controls=[
                                                    ft.Container(# Fresa
                                                        col=6,
                                                        margin=ft.Margin(top=10, bottom=0, left=60, right=30),
                                                        # padding=ft.padding.symmetric(horizontal=5, vertical=5),
                                                        # bgcolor="blue",
                                                        content=ft.Column(
                                                            # alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                                            # horizontal_alignment="center",
                                                            controls=[
                                                                ft.Container(# Fresa
                                                                    # margin=ft.margin.symmetric(horizontal=5, vertical=10),
                                                                    # height=250,
                                                                    # width=600,
                                                                    margin=10,
                                                                    alignment=ft.alignment.center,
                                                                    bgcolor="#292929",
                                                                    border=ft.border.all(width=3, color="white"),
                                                                    border_radius=5,
                                                                    padding=ft.Padding(top=5, bottom=7, left=0, right=0),
                                                                    shadow=ft.BoxShadow(
                                                                        spread_radius=1,
                                                                        blur_radius=15,
                                                                        color=ft.colors.BLUE_GREY_100,
                                                                        offset=ft.Offset(0, 0),
                                                                        blur_style=ft.ShadowBlurStyle.OUTER,
                                                                    ),
                                                                    content=ft.Column(
                                                                        alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                                                        controls=[
                                                                            ft.Container(# Titulo
                                                                                alignment=ft.alignment.center,
                                                                                height=15,
                                                                                # padding=7,
                                                                                # bgcolor="blue",
                                                                                # border_radius=20,
                                                                                # width=180,
                                                                                content=ft.Column(# Titulo
                                                                                    # horizontal_alignment="center",
                                                                                    controls=[
                                                                                        ft.Text("* FRESA *", color="#bfc244", weight=ft.FontWeight.BOLD, size=18, style=ft.TextStyle(letter_spacing=10)),
                                                                                        # ft.Divider(# Separador de seccion con Divider
                                                                                        #     height=1,
                                                                                        #     color="white",
                                                                                        #     thickness=.5,
                                                                                        #     leading_indent=400,
                                                                                        #     trailing_indent=400
                                                                                        # ),
                                                                                    ]
                                                                                )
                                                                            ),
                                                                                ft.Container(# Fresa Picada
                                                                                alignment=ft.alignment.center,
                                                                                # margin=ft.margin.only(bottom=25),
                                                                                # bgcolor="pink",
                                                                                # padding=ft.padding.symmetric(horizontal=0, vertical=5),
                                                                                # border_radius=20,
                                                                                content=ft.ResponsiveRow(
                                                                                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                                                                    vertical_alignment="center",
                                                                                    controls=[
                                                                                        ft.Container(
                                                                                            alignment=ft.alignment.center,
                                                                                            col=4,
                                                                                            # bgcolor="yellow",
                                                                                            content=ft.Container(
                                                                                                # bgcolor=self.color_teal_2,
                                                                                                padding=2.5,
                                                                                                border_radius=5,
                                                                                                content=self.fpi
                                                                                            )
                                                                                        ),
                                                                                        ft.Container(
                                                                                            alignment=ft.alignment.center,
                                                                                            col=4,
                                                                                            # bgcolor="yellow",
                                                                                            content=ft.Container(
                                                                                                # bgcolor=self.color_teal_2,
                                                                                                padding=2.5,
                                                                                                border_radius=5,
                                                                                                content=self.fpf
                                                                                            ),
                                                                                        ),
                                                                                    ]
                                                                                )
                                                                            ),
                                                                            ft.Container(# Fresa Entera
                                                                                alignment=ft.alignment.center,
                                                                                # margin=ft.margin.only(bottom=25),
                                                                                # bgcolor="pink",
                                                                                # padding=ft.padding.symmetric(horizontal=0, vertical=5),
                                                                                # border_radius=20,
                                                                                content=ft.ResponsiveRow(
                                                                                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                                                                    vertical_alignment="center",
                                                                                    controls=[
                                                                                        ft.Container(
                                                                                            alignment=ft.alignment.center,
                                                                                            col=4,
                                                                                            # bgcolor="yellow",
                                                                                            content=ft.Container(
                                                                                                # bgcolor=self.color_teal_2,
                                                                                                padding=2.5,
                                                                                                border_radius=5,
                                                                                                content=self.fei
                                                                                            )
                                                                                        ),
                                                                                        ft.Container(
                                                                                            alignment=ft.alignment.center,
                                                                                            col=4,
                                                                                            # bgcolor="yellow",
                                                                                            content=ft.Container(
                                                                                                # bgcolor=self.color_teal_2,
                                                                                                padding=2.5,
                                                                                                border_radius=5,
                                                                                                content=self.fef
                                                                                            ),
                                                                                        ),
                                                                                    ]
                                                                                )
                                                                            ),
                                                                            ft.Container(# Fresa Venta Total
                                                                                alignment=ft.alignment.center,
                                                                                # margin=ft.margin.only(bottom=25),
                                                                                # bgcolor="pink",
                                                                                # padding=ft.padding.symmetric(horizontal=0, vertical=5),
                                                                                # border_radius=20,
                                                                                content=ft.ResponsiveRow(
                                                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                                                    vertical_alignment="center",
                                                                                    controls=[
                                                                                        ft.Container(
                                                                                            alignment=ft.alignment.center,
                                                                                            col=6,
                                                                                            # bgcolor="yellow",
                                                                                            content=ft.Container(
                                                                                                # bgcolor=self.color_teal_2,
                                                                                                padding=2.5,
                                                                                                border_radius=5,
                                                                                                content=self.fv
                                                                                            )
                                                                                        ),
                                                                                    ]
                                                                                )
                                                                            ),
                                                                        ]
                                                                    )
                                                                )
                                                            ]
                                                        )
                                                    ),
                                                    ft.Container(# Uva
                                                        col=6,
                                                        margin=ft.Margin(top=10, bottom=0, left=30, right=60),
                                                        # padding=ft.padding.symmetric(horizontal=5, vertical=5),
                                                        # bgcolor="blue",
                                                        content=ft.Column(
                                                            # alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                                            # horizontal_alignment="center",
                                                            controls=[
                                                                ft.Container(# Uva
                                                                    # margin=ft.margin.symmetric(horizontal=5, vertical=10),
                                                                    # height=250,
                                                                    # width=600,
                                                                    margin=10,
                                                                    alignment=ft.alignment.center,
                                                                    bgcolor="#292929",
                                                                    border=ft.border.all(width=3, color="white"),
                                                                    border_radius=5,
                                                                    padding=ft.Padding(top=5, bottom=7, left=0, right=0),
                                                                    shadow=ft.BoxShadow(
                                                                        spread_radius=1,
                                                                        blur_radius=15,
                                                                        color=ft.colors.BLUE_GREY_100,
                                                                        offset=ft.Offset(0, 0),
                                                                        blur_style=ft.ShadowBlurStyle.OUTER,
                                                                    ),
                                                                    content=ft.Column(
                                                                        alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                                                        controls=[
                                                                            ft.Container(# Titulo
                                                                                alignment=ft.alignment.center,
                                                                                height=15,
                                                                                # padding=7,
                                                                                # bgcolor="blue",
                                                                                # border_radius=20,
                                                                                # width=180,
                                                                                content=ft.Column(
                                                                                    # horizontal_alignment="center",
                                                                                    controls=[
                                                                                        ft.Text("* UVA *", color="#bfc244", weight=ft.FontWeight.BOLD, size=18, style=ft.TextStyle(letter_spacing=10)),
                                                                                        # ft.Divider(# Separador de seccion con Divider
                                                                                        #     height=1,
                                                                                        #     color="white",
                                                                                        #     thickness=.5,
                                                                                        #     leading_indent=400,
                                                                                        #     trailing_indent=400
                                                                                        # ),
                                                                                    ]
                                                                                )
                                                                            ),
                                                                            ft.Container(# Uva Picada
                                                                                alignment=ft.alignment.center,
                                                                                # margin=ft.margin.only(bottom=25),
                                                                                # bgcolor="pink",
                                                                                # padding=ft.padding.symmetric(horizontal=0, vertical=5),
                                                                                # border_radius=20,
                                                                                content=ft.ResponsiveRow(
                                                                                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                                                                    vertical_alignment="center",
                                                                                    controls=[
                                                                                        ft.Container(
                                                                                            alignment=ft.alignment.center,
                                                                                            col=4,
                                                                                            # bgcolor="yellow",
                                                                                            content=ft.Container(
                                                                                                # bgcolor=self.color_teal_2,
                                                                                                padding=2.5,
                                                                                                border_radius=5,
                                                                                                content=self.upi
                                                                                            )
                                                                                        ),
                                                                                        ft.Container(
                                                                                            alignment=ft.alignment.center,
                                                                                            col=4,
                                                                                            # bgcolor="yellow",
                                                                                            content=ft.Container(
                                                                                                # bgcolor=self.color_teal_2,
                                                                                                padding=2.5,
                                                                                                border_radius=5,
                                                                                                content=self.upf
                                                                                            ),
                                                                                        ),
                                                                                    ]
                                                                                )
                                                                            ),
                                                                            ft.Container(# Uva entera
                                                                                alignment=ft.alignment.center,
                                                                                # margin=ft.margin.only(bottom=25),
                                                                                # bgcolor="pink",
                                                                                # padding=ft.padding.symmetric(horizontal=0, vertical=5),
                                                                                # border_radius=20,
                                                                                content=ft.ResponsiveRow(
                                                                                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                                                                    vertical_alignment="center",
                                                                                    controls=[
                                                                                        ft.Container(
                                                                                            alignment=ft.alignment.center,
                                                                                            col=4,
                                                                                            # bgcolor="yellow",
                                                                                            content=ft.Container(
                                                                                                # bgcolor=self.color_teal_2,
                                                                                                padding=2.5,
                                                                                                border_radius=5,
                                                                                                content=self.uei
                                                                                            )
                                                                                        ),
                                                                                        ft.Container(
                                                                                            alignment=ft.alignment.center,
                                                                                            col=4,
                                                                                            # bgcolor="yellow",
                                                                                            content=ft.Container(
                                                                                                # bgcolor=self.color_teal_2,
                                                                                                padding=2.5,
                                                                                                border_radius=5,
                                                                                                content=self.uef
                                                                                            ),
                                                                                        ),
                                                                                    ]
                                                                                )
                                                                            ),
                                                                            ft.Container(# Uva venta total
                                                                                alignment=ft.alignment.center,
                                                                                # margin=ft.margin.only(bottom=25),
                                                                                # bgcolor="pink",
                                                                                # padding=ft.padding.symmetric(horizontal=0, vertical=5),
                                                                                # border_radius=20,
                                                                                content=ft.ResponsiveRow(
                                                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                                                    vertical_alignment="center",
                                                                                    controls=[
                                                                                        ft.Container(
                                                                                            alignment=ft.alignment.center,
                                                                                            col=6,
                                                                                            # bgcolor="yellow",
                                                                                            content=ft.Container(
                                                                                                # bgcolor=self.color_teal_2,
                                                                                                padding=2.5,
                                                                                                border_radius=5,
                                                                                                content=self.uv
                                                                                            )
                                                                                        ),
                                                                                    ]
                                                                                )
                                                                            ),
                                                                        ]
                                                                    )
                                                                )
                                                            ]
                                                        )
                                                    ),
                                                ]
                                            )
                                        ),
                                        ft.Container(
                                            content=ft.ResponsiveRow(
                                                alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                                                controls=[
                                                    ft.Container(# Crema Original
                                                        col=4,
                                                        margin=ft.Margin(top=5, bottom=0, left=20, right=3),
                                                        # padding=ft.padding.symmetric(horizontal=5, vertical=5),
                                                        # bgcolor="blue",
                                                        content=ft.Column(
                                                            # alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                                            # horizontal_alignment="center",
                                                            controls=[
                                                                ft.Container(# Crema original
                                                                    # margin=ft.margin.symmetric(horizontal=5, vertical=10),
                                                                    # height=250,
                                                                    # width=600,
                                                                    margin=8,
                                                                    alignment=ft.alignment.center,
                                                                    bgcolor="#292929",
                                                                    border=ft.border.all(width=3, color="white"),
                                                                    border_radius=5,
                                                                    padding=ft.Padding(top=5, bottom=7, left=0, right=0),
                                                                    shadow=ft.BoxShadow(
                                                                        spread_radius=1,
                                                                        blur_radius=15,
                                                                        color=ft.colors.BLUE_GREY_100,
                                                                        offset=ft.Offset(0, 0),
                                                                        blur_style=ft.ShadowBlurStyle.OUTER,
                                                                    ),
                                                                    content=ft.Column(
                                                                        alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                                                        controls=[
                                                                            ft.Container(# Titulo
                                                                                alignment=ft.alignment.center,
                                                                                height=15,
                                                                                # padding=7,
                                                                                # bgcolor="blue",
                                                                                # border_radius=20,
                                                                                # width=180,
                                                                                content=ft.Column(
                                                                                    # horizontal_alignment="center",
                                                                                    controls=[
                                                                                        ft.Text("* CREMA ORIGINAL *", color="#bfc244", weight=ft.FontWeight.BOLD, size=16, style=ft.TextStyle(letter_spacing=10)),
                                                                                        # ft.Divider(# Separador de seccion con Divider
                                                                                        #     height=1,
                                                                                        #     color="white",
                                                                                        #     thickness=.5,
                                                                                        #     leading_indent=400,
                                                                                        #     trailing_indent=400
                                                                                        # ),
                                                                                    ]
                                                                                )
                                                                            ),
                                                                                ft.Container(# Botes Dia
                                                                                alignment=ft.alignment.center,
                                                                                # margin=ft.margin.only(bottom=25),
                                                                                # bgcolor="pink",
                                                                                # padding=ft.padding.symmetric(horizontal=0, vertical=5),
                                                                                # border_radius=20,
                                                                                content=ft.ResponsiveRow(
                                                                                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                                                                    vertical_alignment="center",
                                                                                    controls=[
                                                                                        ft.Container(# Botes Iniciales
                                                                                            alignment=ft.alignment.center,
                                                                                            col=4,
                                                                                            # bgcolor="yellow",
                                                                                            content=ft.Container(
                                                                                                # bgcolor=self.color_teal_2,
                                                                                                padding=2.5,
                                                                                                border_radius=5,
                                                                                                content=self.coi
                                                                                            )
                                                                                        ),
                                                                                        ft.Container(# Botes Finales
                                                                                            alignment=ft.alignment.center,
                                                                                            col=4,
                                                                                            # bgcolor="yellow",
                                                                                            content=ft.Container(
                                                                                                # bgcolor=self.color_teal_2,
                                                                                                padding=2.5,
                                                                                                border_radius=5,
                                                                                                content=self.cof
                                                                                            ),
                                                                                        ),
                                                                                    ]
                                                                                )
                                                                            ),
                                                                            ft.Container(# Venta Botes
                                                                                alignment=ft.alignment.center,
                                                                                # margin=ft.margin.only(bottom=25),
                                                                                # bgcolor="pink",
                                                                                # padding=ft.padding.symmetric(horizontal=0, vertical=5),
                                                                                # border_radius=20,
                                                                                content=ft.ResponsiveRow(
                                                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                                                    vertical_alignment="center",
                                                                                    controls=[
                                                                                        ft.Container(
                                                                                            alignment=ft.alignment.center,
                                                                                            col=6,
                                                                                            # bgcolor="yellow",
                                                                                            content=ft.Container(
                                                                                                # bgcolor=self.color_teal_2,
                                                                                                padding=2.5,
                                                                                                border_radius=5,
                                                                                                content=self.cov
                                                                                            )
                                                                                        ),
                                                                                    ]
                                                                                )
                                                                            ),
                                                                        ]
                                                                    )
                                                                )
                                                            ]
                                                        )
                                                    ),
                                                    ft.Container(# Crema Chocolate
                                                        col=4,
                                                        margin=ft.Margin(top=5, bottom=0, left=5, right=5),
                                                        # padding=ft.padding.symmetric(horizontal=5, vertical=5),
                                                        # bgcolor="blue",
                                                        content=ft.Column(
                                                            # alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                                            # horizontal_alignment="center",
                                                            controls=[
                                                                ft.Container(# Crema Chocolate
                                                                    # margin=ft.margin.symmetric(horizontal=5, vertical=10),
                                                                    # height=250,
                                                                    # width=600,
                                                                    margin=8,
                                                                    alignment=ft.alignment.center,
                                                                    bgcolor="#292929",
                                                                    border=ft.border.all(width=3, color="white"),
                                                                    border_radius=5,
                                                                    padding=ft.Padding(top=5, bottom=7, left=0, right=0),
                                                                    shadow=ft.BoxShadow(
                                                                        spread_radius=1,
                                                                        blur_radius=15,
                                                                        color=ft.colors.BLUE_GREY_100,
                                                                        offset=ft.Offset(0, 0),
                                                                        blur_style=ft.ShadowBlurStyle.OUTER,
                                                                    ),
                                                                    content=ft.Column(
                                                                        alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                                                        controls=[
                                                                            ft.Container(# Titulo
                                                                                alignment=ft.alignment.center,
                                                                                height=15,
                                                                                # padding=7,
                                                                                # bgcolor="blue",
                                                                                # border_radius=20,
                                                                                # width=180,
                                                                                content=ft.Column(
                                                                                    # horizontal_alignment="center",
                                                                                    controls=[
                                                                                        ft.Text("* CREMA CHOCOLATE *", color="#bfc244", weight=ft.FontWeight.BOLD, size=16, style=ft.TextStyle(letter_spacing=10)),
                                                                                        # ft.Divider(# Separador de seccion con Divider
                                                                                        #     height=1,
                                                                                        #     color="white",
                                                                                        #     thickness=.5,
                                                                                        #     leading_indent=400,
                                                                                        #     trailing_indent=400
                                                                                        # ),
                                                                                    ]
                                                                                )
                                                                            ),
                                                                            ft.Container(# Botes Dia
                                                                                alignment=ft.alignment.center,
                                                                                # margin=ft.margin.only(bottom=25),
                                                                                # bgcolor="pink",
                                                                                # padding=ft.padding.symmetric(horizontal=0, vertical=5),
                                                                                # border_radius=20,
                                                                                content=ft.ResponsiveRow(
                                                                                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                                                                    vertical_alignment="center",
                                                                                    controls=[
                                                                                        ft.Container(# Botes Iniciales
                                                                                            alignment=ft.alignment.center,
                                                                                            col=4,
                                                                                            # bgcolor="yellow",
                                                                                            content=ft.Container(
                                                                                                # bgcolor=self.color_teal_2,
                                                                                                padding=2.5,
                                                                                                border_radius=5,
                                                                                                content=self.cchi
                                                                                            )
                                                                                        ),
                                                                                        ft.Container(# Botes Finales
                                                                                            alignment=ft.alignment.center,
                                                                                            col=4,
                                                                                            # bgcolor="yellow",
                                                                                            content=ft.Container(
                                                                                                # bgcolor=self.color_teal_2,
                                                                                                padding=2.5,
                                                                                                border_radius=5,
                                                                                                content=self.cchf
                                                                                            ),
                                                                                        ),
                                                                                    ]
                                                                                )
                                                                            ),
                                                                            ft.Container(# Venta Botes
                                                                                alignment=ft.alignment.center,
                                                                                # margin=ft.margin.only(bottom=25),
                                                                                # bgcolor="pink",
                                                                                # padding=ft.padding.symmetric(horizontal=0, vertical=5),
                                                                                # border_radius=20,
                                                                                content=ft.ResponsiveRow(
                                                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                                                    vertical_alignment="center",
                                                                                    controls=[
                                                                                        ft.Container(
                                                                                            alignment=ft.alignment.center,
                                                                                            col=6,
                                                                                            # bgcolor="yellow",
                                                                                            content=ft.Container(
                                                                                                # bgcolor=self.color_teal_2,
                                                                                                padding=2.5,
                                                                                                border_radius=5,
                                                                                                content=self.cchv
                                                                                            )
                                                                                        ),
                                                                                    ]
                                                                                )
                                                                            ),
                                                                        ]
                                                                    )
                                                                ),
                                                            ]
                                                        )
                                                    ),
                                                    ft.Container(# Crema Cafe
                                                        col=4,
                                                        margin=ft.Margin(top=5, bottom=0, left=3, right=20),
                                                        # padding=ft.padding.symmetric(horizontal=5, vertical=5),
                                                        # bgcolor="blue",
                                                        content=ft.Column(
                                                            # alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                                            # horizontal_alignment="center",
                                                            controls=[
                                                                ft.Container(# Crema Cafe
                                                                    # margin=ft.margin.symmetric(horizontal=5, vertical=10),
                                                                    # height=250,
                                                                    # width=600,
                                                                    margin=8,
                                                                    alignment=ft.alignment.center,
                                                                    bgcolor="#292929",
                                                                    border=ft.border.all(width=3, color="white"),
                                                                    border_radius=5,
                                                                    padding=ft.Padding(top=5, bottom=7, left=0, right=0),
                                                                    shadow=ft.BoxShadow(
                                                                        spread_radius=1,
                                                                        blur_radius=15,
                                                                        color=ft.colors.BLUE_GREY_100,
                                                                        offset=ft.Offset(0, 0),
                                                                        blur_style=ft.ShadowBlurStyle.OUTER,
                                                                    ),
                                                                    content=ft.Column(
                                                                        alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                                                        controls=[
                                                                            ft.Container(# Titulo
                                                                                alignment=ft.alignment.center,
                                                                                height=15,
                                                                                # padding=7,
                                                                                # bgcolor="blue",
                                                                                # border_radius=20,
                                                                                # width=180,
                                                                                content=ft.Column(
                                                                                    # horizontal_alignment="center",
                                                                                    controls=[
                                                                                        ft.Text("* CREMA CAFE *", color="#bfc244", weight=ft.FontWeight.BOLD, size=16, style=ft.TextStyle(letter_spacing=10)),
                                                                                        # ft.Divider(# Separador de seccion con Divider
                                                                                        #     height=1,
                                                                                        #     color="white",
                                                                                        #     thickness=.5,
                                                                                        #     leading_indent=400,
                                                                                        #     trailing_indent=400
                                                                                        # ),
                                                                                    ]
                                                                                )
                                                                            ),
                                                                            ft.Container(# Botes Dia
                                                                                alignment=ft.alignment.center,
                                                                                # margin=ft.margin.only(bottom=25),
                                                                                # bgcolor="pink",
                                                                                # padding=ft.padding.symmetric(horizontal=0, vertical=5),
                                                                                # border_radius=20,
                                                                                content=ft.ResponsiveRow(
                                                                                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                                                                    vertical_alignment="center",
                                                                                    controls=[
                                                                                        ft.Container(# Botes Iniciales
                                                                                            alignment=ft.alignment.center,
                                                                                            col=4,
                                                                                            # bgcolor="yellow",
                                                                                            content=ft.Container(
                                                                                                # bgcolor=self.color_teal_2,
                                                                                                padding=2.5,
                                                                                                border_radius=5,
                                                                                                content=self.ccai
                                                                                            )
                                                                                        ),
                                                                                        ft.Container(# Botes Finales
                                                                                            alignment=ft.alignment.center,
                                                                                            col=4,
                                                                                            # bgcolor="yellow",
                                                                                            content=ft.Container(
                                                                                                # bgcolor=self.color_teal_2,
                                                                                                padding=2.5,
                                                                                                border_radius=5,
                                                                                                content=self.ccaf
                                                                                            ),
                                                                                        ),
                                                                                    ]
                                                                                )
                                                                            ),
                                                                            ft.Container(# Venta Botes
                                                                                alignment=ft.alignment.center,
                                                                                # margin=ft.margin.only(bottom=25),
                                                                                # bgcolor="pink",
                                                                                # padding=ft.padding.symmetric(horizontal=0, vertical=5),
                                                                                # border_radius=20,
                                                                                content=ft.ResponsiveRow(
                                                                                    alignment=ft.MainAxisAlignment.CENTER,
                                                                                    vertical_alignment="center",
                                                                                    controls=[
                                                                                        ft.Container(
                                                                                            alignment=ft.alignment.center,
                                                                                            col=6,
                                                                                            # bgcolor="yellow",
                                                                                            content=ft.Container(
                                                                                                # bgcolor=self.color_teal_2,
                                                                                                padding=2.5,
                                                                                                border_radius=5,
                                                                                                content=self.ccav
                                                                                            )
                                                                                        ),
                                                                                    ]
                                                                                )
                                                                            ),
                                                                        ]
                                                                    )
                                                                ),
                                                            ]
                                                        )
                                                    ),
                                                ]
                                            )
                                        ),
                                    ]
                                )
                            ),
                            ft.Tab(# Vasos
                                text="Vasos",
                                content=ft.ResponsiveRow(
                                    alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                                    controls=[
                                        ft.Container(# Vasos Chicos
                                            col=12,
                                            margin=ft.Margin(top=30, bottom=0, left=30, right=30),
                                            # padding=ft.padding.symmetric(horizontal=5, vertical=5),
                                            # bgcolor="blue",
                                            content=ft.Column(
                                                # alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                                # horizontal_alignment="center",
                                                controls=[
                                                    ft.Container(# Vasos Chicos
                                                        # margin=ft.margin.symmetric(horizontal=5, vertical=10),
                                                        height=530,
                                                        width=1300,
                                                        margin=10,
                                                        alignment=ft.alignment.center,
                                                        bgcolor="#292929",
                                                        border=ft.border.all(width=3, color="white"),
                                                        border_radius=5,
                                                        padding=ft.Padding(top=5, bottom=5, left=0, right=0),
                                                        shadow=ft.BoxShadow(
                                                            spread_radius=1,
                                                            blur_radius=15,
                                                            color=ft.colors.BLUE_GREY_100,
                                                            offset=ft.Offset(0, 0),
                                                            blur_style=ft.ShadowBlurStyle.OUTER,
                                                        ),
                                                        content=ft.Column(
                                                            alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                                            controls=[
                                                                ft.Container(# Vasos Chicos
                                                                    alignment=ft.alignment.center,
                                                                    height=15,
                                                                    # padding=7,
                                                                    # bgcolor="blue",
                                                                    # border_radius=20,
                                                                    # width=180,
                                                                    content=ft.Column(
                                                                        # horizontal_alignment="center",
                                                                        controls=[
                                                                            ft.Text("* VASOS CHICOS *", color="#bfc244", weight=ft.FontWeight.BOLD, size=18, style=ft.TextStyle(letter_spacing=10)),
                                                                            # ft.Divider(# Separador de seccion con Divider
                                                                            #     height=1,
                                                                            #     color="white",
                                                                            #     thickness=.5,
                                                                            #     leading_indent=400,
                                                                            #     trailing_indent=400
                                                                            # ),
                                                                        ]
                                                                    )
                                                                ),
                                                                ft.Container(# Vasos Chicos
                                                                    alignment=ft.alignment.center,
                                                                    margin=ft.margin.only(bottom=25),
                                                                    # bgcolor="pink",
                                                                    # padding=ft.padding.symmetric(horizontal=0, vertical=5),
                                                                    # border_radius=20,
                                                                    content=ft.ResponsiveRow(
                                                                        alignment=ft.MainAxisAlignment.CENTER,
                                                                        vertical_alignment="center",
                                                                        controls=[
                                                                            ft.Container(# Tapas chicas iniciales
                                                                                alignment=ft.alignment.center,
                                                                                col=2,
                                                                                # bgcolor="yellow",
                                                                                content=ft.Container(
                                                                                    # bgcolor=self.color_teal_2,
                                                                                    border_radius=5,
                                                                                    content=self.tci
                                                                                )
                                                                            ),
                                                                            ft.Container(# Tapas chicos finales
                                                                                alignment=ft.alignment.center,
                                                                                col=2,
                                                                                # bgcolor="yellow",
                                                                                content=ft.Container(
                                                                                    # bgcolor=self.color_teal_2,
                                                                                    # padding=2.5,
                                                                                    border_radius=5,
                                                                                    content=self.tcf
                                                                                ),
                                                                            ),
                                                                            ft.Container(# Vasos chicos inciales
                                                                                alignment=ft.alignment.center,
                                                                                col=2,
                                                                                # bgcolor="yellow",
                                                                                content=ft.Container(
                                                                                    # bgcolor=self.color_teal_2,
                                                                                    border_radius=5,
                                                                                    content=self.vci
                                                                                ),
                                                                            ),
                                                                            ft.Container(# Vasos chicos finales
                                                                                alignment=ft.alignment.center,
                                                                                col=2,
                                                                                # bgcolor="yellow",
                                                                                content=ft.Container(# Vasos Chicos
                                                                                    # bgcolor=self.color_teal_2,
                                                                                    border_radius=5,
                                                                                    content=self.vcf
                                                                                ),
                                                                            ),
                                                                            ft.Container(# Vasos chicos vendidos
                                                                                alignment=ft.alignment.center,
                                                                                col=2,
                                                                                # bgcolor="yellow",
                                                                                content=ft.Container(
                                                                                    # bgcolor=self.color_teal_2,
                                                                                    padding=2.5,
                                                                                    border_radius=5,
                                                                                    content=self.vcven
                                                                                ),
                                                                            ),
                                                                            ft.Container(# Venta total vasos chicos
                                                                                alignment=ft.alignment.center,
                                                                                col=2,
                                                                                # bgcolor="yellow",
                                                                                content=ft.Container(
                                                                                    # bgcolor="#f00000",
                                                                                    border_radius=5,
                                                                                    content=self.vcvt
                                                                                ),
                                                                            ),
                                                                        ]
                                                                    )
                                                                ),
                                                                ft.Container(# Vasos Medianos
                                                                    alignment=ft.alignment.center,
                                                                    height=15,
                                                                    # padding=7,
                                                                    # bgcolor="blue",
                                                                    # border_radius=20,
                                                                    # width=180,
                                                                    content=ft.Column(
                                                                        horizontal_alignment="center",
                                                                        controls=[
                                                                            ft.Text("* VASOS MEDIANOS *", color="#bfc244", weight=ft.FontWeight.BOLD, size=18, style=ft.TextStyle(letter_spacing=10)),
                                                                            # ft.Divider(# Separador de seccion con Divider
                                                                            #     height=1,
                                                                            #     color="#ff1765",
                                                                            #     thickness=1,
                                                                            #     leading_indent=400,
                                                                            #     trailing_indent=400
                                                                            # ),
                                                                        ]
                                                                    )
                                                                ),
                                                                ft.Container(# Vasos Medianos
                                                                    alignment=ft.alignment.center,
                                                                    margin=ft.margin.only(bottom=25),
                                                                    # bgcolor="pink",
                                                                    # padding=ft.padding.symmetric(horizontal=0, vertical=5),
                                                                    # border_radius=20,
                                                                    content=ft.ResponsiveRow(
                                                                        alignment=ft.MainAxisAlignment.CENTER,
                                                                        vertical_alignment="center",
                                                                        controls=[
                                                                            ft.Container(# Tapas medianas iniciales
                                                                                alignment=ft.alignment.center,
                                                                                col=2,
                                                                                # bgcolor="yellow",
                                                                                content=ft.Container(
                                                                                    # bgcolor=self.color_teal_2,
                                                                                    border_radius=5,
                                                                                    content=self.tmi
                                                                                )
                                                                            ),
                                                                            ft.Container(# Tapas medianas finales
                                                                                alignment=ft.alignment.center,
                                                                                col=2,
                                                                                # bgcolor="yellow",
                                                                                content=ft.Container(
                                                                                    # bgcolor=self.color_teal_2,
                                                                                    border_radius=5,
                                                                                    content=self.tmf
                                                                                ),
                                                                            ),
                                                                            ft.Container(# vasos medianos iniciales
                                                                                alignment=ft.alignment.center,
                                                                                col=2,
                                                                                # bgcolor="yellow",
                                                                                content=ft.Container(
                                                                                    # bgcolor=self.color_teal_2,
                                                                                    border_radius=5,
                                                                                    content=self.vmi
                                                                                ),
                                                                            ),
                                                                            ft.Container(# Vasos medianos finales
                                                                                alignment=ft.alignment.center,
                                                                                col=2,
                                                                                # bgcolor="yellow",
                                                                                content=ft.Container(# Vasos Chicos
                                                                                    # bgcolor=self.color_teal_2,
                                                                                    border_radius=5,
                                                                                    content=self.vmf
                                                                                ),
                                                                            ),
                                                                            ft.Container(# Vasos medianos vendidos
                                                                                alignment=ft.alignment.center,
                                                                                col=2,
                                                                                # bgcolor="yellow",
                                                                                content=ft.Container(
                                                                                    # bgcolor=self.color_teal_2,
                                                                                    border_radius=5,
                                                                                    content=self.vmven
                                                                                ),
                                                                            ),
                                                                            ft.Container(# Venta total vasos medianos
                                                                                alignment=ft.alignment.center,
                                                                                col=2,
                                                                                # bgcolor="yellow",
                                                                                content=ft.Container(
                                                                                    # bgcolor="#f00000",
                                                                                    border_radius=5,
                                                                                    content=self.vmvt
                                                                                ),
                                                                            ),
                                                                        ]
                                                                    )
                                                                ),
                                                                ft.Container(# Vasos Grandes
                                                                    alignment=ft.alignment.center,
                                                                    height=15,
                                                                    # padding=7,
                                                                    # bgcolor="blue",
                                                                    # border_radius=20,
                                                                    # width=180,
                                                                    content=ft.Column(
                                                                        horizontal_alignment="center",
                                                                        controls=[
                                                                            ft.Text("* VASOS GRANDES *", color="#bfc244", weight=ft.FontWeight.BOLD, size=18, style=ft.TextStyle(letter_spacing=10)),
                                                                            # ft.Divider(# Separador de seccion con Divider
                                                                            #     height=1,
                                                                            #     color="#ff1765",
                                                                            #     thickness=1,
                                                                            #     leading_indent=400,
                                                                            #     trailing_indent=400
                                                                            # ),
                                                                        ]
                                                                    )
                                                                ),
                                                                ft.Container(# Vasos Grandes
                                                                    alignment=ft.alignment.center,
                                                                    margin=ft.margin.only(bottom=25),
                                                                    # bgcolor="pink",
                                                                    # padding=ft.padding.symmetric(horizontal=0, vertical=5),
                                                                    # border_radius=20,
                                                                    content=ft.ResponsiveRow(
                                                                        alignment=ft.MainAxisAlignment.CENTER,
                                                                        vertical_alignment="center",
                                                                        controls=[
                                                                            ft.Container(# Tapas grandes iniciales
                                                                                alignment=ft.alignment.center,
                                                                                col=2,
                                                                                # bgcolor="yellow",
                                                                                content=ft.Container(
                                                                                    # bgcolor=self.color_teal_2,
                                                                                    border_radius=5,
                                                                                    content=self.tgi
                                                                                )
                                                                            ),
                                                                            ft.Container(# Tapas grandes finales
                                                                                alignment=ft.alignment.center,
                                                                                col=2,
                                                                                # bgcolor="yellow",
                                                                                content=ft.Container(
                                                                                    # bgcolor=self.color_teal_2,
                                                                                    border_radius=5,
                                                                                    content=self.tgf
                                                                                ),
                                                                            ),
                                                                            ft.Container(# Vasos grandes inciales
                                                                                alignment=ft.alignment.center,
                                                                                col=2,
                                                                                # bgcolor="yellow",
                                                                                content=ft.Container(
                                                                                    # bgcolor=self.color_teal_2,
                                                                                    border_radius=5,
                                                                                    content=self.vgi
                                                                                ),
                                                                            ),
                                                                            ft.Container(# Vasos grandes finales
                                                                                alignment=ft.alignment.center,
                                                                                col=2,
                                                                                # bgcolor="yellow",
                                                                                content=ft.Container(# Vasos Chicos
                                                                                    # bgcolor=self.color_teal_2,
                                                                                    border_radius=5,
                                                                                    content=self.vgf
                                                                                ),
                                                                            ),
                                                                            ft.Container(# Vasos grandes vendidos
                                                                                alignment=ft.alignment.center,
                                                                                col=2,
                                                                                # bgcolor="yellow",
                                                                                content=ft.Container(
                                                                                    # bgcolor=self.color_teal_2,
                                                                                    border_radius=5,
                                                                                    content=self.vgven
                                                                                ),
                                                                            ),
                                                                            ft.Container(# Venta total vasos grandes
                                                                                alignment=ft.alignment.center,
                                                                                col=2,
                                                                                # bgcolor="yellow",
                                                                                content=ft.Container(
                                                                                    # bgcolor="#f00000",
                                                                                    border_radius=5,
                                                                                    content=self.vgvt
                                                                                ),
                                                                            ),
                                                                        ]
                                                                    )
                                                                ),
                                                                ft.Container(# Venta Total Vasos en General
                                                                    alignment=ft.alignment.center,
                                                                    height=45,
                                                                    # padding=7,
                                                                    # bgcolor="blue",
                                                                    # border_radius=20,
                                                                    # width=180,
                                                                    content=ft.Column(
                                                                        horizontal_alignment="center",
                                                                        controls=[
                                                                            ft.Text("<<< VENTA GENERAL DE VASOS >>>", color="#bfc244", weight=ft.FontWeight.BOLD, size=20, style=ft.TextStyle(letter_spacing=10)),
                                                                            # ft.Divider(# Separador de seccion con Divider
                                                                            #     height=1,
                                                                            #     color="#ff1765",
                                                                            #     thickness=1,
                                                                            #     leading_indent=400,
                                                                            #     trailing_indent=400
                                                                            # ),
                                                                        ]
                                                                    )
                                                                ),
                                                                ft.Container(# Venta Total Vasos en General
                                                                    alignment=ft.alignment.center,
                                                                    margin=ft.margin.only(bottom=5),
                                                                    # margin=ft.margin.only(bottom=20),
                                                                    # bgcolor="pink",
                                                                    # padding=ft.padding.symmetric(horizontal=0, vertical=5),
                                                                    # border_radius=20,
                                                                    content=ft.ResponsiveRow(
                                                                        alignment=ft.MainAxisAlignment.CENTER,
                                                                        vertical_alignment="center",
                                                                        controls=[
                                                                            ft.Container(# Total Vasos Vendidos
                                                                                col=2.5,
                                                                                alignment=ft.alignment.center,
                                                                                bgcolor="#292929",
                                                                                padding=2.5,
                                                                                border=ft.border.all(width=1, color="#292929"),
                                                                                border_radius=5,
                                                                                margin=ft.margin.only(right=60),
                                                                                shadow=ft.BoxShadow(
                                                                                    spread_radius=.5,
                                                                                    blur_radius=5,
                                                                                    color="#0042e8",
                                                                                    offset=ft.Offset(0, 0),
                                                                                    blur_style=ft.ShadowBlurStyle.OUTER,
                                                                                ),
                                                                                content=self.vtv
                                                                            ),
                                                                            ft.Container(# Total Vasos Vendidos
                                                                                col=2.5,
                                                                                alignment=ft.alignment.center,
                                                                                bgcolor="#292929",
                                                                                padding=2.5,
                                                                                border=ft.border.all(width=1, color="#292929"),
                                                                                border_radius=5,
                                                                                margin=ft.margin.only(left=60),
                                                                                shadow=ft.BoxShadow(
                                                                                    spread_radius=.5,
                                                                                    blur_radius=5,
                                                                                    color="#ff0707",
                                                                                    offset=ft.Offset(0, 0),
                                                                                    blur_style=ft.ShadowBlurStyle.OUTER,
                                                                                ),
                                                                                content=self.vvmt
                                                                            ),
                                                                        ]
                                                                    )
                                                                ),
                                                            ]
                                                        )
                                                    )
                                                ]
                                            )
                                        ),
                                    ]
                                )
                            ),
                            ft.Tab(# Extras y Adicionales
                                text="Extras y Adicionales",
                            )
                        ]
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
                margin=3,
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
                                # ft.Column(# Separador de secciones
                                #     col=12,
                                #     controls=[
                                #         ft.Container(
                                #             margin=ft.Margin(right=25, left=25, top=0, bottom=0),
                                #             bgcolor=self.color_teal,
                                #             height=2,
                                #             border_radius=2.5
                                #         ),
                                #     ]
                                # ),
                                ft.Divider(# Separador de seccion con Divider
                                    height=1,
                                    color=self.color_teal,
                                    thickness=3,
                                    # leading_indent=50,
                                    # trailing_indent=10
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
                                                    # bgcolor=self.color_teal,
                                                    alignment=ft.alignment.center,
                                                    border_radius=5,
                                                    padding=1,
                                                    shadow=ft.BoxShadow(
                                                        spread_radius=1,
                                                        blur_radius=15,
                                                        color=ft.colors.BLUE_GREY_100,
                                                        offset=ft.Offset(0, 0),
                                                        blur_style=ft.ShadowBlurStyle.OUTER,
                                                    ),
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
                                                                        content=ft.ElevatedButton(text="Cargar Archivo", bgcolor=self.color_teal, color="black", icon=ft.Icons.ADD, icon_color="black", style=ft.ButtonStyle(text_style={
                                                                            ft.ControlState.DEFAULT: ft.TextStyle(size=12),
                                                                            ft.ControlState.PRESSED: ft.TextStyle(size=10)
                                                                        })),
                                                                    ),
                                                                    ft.Container(
                                                                        alignment=ft.alignment.center,
                                                                        padding=15,
                                                                        content=ft.ElevatedButton(text="Exportar Archivo", bgcolor=self.color_teal, color="black", icon=ft.Icons.UPLOAD, icon_color="black", style=ft.ButtonStyle(text_style={
                                                                            ft.ControlState.DEFAULT: ft.TextStyle(size=12),
                                                                            ft.ControlState.PRESSED: ft.TextStyle(size=10)
                                                                        }), on_click=self.create_ReportePDF),
                                                                    ),
                                                                    ft.Container(
                                                                        alignment=ft.alignment.center,
                                                                        padding=15,
                                                                        content=ft.ElevatedButton(text="Borrar Archivo", bgcolor=self.color_teal, color="black", icon=ft.Icons.DELETE, icon_color="black", style=ft.ButtonStyle(text_style={
                                                                            ft.ControlState.DEFAULT: ft.TextStyle(size=12),
                                                                            ft.ControlState.PRESSED: ft.TextStyle(size=10)
                                                                        })),
                                                                    ),
                                                                    ft.Container(
                                                                        alignment=ft.alignment.center,
                                                                        padding=15,
                                                                        content=ft.ElevatedButton(text="Limpiar Campos", bgcolor=self.color_teal, color="black", icon=ft.Icons.CLEAR_ALL, icon_color="black", style=ft.ButtonStyle(text_style={
                                                                            ft.ControlState.DEFAULT: ft.TextStyle(size=12),
                                                                            ft.ControlState.PRESSED: ft.TextStyle(size=10)
                                                                        }), on_click=self.reset_fieldsText),
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
                                                    # bgcolor=self.color_teal,
                                                    alignment=ft.alignment.center,
                                                    border_radius=5,
                                                    padding=1,
                                                    shadow=ft.BoxShadow(
                                                        spread_radius=1,
                                                        blur_radius=15,
                                                        color=ft.colors.BLUE_GREY_100,
                                                        offset=ft.Offset(0, 0),
                                                        blur_style=ft.ShadowBlurStyle.OUTER,
                                                    ),
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


        self.branches = ft.Row(
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
                                    alignment=ft.alignment.center,
                                    content=ft.Column(
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        horizontal_alignment="center",
                                        controls=[
                                            ft.Text("En proceso...", size=25),
                                            ft.Container(
                                                bgcolor="#ff2525",
                                                width=200,
                                                height=2
                                            )
                                        ]
                                    )
                                )
                            ]
                        )
                    )
                )
            ]
        )

        self.stock = ft.Row(
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
                                    alignment=ft.alignment.center,
                                    content=ft.Column(
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        horizontal_alignment="center",
                                        controls=[
                                            ft.Text("En proceso...", size=25),
                                            ft.Container(
                                                bgcolor="#ff2525",
                                                width=200,
                                                height=2
                                            )
                                        ]
                                    )
                                )
                            ]
                        )
                    )
                )
            ]
        )
       
        # ***** Paginas de los respectivos elementos laterales encerrados en una lista para el control de estas con los elementos laterales *****


        self.pages_containers = [ft.Column(controls=[self.select_Bar_Sucursales, self.home]), self.sales, self.branches, self.stock]

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
                self.pages
            ]
        )

    # ***** FUNCIONES *****

    # Funcion para el manejo del cambio de ventanas mediante la barra lateral de navegacion

    def change_page(self, e):
        index = e.control.selected_index
        self.main_container.content = self.pages_containers[index]
        self.update()

    def pdv_selection(self, e):
        if e.control.value == "glorieta":
            self.pdv = "Suc. Glorieta"

        if e.control.value == "sanmiguel":
            self.pdv = "Suc. San Miguel"

        if e.control.value == "vips":
            self.pdv = "Suc. Vips"

        if e.control.value == "cofradia2":
            self.pdv = "Suc. Cofradía 2"

        if e.control.value == "ensueños":
            self.pdv = "Suc. Ensueños"

        if e.control.value == "operagua":
            self.pdv = "Suc. Operagua"

        if e.control.value == "sanantonio":
            self.pdv = "Suc. San Antonio"

        if e.control.value == "lapiedad":
            self.pdv = "Suc. La Piedad"

    # ***** Funcion para el manejo de los radios boton's y la seleccion de las sucursales

    def generar_Reporte(self, e):
        # print(f"La sucursal seleccionada es: {e.control.value}")
        self.fecha_Actual = dt.datetime.today().date()

        self.fecha_Formateada = self.fecha_Actual.strftime("%d-%b-%Y")

        self.report_field.value = self.fecha_Formateada

        self.report_field.value = (
                                f"                                                   {self.fecha_Formateada}\n\n"
                                f"<<< {self.pdv} >>>\n\n"
                                f"Tapas Chicas Iniciales: {self.tci.value}\n"  
                                f"Tapas Chicas Finales: {self.tcf.value}\n"   
                                f"Tapas Chicas Diferencia: {self.tcdif.value}\n"
                                f"Vasos Chicos Iniciales: {self.vci.value}\n"  
                                f"Vasos Chicos Finales: {self.vcf.value}\n"   
                                f"Vasos Chicos Diferencia: {self.vcdif.value}\n"
                                f"Vasos Chicos Sin Vender: {self.vcsv.value}\n"  
                                f"VASOS CHICOS VENDIDOS: {self.vcven.value}\n"   
                                f"VENTA TOTAL VASOS CHICOS: $ {self.vcvt.value}\n\n"

                                f"Tapas Medianas Iniciales: {self.tmi.value}\n"  
                                f"Tapas Medianas Finales: {self.tmf.value}\n"   
                                f"Tapas Medianas Diferencia: {self.tmdif.value}\n"
                                f"Vasos Medianos Iniciales: {self.vmi.value}\n"  
                                f"Vasos Medianos Finales: {self.vmf.value}\n"   
                                f"Vasos Medianos Diferencia: {self.vmdif.value}\n"
                                f"Vasos Medianos Sin Vender: {self.vmsv.value}\n"  
                                f"VASOS MEDIANOS VENDIDOS: {self.vmven.value}\n"   
                                f"VENTA TOTAL VASOS MEDIANOS: $ {self.vmvt.value}\n\n"

                                f"Tapas Grandes Iniciales: {self.tgi.value}\n"  
                                f"Tapas Grandes Finales: {self.tgf.value}\n"   
                                f"Tapas Grandes Diferencia: {self.tgdif.value}\n"
                                f"Vasos Grandes Iniciales: {self.vgi.value}\n"  
                                f"Vasos Grandes Finales: {self.vgf.value}\n"   
                                f"Vasos Grandes Diferencia: {self.vgdif.value}\n"
                                f"Vasos Grandes Sin Vender: {self.vgsv.value}\n"  
                                f"VASOS GRANDES VENDIDOS: {self.vgven.value}\n"   
                                f"VENTA TOTAL VASOS GRANDES: $ {self.vgvt.value}\n\n"

                                f"Fresa Picada Inicial (Botes): {self.fpi.value}\n"  
                                f"Fresa Picada Final (Botes): {self.fpf.value}\n"   
                                f"Fresa Entera Inicial (Botes): {self.fei.value}\n"
                                f"Fresa Entera Final (Botes): {self.fef.value}\n"  
                                f"Fresa Remanente (Botes): {self.fr.value}\n"   
                                f"TOTAL FRESA VENDIDA (BOTES): {self.fv.value}\n\n"

                                f"Uva Picada Inicial (Botes): {self.upi.value}\n"  
                                f"Uva Picada Final (Botes): {self.upf.value}\n"   
                                f"Uva Entera Inicial (Botes): {self.uei.value}\n"
                                f"Uva Entera Final (Botes): {self.uef.value}\n"  
                                f"Uva Remanente (Botes): {self.ur.value}\n"   
                                f"TOTAL UVA VENDIDA (BOTES): {self.uv.value}\n\n"

                                f"Crema Original Inicial (Botes): {self.coi.value}\n"  
                                f"Crema Original Final (Botes): {self.cof.value}\n"   
                                f"CREMA ORIGINAL VENDIDA (Botes): {self.cov.value}\n\n"

                                f"Crema Chocolate Inicial (Botes): {self.cchi.value}\n"  
                                f"Crema Chocolate Final (Botes): {self.cchf.value}\n"   
                                f"CREMA CHOCOLATE VENDIDA (Botes): {self.cchv.value}\n\n"
                                
                                f"Crema Cafe Inicial (Botes): {self.ccai.value}\n"  
                                f"Crema Cafe Final (Botes): {self.ccaf.value}\n"   
                                f"CREMA CAFE VENDIDA (Botes): {self.ccav.value}\n\n"

                                f"Topping Extra de $5: {self.t5.value}\n"
                                f"Topping Extra de $10: {self.t10.value}\n"   
                                f"TOTAL TOPPINGS EXTRA: $ {self.tt.value}\n\n"

                                f"Servicio a Domicilio de $25: {self.sd25.value}\n"  
                                f"Servicio a Domicilio de $35: {self.sd35.value}\n"   
                                f"TOTAL SERVICIOS A DOMICILIO: $ {self.sdt.value}\n\n"

                                f"No. de Transferencias: {self.trn.value}\n"  
                                f"MONTO TOTAL TRANSFERENCIAS: $ {self.trt.value}\n\n"

                                f"No. de Gastos / Retiros: {self.grn.value}\n"
                                f"MONTO TOTAL GASTOS / RETIROS: $ {self.grt.value}\n\n"

                                f"Total de Ingresos: $ {self.bgi.value}\n"
                                f"Diferencia entre I/G/R/T: $ {self.bgd.value}\n\n"
                                f"TOTAL EFECTIVO PDV: $ {self.bgt.value}\n\n"

                                f"<<< FIN DEL REPORTE >>>"
                            )
        
    def create_ReportePDF(self, e):
        self.fecha_Actual = dt.datetime.today().date()

        self.fecha_Formateada = self.fecha_Actual.strftime("%d-%b-%Y")

        self.fecha_Formateada_RN = self.fecha_Actual.strftime("%d-%m-%y")

        pdf = FPDF(orientation="P", unit="mm", format="A4")
        pdf.add_page()
        
        pdf.set_font("Arial", "", 10)
        
        pdf.image("../Images/Images_Program/FresaReporte.png", 10, 7, 20)
        pdf.cell(187, 5, f'{self.fecha_Formateada}', 0, 1, "R")
        
        # Titulo
        pdf.cell(0, 25, f'Reporte {self.pdv}'.upper(), 0, 1, 'C')
        pdf.line(70, 28, 140, 28)
        
        # Vasos Chicos
        pdf.cell(160, 7, 'Tapas Chicas Iniciales', 1, 0)
        pdf.cell(30, 7, f'{self.tci.value}', 1, 1, 'C')
        pdf.cell(160, 7, 'Tapas Chicas Finales', 1, 0)
        pdf.cell(30, 7, f'{self.tcf.value}', 1, 1, 'C')
        pdf.cell(160, 7, 'Tapas Chicas Diferencia', 1, 0)
        pdf.cell(30, 7, f'{self.tcdif.value}', 1, 1, 'C')
        pdf.cell(160, 7, 'Vasos Chicos Iniciales', 1, 0)
        pdf.cell(30, 7, '0', 1, 1, 'C')
        pdf.cell(160, 7, 'Vasos Chicos Finales', 1, 0)
        pdf.cell(30, 7, '0', 1, 1, 'C')
        pdf.cell(160, 7, 'Vasos Chicos Diferencia', 1, 0)
        pdf.cell(30, 7, '0', 1, 1, 'C')
        pdf.cell(160, 7, 'Vasos Chicos Sin Vender', 1, 0)
        pdf.cell(30, 7, '0', 1, 1, 'C')
        pdf.cell(160, 7, 'VASOS CHICOS VENDIDOS', 1, 0)
        pdf.cell(30, 7, '0', 1, 1, 'C')
        pdf.cell(160, 7, 'VENTA TOTAL VASOS CHICOS', 1, 0)
        pdf.cell(30, 7, '0', 1, 1, 'C')
        
        # Separador con celda
        pdf.cell(0, 4, '', 0, 1)
        
        # Vasos Medianos
        pdf.cell(160, 7, 'Tapas Medianas Iniciales', 1, 0)
        pdf.cell(30, 7, '0', 1, 1, 'C')
        pdf.cell(160, 7, 'Tapas Medianas Finales', 1, 0)
        pdf.cell(30, 7, '0', 1, 1, 'C')
        pdf.cell(160, 7, 'Tapas Medianas Diferencia', 1, 0)
        pdf.cell(30, 7, '0', 1, 1, 'C')
        pdf.cell(160, 7, 'Vasos Medianos Iniciales', 1, 0)
        pdf.cell(30, 7, '0', 1, 1, 'C')
        pdf.cell(160, 7, 'Vasos Medianos Finales', 1, 0)
        pdf.cell(30, 7, '0', 1, 1, 'C')
        pdf.cell(160, 7, 'Vasos Medianos Diferencia', 1, 0)
        pdf.cell(30, 7, '0', 1, 1, 'C')
        pdf.cell(160, 7, 'Vasos Medianos Sin Vender', 1, 0)
        pdf.cell(30, 7, '0', 1, 1, 'C')
        pdf.cell(160, 7, 'VASOS MEDIANOS VENDIDOS', 1, 0)
        pdf.cell(30, 7, '0', 1, 1, 'C')
        pdf.cell(160, 7, 'VENTA TOTAL VASOS MEDIANOS', 1, 0)
        pdf.cell(30, 7, '0', 1, 1, 'C')
        
        # Separador con celda
        pdf.cell(0, 4, '', 0, 1)
        
        # Vasos Grandes
        pdf.cell(160, 7, 'Tapas Grandes Iniciales', 1, 0)
        pdf.cell(30, 7, '0', 1, 1, 'C')
        pdf.cell(160, 7, 'Tapas Grandes Finales', 1, 0)
        pdf.cell(30, 7, '0', 1, 1, 'C')
        pdf.cell(160, 7, 'Tapas Grandes Diferencia', 1, 0)
        pdf.cell(30, 7, '0', 1, 1, 'C')
        pdf.cell(160, 7, 'Vasos Grandes Iniciales', 1, 0)
        pdf.cell(30, 7, '0', 1, 1, 'C')
        pdf.cell(160, 7, 'Vasos Grandes Finales', 1, 0)
        pdf.cell(30, 7, '0', 1, 1, 'C')
        pdf.cell(160, 7, 'Vasos Grandes Diferencia', 1, 0)
        pdf.cell(30, 7, '0', 1, 1, 'C')
        pdf.cell(160, 7, 'Vasos Grandes Sin Vender', 1, 0)
        pdf.cell(30, 7, '0', 1, 1, 'C')
        pdf.cell(160, 7, 'VASOS GRANDES VENDIDOS', 1, 0)
        pdf.cell(30, 7, '0', 1, 1, 'C')
        pdf.cell(160, 7, 'VENTA TOTAL VASOS ', 1, 0)
        pdf.cell(30, 7, '0', 1, 1, 'C')
        
        # Fresa
        pdf.cell(160, 7, 'Fresa Picada Inicial (Botes)', 1, 0)
        pdf.cell(30, 7, '0', 1, 1, 'C')
        pdf.cell(160, 7, 'Fresa Picada Final (Botes)', 1, 0)
        pdf.cell(30, 7, '0', 1, 1, 'C')
        pdf.cell(160, 7, 'Fresa Entera Inicial (Botes)', 1, 0)
        pdf.cell(30, 7, '0', 1, 1, 'C')
        pdf.cell(160, 7, 'Fresa Entera Final (Botes)', 1, 0)
        pdf.cell(30, 7, '0', 1, 1, 'C')
        pdf.cell(160, 7, 'Fresa Remanente (Botes)', 1, 0)
        pdf.cell(30, 7, '0', 1, 1, 'C')
        pdf.cell(160, 7, 'TOTAL DE FRESA VENDIDA (BOTES)', 1, 0)
        pdf.cell(30, 7, '0', 1, 1, 'C')
        
        pdf.output(f"../Reportes_PDV's/{self.fecha_Formateada_RN} - Reporte {self.pdv}.pdf")
    
    # ***** Funciones para el manejo de los campos de texto de la seccion de vasos *****

    # Vasos Chicos

    def conversion_n_capture_vc(self, e):
        try:
            self.num_tci = int(self.tci.value)
            self.num_tcf = int(self.tcf.value)
            # self.num_tcdif = self.num_tci - self.num_tcf
            # self.tcdif.value = self.num_tcdif
            self.num_vci = int(self.vci.value)
            self.num_vcf = int(self.vcf.value)
            # self.num_vcdif = self.num_vci - self.num_vcf
            # self.vcdif.value = self.num_vcdif
            self.values_columnSale_vc()
            self.venta_Total_Vasos()
        except ValueError:
            pass
        finally:
            self.update()

    # Vasos Medianos

    def conversion_n_capture_vm(self, e):
        try:
            self.num_tmi = int(self.tmi.value)
            self.num_tmf = int(self.tmf.value)
            # self.num_tmdif = self.num_tmi - self.num_tmf
            # self.tmdif.value = self.num_tmdif
            self.num_vmi = int(self.vmi.value)
            self.num_vmf = int(self.vmf.value)
            # self.num_vmdif = self.num_vmi - self.num_vmf
            # self.vmdif.value = self.num_vmdif
            self.values_columnSale_vm()
            self.venta_Total_Vasos()
        except ValueError:
            pass
        finally:
            self.update()       

    # Vasos Grandes

    def conversion_n_capture_vg(self, e):
        try:
            self.num_tgi = int(self.tgi.value)
            self.num_tgf = int(self.tgf.value)
            # self.num_tgdif = self.num_tgi - self.num_tgf
            # self.tgdif.value = self.num_tgdif
            self.num_vgi = int(self.vgi.value)
            self.num_vgf = int(self.vgf.value)
            # self.num_vgdif = self.num_vgi - self.num_vgf
            # self.vgdif.value = self.num_vgdif
            self.values_columnSale_vg()
            self.venta_Total_Vasos()
        except ValueError:
            pass
        finally:
            self.update()       

    # Vasos Chicos

    def values_columnSale_vc(self):
        # self.num_vcsv = self.num_vcf
        # self.vcsv.value = self.num_vcsv
        # self.num_vcven = self.num_vcdif
        self.num_vcven = self.num_vci - self.num_vcf
        self.vcven.value = self.num_vcven
        self.num_vcvt = self.num_vcven * 50
        self.vcvt.value = self.num_vcvt

    # Vasos Medianos

    def values_columnSale_vm(self):
        # self.num_vmsv = self.num_vmf
        # self.vmsv.value = self.num_vmsv
        # self.num_vmven = self.num_vmdif
        self.num_vmven = self.num_vmi - self.num_vmf
        self.vmven.value = self.num_vmven
        self.num_vmvt = self.num_vmven * 70
        self.vmvt.value = self.num_vmvt

    # Vasos Grandes
    def values_columnSale_vg(self):
        # self.num_vgsv = self.num_vgf
        # self.vgsv.value = self.num_vgsv
        # self.num_vgven = self.num_vgdif
        self.num_vgven = self.num_vgi - self.num_vgf
        self.vgven.value = self.num_vgven
        self.num_vgvt = self.num_vgven * 150
        self.vgvt.value = self.num_vgvt

    def venta_Total_Vasos(self):
        self.num_vtv = self.vcven.value
        self.num_vvmt = self.vcvt.value
        self.vtv.value = self.num_vtv
        self.vvmt.value = self.num_vvmt

        self.num_vtv = self.num_vtv + self.vmven.value
        self.num_vvmt = self.num_vvmt + self.vmvt.value
        self.vtv.value = self.num_vtv
        self.vvmt.value = self.num_vvmt

        self.num_vtv = self.num_vtv + self.vgven.value
        self.num_vvmt = self.num_vvmt + self.vgvt.value
        self.vtv.value = self.num_vtv
        self.vvmt.value = self.num_vvmt
        self.update()

    # ***** Funciones para el manejo de los campos de texto de la seccion de frutas *****

    def conversion_n_capture_fr(self, e):
        try:
            if "." in self.fpi.value or "." in self.fpf.value or "." in self.fei.value or "." in self.fef.value:
                self.num_fpi = float(self.fpi.value)
                self.num_fpf = float(self.fpf.value)
                self.num_fei = float(self.fei.value)
                self.num_fef = float(self.fef.value)
            else:
                self.num_fpi = int(self.fpi.value)
                self.num_fpf = int(self.fpf.value)
                self.num_fei = int(self.fei.value)
                self.num_fef = int(self.fef.value)
            
            # self.num_fr = self.num_fpf + self.num_fef
            # self.num_fv = (self.num_fpi + self.num_fei) - self.num_fr
            self.num_fv = (self.num_fpi + self.num_fei) - (self.num_fpf + self.num_fef)

            # if self.num_fr % 2 == 0 or self.num_fr % 2 == 1:
            #     self.num_fr = int(self.num_fr)

            if self.num_fv % 2 == 0 or self.num_fv % 2 == 1:
                self.num_fv = int(self.num_fv)

            # self.fr.value = round(self.num_fr, 2)
            self.fv.value = round(self.num_fv, 2)
        except ValueError:
            pass
        finally:
            self.update()

    def conversion_n_capture_uva(self, e):
        try:
            if "." in self.upi.value or "." in self.upf.value or "." in self.uei.value or "." in self.uef.value:
                self.num_upi = float(self.upi.value)
                self.num_upf = float(self.upf.value)
                self.num_uei = float(self.uei.value)
                self.num_uef = float(self.uef.value)
            else:
                self.num_upi = int(self.upi.value)
                self.num_upf = int(self.upf.value)
                self.num_uei = int(self.uei.value)
                self.num_uef = int(self.uef.value)

            # self.num_ur = self.num_upf + self.num_uef
            # self.num_uv = (self.num_upi + self.num_uei) - self.num_ur
            self.num_uv = (self.num_upi + self.num_uei) - (self.num_upf + self.num_uef)

            # if self.num_ur % 2 == 0 or self.num_ur % 2 == 1:
            #     self.num_ur = int(self.num_ur)

            if self.num_uv % 2 == 0 or self.num_uv % 2 == 1:
                self.num_uv = int(self.num_uv)

            # self.ur.value = round(self.num_ur, 2)
            self.uv.value = round(self.num_uv, 2)
        except ValueError:
            pass
        finally:
            self.update()

    # ***** Funciones para el manejo de los campos de texto de la seccion de cremas *****

    def conversion_n_capture_co(self, e):
        try:
            if "." in self.coi.value or "." in self.cof.value:
                self.num_coi = float(self.coi.value)
                self.num_cof = float(self.cof.value)
            else:
                self.num_coi = int(self.coi.value)
                self.num_cof = int(self.cof.value)

            self.num_cov = self.num_coi - self.num_cof

            if self.num_cov % 2 == 0 or self.num_cov % 2 == 1:
                self.num_cov = int(self.num_cov)
                
            self.cov.value = round(self.num_cov, 2)
        except ValueError:
            pass
        finally:
            self.update()

    def conversion_n_capture_cch(self, e):
        try:
            if "." in self.cchi.value or "." in self.cchf.value:
                self.num_cchi = float(self.cchi.value)
                self.num_cchf = float(self.cchf.value)
            else:
                self.num_cchi = int(self.cchi.value)
                self.num_cchf = int(self.cchf.value)

            self.num_cchv = self.num_cchi - self.num_cchf

            if self.num_cchv % 2 == 0 or self.num_cchv % 2 == 1:
                self.num_cchv = int(self.num_cchv)

            self.cchv.value = round(self.num_cchv, 2)
        except ValueError:
            pass
        finally:
            self.update()

    def conversion_n_capture_cca(self, e):
        try:
            if "." in self.ccai.value or "." in self.ccaf.value:
                self.num_ccaf = float(self.ccaf.value)
                self.num_ccai = float(self.ccai.value)
            else:
                self.num_ccaf = int(self.ccaf.value)
                self.num_ccai = int(self.ccai.value)

            self.num_ccav = self.num_ccai - self.num_ccaf

            if self.num_ccav % 2 == 0 or self.num_ccav % 2 == 1:
                self.num_ccav = int(self.num_ccav)
            
            self.ccav.value = round(self.num_ccav, 2)
        except ValueError:
            pass
        finally:
            self.update()

    # ***** Funciones para el manejo de los campos de texto de la seccion de extras y adicionales *****

    def conversion_n_capture_tE(self, e):
        try:
            self.num_t5 = int(self.t5.value)
            self.num_t10 = int(self.t10.value)
            self.total_t5 = self.num_t5 * 5
            self.total_t10 = self.num_t10 * 10
            self.num_tt = self.total_t5 + self.total_t10
            self.tt.value = self.num_tt
        except:
            pass
        finally:
            self.update()

    def conversion_n_capture_sD(self, e):
        try:
            self.num_sd25 = int(self.sd25.value)
            self.num_sd35 = int(self.sd35.value)
            self.total_sd25 = self.num_sd25 * 25
            self.total_sd35 = self.num_sd35 * 35
            self.num_sdt = self.total_sd25 + self.total_sd35
            self.sdt.value = self.num_sdt
        except:
            pass
        finally:
            self.update()

    def balance_General(self, e):
        self.num_bgi = self.vcvt.value + self.vmvt.value + self.vgvt.value + self.tt.value + self.sdt.value
        self.bgi.value = self.num_bgi
        
        try:
            self.num_trt = int(self.trt.value)
            self.num_grt = int(self.grt.value)
            self.num_bgd = self.num_trt + self.num_grt
            self.bgd.value = self.num_bgd
            self.num_bgt = self.bgi.value - self.bgd.value
            self.bgt.value = self.num_bgt
        except ValueError:
            pass
        finally:
            self.update()

    def reset_Fields(self, e):
        self.variables_vc = [self.tci, self.tcf, self.tcdif, self.vci, self.vcf, self.vcdif, self.vcsv, self.vcven, self.vcvt]
        for element in self.variables_vc:
            element.value = ""

        self.variables_vm = [self.tmi, self.tmf, self.tmdif, self.vmi, self.vmf, self.vmdif, self.vmsv, self.vmven, self.vmvt]
        for element in self.variables_vm:
            element.value = ""

        self.variables_vg = [self.tgi, self.tgf, self.tgdif, self.vgi, self.vgf, self.vgdif, self.vgsv, self.vgven, self.vgvt]
        for element in self.variables_vg:
            element.value = ""

        self.variables_frutas = [self.fpi, self.fpf, self.fei, self.fef, self.fr, self.fv, self.upi, self.upf, self.uei, self.uef, self.ur, self.uv]
        for element in self.variables_frutas:
            element.value = ""

        self.variables_cremas = [self.coi, self.cof, self.cov, self.cchi, self.cchf, self.cchv, self.ccai, self.ccaf, self.ccav]
        for element in self.variables_cremas:
            element.value = ""

        self.extras = [self.t5, self.t10, self.tt, self.sd25, self.sd35, self.sdt, self.trn, self.trt, self.grn, self.grt, self.bgi, self.bgd, self.bgt]
        for element in self.extras:
            element.value = ""

        self.update()

    def reset_fieldsText(self, e):
        self.report_field.value = ""
        self.sales_field.value = ""
        self.update()

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
    page.theme_mode = ft.ThemeMode.DARK
    page.title = "Control PDV's"
    page.window.maximized = True
    page.window_resizable = True
    # page.window_opacity = .95
    page.add(UI(page))

# ***** Web Mode *****
# ft.app(target=main, view=ft.WEB_BROWSER)

# ***** Desktop Mode *****
ft.app(target=main)