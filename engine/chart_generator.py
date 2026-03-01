import matplotlib.pyplot as plt

def save_chart(df, stock):

    plt.figure()
    plt.plot(df["Date"], df["Close"])
    plt.title(stock)
    plt.xticks(rotation=45)

    path = f"output/charts/{stock}.png"
    plt.savefig(path)
    plt.close()

    return path
