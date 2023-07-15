import pyautogui
import random

from PIL import Image
from pytesseract import pytesseract
import pywhatkit
import time
import datetime


 
while True:

    time.sleep(20)
  
    # Take the screenshot using screenshot()
    # method
    myScreenshot = pyautogui.screenshot()
  
    # Save the screenshot shot using current
    # time as file name.
    file_name = "image"+".png"
    myScreenshot.save(file_name)

    img=Image.open("C:\\Users\\HARSHAVA-B024DC\\Desktop\\sem4\\computer networks\\final_project\\image.png")
    b=(1090,920,1520,1030)
    c_i=img.crop(box=b)
    file_name="cropped"+".png"
    c_i.save(file_name)


    # Defining paths to tesseract.exe
    # and the image we would be using
    path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    image_path = r"C:\Users\HARSHAVA-B024DC\Desktop\sem4\computer networks\final_project\cropped.png"
  
    # Opening the image & storing it in an image object
    img = Image.open(image_path)
  
    # Providing the tesseract executable
    # location to pytesseract library
    pytesseract.tesseract_cmd = path_to_tesseract
  
    # Passing the image object to image_to_string() function
    # This function will extract the text from the image
    text = pytesseract.image_to_string(img)
  
    # Displaying the extracted text
    print(text[:-1])
    a=datetime.datetime.now().strftime("%H:%M:%S")
    b=datetime.datetime.now().strftime("%Y-%m-%d")

    c=datetime.datetime.now().strftime("%H")
    d=datetime.datetime.now().strftime("%M")

    with open('C:\\Users\\HARSHAVA-B024DC\\Desktop\\sem4\\computer networks\\final_project\\test.txt','w') as f:
        f.write(b)
        f.write('\n')
        f.write(a)
        f.write('\n')
        f.write(text)
            

    if "red alert" in text:
        pywhatkit.sendwhatmsg("+918688440399",text,c,d)
        

    pywhatkit.sendwhatmsg("+918688440399",text,13,56)
