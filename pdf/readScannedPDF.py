import pytesseract
from pdf2image import convert_from_path
import sys

def ocr_pdf(pdf_path, tesseract_path=None):

    # Set Tesseract path if provided
    if tesseract_path:
        pytesseract.pytesseract.tesseract_cmd = tesseract_path

    # Convert PDF to images
    pages = convert_from_path(pdf_path, 500)  # Adjust the DPI as needed

    # Extract text from the first page
    if pages:
        return pytesseract.image_to_string(pages[0])

    return ""

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <pdf_path> [<tesseract_path>]")
        sys.exit(1)

    pdf_path = sys.argv[1]
    tesseract_path = sys.argv[2] if len(sys.argv) >= 3 else None
    extracted_text = ocr_pdf(pdf_path, tesseract_path)

    output_file = "Incheri.txt"
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(extracted_text)

    print(f"Extracted text has been written to {output_file}")
