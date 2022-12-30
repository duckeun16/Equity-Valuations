# https://site.financialmodelingprep.com/
""" Available functions to scrape data
 when needed from Financial modeling Prep."""
import requests
import pandas as pd
import numpy as np

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


# Equalize dates of the data to the target data
def equalize_date(data,target,length=5):
    data = data.iloc[-length:]
    data.index = target.index
    return data


# Restore annual data points based on fully available annual growth data
def restoredata(limited_data, growth_data):
    limited_data = limited_data[-1]
    growth_data = (1+growth_data).iloc[::-1]
    growth_data = np.cumprod(growth_data).iloc[::-1]
    growth_data = growth_data.shift(-1)
    growth_data.iloc[-1] = 1
    
    full_data = limited_data/growth_data
    return full_data


def reconstruct_BV(ShE, WASHO, ShEpsh_g_3Y):
    try:
        ShEpsh = ShE / WASHO.tail(5).values # ShE limited to 5Y, WASHO is unlimited
        d_ShEpsh = ShEpsh.pct_change() 

        # uses 3Y growth data which is fully available
        constant_G5 = ShEpsh_g_3Y[-1]
        constant_G4 = ShEpsh_g_3Y[-2]
        constant_G3 = ShEpsh_g_3Y[-3]

        # using gt=5, index -1 --> get g2
        X = (1+constant_G4)/(1+constant_G5)
        g2 = X * (1+d_ShEpsh[-1]) - 1

        # using gt=4, index -2 --> g1
        Y = (1+constant_G3)/(1+constant_G4)
        g1 = Y * (1+d_ShEpsh[-2]) - 1

        # deduce g3 using g1 and g2
        g3 = (1+constant_G3)/((1+g1)*(1+g2)) - 1

        # deduce g4 using g2 and g3
        g4 = (1+constant_G4)/((1+g2)*(1+g3)) - 1

        # deduce g5 using g3 and g4
        g5 = (1+constant_G5)/((1+g3)*(1+g4)) - 1

        # build DF for ShEpsh_g_1Y
        ShEpsh_g_1Y = pd.DataFrame(['NaN'] * len(ShEpsh_g_3Y.index[:-5]))
        ShEpsh_g_1Y.index = ShEpsh_g_3Y.index[:-5] #ShEpsh
        ShEpsh_g_1Y = ShEpsh_g_1Y.rename(columns={0:'d_ShEpsh'})

        # Will be added to ShEpsh_g_1Y after ShEpsh_g_1Y is filled
        add_df = pd.DataFrame([g1,g2,g3,g4,g5],index = ShEpsh_g_3Y.index[-5:])
        add_df = add_df.rename(columns={0:'d_ShEpsh'})
        ShEpsh_g_1Y = pd.concat([ShEpsh_g_1Y, add_df], axis=0)

        # to get: ShEpsh_g_1Y index = -6
        # use ShEpsh_g_3Y index -3, -2; ShEpsh_g_1Y index = -3

        for idx in range(len(ShEpsh_g_1Y)-5): # fill from 6th from the last to the first data
            constant_Gt = ShEpsh_g_3Y[-(3+idx)]
            constant_Gt_L1 = ShEpsh_g_3Y[-(4+idx)]
            gt = ShEpsh_g_1Y.iloc[-(3+idx)]

            X = (1+constant_Gt_L1)/(1+constant_Gt)
            gfill = X * (1+gt) - 1

            ShEpsh_g_1Y.iloc[-(idx+6)] = gfill # start from 6th from the last and fill data

        rst_ShEpsh = restoredata(ShEpsh,ShEpsh_g_1Y).rename(columns={'d_ShEpsh': 'ShEpsh'})
    except:
        print('error occurred during Past Book Value of Equity calculation')
    
    try:
        if len(rst_ShEpsh) < len(WASHO):
            rst_start = rst_ShEpsh.index[0]
            # WASHO_ = WASHO.loc[rst_start:]
            WASHO_ = WASHO.iloc[-len(rst_ShEpsh):]
            WASHO_ = equalize_date(WASHO_, rst_ShEpsh['ShEpsh'], 0)
            constructed_ShE = rst_ShEpsh['ShEpsh'] * WASHO_ # ShE
        else:
            WASHO_start = WASHO.index[0]
            # rst_ShEpsh_ = rst_ShEpsh.loc[WASHO_start:]
            rst_ShEpsh_ = rst_ShEpsh.iloc[-len(WASHO):]
            rst_ShEpsh_ = equalize_date(rst_ShEpsh, WASHO, 0)
            constructed_ShE = rst_ShEpsh_['ShEpsh'] * WASHO # ShE
    except: 
        print('error occurred during Book Value Equity per share calculation')
    
    return constructed_ShE


