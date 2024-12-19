import os 
from docx import Document

folder=r"C:\Users\yk687_000\Desktop\Python\openAI\CV From Engage"
for filename in os.listdir(folder):
    file=os.path.join(folder,filename)
    # only docx file 
    if filename.endswith(".docx"):
        # load docx file
        doc=Document(file)
        # print content line by line 
        for paragraph in doc.paragraphs:
            print(paragraph.text)

        #if you want to store it in a single variable 
'''
text =""
        for paragraph in doc.paragraph
        text=text+paragrapgh
print(text)        
'''        
