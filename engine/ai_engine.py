from sklearn.linear_model import LinearRegression
import numpy as np

def predict_price(df):

    X = np.arange(len(df)).reshape(-1,1)
    y = df["Close"].values

    model = LinearRegression()
    model.fit(X,y)

    next_day = np.array([[len(df)+1]])
    pred = model.predict(next_day)

    return round(float(pred[0]),2)
