from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.network.urlrequest import UrlRequest

class TestApp(App):

    def build(self):
        layout = GridLayout(rows=3)
        btn =  Button(text='Button', font_size=120)
        btn.bind(on_press=self.callback)
        self.label = Label(text="------------", font_size='14sp')
        layout.add_widget(btn)
        layout.add_widget(self.label)
        return layout

    def got_database(self, request, results):
        self.label.text = results

    def callback(self, event):
        request = UrlRequest('http://bsccg03.ga.fal.io/', self.got_database)


TestApp().run()
