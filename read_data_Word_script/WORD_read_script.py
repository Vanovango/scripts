from docx import Document

wordDoc = Document('test.docx')

for table in wordDoc.tables:
    for row in table.rows:
        for cell in row.cells:
            print(cell.text)
