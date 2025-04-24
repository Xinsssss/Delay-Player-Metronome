from tkinter import *
import pyautogui
import time

window = Tk()
window.title("Delayed Player")
window.geometry("250x250+1200+0")

def delayed_play():
    seconds = int(seconds_entry.get())
    time.sleep(seconds)
    pyautogui.press('playpause')
    print("Play key triggered!")


label = Label(window, text="Seconds delayed")
label.pack()

seconds_entry = Entry(window)
seconds_entry.insert(0,"1")
seconds_entry.pack()

play = Button(window,text="Play",command = delayed_play, width = 5, height = 5)
play.pack()

window.mainloop()


