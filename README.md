# bookinfo

**Requirements:**

* _Python3 Libraries:_
  * django==2.1.5
  * opencv==2.0
  * pytesseract==0.2.6
  * PIL==1.1.7
  * Numpy
  
* _Linux Packages:_
  * tesseract-ocr 
  * libtesseract-dev

**Steps to run:**
1. Install tesseract for linux
`sudo apt install tesseract-ocr` 
`sudo apt install libtesseract-dev` 
1. Install Python packages
`pip install -r requirements.txt`
1. Migrations:
`python manage.py migrate` 
`python manage.py makemigrations`
1. Run server: ` python manage.py runserver`
1. Open link http://127.0.0.1:8000/ in browser
1. Upload an image for whose text has to be extracted
