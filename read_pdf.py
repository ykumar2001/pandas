import os 
from pdfminer.high_level import extract_text

folder=r"C:\Users\yk687_000\Desktop\Python\openAI\CV From Engage"

for filename in os.listdir(folder):
    file=os.path.join(folder,filename)
    if filename.endswith(".pdf"):
        print(filename)

    # extract data 
        text=extract_text(file) 
        print(text)