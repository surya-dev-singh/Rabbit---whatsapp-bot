import webbrowser as wb
import pyautogui 
import time
from termcolor import colored
import sys

banner='''
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
                  ___     ___
                 /   \   /   \       _____________________________
                /   / \_/ \   \     /                             \\
                \__/\     /\__/    /       CATCH THE RABBIT        \\
                     \O O/         \     BY : SURYA DEV SINGH      /
                  ___/ ^ \___      / _____________________________/
                     \___/        /_/
                     _/ \_
                  __//   \\\\__
                 /___\/_\/___\\
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
'''
print(colored(banner,"cyan"))

def send(wordlist):
    wb.open(f"https://web.whatsapp.com/send?phone={sys.argv[1]}&text=hii {sys.argv[2]} ")
    time.sleep(25)
    for i in wordlist:
        pyautogui.press("enter")
        pyautogui.write(f"{sys.argv[2]} is {i}")
        time.sleep(1)

if (len(sys.argv))==4:
        animal=open("animal.txt").readlines()
        send(animal)
else :
    print("some error")







