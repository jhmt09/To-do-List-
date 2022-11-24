from kivy.app import App
from kivy.uix.boxlayout import BoxLayout




class Incrementador(BoxLayout):
    def __init__(self,incrementador,**kwargs):
           super().__init__()
           for incrementador in incrementador:
                self.ids.box.add_widget(Incrementado(text=incrementador))

    def addwidget (self):
        texto = self.ids.texto.text
        self.ids.box.add_widget(Incrementado(text=texto))

class Incrementado(BoxLayout):
    def __init__(self,text='', **kwargs):
        super().__init__(**kwargs)
        self.ids.label.text= text
        



class Test (App):
    def build(self):
      return Incrementador([''])
  


Test() .run()