import kivy
from kivy import Config
Config.set('graphics', 'multisamples', '0')
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.audio import SoundLoader

class MyApp(App):
    dogsoundload = SoundLoader.load("Dog3.wav")
    catsoundload = SoundLoader.load("Meow2.wav")
    DrumSoundLoad = SoundLoader.load("Drum Bass1.wav")
    SnareDrumLoad = SoundLoader.load("Snare Drum.wav")

    def drumnoise(self, instance):
        self.DrumSoundLoad.play()

    def snaredrum(self, instance):
        self.SnareDrumLoad.play()


    def catnoise(self, instance):
        self.catsoundload.play()


    def dognoise(self, instance):
        self.dogsoundload.play()


    def build(self):
        cat = Button(text='Cat', font_size=50)
        dog = Button(text='Dog', font_size=50)
        drum = Button(text='Drum', font_size=50)
        snare = Button(text='Snare', font_size=50)


        dog.bind(on_press=self.dognoise)
        cat.bind(on_press=self.catnoise)
        drum.bind(on_press=self.drumnoise)
        snare.bind(on_press=self.snaredrum)


        HAHAHA = BoxLayout()
        HAHAHA.add_widget(cat)
        HAHAHA.add_widget(dog)
        HAHAHA.add_widget(drum)
        HAHAHA.add_widget(snare)




        return HAHAHA


if __name__ == '__main__':
    MyApp().run()