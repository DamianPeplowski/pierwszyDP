import pandas as pd
import matplotlib.pyplot as plt

#Description of Dataset:
#Date: It gives the date of which stocks details are given.
#Open: It gives the opening price of stock on that date.
#High: It gives the highest price to which the stock ascened on that day.
#Low: It gives the highest price to which the stock plummeted on that day.
#Close: It gives the closing price of stock on that date.
#Volume: It gives the amount of stock traded on that date.
#Adjusted Close: An adjusted closing price is a stock’s closing price on any
#given day of trading that has been amended to include any
#distributions and corporate actions that occurred at any
#time prior to the next day’s open.

df = pd.read_csv("alphabet_stock_data.csv")
start_date = pd.to_datetime('2020-4-1')
end_date = pd.to_datetime('2020-09-30')
df['Date'] = pd.to_datetime(df['Date'])
new_df = (df['Date'] >= start_date) & (df['Date'] <= end_date)
df1 = df.loc[new_df]
df2 = df1.set_index('Date')
plt.figure(figsize=(5, 5))
plt.suptitle('Stock prices of Alphabet Inc.,\n01-04-2020 to 30-09-2020',fontsize=18, color='black')
plt.xlabel("Date", fontsize=16, color='black')
plt.ylabel("$ price", fontsize=16, color='black')
df2['Close'].plot(color='green');
plt.show()

df = pd.read_csv("alphabet_stock_data.csv")
start_date = pd.to_datetime('2020-4-1')
end_date = pd.to_datetime('2020-09-30')
df['Date'] = pd.to_datetime(df['Date'])
new_df = (df['Date']>= start_date) & (df['Date']<= end_date)
df2 = df.loc[new_df]
plt.figure(figsize=(10,10))
df2.plot(x='Date', y=['Open', 'Close']);
plt.suptitle('Opening/Closing stock prices of Alphabet Inc.,\n 01-04-2020 to 30-09-2020', fontsize=12, color='black')
plt.xlabel("Date",fontsize=12, color='black')
plt.ylabel("$ price", fontsize=12, color='black')
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("alphabet_stock_data.csv")
start_date = pd.to_datetime('2020-4-1')
end_date = pd.to_datetime('2020-4-30')
df['Date'] = pd.to_datetime(df['Date'])
new_df = (df['Date']>= start_date) & (df['Date']<= end_date)
df1 = df.loc[new_df]
df2 = df1.set_index('Date')
plt.figure(figsize=(6,6))
plt.suptitle('Trading Volume of Alphabet Inc. stock,\n01-04-2020 to 30-04-2020', fontsize=16, color='black')
plt.xlabel("Date",fontsize=12, color='black')
plt.ylabel("Trading Volume", fontsize=12, color='black')
df2['Volume'].plot(kind='bar');
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("alphabet_stock_data.csv")
start_date = pd.to_datetime('2020-4-1')
end_date = pd.to_datetime('2020-4-30')
df['Date'] = pd.to_datetime(df['Date'])
new_df = (df['Date']>= start_date) & (df['Date']<= end_date)
df1 = df.loc[new_df]
df2 = df1[['Date', 'Open', 'Close']]
df3 = df2.set_index('Date')
plt.figure(figsize=(20,20))
df3.plot(kind='bar');
plt.suptitle('Opening/Closing stock prices Alphabet Inc.,\n01-04-2020 to 30-04-2020', fontsize=12, color='black')
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("alphabet_stock_data.csv")
start_date = pd.to_datetime('2020-4-1')
end_date = pd.to_datetime('2020-4-30')
df['Date'] = pd.to_datetime(df['Date'])
new_df = (df['Date']>= start_date) & (df['Date']<= end_date)
df1 = df.loc[new_df]
df2 = df1[['Date', 'Open', 'Close']]
df3 = df2.set_index('Date')
plt.figure(figsize=(20,20))
df3.plot.bar(stacked=True);
plt.suptitle('Opening/Closing stock prices Alphabet Inc.,\n01-04-2020 to 30-04-2020', fontsize=12, color='black')
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("alphabet_stock_data.csv")
start_date = pd.to_datetime('2020-4-1')
end_date = pd.to_datetime('2020-4-30')
df['Date'] = pd.to_datetime(df['Date'])
new_df = (df['Date']>= start_date) & (df['Date']<= end_date)
df1 = df.loc[new_df]
df2 = df1[['Date', 'Open', 'Close']]
df3 = df2.set_index('Date')
plt.figure(figsize=(20,20))
df3.plot.barh(stacked=True)
plt.suptitle('Opening/Closing stock prices Alphabet Inc.,\n01-04-2020 to 30-04-2020', fontsize=12, color='black')
plt.show()

