
import urllib.request
import json
import time
import datetime

STOCK = ["TSLA","AAPL"]
COMPANY_NAME = {"TSLA":"Tesla","AAPL":"Apple"}
API_KEY = '<>'
new_api_key = '<>'


proxy_handler = urllib.request.ProxyHandler({'https': '<>',
                                                 'http': '<>'})

def api_call_get_stock():

    opener = urllib.request.build_opener(proxy_handler)

    for stock in STOCK:
        url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={stock}&apikey={API_KEY}"
        response = opener.open(url)
        data = response.read().decode('utf8')
        json_data = json.loads(data)
        close_nkey = '4. close'
        yesterday = str(datetime.date.today() - datetime.timedelta(1))
        day_before_yesterday = str(datetime.date.today() - datetime.timedelta(2))
        cur_price = float(json_data["Time Series (Daily)"][str(yesterday)][close_nkey])
        prev_price = float(json_data["Time Series (Daily)"][str(day_before_yesterday)][close_nkey])
        percentage_change = (cur_price-prev_price)/prev_price*100

        if percentage_change > 2:
            print("get news")
            get_news(COMPANY_NAME[stock])

def get_news(company_name):
    opener = urllib.request.build_opener(proxy_handler)
    today = str(datetime.date.today())
    url = f"https://newsapi.org/v2/everything?q={company_name}&sortBy=publishedAt&sortBy=publishedAt&apiKey={new_api_key}"
    response = opener.open(url)
    data = response.read()
    json_data = json.loads(data)
    print(json_data['articles'][0]['source'],json_data['articles'][0]['title'],json_data['articles'][0]['url'])
    print(json_data['articles'][2]['source'],json_data['articles'][0]['title'],json_data['articles'][0]['url'])
    print(json_data['articles'][3]['source'],json_data['articles'][0]['title'],json_data['articles'][0]['url'])

if __name__ == '__main__':
    api_call_get_stock()
