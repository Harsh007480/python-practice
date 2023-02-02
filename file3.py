import pyautogui as pt
import time

time.sleep(3)

limit=int(input("enter the limit"))
msg=input("enter the msg")
i=0



while i<=int(limit):
    pt.typewrite(msg)
    pt.press("enter")
    i+=1