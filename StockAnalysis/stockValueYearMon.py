
####################
# Import Libraries #
####################
import yfinance as yf
import pandas as pd

#############################
# Configure Ticker and Year #
#############################
ticker='BB'
year='2023'
stock = yf.Ticker(ticker)

####################
# Pull Stock Data  #
####################
data = yf.download(ticker, start=str(year) + str('-01-01'),
              end=str(year) + str('-12-31'), group_by='tickers', progress=False)
df = pd.DataFrame(
     data, columns=['Open', 'Close'])
####################
# Print Ticker Data#
####################
print(df)
