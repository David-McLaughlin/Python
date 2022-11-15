"""
Created on Tue Nov 15 09:55:49 2022
@author: David.McLaughlin
Script integrates with Yahoo Finance or yfinance to pull stock prices for a given ticker.
Configurable to pull one to many year and one to many months.
"""
# -*- coding: utf-8 -*-


import yfinance as yf
import pandas as pd
import numpy as np
import sys

# Get Stock ticker
ticker = "RCI-B.TO"
stock = yf.Ticker(ticker)

#################################
# define years/months to download
# Script will iterate and capture 
#################################
year = [2021]
mon = [1,2,3,4,5,6,7,8,9,10,11,12]
#########################
# Configure Month Lengths
#########################
thirOne = [1,3,5,7,8,10,12]
thirty = [4,6,9,11]
feb = [2]

def GetStockValueByYear():
  # loop on years and download the stock data for assigned dates
  for i in range(len(year)):
    for x in range(len(mon)):
      ############################
      # Get 28 Day Month February 
      ############################
      if x+1 in [10,11,12]:
        start_date=str(year[i])+"-" + str(mon[x]) +"-01"
      else:
        start_date=str(year[i])+"-0" + str(mon[x]) +"-01"		

      if x+1 in feb:
        end_date=str(year[i])+"-0" + str(mon[x]) + "-28"
        ############################
        # Get 30 Day Month Sept, Apr, Jun, Nov
        ############################
      elif x+1 in thirty:
        ###############################
        # Handle dbl digit month (Nov)
        ###############################
        if x+1 == 11:
          end_date=end=str(year[i])+"-" + str(mon[x]) + "-30"
          ################################################
          # Handle Months Starting with 0, Apr, Jun, Sep
          ################################################
        else:
          end_date=end=str(year[i])+"-0" + str(mon[x]) + "-30"
      else:
        ###########################
        # Handle dbl digit months 
        ###########################
        if x+1 in [10,12]:
          end_date=end=str(year[i])+"-" + str(mon[x]) + "-31"
        else:
          end_date=end=str(year[i])+"-0" + str(mon[x]) + "-31"

      data = yf.download(ticker, start=start_date,
            end=end_date, group_by='tickers',progress=False, header=None)
      df = pd.DataFrame(data, columns=['Open','High','Low','Close','Adj Close'])
      print(df)

# Get Highest Stock Price by year
#################################
print("----------------------------------------------------")
print(" List Stock Price by Year --------------------------")
print("----------------------------------------------------")
GetStockValueByYear()
