from os import listdir
from docx import Document
from docx.shared import Inches

myDocument=Document()
pictures=[fn for fn in listdir('C:/Users/jerry86064/Desktop/Photo') if fn.endswith('.png')]
pictures.sort()


for fn in pictures:
    myDocument.add_picture(fn, width=Inches(6), height=Inches(8))
myDocument.save('0506-上班族以「玩電動或線上遊戲紓壓」年輕者比例明顯高於年長者.docx')