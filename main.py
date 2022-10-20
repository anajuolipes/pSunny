### Sum numbers

import utils
from time import sleep
import keyboard
import sys
import pyautogui

while True:
    numbersList = [0]
    utils.numbersList = numbersList

    print("Press 's' to start the script, or 'q' to quit")
    keyboard.read_key()

    if keyboard.is_pressed('s'):
        pyautogui.press('backspace')
        utils.pickNumbers()

        utils.spell("Calculating...\n",0.15)
        sleep(1)

        utils.sumNumbers()

    elif keyboard.is_pressed('q'):
        pyautogui.press('backspace')
        sleep(0.5)
        print("Leaving")
        sleep(1)
        sys.exit()
