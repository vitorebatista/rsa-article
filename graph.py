import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def plot(valuesY: dict, title: str = "", bits: int = 0) -> None:
    plt.figure(figsize=(20,10))
    # Ref:
    # https://python-graph-gallery.com/124-spaghetti-plot/
    plt.style.use("seaborn-darkgrid")
    palette = plt.get_cmap("Set1")
    size = len(valuesY['fermat']) + 1
    valuesY.update( {"x": range(4, size* 2 + 2, 2 ) })
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
    plt.xticks(np.arange(4, size * 2 + 1, step = 2))
    plt.xlabel("n bits")
    plt.ylabel("time spent (seconds)")
    plt.title(f"RSA - {title} {bits} bits", loc="left")
    plt.savefig(f'./images/{bits}_{title.replace(" ", "")}')
    # plt.show()

