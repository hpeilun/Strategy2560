import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
from io import BytesIO

def draw_chart(df):
    fig, ax = plt.subplots(figsize=(5,3))
    ax.plot(df["close"], label="Close")
    ax.legend()

    buf = BytesIO()
    plt.tight_layout()
    fig.savefig(buf, format="png")
    plt.close(fig)
    buf.seek(0)

    return buf
