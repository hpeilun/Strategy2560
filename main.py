from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.core.image import Image as CoreImage

from realtime import get_realtime
from strategy2560 import run_strategy, backtest
from chart import draw_chart


class StrategyApp(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", **kwargs)

        self.info = Label(text="載入中...", size_hint_y=0.3)
        self.chart = Image(size_hint_y=0.7)

        self.add_widget(self.info)
        self.add_widget(self.chart)

        self.update_all(0)
        Clock.schedule_interval(self.update_all, 60)

    def update_all(self, dt):
        df = get_realtime("BTC-USD")
        df = run_strategy(df)
        stats = backtest(df)

        last = df["close"].iloc[-1]

        self.info.text = (
            f"BTC 價格：{last}\n"
            f"交易次數：{stats['trades']}\n"
            f"勝率：{stats['winrate']}%"
        )

        img_buf = draw_chart(df)
        self.chart.texture = CoreImage(img_buf, ext="png").texture


class Strategy2560App(App):
    def build(self):
        return StrategyApp()


if __name__ == "__main__":
    Strategy2560App().run()
