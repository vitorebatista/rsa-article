import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def plot(values: dict, title: str = "", bits: int = 0) -> None:
    # Ref:
    # https://python-graph-gallery.com/124-spaghetti-plot/
    plt.style.use("seaborn-darkgrid")
    palette = plt.get_cmap("Set1")
    size = len(values['brutal']) + 1
    values.update({"x": range(2, size* 2, 2 ) })
    df = pd.DataFrame( values )
    num = 0

    for column in df.drop("x", axis=1):
        num += 1
        plt.plot(
            df["x"],
            df[column],
            marker="",
            color=palette(num),
            linewidth=1,
            alpha=0.9,
            label=column,
        )

    plt.legend(loc=2, ncol=2)
    plt.xticks(np.arange(0, size * 2 + 1, step = 2))
    plt.xlabel("n bits")
    plt.ylabel("time spent (seconds)")
    plt.title(f"Criptografia RSA - {title.capitalize()} de {bits}", loc="left")

    plt.show()

