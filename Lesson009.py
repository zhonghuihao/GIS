from pandas_datareader import data
from yahoo_finance import Share
from datetime import datetime


swtx = Share('002405.sz')
dictK = swtx.get_historical('2016-08-06', '2016-09-06')
# print(swtx.get_trade_datetime(), swtx.get_open(),
#       swtx.get_days_high(), swtx.get_days_low(), swtx.get_price(),
#       swtx.get_short_ratio())
f = open('file/STK.txt', 'w')

for ln in dictK:
    f.write(str(ln) + '\n')





