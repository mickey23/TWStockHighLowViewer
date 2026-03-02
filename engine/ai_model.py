from sklearn.ensemble import RandomForestRegressor
import numpy as np

def train_ai_model(dataframe_list):

    X = []
    y = []

    for df in dataframe_list:
        if df is None or len(df) < 250:
            continue

        df = df.dropna()

        df["未來報酬"] = df["Close"].pct_change(20).shift(-20)

        features = df[["報酬率_20日","報酬率_60日","RSI","波動度"]]
        target = df["未來報酬"]

        X.extend(features.values)
        y.extend(target.values)

    model = RandomForestRegressor(n_estimators=50)
    model.fit(X, y)

    return model


def predict_score(model, df):

    latest = df.iloc[-1]

    X = [[
        latest["報酬率_20日"],
        latest["報酬率_60日"],
        latest["RSI"],
        latest["波動度"]
    ]]

    return model.predict(X)[0]
