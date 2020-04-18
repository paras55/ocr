# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 00:13:37 2020

@author: dell
"""

import io
from PIL import Image
import pytesseract
from wand.image import Image as wi

pdf = wi(filename = "python.pdf", resolution = 300)
pdfImage = pdf.convert('jpeg')

imageBlobs = []

for img in pdfImage.sequence:
	imgPage = wi(image = img)
	imageBlobs.append(imgPage.make_blob('jpeg'))

recognized_text = []

for imgBlob in imageBlobs:
	im = Image.open(io.BytesIO(imgBlob))
	text = pytesseract.image_to_string(im, lang = 'eng')
	recognized_text.append(text)

print(recognized_text)