df = pd.read_csv("alphabet_stock_data.csv")
start_date = pd.to_datetime('2020-4-1')
end_date = pd.to_datetime('2020-9-30')
df['Date'] = pd.to_datetime(df['Date'])
new_df = (df['Date']>= start_date) & (df['Date']<= end_date)
df1 = df.loc[new_df]
df2 = df1[['Open','Close','High','Low']]
#df3 = df2.set_index('Date')
plt.figure(figsize=(25,25))
df2.plot.hist(alpha=0.5)
plt.suptitle('Opening/Closing/High/Low stock prices of Alphabet Inc.,\n From 01-04-2020 to 30-09-2020', fontsize=12, color='blue')
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("alphabet_stock_data.csv")
start_date = pd.to_datetime('2020-4-1')
end_date = pd.to_datetime('2020-9-30')
df['Date'] = pd.to_datetime(df['Date'])
new_df = (df['Date']>= start_date) & (df['Date']<= end_date)
df1 = df.loc[new_df]
df2 = df1[['Open','Close','High','Low']]
plt.figure(figsize=(25,25))
df2.plot.hist(stacked=True, bins=20)
plt.suptitle('Opening/Closing/High/Low stock prices of Alphabet Inc.,\n From 01-04-2020 to 30-09-2020', fontsize=12, color='blue')
plt.show()

df = pd.read_csv("alphabet_stock_data.csv")
start_date = pd.to_datetime('2020-4-1')
end_date = pd.to_datetime('2020-9-30')
df['Date'] = pd.to_datetime(df['Date'])
new_df = (df['Date']>= start_date) & (df['Date']<= end_date)
df1 = df.loc[new_df]
df2 = df1[['Open','Close','High','Low']]
plt.figure(figsize=(25,25))
df2.plot.hist(stacked=True, bins=200)
plt.suptitle('Opening/Closing/High/Low stock prices of Alphabet Inc.,\n From 01-04-2020 to 30-09-2020', fontsize=12, color='black')
plt.show()

df = pd.read_csv("alphabet_stock_data.csv")
start_date = pd.to_datetime('2020-4-1')
end_date = pd.to_datetime('2020-9-30')
df['Date'] = pd.to_datetime(df['Date'])
new_df = (df['Date']>= start_date) & (df['Date']<= end_date)
df1 = df.loc[new_df]
df2 = df1[['Open','Close','High','Low']]
plt.figure(figsize=(30,30))
df2.hist();
plt.suptitle('Opening/Closing/High/Low stock prices of Alphabet Inc., From 01-04-2020 to 30-09-2020', fontsize=12, color='black')
plt.show()

