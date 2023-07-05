import requests
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime, timedelta


def get_exchange_rate(date):
    url = f"https://www.cbr.ru/eng/currency_base/daily/?UniDbQuery.Posted=True&UniDbQuery.To={date.strftime('%d.%m.%Y')}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table', class_='data')
    rows = table.find_all('tr')
    exchange_rate = None
    for row in rows:
        columns = row.find_all('td')
        if len(columns) >= 2 and columns[1].text.strip() == 'USD':
            exchange_rate = columns[4].text.strip()
            break
    return exchange_rate

# Define the start and end dates for the month of November 2022
start_date = datetime(2022, 11, 1)
end_date = datetime(2022, 11, 30)

# Generate a list of dates within the date range
dates = [start_date + timedelta(days=i) for i in range((end_date - start_date).days + 1)]

# Retrieve the exchange rates for the specified dates
exchange_rates = {}
for date in dates:
    rate = get_exchange_rate(date)
    if rate is not None:
        exchange_rates[date.strftime('%Y-%m-%d')] = float(rate.replace(',', '.'))

# Create a DataFrame with the dates and exchange rates
USD_to_RUB_df = pd.DataFrame(list(exchange_rates.items()), columns=['Date', 'USD_to_RUB'])
USD_to_RUB_df['SB Date'] = pd.to_datetime(USD_to_RUB_df['Date'], format='%Y-%m-%d')


#print(USD_to_RUB_df)
