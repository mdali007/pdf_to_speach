import pyttsx3
import PyPDF2

def pdf_to_speech(pdf_path):
    # Open the PDF file
    with open(pdf_path, 'rb') as file:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfFileReader(file)

        # Get the number of pages in the PDF
        num_pages = pdf_reader.numPages

        # Create a text-to-speech engine
        engine = pyttsx3.init()

        # Iterate through each page and extract text
        for page_num in range(num_pages):
            # Get the page
            page = pdf_reader.getPage(page_num)

            # Extract text from the page
            text = page.extractText()

            # Speak the extracted text
            engine.say(text)
            engine.runAndWait()

if __name__ == "__main__":
    # Replace 'your_pdf_file.pdf' with the path to your PDF file
    pdf_file_path = 'your_pdf_file.pdf'

    pdf_to_speech(pdf_file_path)
