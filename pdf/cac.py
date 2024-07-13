import pytesseract
from PIL import Image
from pdf2image import convert_from_path
import sys


def read_pdf(pdf_file):
    pytesseract.pytesseract.tesseract_cmd = r"Tesseract-OCR\tesseract.exe"

    # Convert PDF to the first page image
    images = convert_from_path(pdf_file, dpi=200, first_page=1, last_page=1)
    page = images[0]

    # Extract text using Tesseract OCR
    text = pytesseract.image_to_string(page)
    return text

if __name__ == "__main__":
    if len(sys.argv) < 1:
        print("Usage: python script.py <pdf_path>")
        sys.exit(1)
    pdf_file = sys.argv[1]
    output_file = "Incheri.txt"
    extracted_text = read_pdf(pdf_file)
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(extracted_text)
    print("PDF processing completed!")
