#!/usr/bin/python

from datetime import datetime
import datetime as dt
import os
import threading
from time import sleep
from shutil import rmtree

from pynput import keyboard
import keyboard as kbd
from picamera import PiCamera, Color
import pyautogui

pyautogui.FAILSAFE = False

## Set directory
root_path = os.getenv("ROOT_PATH", "/boot")
dir_path = os.getenv("RECORDINGS_PATH", "DashcamRecordings")
dashcam_path = os.path.join(root_path, dir_path)

## Video resolution
vid_width = 1296
vid_height = 860

def set_camera():
    global camera
    camera = PiCamera()
    camera.resolution = (vid_width, vid_height)
    camera.framerate = 30

    camera.hflip = True

    ## Overlay words style
    camera.annotate_background = Color('black')
    camera.annotate_text_size = 15
    
def make_folder_num():
    """Make folder name with number"""

    if not os.path.exists(dashcam_path):
        os.makedirs(dashcam_path)

    zero_dir_path = os.getenv("ZERO_PATH", "0000")
    zero_path = os.path.join(dashcam_path, zero_dir_path)

    ## Make 0000 folder if empty at first 
    if not os.path.exists(zero_path):
        os.mkdir(zero_path)
        print("Directory '0000' created")

    ## Make list of folder numbers now exist
    folder_nums = []
    for folder_name in os.listdir(dashcam_path):
        folder_nums.append(int(folder_name))

    ## Generate new folder number
    new_folder_nums = max(folder_nums) + 1

    ## Set recording path
    video_dir = str('%04i' % new_folder_nums)
    global video_path
    video_path = os.path.join(dashcam_path, video_dir)

    ## Make new folder
    if not os.path.exists(video_path):
        os.makedirs(video_path)
        print("Directory '%s' created" % video_dir)
    
    ## Clear list of folder numbers
    folder_nums.clear()

def make_folder_date():
    """Make folder name with date"""

    if not os.path.exists(dashcam_path):
        os.makedirs(dashcam_path)

    #Set recording path
    video_dir = datetime.now().strftime('%Y.%m.%d_%H.%M.%S')
    global video_path
    video_path = os.path.join(dashcam_path, video_dir)

    ## Make new folder
    if not os.path.exists(video_path):
        os.makedirs(video_path)
        print("Directory '%s' created" % video_dir)

def erase():
    """Check storage and erase oldest recording folder"""

    videos  = []

    ## Free memeory space calculate
    statvfs = os.statvfs(root_path)
    free_bytes = statvfs.f_frsize * statvfs.f_bfree
    total_bytes = statvfs.f_frsize * statvfs.f_blocks
    free_bytes_percentage = ((1.0 * free_bytes) / total_bytes) * 100
    
    print ("free_bytes_percentage="+str(free_bytes_percentage))

    ## Set free storage percentage
    percentage_threshold = 5
  
    if free_bytes_percentage < percentage_threshold:

        ## Make video folder list and remove first one
        for dir_list in os.listdir(dashcam_path):
            dir_path = os.path.join(dashcam_path, dir_list)
            videos.append((dir_path))
        videos.sort()
        rmtree(videos[0])
        videos.clear()
        print ("Deleted oldest folder")

def dashcam():
    """Loop record"""

    ## First video
    filename = video_path+'/dashcam_'+datetime.now().strftime('%Y.%m.%d_%H.%M.%S')+'.h264'
    camera.start_recording(filename, format='h264', resize=(vid_width,vid_height))

    while True:
        erase()

        print ("Saving video")

        ## Set time of start recording
        starttime = dt.datetime.now()

        ## Set video length and annotate realtime text
        while (dt.datetime.now() - starttime).seconds < 300: #Video length in seconds
            #camera.annotate_text = datetime.now().strftime('%Y.%m.%d_%H.%M.%S')
            camera.annotate_text = str('VUDEV Pi-SIGHT')

        ## Split and record next video
        filename = video_path+'/dashcam_'+datetime.now().strftime('%Y.%m.%d_%H.%M.%S')+'.h264'
        camera.split_recording(filename)

def startAA():
    """Android auto button command"""

    pyautogui.moveTo(150, 150)
    pyautogui.click()

def keymap():
    """keyboard mapping"""

    global preview_on
    global display_on
    preview_on = False
    display_on = True

    def on_press(key):

        global preview_on
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
                if preview_on:
                    camera.stop_preview()
                    preview_on = False
                else:
                    camera.start_preview()
                    sleep(3)
                    camera.stop_preview()
                    preview_on = False

            elif key.char == 't':
                if preview_on:
                  camera.stop_preview()
                  preview_on = False
                else:
                  camera.start_preview()
                  preview_on = True

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

    set_camera()

    make_folder_num()
    #make_folder_date()

    ## Set thread and start
    dashcam_thread = threading.Thread(target=dashcam, args=())
    dashcam_thread.start()

    keymap()

if __name__ == '__main__':
    main()