df = pd.read_csv("alphabet_stock_data.csv")
start_date = pd.to_datetime('2020-4-1')
end_date = pd.to_datetime('2020-9-30')
df['Date'] = pd.to_datetime(df['Date'])
new_df = (df['Date']>= start_date) & (df['Date']<= end_date)
df1 = df.loc[new_df]
stock_data = df1.set_index('Date')
top_plt = plt.subplot2grid((5,4), (0, 0), rowspan=3, colspan=4)
top_plt.plot(stock_data.index, stock_data["Close"])
plt.title('Historical stock prices of Alphabet Inc. [01-04-2020 to 30-09-2020]')
bottom_plt = plt.subplot2grid((5,4), (3,0), rowspan=1, colspan=4)
bottom_plt.bar(stock_data.index, stock_data['Volume'])
plt.title('\nAlphabet Inc. Trading Volume', y=-0.60)
plt.gcf().set_size_inches(12,8)

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("alphabet_stock_data.csv")
start_date = pd.to_datetime('2020-4-1')
end_date = pd.to_datetime('2020-9-30')
df['Date'] = pd.to_datetime(df['Date'])
new_df = (df['Date']>= start_date) & (df['Date']<= end_date)
df1 = df.loc[new_df]
stock_data = df1.set_index('Date')
stock_data.plot(subplots = True, figsize = (8, 8));
plt.legend(loc = 'best')
plt.suptitle('Open,High,Low,Close,Adj Close prices & Volume of Alphabet Inc., From 01-04-2020 to 30-09-2020', fontsize=12, color='black')
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("alphabet_stock_data.csv")
start_date = pd.to_datetime('2020-4-1')
end_date = pd.to_datetime('2020-9-30')
df['Date'] = pd.to_datetime(df['Date'])
new_df = (df['Date']>= start_date) & (df['Date']<= end_date)
df1 = df.loc[new_df]
stock_data = df1.set_index('Date')
close_px = stock_data['Adj Close']
stock_data['SMA_30_days'] = stock_data.iloc[:,4].rolling(window=30).mean()
stock_data['SMA_40_days'] = stock_data.iloc[:,4].rolling(window=40).mean()
plt.figure(figsize=[10,8])
plt.grid(True)
plt.title('Historical stock prices of Alphabet Inc. [01-04-2020 to 30-09-2020]\n',fontsize=18, color='black')
plt.plot(stock_data['Adj Close'],label='Adjusted Closing Price', color='black')
plt.plot(stock_data['SMA_30_days'],label='30 days simple moving average', color='red')
plt.plot(stock_data['SMA_40_days'],label='40 days simple moving average', color='green')
plt.legend(loc=2)
plt.show()

df = pd.read_csv("alphabet_stock_data.csv")
start_date = pd.to_datetime('2020-4-1')
end_date = pd.to_datetime('2020-9-30')
df['Date'] = pd.to_datetime(df['Date'])
new_df = (df['Date']>= start_date) & (df['Date']<= end_date)
df1 = df.loc[new_df]
df2 = df1.set_index('Date')
x= ['Close']; y = ['Volume']
plt.figure(figsize=[15,10])
df2.plot.scatter(x, y, s=50);
plt.grid(True)
plt.title('Trading Volume/Price of Alphabet Inc. stock,\n01-04-2020 to 30-09-2020', fontsize=14, color='black')
plt.xlabel("Stock Price",fontsize=12, color='black')
plt.ylabel("Trading Volume", fontsize=12, color='black')
plt.show()

df = pd.read_csv("alphabet_stock_data.csv")
start_date = pd.to_datetime('2020-4-1')
end_date = pd.to_datetime('2020-9-30')
df['Date'] = pd.to_datetime(df['Date'])
new_df = (df['Date']>= start_date) & (df['Date']<= end_date)
df1 = df.loc[new_df]
df2 = df1[['Date', 'Adj Close']]
df3 = df2.set_index('Date')
daily_changes = df3.pct_change(periods=1)
daily_changes['Adj Close'].plot(figsize=(10,7),legend=True,linestyle='--',marker='o')
plt.suptitle('Daily % return of Alphabet Inc. stock price,\n01-04-2020 to 30-09-2020', fontsize=12, color='black')
plt.grid(True)
plt.show()

df = pd.read_csv("alphabet_stock_data.csv")
start_date = pd.to_datetime('2020-4-1')
end_date = pd.to_datetime('2020-9-30')
df['Date'] = pd.to_datetime(df['Date'])
new_df = (df['Date']>= start_date) & (df['Date']<= end_date)
df1 = df.loc[new_df]
df2 = df1[['Date', 'Close']]
df3 = df2.set_index('Date')
data_filled = df3.asfreq('D', method='ffill')
data_returns = data_filled.pct_change()
data_std = data_returns.rolling(window=30, min_periods=30).std()
plt.figure(figsize=(20,20))
data_std.plot();
plt.suptitle('Volatility over a period of time  of Alphabet Inc. stock price,\n01-04-2020 to 30-09-2020', fontsize=12, color='black')
plt.grid(True)
plt.show()
















