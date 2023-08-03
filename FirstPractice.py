# First trial: Using Pytesseract to read text from the image
# Pytesseract is an Optical Character Recognition (OCR) tool for pyton. It will read and recognize the text in images, license plates, etc.
import cv2
import os, argparse
from pytesseract import pytesseract
from PIL import Image

path_to_tesseract=r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# Construct an Argument Parser
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image folder")
ap.add_argument("-p", "--pre_processor", default="thresh", help="the preprocessor usage")
args = vars(ap.parse_args())

# Read the image with text
images = cv2.imread(args["image"])

# convert to grayscale image
gray = cv2.cvtColor(images, cv2.COLOR_BGRA2GRAY)

# Check whether thresh or blur
if args["pre_processor"] == "thresh":
    cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
if args["pre_processor"] == "blur":
    cv2.medianBlur(gray, 3)

# Memory usage with image i.e. adding image to memory
filename = "{}.jpg".format(os.getpid())
cv2.imwrite(filename, gray)

# Point tesseract_cmd to tesseract.exe
#pytesseract.tesseract_cmd = path_to_tesseract

pytesseract.tesseract_cmd =path_to_tesseract
text = pytesseract.image_to_string(Image.open(filename))
os.remove(filename)
print("The text in given image: ", text)

# show the output images
cv2.imshow("Image Input", images)
cv2.imshow("Output In Grayscale", gray)
cv2.waitKey(0)
