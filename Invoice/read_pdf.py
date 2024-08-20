import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path, output_txt_path):
    # Open the PDF file
    doc = fitz.open(pdf_path)
    
    # Initialize a variable to hold the text
    all_text = ""
    
    # Loop through all the pages
    for page_number in range(len(doc)):
        page = doc[page_number]
        print(f"Reading page {page_number + 1}...")
        
        # Extract text from the page
        page_text = page.get_text()
        
        # Append the page text to the overall text variable
        all_text += page_text + "\n"  # Adding a newline to separate pages
    
    # Close the PDF document
    doc.close()
    
    # Write the extracted text to a text file
    with open(output_txt_path, 'w', encoding='utf-8') as txt_file:
        txt_file.write(all_text)
    
    print(f"Text extracted and saved to {output_txt_path}")

# Usage example
pdf_path = r"E:\Common Data\Foster\InvoiceSamples\Foster_Invoice Sample1 1.pdf"
output_txt_path = r"cac.txt"
extract_text_from_pdf(pdf_path, output_txt_path)
