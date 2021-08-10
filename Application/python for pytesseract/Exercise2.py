import pytesseract
from PIL import Image


tesseract_cmd = 'D:\\Tesseract-OCR\\tesseract'
tessdata_dir_config = '--tessdata-dir "D:\\Tesseract-OCR\\tessdata"'
  
img = Image.open('test2.jpeg')


text = pytesseract.image_to_string(img, lang='eng')
print(text)

# 英文 'eng'、簡體中文 'chi_sim'、繁體中文 'chi_tra'