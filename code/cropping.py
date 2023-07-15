from PIL import Image
import time
while True:
    time.sleep(15)
    img=Image.open("C:\\Users\\HARSHAVA-B024DC\\Desktop\\sem4\\computer networks\\final_project\\screenshots\\image.png")
    b=(1090,920,1520,1030)
    c_i=img.crop(box=b)
    file_name="cropped"+".png"
    c_i.save(file_name)
