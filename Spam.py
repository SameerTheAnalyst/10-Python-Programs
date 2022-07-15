import pyautogui as spam
import time


i = int(1)


limit = input("Enter no. of messages: ")
msg = input("Message you want to send : ")


time.sleep(5000)

while i < int(limit):
    spam.typewrite(msg)
    print(f"Value of I is {i}")
    spam.press("Enter")
    i = i + 1
