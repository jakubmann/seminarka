import docx
from docx import Document
from docx.shared import Cm
from docx.shared import Pt
import os
import platform
import re

def cls():
    if platform.system() == 'Windows':
        os.system('cls')
    elif platform.system() == 'Darwin':
        os.system('clear')
    elif platform.system() == 'Linux':
        os.system('clear')

#Creating the document
while True:
    document_name = input('Enter the name of the document (without .docx): ') + '.docx'
    try:
        document = Document(document_name)
        break
    except docx.opc.exceptions.PackageNotFoundError:
        cls()
        print('Incorrect document name')


#section / sections
sections = document.sections
for section in sections:
    section.top_margin = Cm(3.5)
    section.bottom_margin = Cm(3.0)
    section.left_margin = Cm(4.0)
    section.right_margin = Cm(2.5)

styles = document.styles

#Normal style formatting
normal_style = styles['Normal']
normal_paragraph = normal_style.paragraph_format
normal_paragraph.first_line_indent = Cm(1)
normal_font = normal_style.font
normal_font.size = Pt(12)
normal_font.name = 'Times New Roman'


for paragraph in document.paragraphs:
    if '  ' in paragraph.text:
        paragraph.text = re.sub(' +',' ', paragraph.text)
while True:
    try:
        document.save(document_name)
        print('Success!')
        break
    except PermissionError:
        print('Permission denied\nMaybe check if the document is open?')
        input('Press enter to try again...\n')
