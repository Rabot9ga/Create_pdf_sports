from reportlab.platypus.tables import Table, TableStyle, colors
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate
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
        if len(fixtures_data_dct[i][0])>max_len:
            max_len = len(fixtures_data_dct[i][0])
    lst_of_datas = [headers]
    for i in range(max_len):
        lst_of_row = []
        for j in fixtures_data_dct:
            if i>len(fixtures_data_dct[j])-1 and j == list(fixtures_data_dct.keys())[-1]:
                lst_of_row.extend([" ", " "])
            elif i>len(fixtures_data_dct[j])-1:
                lst_of_row.extend([" ", " ", " "])
            elif j == list(fixtures_data_dct.keys())[-1]:
                lst_of_row.extend([fixtures_data_dct[j][0][i], fixtures_data_dct[j][1][i]])
            else:
                lst_of_row.extend([fixtures_data_dct[j][0][i], fixtures_data_dct[j][1][i], " "])
        lst_of_datas.append(lst_of_row)
    return lst_of_datas


def create_pdf():
    green_color_bg = colors.HexColor("#34a85399", hasAlpha=True)
    doc = SimpleDocTemplate("trying.pdf", leftMargin=0, topMargin=0)
    data = creating_data_pdf()
    row_heights = len(data) * [0.37 * cm]
    row_heights[0] = 25
    column_width = len(data[0])*[1.5 * cm]
    t = Table(data, column_width, row_heights)
    t.setStyle(TableStyle([('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
    ('BOX', (0, 0), (-1, -1), 0.25, colors.black), ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE')])) # set all table style
    # set headers style

    doc.build([t])

if __name__ == "__main__":
    create_pdf()

# t.setStyle(TableStyle(
#     [("SPAN", (0, 0), (1, 0)), ("SPAN", (3, 0), (4, 0)), ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
#      ('BOX', (0, 0), (-1, -1), 0.25, colors.black), ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
#      ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'), ('FONTSIZE', (0, 0), (14, 0), 15)]))
# t.setStyle(TableStyle([("BACKGROUND", (1, 2), (1, 2), green_color_bg)]))


