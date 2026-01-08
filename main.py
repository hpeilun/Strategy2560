from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.clock import Clock

from realtime import get_realtime


class StrategyApp(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", **kwargs)

        self.label = Label(text="載入中...", font_size=24)
        self.add_widget(self.label)

        # 第一次載入
        self.update_data(0)

        # ⭐ 每 60 秒自動刷新（可改）
        Clock.schedule_interval(self.update_data, 60)

    def update_data(self, dt):
        df = get_realtime("BTC-USD")

        last_close = df["close"].iloc[-1]
        self.label.text = f"BTC 即時價格\n{last_close}"


class Strategy2560App(App):
    def build(self):
        return StrategyApp()


if __name__ == "__main__":
    Strategy2560App().run()
