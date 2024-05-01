from reportlab.platypus.tables import Table, TableStyle, colors
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate
import pandas as pd
import os

green_color_bg = colors.HexColor("#34a85399", hasAlpha=True)
doc = SimpleDocTemplate("trying.pdf", leftMargin=0, topMargin=0)

def creating_dct_fixtures():
    dict_of_fixtures = dict()
    for i in os.listdir():
        if i[-4:] == ".txt":
            data = pd.read_csv(i, sep=",", header=None)
            dict_of_fixtures[i[0:-4]] = data
    return dict_of_fixtures

def creating_headers_pdf():
    fixtures_data_dct = creating_dct_fixtures()
    headers = []
    for i in fixtures_data_dct:
        if i == list(fixtures_data_dct.keys())[-1]:
            headers.extend([i, " "])
        else:
            headers.extend([i, " ", " "])
    return headers

creating_headers_pdf()

data = [["Soccer", " ", "", "Tennis"], [1, 2, " ", 4, 5], [4, 5, " ", 7, 8], [7, 8]]

rowHeights = 4 * [0.5 * cm]
rowHeights[0] = 25
t = Table(data, 5 * [1.5 * cm], rowHeights)
t.setStyle(TableStyle(
    [("SPAN", (0, 0), (1, 0)), ("SPAN", (3, 0), (4, 0)), ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
     ('BOX', (0, 0), (-1, -1), 0.25, colors.black), ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
     ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'), ('FONTSIZE', (0, 0), (14, 0), 15)]))
t.setStyle(TableStyle([("BACKGROUND", (1, 2), (1, 2), green_color_bg)]))

doc.build([t])
