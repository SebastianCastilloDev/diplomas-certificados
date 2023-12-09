""" First page of PDF to png """

import os
import fitz  # PyMuPDF
from PIL import Image


def convert_pdf_to_image(pdf_path, output_image_path):
    pdf_document = fitz.open(pdf_path)
    page = pdf_document[0]
    image = page.get_pixmap()
    image.save(output_image_path)
    pdf_document.close()


def convert_all_pdfs_in_directory(pdf_directory, output_directory):
    os.makedirs(output_directory, exist_ok=True)
    for filename in os.listdir(pdf_directory):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(pdf_directory, filename)
            output_image_path = os.path.join(
                output_directory, os.path.splitext(filename)[0] + ".png")
            convert_pdf_to_image(pdf_path, output_image_path)


if __name__ == "__main__":
    script_directory = os.path.dirname(os.path.abspath(__file__))
    pdf_directory = os.path.join(script_directory, "pdf")
    output_img_directory = os.path.join(script_directory, "img")
    convert_all_pdfs_in_directory(pdf_directory, output_img_directory)
