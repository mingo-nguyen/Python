import os
import sys
import comtypes.client
import concurrent.futures
import pythoncom
import time
import logging

# Set up logging
logging.basicConfig(filename='conversion.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def convert_doc_to_pdf(doc_path, pdf_path, retries=3):
    pythoncom.CoInitialize()  # Initialize COM library
    try:
        for attempt in range(retries):
            try:
                word = comtypes.client.CreateObject('Word.Application')
                word.Visible = False
                doc = word.Documents.Open(doc_path, ReadOnly=True)  # Open in read-only mode
                doc.SaveAs(pdf_path, FileFormat=17)
                doc.Close()
                word.Quit()
                logging.info(f"Successfully converted: {doc_path} to {pdf_path}")
                break
            except Exception as e:
                logging.error(f"Error converting {doc_path} on attempt {attempt + 1}: {e}")
                if attempt + 1 == retries:
                    logging.critical(f"Failed to convert {doc_path} after {retries} attempts")
                time.sleep(1)  # Add a delay before retrying
    finally:
        pythoncom.CoUninitialize()  # Uninitialize COM library

def convert_docs_in_folder(source_folder, destination_folder, max_workers=4):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    doc_paths = []
    pdf_paths = []
    for filename in os.listdir(source_folder):
        if filename.lower().endswith('.doc'):
            doc_path = os.path.join(source_folder, filename)
            pdf_filename = f"{os.path.splitext(filename)[0]}.pdf"
            pdf_path = os.path.join(destination_folder, pdf_filename)
            doc_paths.append(doc_path)
            pdf_paths.append(pdf_path)

    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(convert_doc_to_pdf, doc_path, pdf_path) for doc_path, pdf_path in zip(doc_paths, pdf_paths)]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                logging.error(f"Error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: script.py <source_folder> <destination_folder> <max_workers>")
        sys.exit(1)

    source_folder = sys.argv[1]
    destination_folder = sys.argv[2]
    max_workers = int(sys.argv[3])

    convert_docs_in_folder(source_folder, destination_folder, max_workers)
