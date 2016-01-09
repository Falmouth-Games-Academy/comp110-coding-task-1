from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.network.urlrequest import UrlRequest
from kivy.uix.textinput import TextInput
import cgitb

cgitb.enable()


class LeaderboardApp(App):
    global textinput
    def build(self):
        layout = GridLayout(rows=5)
        btn = Button(text='Button', font_size=120)
        btn.bind(on_press=self.callback)
        self.label = Label(text="------------", font_size='50sp')

        textinput = TextInput(text='Please enter a 3 letter username', multiline=False)
        #textinput.bind(text=on_text)

        layout.add_widget(btn)
        layout.add_widget(self.label)
        layout.add_widget(textinput)
        return layout

    def got_weather(self, request, results):
        self.label.text = results

    def callback(self, textinput):
        #player_name = textinput.text
        self.label.text = "Searching"
        request = UrlRequest('http://http://bsccg04.ga.fal.io/top10.py', self.got_weather)

LeaderboardApp().run()