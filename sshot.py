import time
import pyautogui
import tkinter as tk

def take_screenshot():

    # Naming each screenshot with a timestamp to avoid overwriting
    name = int(round(time.time()*1000))
    name = 'C:/Users/HP/Desktop/Tutorial/Screenshot/sstaken/{}.png'.format(name)

    # Wait for 5 seconds before taking the screenshot
    time.sleep(2)
    
    # Take a screenshot and save it
    img = pyautogui.screenshot(name)
    img.show()

root =tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame, text='Take Screenshot', command=take_screenshot)
button.pack(side=tk.LEFT)
close = tk.Button(frame, text='Close', command=root.quit)
close.pack(side=tk.LEFT)

root.mainloop()