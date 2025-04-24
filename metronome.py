from tkinter import *
import pygame

class Metronome:
    
    def __init__(self,window):

        pygame.mixer.init()
        self.sound = pygame.mixer.Sound('assets/metronome-85688.wav')
        self.window = window
        self.bpm = 100
        self.playing = True
        self.createGUI()
    
    def start_metro(self,slider):
        self.playing = True
        self.bpm = int(slider.get())
        self.play_sound()
    
    def play_sound(self):

        if self.playing:
            self.sound.play()
            self.window.after(int(60000/self.bpm),self.play_sound)

    def end_metro(self):
        self.playing = False

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

        start_button = Button(self.window,text="Start",command=lambda: self.start_metro(slider))
        start_button.pack()

        stop_button = Button(self.window,text="Stop",command=self.end_metro)
        stop_button.pack()


if __name__=="__main__":

    window = Tk()
    window.geometry("150x400+1000+50")
    window.title("Metronome")

    metronome = Metronome(window)
    window.mainloop()