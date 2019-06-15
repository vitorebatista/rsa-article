import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def plot(valuesY: dict, title: str = "", bits: int = 0, showGraph: bool = False) -> None:
    plt.figure(figsize=(20,10))
    plt.style.use("seaborn-darkgrid")
    palette = plt.get_cmap("Set1")
    df = pd.DataFrame( valuesY )
    size = df.index.size
    valuesY.update( {"x": range(8, size * 8 + 2, 8 ) })
    df = pd.DataFrame( valuesY )
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
    plt.xticks(np.arange(8, size * 8 + 2, step = 8))
    plt.xlabel("n bits")
    plt.ylabel("time spent (seconds)")
    plt.title(f"RSA - {title} {bits} bits", loc="left")
    plt.savefig(f'./images/{bits}_{title.replace(" ", "")}')

    if (showGraph):
        plt.show()

