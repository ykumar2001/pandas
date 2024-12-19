import os
import pandas as pd
from pdfminer.high_level import extract_text
from docx import Document
# import warnings

# Use PendingDeprecationWarning directly
# warnings.warn("This is a pending deprecation warning.", PendingDeprecationWarning)

# Define the template structure
template = {
    "personal_information": {
        "name": "",
        "designation": "",
        "email": "",
        "primary_mobile_number": "",
        "secondary_mobile_number": "",
        "dob": "",
        "marital_status": "",
        "gender": "",
        "physically_challenged": "",
        "present_location": ""
    },
    "skills": {
        "key_skills": "",
        "it_skills": ""
    },
    "work_experience": [
        {
            "work_summary": "",
            "total_experience": "",
            "current_company": "",
            "last_company": "",
            "permanent_location": ""
        }
    ],
    "education": [
        {
            "ug": "",
            "pg": "",
            "qualification": "",
            "passed_out_from_premier_institute": False
        }
    ]
}

# Define a function to extract text from a PDF using PDFMiner
def extract_text_from_pdf(file_path):
    try:
        text = extract_text(file_path)
        return text
    except Exception as e:
        print(f"Error reading PDF {file_path}: {e}")
        return ""

# Define a function to extract text from a DOCX
def extract_text_from_docx(file_path):
    doc = Document(file_path)
    text = "\n".join([paragraph.text for paragraph in doc.paragraphs])
    return text

# Define a function to parse extracted text into the template
def parse_to_template(text):
    # Replace with your parsing logic (Regex, NLP, or any other method)
    # Example: Extracting name, email, etc., from the text
    parsed_data = template.copy()
    # Populate parsed_data based on the text
    # For now, it returns the empty template
    return parsed_data

# Define a function to save results in an Excel file
def save_to_excel(results, output_file):
    rows = []
    for result in results:
        file_name = result["file_name"]
        data = result["data"]
        for section, content in data.items():
            if isinstance(content, list):  # For sections like 'work_experience', 'education'
                for item in content:
                    rows.append([file_name, section, item])
            else:  # For other sections
                for key, value in content.items():
                    rows.append([file_name, section, key, value])
    # Create a DataFrame
    df = pd.DataFrame(rows, columns=["File Name", "Section", "Key", "Value"])
    df.to_excel(output_file, index=False)
    print(f"Data saved to {output_file}")

# Main script
folder_path = r"C:\Users\yk687_000\Desktop\Python\openAI\CV From Engage"  # Update the path
output_file = "output.xlsx"
results = []

for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    if os.path.isfile(file_path):
        print(f"Processing file: {filename}")
        if filename.endswith(".pdf"):
            text = extract_text_from_pdf(file_path)
        elif filename.endswith(".docx"):
            text = extract_text_from_docx(file_path)
        else:
            print(f"Skipping unsupported file: {filename}")
            continue
        parsed_data = parse_to_template(text)
        results.append({"file_name": filename, "data": parsed_data})

# Save the extracted and mapped data to an Excel file
save_to_excel(results, output_file)
