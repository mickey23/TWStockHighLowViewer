def walk_forward(df, train=252):

    results = []

    for i in range(train, len(df)-20):
        entry = df.iloc[i]["Close"]
        exit_price = df.iloc[i+20]["Close"]
        ret = (exit_price / entry) - 1
        results.append(ret)

    return results
