import requests 
import fitz  # PyMuPDF 
 
def extract_text_from_pdf(url): 
   response = requests.get(url) 
   with open("temp.pdf", "wb") as f: 
       f.write(response.content) 
 
   doc = fitz.open("temp.pdf") 
   text = "" 
   for page in doc: 
       text += page.get_text() 
 
   return text
