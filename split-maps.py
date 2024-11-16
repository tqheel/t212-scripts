import PyPDF2
import pandas as pd

def split_pdf_pages(input_pdf_path, output_pdf_name, page_numbers):
    try:
        # Open the input PDF file.
        with open(input_pdf_path, 'rb') as pdf_file:
            pdf = PyPDF2.PdfReader(pdf_file)
            total_pages = len(pdf.pages)
            
            # Ensure valid page numbers.
            page_numbers = [page for page in page_numbers if 1 <= page <= total_pages]
            
            # Create a PDF writer for the output PDF.
            pdf_writer = PyPDF2.PdfWriter()
            
            # Add selected pages to the output PDF.
            for page_number in page_numbers:
                pdf_writer.add_page(pdf.pages[(page_number - 1)])  # Page numbers are 1-based.
            
            # Save the output PDF.
            with open(output_pdf_name, 'wb') as output_pdf:
                pdf_writer.write(output_pdf)
                
        return "PDF pages split successfully."
    except Exception as e:
        return f"Error: {str(e)}"

def process_excel_file(excel_file_path):
    try:
        # Read the Excel spreadsheet, ignoring the header row.
        df = pd.read_excel(excel_file_path, header=None, usecols=[0, 2], skiprows=[0])
        input_pdf_file = 'data/2023-final-merged.pdf'
        # Iterate through the rows and call split_pdf_pages.
        for index, row in df.iterrows():
            pdf_file_name = row[0]
            page_numbers = [int(page) for page in str(row[2]).split(',')]
            print(page_numbers)
            output_pdf_name = pdf_file_name + '.pdf'
            print(output_pdf_name)
            result = split_pdf_pages(input_pdf_file, "data/2023-lumiaria-final-sales-maps-scans/neighborhoods/2024/" + output_pdf_name, page_numbers)
            print(result)
    
    except Exception as e:
        print(f"Error: {str(e)}")


process_excel_file('data/neighborhoods-2024.xlsx')  # Replace 'example.xlsx' with the path to your Excel file.
