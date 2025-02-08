from PyPDF2 import PdfWriter, PdfReader

import os

path_form = 'C:/Users/voyte/Desktop/Ankets/SPO/2_year'
save_path = './Анкеты/спо/2_курс'

directory = os.fsencode(path_form)

index = 1

for file in os.listdir(directory):
    filename = os.fsdecode(file)

    input_pdf = PdfReader(open(f"{path_form}/{filename}", "rb"))

    for i in range(0, len(input_pdf.pages), 2):
        output = PdfWriter()
        output.add_page(input_pdf.pages[i])
        output.add_page(input_pdf.pages[i + 1])
        with open(f"{save_path}/{index}.pdf", "wb") as outputStream:
            output.write(outputStream)
        index += 1
