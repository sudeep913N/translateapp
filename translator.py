from tkinter import Button
from unittest import result
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.lang import Builder
from helpers import username_helper
from kivymd.uix.button import MDRectangleFlatButton,MDFlatButton
from kivymd.uix.dialog import MDDialog
from googletrans import Translator

class Myapp(MDApp):
    def build(self):
        self.theme_cls.primary_palette='Green'
        screen=Screen()
        self.username=Builder.load_string(username_helper)
        screen.add_widget(self.username)
        btn=MDRectangleFlatButton(text="Show",pos_hint={'center_x':0.5, 'center_y':0.4},on_release=self.show_data)
        screen.add_widget(btn)

        return screen
    def show_data(self,obj):
        def trans(word):
            translator=Translator()
            x=str(word)
            z=translator.translate(text=x,dest='en')
            rest=z.text
            return rest
        if self.username.text is "":
            string="Enter the Word"
        else:
            y=self.username.text
            string=str(trans(y))
        close_button=MDFlatButton(text='Close',on_release=self.close_dialog)
        more_button=MDFlatButton(text='More')
        self.dialog=MDDialog(title='Word',text=string,size_hint=(0.5,1),buttons=[close_button,more_button])
        self.dialog.open()
    def close_dialog(self,obj):
        self.dialog.dismiss()
    
        


Myapp().run()