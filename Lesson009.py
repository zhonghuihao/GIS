import pandas_datareader.data as web
import datetime
import matplotlib.pyplot as plt


start = datetime.datetime.strptime('1/1/2015', '%m/%d/%Y')
end = datetime.datetime.strptime('2/20/2016', '%m/%d/%Y')
f = web.DataReader(['002405.sz', '600589.ss'], 'yahoo', start, end)
print('Adjusted Closing Prices')
print(f['Adj Close'].describe())
ax = f['Adj Close'].plot(grid=True, fontsize=10, rot=45.)
ax.set_ylabel('Adjusted Closing Price ($)')
plt.legend(loc='upper center', ncol=2, bbox_to_anchor=(0.5, 1.1),
           shadow=True, fancybox=True, prop={'size': 10})
plt.show()

