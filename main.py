import pyautogui
import time

time.sleep(5)
text1 = 'Interesting match'
text2 = 'Thanks Everyone'
text3 = 'Love for Argentina '
text4 = 'Want more live match'
text5 = 'Big fan bro'
text6 = 'Please everyone follow this page'
while True:
    pyautogui.typewrite(text1)
    time.sleep(1)
    pyautogui.press('enter')

    pyautogui.typewrite(text2)
    time.sleep(1)
    pyautogui.press('enter')

    pyautogui.typewrite(text3)
    time.sleep(1)
    pyautogui.press('enter')

    pyautogui.typewrite(text4)
    time.sleep(1)
    pyautogui.press('enter')

    pyautogui.typewrite(text5)
    time.sleep(1)
    pyautogui.press('enter')

    pyautogui.typewrite(text6)
    time.sleep(1)
    pyautogui.press('enter')
