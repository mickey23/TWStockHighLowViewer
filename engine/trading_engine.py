import shioaji as sj

api = sj.Shioaji()


def login(api_key, secret_key):

    api.login(api_key=api_key, secret_key=secret_key)
    print("✅ 登入成功")


def buy(stock, price, qty):

    contract = api.Contracts.Stocks[stock]

    order = api.Order(
        price=price,
        quantity=qty,
        action="Buy",
        price_type="LMT",
        order_type="ROD",
        account=api.stock_account
    )

    return api.place_order(contract, order)

    print("✅ 下單完成:", trade)
