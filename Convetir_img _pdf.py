from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from PIL import Image

def image_to_pdf(image_path, output_pdf_path):
    # Abre la imagen usando Pillow
    img = Image.open(image_path)

    # Crea un objeto canvas de ReportLab para el PDF
    c = canvas.Canvas(output_pdf_path, pagesize=letter)

    # Obtiene las dimensiones de la página
    width, height = letter

    # Calcula las dimensiones para ajustar la imagen en la página
    img_width, img_height = img.size
    aspect_ratio = img_width / img_height

    if aspect_ratio > 1:
        img_width = width
        img_height = width / aspect_ratio
    else:
        img_height = height
        img_width = height * aspect_ratio

    # Dibuja la imagen en el PDF
    c.drawImage(image_path, 0, 0, img_width, img_height)

    # Guarda el PDF
    c.showPage()
    c.save()

if __name__ == "__main__":
    image_path = "tu_imagen.jpg"  # Reemplaza con la ruta de tu imagen
    output_pdf_path = "imagen_convertida.pdf"  # Nombre del archivo PDF de salida

    image_to_pdf(image_path, output_pdf_path)
