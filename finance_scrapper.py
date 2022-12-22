# https://site.financialmodelingprep.com/

""" Available functions to scrape data
    when needed from Financial modeling Prep.
    Source Code from: https://github.com/SpencerPao/FinanceScrape"""

import requests
import pandas as pd

# period = 'quarter' or 'annual'
def get_income_statement(ticker, limit, key, period, growth=False):
    """Get the Income Statement."""
    URL = 'https://financialmodelingprep.com/api/v3/income-statement/'
    if growth == True:
        URL = 'https://financialmodelingprep.com/api/v3/income-statement-growth/'
    try:
        r = requests.get(
            '{}{}?period={}&limit={}&apikey={}'.format(URL,
                                                       ticker,
                                                       period,
                                                       limit,
                                                       key))
        incomeStatement = pd.DataFrame.from_dict(r.json()).transpose()
        if growth == True:
            incomeStatement.columns = incomeStatement.loc['date']
        else:
            incomeStatement.columns = incomeStatement.loc['fillingDate']
        return incomeStatement
    except requests.exceptions.HTTPError as e:
        # We want a 200 value
        print('Requesting Income statement sheet ERROR: ', str(e))


def get_balance_sheet(ticker, limit, key, period,growth=False):
    """Get the Balance sheet."""
    URL = 'https://financialmodelingprep.com/api/v3/balance-sheet-statement/'
    if growth == True:
        URL = 'https://financialmodelingprep.com/api/v3/balance-sheet-statement-growth/'
    try:
        r = requests.get(
            '{}{}?period={}&?limit={}&apikey={}'.format(URL,
                                                        ticker,
                                                        period,
                                                        limit,
                                                        key))
        balanceSheet = pd.DataFrame.from_dict(r.json()).transpose()
        if growth == True:
            balanceSheet.columns = balanceSheet.loc['date']
        else:
            balanceSheet.columns = balanceSheet.loc['fillingDate']
        return balanceSheet
    except requests.exceptions.HTTPError as e:
        # We want a 200 value
        print('Requesting Balance sheet statement ERROR: ', str(e))


def get_cash_flow_statement(ticker, limit, key, period, growth=False):
    """Get the Cash flow statements."""
    URL = 'https://financialmodelingprep.com/api/v3/cash-flow-statement/'
    if growth == True:
        URL = 'https://financialmodelingprep.com/api/v3/cash-flow-statement-growth/'
    try:
        r = requests.get(
            '{}{}?period={}&?limit={}&apikey={}'.format(URL,
                                                        ticker,
                                                        period,
                                                        limit,
                                                        key))
        cashFlow = pd.DataFrame.from_dict(r.json()).transpose()
        if growth == True:
            cashFlow.columns = cashFlow.loc['date']
        else:
            cashFlow.columns = cashFlow.loc['fillingDate']
        return cashFlow
    except requests.exceptions.HTTPError as e:
        print('Requesting Cash flow statement ERROR: ', str(e))

def get_financial_growth(ticker, limit, key):
    """Get the Cash flow statements."""
    URL = 'https://financialmodelingprep.com/api/v3/financial-growth/'
    try:
        r = requests.get(
            '{}{}?limit={}&apikey={}'.format(URL,
                                   ticker,
                                   limit,
                                   key))
        fgrowth = pd.DataFrame.from_dict(r.json()).transpose()
        fgrowth.columns = fgrowth.loc['date']
        return fgrowth
    except requests.exceptions.HTTPError as e:
        print('Requesting financial growth ERROR: ', str(e))
        
# def get_financial_ratios(ticker, limit, key, period):
#     """Get financial ratios."""
#     URL = 'https://financialmodelingprep.com/api/v3/ratios/'
#     try:
#         r = requests.get(
#             '{}{}?period={}&?limit={}&apikey={}'.format(URL,
#                                                         ticker,
#                                                         period,
#                                                         limit,
#                                                         key))
#         ratios = pd.DataFrame.from_dict(r.json()).transpose()
#         ratios.columns = ratios.loc['date']
#         return ratios
#     except requests.exceptions.HTTPError as e:
#         print('Requesting financial ratios ERROR: ', str(e))

def get_financial_ratios(ticker, limit, key, period):
    """Period is ttm | annual | quarter."""
    URL = 'https://financialmodelingprep.com/api/v3/'
    if period == "ttm":
        try:
            r = requests.get(
                '{}/ratios-ttm/{}?{}&apikey={}'.format(URL,
                                                       ticker,
                                                       period,
                                                       key))
            fr = pd.DataFrame.from_dict(r.json()).transpose()
            fr.columns = [ticker + " TTM Ratios"]
            return fr
        except requests.exceptions.HTTPError as e:
            print('Requesting Financial ratios ERROR(1): ', str(e))
    elif period == "annual" or period == "quarter":
        try:
            r = requests.get(
                '{}ratios/{}?period={}&?limit={}&apikey={}'.format(URL,
                                                                   ticker,
                                                                   period,
                                                                   limit,
                                                                   key))
            fr = pd.DataFrame.from_dict(r.json()).transpose()
            fr.columns = fr.iloc[1]
            return fr[2:]
        except requests.exceptions.HTTPError as e:
            print('Requesting Financial ratios ERROR(2): ', str(e))
    else:
        print('ERROR: Define the period you want: ttm | annual | quarter')
        return None

