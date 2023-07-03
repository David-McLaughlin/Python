#######################################################################################
# Function takes year and ticker as input and returns a dataframe of the stock detail #
#######################################################################################
import yfinance as yf
import pandas as pd

def getAnnualStkData(year, ticker):
    stock = yf.Ticker(ticker)
    ############################
    # Get 28 Day Month February
    ############################

    data = yf.download(ticker, start=str(year) + str('-01-01'),
                   end=str(year) + str('-12-31'), group_by='tickers', progress=False, header=None)
    df = pd.DataFrame(
         data, columns=['Open', 'Close'])
    #print(df)
    return df
