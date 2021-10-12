from bs4 import BeautifulSoup
from requests import get


url = 'https://finance.yahoo.com/quote/AAPL/key-statistics?p=AAPL'
response = get(url)
soup = BeautifulSoup(response.text, 'html.parser')

stock_data = soup.find_all("table")
# stock_data will contain multiple tables, next we examine each table one by one

for table in stock_data:
    # Scrape all table rows into variable trs
    trs = table.find_all('tr')
    for tr in trs:
        # Scrape all table data tags into variable tds
        tds = tr.find_all('td')
        # Index 0 of tds will contain the measurement
        print("Measure: {}".format(tds[0].get_text()))
        # Index 1 of tds will contain the value
        print("Value: {}".format(tds[1].get_text()))
        print("")


def get_measurement(table_array, measurement):
    for table in table_array:
        trs = table.find_all('tr')
        for tr in trs:
            tds = tr.find_all('td')
            if measurement.lower() in tds[0].get_text().lower():
                return(tds[1].get_text())


# print only one measurement, e.g. operating cash flow
print(get_measurement(stock_data, "operating cash flow"))
