from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import pandas as pd
from indicators import EMA
from strategy2560 import strategy_2560
from chart import build_chart

class Strategy2560App(App):
    def build(self):
        df = pd.read_csv("data.csv")
        df["ema5"] = EMA(df["close"], 5)
        df["ema25"] = EMA(df["close"], 25)
        df["ema60"] = EMA(df["close"], 60)

        signals = strategy_2560(df)

        layout = BoxLayout()
        layout.add_widget(build_chart(df, signals))
        return layout

Strategy2560App().run()
