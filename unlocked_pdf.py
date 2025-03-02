import pikepdf
import os

pdf_path = input('Enter the path of the PDF file: ').strip().strip("'\"")
pdf_password = input('Enter the password of the PDF file: ').strip()
save_path = '/Users/geyvtam/Documents/Github/pandas_1/unlocked_pdf'

try:
    pdf = pikepdf.open(pdf_path, password=pdf_password)
    file_name = os.path.basename(pdf_path).replace('.pdf')
    output_path = os.path.join(save_path, file_name)

    pdf.save(output_path)

    print(f'Unlocked PDF saved to: {output_path}')
except pikepdf.PasswordError:
    print('Invalid password')
except Exception as e:
    print(f'An error occurred: {e}')