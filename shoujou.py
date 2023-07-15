import fpdf
import sys
import csv

START_Y = 78
START_X = 30
SHUMOKU_FONT = 20
HYOUSHOU_FONT = 32
NAME_FONT = 30
AFF_FONT = 22
CELL_HEIGHT_NAME = 12
CELL_HEIGHT_SHOU = 24
AFF_FONT_THRESH = 8
NAME_FONT_THRESH = 7

FIELD_TAIKAI = '大会名'
FIELD_SHUMOKU = '種目名'
FIELD_PLACE = '順位'
FIELD_AWARD = '表彰'
FIELD_TODOFUKEN = '都道府県'
FIELD_CODE_1 = '拳士コード1'
FIELD_AFF_1 = '所属名1'
FIELD_AFF_1_YOMI = '所属名ヨミガナ1'
FIELD_NAME_1 = '拳士名1'
FIELD_NAME_1_YOMI = '拳士名ヨミガナ1'
FIELD_CODE_2 = '拳士コード2'
FIELD_AFF_2 = '所属名2'
FIELD_AFF_2_YOMI = '所属名ヨミガナ2'
FIELD_NAME_2 = '拳士名2'
FIELD_NAME_2_YOMI = '拳士名ヨミガナ2'

"""
pdf = fpdf.FPDF('P','mm','A4')
pdf.add_page()
pdf.set_font('Arial','B',16)
pdf.cell(40,10,'Hello world!')
pdf.output('test.pdf','F')
"""

def getData(fname):
    res = list()
    with open(fname) as cf:
        cfr = csv.DictReader(cf)
        for row in cfr:
            res.append(row)
    return res

def getAffFont(aff):
    if len(aff) > AFF_FONT_THRESH:
        new_font = AFF_FONT - 2*(len(aff) - AFF_FONT_THRESH)
    else:
        new_font = AFF_FONT
    return new_font

def getNameFont(name):
    if len(name) > NAME_FONT_THRESH:
        new_font = NAME_FONT - 2*(len(name) - NAME_FONT_THRESH)
    else:
        new_font = NAME_FONT
    return new_font


def generatePDFs(data):
    pdf = fpdf.FPDF('P','mm','A4')
    pdf.add_font("ack",'','ackaisyo.ttf',uni=True)
    lData = len(data)
    for i in range(0,lData):
        pdf.add_page()
        pdf.set_font('ack','',1)
        pdf.image('bg.jpg',x=0,y=0,w=210)
        pdf.cell(0,h=START_Y)
        pdf.ln()

        pdf.cell(START_X)
        data_hs = data[i][FIELD_AWARD];
        data_sm = data[i][FIELD_SHUMOKU];
        pdf.set_font('ack','',SHUMOKU_FONT)
        pdf.cell(65,CELL_HEIGHT_SHOU,data_sm,align='R')
        pdf.cell(5,CELL_HEIGHT_SHOU)
        pdf.set_font('ack','',HYOUSHOU_FONT)
        pdf.cell(45,CELL_HEIGHT_SHOU,data_hs,align='L')

        pdf.ln()

        data_aff1 = data[i][FIELD_AFF_1]
        data_aff2 = data[i][FIELD_AFF_2]
        data_name1 = data[i][FIELD_NAME_1]
        data_name2 = data[i][FIELD_NAME_2]

        if len(data_aff1) > 0 and len(data_aff2) > 0:
            pdf.set_font('ack','',getAffFont(data_aff1))
            pdf.cell(30,CELL_HEIGHT_NAME)
            pdf.cell(55,CELL_HEIGHT_NAME,data_aff1,align='R')
            pdf.cell(10,CELL_HEIGHT_NAME)
            pdf.set_font('ack','',getNameFont(data_name1))
            pdf.cell(95,CELL_HEIGHT_NAME,data_name1,align='L')
            pdf.ln()

            pdf.set_font('ack','',getAffFont(data_aff2))
            pdf.cell(30,CELL_HEIGHT_NAME)
            pdf.cell(55,CELL_HEIGHT_NAME,data_aff2,align='R')
            pdf.cell(10,CELL_HEIGHT_NAME)
            pdf.set_font('ack','',getNameFont(data_name2))
            pdf.cell(95,CELL_HEIGHT_NAME,data_name2,align='L')
        elif len(data_aff1) > 0 and len(data_name1) > 0:
            pdf.set_font('ack','',getAffFont(data_aff1))
            pdf.cell(30,2*CELL_HEIGHT_NAME)
            pdf.cell(55,2*CELL_HEIGHT_NAME,data_aff1,align='R')
            pdf.cell(10,2*CELL_HEIGHT_NAME)
            pdf.set_font('ack','',getNameFont(data_name1))
            pdf.cell(95,2*CELL_HEIGHT_NAME,data_name1,align='L')
        elif len(data_aff1) > 0:
            # 団体
            pdf.set_font('ack','',getNameFont(data_aff1))
            pdf.cell(30,2*CELL_HEIGHT_NAME)
            pdf.cell(150,2*CELL_HEIGHT_NAME,data_aff1,align='C')


    pdf.output('test.pdf','F')

if __name__ == "__main__":
    print("Starting")
    csvFileName = sys.argv[1]
    data = getData(csvFileName)
    generatePDFs(data)
