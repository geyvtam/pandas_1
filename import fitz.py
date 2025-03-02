import os
import subprocess
import pandas as pd
import re
import pdf_to_text

# Run pdf_to_text.py to extract text
subprocess.run(["python3", "pdf_to_text.py"], check=True)

# Read extracted text
with open(pdf_to_text.full_text, "r", encoding="utf-8") as f:
    full_text = f.read()

# Extract transactions using regex
transaction_pattern = re.findall(
    r"([A-Za-z]+\s\d{1,2})\s+([A-Za-z]+\s\d{1,2})\s+(.+?)\s+(-?[\d,]+\.\d{2})", 
    full_text
)

# Convert to DataFrame
df = pd.DataFrame(transaction_pattern, columns=["Transaction Date", "Post Date", "Description", "Amount"])

# Convert Amount to numeric format
df["Amount"] = df["Amount"].str.replace(",", "").astype(float)

# Save extracted transactions
base_name = os.path.splitext(text_file_path)[0]
csv_output = base_name + "_transactions.csv"
excel_output = base_name + "_transactions.xlsx"
df.to_csv(csv_output, index=False)
df.to_excel(excel_output, index=False)

print(f"✅ Transactions saved in: {csv_output}")
print(f"✅ Excel file saved in: {excel_output}")
