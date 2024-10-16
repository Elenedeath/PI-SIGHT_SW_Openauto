#!/usr/bin/python

import os
from time import sleep

from pynput import keyboard
import keyboard as kbd
import pyautogui

pyautogui.FAILSAFE = False

def startAA():
    """Android auto button command"""

    pyautogui.moveTo(150, 150)
    pyautogui.click()


def keymap():
    """keyboard mapping"""

    global display_on
    display_on = True

    def on_press(key):

        global display_on

        try:
            if key.char == 'u':
                keyboard.Controller().press(keyboard.Key.up)
                keyboard.Controller().release(keyboard.Key.up)

            elif key.char == 'd':
                keyboard.Controller().press(keyboard.Key.down)
                keyboard.Controller().release(keyboard.Key.down)

            elif key.char == 'l':
                kbd.press_and_release('1')

            elif key.char == 'a':
                kbd.press_and_release('v')

            elif key.char == 'r':
                kbd.press_and_release('2')

            elif key.char == 'z':
                kbd.press_and_release('n')

            elif key.char == 'e':
                keyboard.Controller().press(keyboard.Key.enter)
                keyboard.Controller().release(keyboard.Key.enter)

            elif key.char == 'q':
                startAA()
                sleep(1)

            elif key.char == 'c':
                pass

            elif key.char == 't':
                pass

            elif key.char == 'f':
                kbd.press_and_release('m')
                kbd.press_and_release('o')

            elif key.char == 'g':
                if display_on:
                    os.system('xset dpms force off')
                    display_on = False
                else:
                    os.system('xset dpms force on')
                    display_on = True

        except AttributeError:
            pass

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

def main():
    keymap()

if __name__ == '__main__':
    main()
