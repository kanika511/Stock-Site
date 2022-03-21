import pandas as pd
import datetime
import requests
from bs4 import BeautifulSoup


def real_time_price(stock_code):
    url = (
        ("https://finance.yahoo.com/quote/")
        + stock_code
        + (".HK?p=")
        + stock_code
        + (".HK&.tsrc-fin-srch")
    )
    ##
    r = requests.get(url)
    web_content = BeautifulSoup(r.text, "lxml")
    web_content = web_content.find(
        "div", {"class": "My(6px) Pos(r) smartphone_Mt(6px)"}
    )
    web_content = web_content.find("span").text

    if web_content == []:
        web_content = "99999"

    return web_content


# web_content = real_time_price("0001")
# print(web_content)

HSI = ["0001", "0002", "0003", "0005"]

for step in range(1, 101):
    price = []
    col = []
    time_stamp = datetime.datetime.now()
    time_stamp = time_stamp.strftime("%Y-%m-%d %H:%M:%S")
    for stock_code in HSI:
        price.append(real_time_price(stock_code))
    col = [time_stamp]
    col.extend(price)
    df = pd.DataFrame(col)
    df = df.T
    df.to_csv("Real Time stock.csv", mode="a", header=False)
    print(col)
