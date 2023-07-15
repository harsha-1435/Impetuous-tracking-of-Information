import pyautogui
import random
import time
  
# Running the while loop for infinite time
while True:
    # generating a random number between 1 
    # to 5 which will represent the time 
    # delay
  
    # create a time delay using the sleep()
    # method
    time.sleep(10)
  
    # Take the screenshot using screenshot()
    # method
    myScreenshot = pyautogui.screenshot()
  
    # Save the screenshot shot using current
    # time as file name.
    file_name = "image"+".png"
    myScreenshot.save(file_name)
