import pyautogui
from pywinauto.application import Application
import os

if (os.path.exists(r"C:\Program Files\VideoLAN\VLC\vlc.exe")):
    app = Application(backend='uia').start(r"C:\Program Files\VideoLAN\VLC\vlc.exe")
else:
    if (os.path.exists(r"C:\Program Files\vlc.exe")):
        app = Application(backend='uia').start(r"C:\Program Files\vlc.exe")
    else:
        print("Can't find app on your computer")

win = app['VLC Media player']

# if app.software_update.exists(timeout=10):
#     app.software_update.skip_this_version.click()
#     app.software_update.wait_not('visible')  # just to make sure it's closed
# win.wait('ready', timeout=15)

app_top_window = app.top_window()
app_top_window.maximize()

win.wait('ready', timeout=15)
print(pyautogui.size())
pyautogui.moveTo(166, 27, 2)
pyautogui.click()

im = pyautogui.screenshot()
im.save(r'C:\Users\40011212\PycharmProjects\screen_resolution\im.png')