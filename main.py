from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from strategy_core import Strategy2560
from kivy.clock import Clock
from kivy.uix.label import Label

class MainUI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.label = Label(text="Strategy2560 APK", font_size=24)
        self.add_widget(self.label)

class StrategyApp(App):
    def build(self):
        return MainUI()

    def on_start(self):
        self.strategy = Strategy2560()
        Clock.schedule_interval(lambda dt: self.strategy.update(), 5)

if __name__ == '__main__':
    StrategyApp().run()