def get_allROE(BV, NI):
#     BV_start = BV.index[0]
#     NI_ = NI.loc[BV_start:]  
    if len(BV) < len(NI):
        NI_ = NI.iloc[-len(BV):]
        BV = equalize_date(BV, NI_, 0)
    else:
        BV_ = BV.iloc[-len(NI):]
        BV = equalize_date(BV_, NI, 0)
      
    EndE = BV
    AvgE = (BV + BV.shift(1))/2

    roe_endE = NI/EndE
    roe_avgE = NI/AvgE
    
    return roe_endE, roe_avgE


def get_GR(roe_data):
    GR = np.prod(1+roe_data.pct_change()) ** (1/(roe_data.pct_change().count()))
    ROE_gmean = roe_data.copy()

    GR_ser = pd.Series([GR for n in range(len(ROE_gmean))])
    GR_ser.index = ROE_gmean.index
    GR_ser[0] = 1
    
    if pd.isna(ROE_gmean.iloc[0]):
        ROE_gmean.iloc[2:] = ROE_gmean.iloc[1]
        GR_ser = GR_ser.shift(1)
    else:
        ROE_gmean.iloc[1:] = ROE_gmean.iloc[0]
        
    ROE_gmean = ROE_gmean.values * GR_ser.cumprod()
    return ROE_gmean, GR


def S_RIM_ROE_estimates(roe_data):
    # S-RIM estimate using past 5 years ROE data
    S_RIM_ROE_estimates = roe_data.copy()

    # integer weights from the start of data = 1 to end of data = N
    weights = list(range(1,1+roe_data.count()))

    # assign weights to past ROE observations
    # (ROE * range(1,6)).cumsum().values / pd.Series(range(1,6)).cumsum()
    for w in weights:
        x = weights[:w]
        if pd.isna(roe_data.iloc[0]):
            estimates = sum(roe_data[1:w+1] * x)/sum(x)
            # assign 1-period forward S-RIM estimates to t-1 period
            S_RIM_ROE_estimates.iloc[w] = estimates
        else:
            estimates = sum(roe_data[0:w] * x)/sum(x)
            # assign 1-period forward S-RIM estimates to t-1 period
            S_RIM_ROE_estimates.iloc[w-1] = estimates
    
    # Last estimate is the complete S-RIM estimate 
    return S_RIM_ROE_estimates # [-1]


# S-RIM ROE_1 estimation
def S_RIM_ROE_Projection(ROE_data, ROE_ttm=None):
    ROE_data = ROE_data.copy()
    
    # Plug in ttm value of ROE if specified
    if ROE_ttm is not None:
        ROE_data.iloc[-1] = ROE_ttm
        
    # Criteria to use S-RIM ROE estimation method:
    # If past ROE has been strictly rising [falling] or geometric return > 1 [GR < 1]: 
    #     Use the last obs data as estimate
    # If past ROE has been neither strictly rising nor falling (or GR = 1):
    #     Use the S-RIM ROE estimation method
    
    # Strictly rising or falling to determine criteria
    if (ROE_data[1:] > ROE_data.shift(1)[1:]).sum() == len(ROE_data[1:]):
        ROE_1 = ROE_data[-1]
        print(f'rising: {ROE_1}')
    elif (ROE_data[1:] < ROE_data.shift(1)[1:]).sum() == len(ROE_data[1:]):
        ROE_1 = ROE_data[-1]
        print(f'falling: {ROE_1}')
    else:
        ROE_1 = S_RIM_ROE_estimates(ROE_data)[-1]
        print(f'sideways: {ROE_1}')
        
    ### OR
    
    # Geometric Return vs 1 to determine criteria
#     ROE_gmean, GR = get_GR(ROE_data)
#     if (GR > 1) or (GR < 1):
#         ROE_1 = ROE_data[-1]
#     else:
#         ROE_1 = S_RIM_ROE_estimates(ROE_data)[-1]

    ROE_data.index = range(1,6)
    ROE_data.loc[6] = ROE_1
    # t=0: now, t+1: estimation period, t-1 ~ t-4: past
    ROE_data.index = ROE_data.index - 5 # now: index_num=5
    
    return ROE_1, ROE_data

