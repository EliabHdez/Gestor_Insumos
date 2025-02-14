from fpdf import FPDF

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.add_page()

pdf.set_font("Arial", "", 12)

pdf.image("FresaReporte.png", 10, 10, 20)
pdf.cell(0, 7, 'FECHA', 0, 1, "R")

# Titulo
pdf.cell(0, 20, 'REPORTE PUNTO DE VENTA', 0, 1, 'C')
pdf.line(70, 30, 140, 30)

# Vasos Chicos
pdf.cell(160, 7, 'Tapas Chicas Iniciales', 1, 0)
pdf.cell(30, 7, '0', 1, 1, 'C')
pdf.cell(160, 7, 'Tapas Chicas Finales', 1, 0)
pdf.cell(30, 7, '0', 1, 1, 'C')
pdf.cell(160, 7, 'Tapas Chicas Diferencia', 1, 0)
pdf.cell(30, 7, '0', 1, 1, 'C')
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
pdf.cell(0, 7, '', 0, 1)

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
pdf.cell(0, 7, '', 0, 1)

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


pdf.output("Reporte del Día.pdf")