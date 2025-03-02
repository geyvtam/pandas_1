import os # Operating system library
import re # Regular expression library
from pdf2image import convert_from_path # Library to convert PDF to image
import pytesseract # Library to extract text from image

poppler_path = '/opt/homebrew/bin/' # Path to the Poppler binaries
pytesseract.pytesseract.tesseract_cmd = '/opt/homebrew/bin/tesseract' # Path to the Tesseract binary
os.environ["POPPLER_HOME"] = poppler_path # Set the environment variable for Poppler

folder_path = "/Users/geyvtam/Documents/GitHub/pandas_1/unlocked_pdf" # Path to the folder containing the PDF
folder_path1 = "/Users/geyvtam/Documents/GitHub/pandas_1/data" # Path to the folder where the output files will be saved
file_name = input("Enter the file name(inlcuding .pdf): ")+str('.pdf') # Name of the PDF file
pdf_path = os.path.join(folder_path, file_name) # Path to the PDF file
if not os.path.exists(pdf_path):
    print("File not found")
    exit()  # Exit the program if the file is not found

file_name_no_ext = os.path.splitext(file_name)[0] # File name without extension
output_folder = os.path.join(folder_path1, file_name_no_ext) # Path to the output folder
if not os.path.exists(output_folder): # Create the output folder if it does not exist
    os.makedirs(output_folder) # Create the output folder

images = convert_from_path(pdf_path) # Convert the PDF to images

ocr_text = [] # List to store the extracted text
for i, image in enumerate(images):
    text = pytesseract.image_to_string(image) # Extract text from the image
    ocr_text.append(text) # Append the extracted text to the list

full_text = "\n".join(ocr_text) # Join the extracted text from all the pages

with open(os.path.join(output_folder, f"{file_name_no_ext}.txt"), "w") as f:
    f.write(full_text) # Save the full extracted text to a text file

print(f" All pages extracted and saved to {output_folder}")