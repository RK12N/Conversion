import PyPDF2

ARCHIVOS=["test2.pdf","test.pdf"]

nombre_salida="pdf_unid.pdf"

pdf_final = PyPDF2.PdfMerger()
for nombre_de_archivo in ARCHIVOS:
    pdf_final.append(nombre_de_archivo)
pdf_final.write(nombre_salida)
pdf_final.close()
