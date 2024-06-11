from reportlab.platypus.tables import Table, TableStyle, colors
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate
from datetime import datetime
import pandas as pd
import os

def creating_dct_fixtures():
    dict_of_fixtures = dict()
    for i in os.listdir():
        if i[-4:] == ".txt":
            data = pd.read_csv(i, sep=",", header=None, index_col=False)
            dict_of_fixtures[i[0:-4]] = data
    return dict_of_fixtures

def creating_data_pdf():
    fixtures_data_dct = creating_dct_fixtures()
    headers = []
    for i in fixtures_data_dct:
        if i == list(fixtures_data_dct.keys())[-1]:
            headers.extend([i, " "])
        else:
            headers.extend([i, " ", " "])
    max_len = 0
    for i in fixtures_data_dct:
        if len(fixtures_data_dct[i][0]) > max_len:
            max_len = len(fixtures_data_dct[i][0])
    lst_of_datas = [headers]
    for i in range(max_len):
        lst_of_row = []
        for j in fixtures_data_dct:
            if i > len(fixtures_data_dct[j]) - 1 and j == list(fixtures_data_dct.keys())[-1]:
                lst_of_row.extend([" ", " "])
            elif i > len(fixtures_data_dct[j]) - 1:
                lst_of_row.extend([" ", " ", " "])
            elif j == list(fixtures_data_dct.keys())[-1]:
                lst_of_row.extend([fixtures_data_dct[j][0][i], fixtures_data_dct[j][1][i]])
            else:
                lst_of_row.extend([fixtures_data_dct[j][0][i], fixtures_data_dct[j][1][i], " "])
        lst_of_datas.append(lst_of_row)
    return lst_of_datas


def create_pdf():
    data = creating_data_pdf()
    row_heights = len(data) * [3.5 * mm]
    row_heights[0] = 30
    column_width = len(data[0]) * [14 * mm]
    today = datetime.today().strftime('%d-%m-%Y-%H')
    doc = SimpleDocTemplate(f"fixture_{today}.pdf", leftMargin=(((250*mm,600*mm)[0])-len(data[0])*14*mm)/2, topMargin=0, pagesize=(250*mm,600*mm))
    t = Table(data, column_width, row_heights)
    t.setStyle(TableStyle([('INNERGRID', (0, 0), (-1, -1), 0.25, colors.grey),
                           ('BOX', (0, 0), (-1, -1), 0.25, colors.grey), ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                           ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'), ('TOPPADDING', (0, 0), (-1, -1), 1),
                           ('BOTTOMPADDING', (0, 0), (-1, -1), 1),
                           ('LEFTPADDING', (0, 0), (-1, -1), 1),
                           ('RIGHTPADDING', (0, 0), (-1, -1), 1)]))  # set all table style
    fixtures_data_dct = creating_dct_fixtures()
    amount_of_sport = len(list(fixtures_data_dct.keys()))
    t.setStyle(TableStyle([('FONTSIZE', (0, 0), (amount_of_sport * 3 - 1, 0), 15)]))  # set headers style
    for i in range(amount_of_sport):
        t.setStyle(TableStyle([("SPAN", (i * 3, 0), (i * 3 + 1, 0))]))  # merge header cells
    start = 1
    for i in fixtures_data_dct:
        step = 255 / max(fixtures_data_dct[i][1])
        for j in range(len(fixtures_data_dct[i][1])):
            transparency = round(fixtures_data_dct[i][1][j] * step)
            green_color_bg = colors.HexColor(f"#15b13e{transparency:02x}", hasAlpha=True)
            t.setStyle(TableStyle([("BACKGROUND", (start, j + 1), (start, j + 1), green_color_bg)]))
        start += 3
    doc.build([t])


if __name__ == "__main__":
    create_pdf()
