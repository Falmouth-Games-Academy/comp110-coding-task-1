from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.network.urlrequest import UrlRequest
from kivy.uix.textinput import TextInput
import cgitb

cgitb.enable()


class HTTPApp(App):
    def build(self):
        layout = GridLayout(rows=5)
        btn = Button(text='Button', font_size=120)
        btn.bind(on_press=self.callback)
        self.label = Label(text="------------", font_size='50sp')
        input1 = TextInput
        layout.add_widget(btn)
        layout.add_widget(self.label)
        layout.add_widget(input1)
        return layout

    def got_weather(self, request, results):
        self.label.text = results

    def callback(self, event,):
        print("button touched")  # test
        self.label.text = "Loading"
        request = UrlRequest('http://bsccg04.ga.fal.io/kivy_app/?player=', self.got_weather)

HTTPApp().run()