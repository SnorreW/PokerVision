import cv2
import pytesseract
from pytesseract import Output


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def ocr_core(img):
    text = pytesseract.image_to_string(img, config='--psm 6')
    return text

img = cv2.imread('data/42.png')

#Grayscale
def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#Remove noise
def remove_noise(image):
    return cv2.medianBlur(image, 5)

#Thresholding
def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

img = get_grayscale(img)
img = thresholding(img)
img = remove_noise(img)

print(ocr_core(img))

#d = pytesseract.image_to_data(img, output_type=Output.DICT)
#print(d.keys())


