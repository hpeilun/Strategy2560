import matplotlib.pyplot as plt
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg

def build_chart(df, signals):
    fig, ax = plt.subplots()

    ax.plot(df["close"], label="Close")
    ax.plot(df["ema25"], label="EMA25")
    ax.plot(df["ema60"], label="EMA60")

    for s in signals:
        ax.scatter(s[1], s[2], color="green" if s[0]=="BUY" else "red")

    ax.legend()
    return FigureCanvasKivyAgg(fig)
