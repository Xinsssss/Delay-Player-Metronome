from tkinter import *
from tkinter import ttk
import pyautogui
import pygame
import time

class Player:
    
    def __init__(self,window):

        pygame.mixer.init()
        self.sound = pygame.mixer.Sound('assets/metronome-85688.wav')
        self.window = window
        self.bpm = 100
        self.playing = True
        self.delayed_beats = 0
        self.createGUI()
    
    def start_metro(self,slider,beat_slider):
        self.playing = True
        self.bpm = int(slider.get())
        self.delayed_beats = int(beat_slider.get())
        self.play_sound()
    
    def play_sound(self):

        if self.playing:
            self.sound.play()
            self.window.after(int(60000/self.bpm),self.play_sound)
            self.delayed_beats -= 1
            if(self.delayed_beats==-1):
                pyautogui.press('playpause')

    def end_metro(self):
        if self.playing:
            pyautogui.press('playpause')
            self.playing = False
            self.delayed_beats = 0

    def update_slider(self,slider,entry):
        try:
            bpm = int(entry.get())
            if(bpm > 240):
                bpm = 240
            elif(bpm<40):
                bpm = 40
            slider.set(bpm)
        except ValueError:
            pass


    def createGUI(self):

        beat_label = Label(self.window,text="Beats Delayed")
        beat_label.pack()

        beat_slider = Scale(self.window,from_=2,to=8,tickinterval=2,orient=HORIZONTAL)
        beat_slider.pack()

        bpm_label = Label(self.window,text="BPM")
        bpm_label.pack()
        
        max_label = Label(self.window,text="240")
        max_label.pack()

        slider = Scale(self.window,from_="240", to="40", length = 200)
        slider.set(self.bpm)
        slider.pack()

        min_label = Label(self.window,text="40")
        min_label.pack()

        bpm_entry = Entry(self.window)
        bpm_entry.insert(0,self.bpm)
        bpm_entry.bind("<Return>",lambda event: self.update_slider(slider,bpm_entry))
        bpm_entry.pack()

        start_button = Button(self.window,text="Start",command=lambda: self.start_metro(slider,beat_slider))
        start_button.pack()

        stop_button = Button(self.window,text="Stop",command=self.end_metro)
        stop_button.pack()


if __name__=="__main__":

    window = Tk()
    window.geometry("150x600+1800+50")
    window.title("Assistance Player")

    metronome = Player(window)
    window.mainloop()