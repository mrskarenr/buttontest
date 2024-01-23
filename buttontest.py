
from kivy.app import App
from kivy.uix.button import Button 

class MainApp(App):
     def build(self):
          button = Button (text = 'Press the button',
                           size_hint = (.5,.5),
                           pos_hint= {'center_x': .5, 'center_y': .5})
          button.bind (on_press = self.on_press_button)
          return button
     def on_press_button (seld, instance):
          print ('You have pressed the button')
if __name__ == '__main__':
     app= MainApp()
     app.run()

from kivy.app import App
from kivy.uix.button import Button    
 
class ButtonApp (App):
     def build(self):
          return Button ()
     
     def on_press_button (self):
          print ('You have pressed the button')

if __name__== '__main__':
     app= ButtonApp()
     app.run()