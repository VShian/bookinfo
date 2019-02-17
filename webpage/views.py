from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage

import os
from pytesseract import image_to_string
# import cv2
import numpy as np
from PIL import Image

def ocr(img_path):
	# Recognize text with tesseract for python
# 	img = cv2.imread(os.path.abspath('.')+img_path, 0)
# 	img = cv2.resize(img, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)
	# Apply dilation and erosion to remove some noise
# 	kernel = np.ones((1, 1), np.uint8)
# 	img = cv2.dilate(img, kernel, iterations=1)
# 	img = cv2.erode(img, kernel, iterations=1)
	# Apply blur to smooth out the edges
# 	img = cv2.GaussianBlur(img, (5, 5), 0)
	# Apply threshold to get image with only b&w (binarization)
# 	img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
	path = os.path.abspath('.')+img_path
	result = image_to_string(Image.open(path))
	result = result.split('\n')

	# print(result)
	return result

def upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        #Check if the file uploaded is a valid image file
        try:
	        trial_image = Image.open(myfile)
        except:    
            return render(request, 'upload.html', {
        	'error' : "Please upload a valid image"
        	})
        #If valid, save the image, extract text and delete the image
        fs = FileSystemStorage()            
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        text = ocr(uploaded_file_url)
        fs.delete(myfile.name)
        return render(request, 'upload.html', {
        	'uploaded_file_url' : uploaded_file_url,
            'text' : text,
        })
    return render(request, 'upload.html')