def get_key_metrics(ticker, limit, key, period):
    """Period is ttm | annual | quarter."""
    URL = 'https://financialmodelingprep.com/api/v3/'
    if period == "ttm":
        try:
            r = requests.get(
                '{}key-metrics-ttm/{}?apikey={}'.format(URL, ticker, key))
            km = pd.DataFrame.from_dict(r.json()).transpose()
            km.columns = [ticker + " TTM Ratios"]
            return km
        except requests.exceptions.HTTPError as e:
            print('Requesting Key Metrics ERROR(1): ', str(e))
    elif period == "annual" or period == "quarter":
        try:
            r = requests.get(
                '{}key-metrics/{}?period={}&?limit={}&apikey={}'.format(URL,
                                                                        ticker,
                                                                        period,
                                                                        limit,
                                                                        key))
            km = pd.DataFrame.from_dict(r.json()).transpose()
            km.columns = km.iloc[1]
            return km[2:]
        except requests.exceptions.HTTPError as e:
            print('Requesting Key Metrcs ERROR(2): ', str(e))
    else:
        print('ERROR: Define the period you want: ttm | annual | quarter')
        return None

def get_enterprise_value(ticker, rate, key, period):
    """Period is annual or quarter. The rate is the number of days."""
    URL = 'https://financialmodelingprep.com/api/v3/enterprise-values/'
    try:
        r = requests.get('{}{}?period={}&limit={}&apikey={}'.format(URL,
                                                                    ticker,
                                                                    period,
                                                                    rate,
                                                                    key))
        return pd.DataFrame.from_dict(r.json())
    except requests.exceptions.HTTPError as e:
        print('Requesting Enterprise Value ERROR: ', str(e))
        
# def sales_by_product(ticker, limit, key, period):
#     """Get sales by product segments."""
#     URL = 'https://financialmodelingprep.com/api/v4/revenue-product-segmentation'
#     try:
#         r = requests.get(
#             '{}?symbol={}&period={}&structure=flat'.format(URL,
#                                                         ticker,
#                                                         period))
#         prodsales = pd.DataFrame.from_dict(r.json()).transpose()
#         prodsales.columns = prodsales.loc['date']
#         return prodsales
#     except requests.exceptions.HTTPError as e:
#         print('Requesting sales by product ERROR: ', str(e))

        
# def sales_by_geographic(ticker, limit, key, period):
#     """Get sales by geographic segments."""
#     URL = 'https://financialmodelingprep.com/api/v4/revenue-geographic-segmentation'
#     try:
#         r = requests.get(
#             '{}?symbol={}&period={}&structure=flat'.format(URL,
#                                                         ticker,
#                                                         period))
#         geosales = pd.DataFrame.from_dict(r.json()).transpose()
#         geosales.columns = geosales.loc['date']
#         return geosales
#     except requests.exceptions.HTTPError as e:
#         print('Requesting sales by geographic ERROR: ', str(e))
        
        
def get_market_capital(ticker, key):
    URL = 'https://financialmodelingprep.com/api/v3/market-capitalization/'
    try:
        r = requests.get(
            '{}{}?apikey={}'.format(URL,
                                    ticker,
                                    key))
        # mcap = pd.DataFrame.from_dict(r.json()).transpose()
        return r.json()[0]['marketCap']
    except requests.exceptions.HTTPError as e:
        print('Requesting Market capitalization ERROR: ', str(e))


def get_full_financial_statement_as_reported(ticker, key, period):
    URL = 'https://financialmodelingprep.com/api/v3/financial-statement-full-as-reported/'
    try:
        r = requests.get(
            '{}{}?period={}&apikey={}'.format(URL,
                                              ticker,
                                              period,
                                              key))
        full_statement = pd.DataFrame.from_dict(r.json()).transpose()
        # full_statement.columns = full_statement.loc['fillingDate']
        return full_statement
    except requests.exceptions.HTTPError as e:
        print('Requesting full financial statement ERROR: ', str(e))

        
def get_quote(ticker, key):
    """Getting the current quote of the company."""
    URL = 'https://financialmodelingprep.com/api/v3/quote/'
    try:
        r = requests.get('{}{}?apikey={}'.format(URL,
                                                 ticker,
                                                 key))
        quote = pd.DataFrame.from_dict(r.json()).transpose()
        return(quote)
    except requests.exceptions.HTTPError as e:
        print('Requesting quote estimate ERROR: ', str(e))


def get_industry_multiples():
    """Getting the Industry Multiples value from NYU. """
    URL = 'http://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/vebitda.html'
    html = requests.get(URL).content
    df_list = pd.read_html(html)
    df = df_list[-1]
    df.columns = df.iloc[1]
    df = df.drop(1)
    df['Industry Name'][0] = 'Category'
    df.iloc[0][0] = 'Category'
    df = df.set_index(df['Industry Name'])
    del df['Industry Name']
    return df
