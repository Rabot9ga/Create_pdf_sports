from reportlab.platypus.tables import Table, TableStyle, colors
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate

green_color_bg = colors.HexColor("#34a85399", hasAlpha=True)
doc = SimpleDocTemplate("trying.pdf", leftMargin=0, topMargin=0)
elements = []
data = [["Soccer", " ", "", "Tennis"],[1, 2, " ", 4, 5], [4, 5, " ", 7, 8], [7, 8]]
rowHeights = 4*[0.5*cm]
rowHeights[0]=25
t = Table(data, 5*[1.5*cm], rowHeights)
t.setStyle(TableStyle([("SPAN", (0, 0), (1, 0)), ("SPAN", (3, 0), (4, 0)), ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black), ('BOX', (0,0), (-1,-1), 0.25, colors.black), ('ALIGN', (0,0), (-1,-1), 'CENTER'), ('VALIGN', (0,0), (-1,-1), 'MIDDLE'), ('FONTSIZE', (0,0), (14, 0), 15)]))
t.setStyle(TableStyle([("BACKGROUND", (1, 2), (1, 2), green_color_bg)]))
elements.append(t)
doc.build(elements)