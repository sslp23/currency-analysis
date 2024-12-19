import pandas as pd
import matplotlib.pyplot as plt
from data_retrieve import *
from datetime import datetime, timedelta
import numpy as np

def get_cum_ret(currencies):
    cum_ret_df = pd.DataFrame()
    for c in currencies.keys():
        currencies[c].columns = currencies[c].columns.get_level_values(0)
        currencies[c]['Daily Return'] = currencies[c]['Adj Close'].pct_change()
        currencies[c]['Cumul Ret'] = (1 + currencies[c]['Daily Return']).cumprod() - 1

        new_cum_ret = currencies[c][['Cumul Ret']]
        
        new_cum_ret.columns = [c]

        cum_ret_df = pd.concat([cum_ret_df, new_cum_ret], axis='columns')
    return cum_ret_df

def plot_rets(rets, title=''):
    fig, ax = plt.subplots(figsize=(16, 8))

    rets.plot(ax=ax)
    ax.legend()
    ax.set_title(title)
    ax.set_ylabel("Returns")
    
    return fig
    
# Get today's date
today = datetime.today()

# Calculate the date 10 years ago
ten_years = today - timedelta(days=10 * 365)

# Format the dates as 'Y-M-D'
today = today.strftime('%Y-%m-%d')
ten_years = ten_years.strftime('%Y-%m-%d')

#most traded currencies
currency_pairs = [
    "EURUSD=x",  # Euro to US Dollar
    "JPYUSD=X",  # Japanese Yen to US Dollar
    "GBPUSD=X",  # British Pound Sterling to US Dollar
    "CNYUSD=X",  # Chinese Renminbi to US Dollar
    "AUDUSD=X",  # Australian Dollar to US Dollar
    "CADUSD=X",  # Canadian Dollar to US Dollar
    "CHFUSD=X",  # Swiss Franc to US Dollar
    "HKDUSD=X",  # Hong Kong Dollar to US Dollar
    "SGDUSD=X",   # Singapore Dollar to US Dollar
    "BRLUSD=X", # Brazilian Real to US Dollar
]

currencies = get_data(currency_pairs, st = ten_years, end = today)

rets = get_cum_ret(currencies)

mt = plot_rets(rets, 'Most Traded Currencies')

mt.savefig('figs/most_traded.png', dpi=300)

#emerging currencies
currency_pairs = [
    "ZARUSD=X",  # South African Rand to US Dollar
    "MXNUSD=X",  # Mexican Peso to US Dollar
    "TRYUSD=X",  # Turkish Lira to US Dollar
    "ARSUSD=X",  # Argentina Peso to US Dollar
    "INRUSD=X",  # Indian Rupee to US Dollar
    "IDRUSD=X",  # Indonesian Rupiah to US Dollar
    "MYRUSD=X",  # Malaysian Ringgit to US Dollar
    "THBUSD=X",  # Thai Baht to US Dollar
    "KRWUSD=X",  # South Korean Won to US Dollar]
    "BRLUSD=X",  # Brazilian Real to US Dollar
]

currencies = get_data(currency_pairs, st = ten_years, end = today)

rets = get_cum_ret(currencies)

em = plot_rets(rets, 'Emerging Countries Currencies')

em.savefig('figs/emerging_countries.png', dpi=300)