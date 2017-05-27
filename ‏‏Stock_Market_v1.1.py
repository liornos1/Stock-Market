import ystockquote
import sqlite3
import time
import datetime

conn=sqlite3.connect('StockMarketDB1.db')
c=conn.cursor() # make c our cursor
c.execute('CREATE TABLE IF NOT EXISTS stuffToPlot2(unix REAL,datestamp TEXT,stockName TEXT,open REAL,close REAL,low REAL,high REAL)')

stock=["GOOGL","AAPL","^GSPC","TEVA","MSFT"]

price=ystockquote.get_historical_prices('GOOGL', '2017-05-09', '2017-05-11')

numOfstock=5

days=20

print(ystockquote.get_all("GOOGL"))
    
unix =time.time()
date=datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d')
year=datetime.datetime.fromtimestamp(unix).strftime('%Y')
month=datetime.datetime.fromtimestamp(unix).strftime('%m')
day=datetime.datetime.fromtimestamp(unix).strftime('%d')

month_i=int(month)
month_i-=1
monthBebore=str(month_i)

dateMonthBefore=year+'-'+monthBebore+'-'+day


#stockValue=ystockquote.get_price(stock[j])
for val in sorted(price.items()):
    high=val[1]['High']
    low=val[1]['Low']
    opening=val[1]['Open']
    close=val[1]['Close']
    date=val[0]  
    c.execute("INSERT INTO stuffToPlot2(unix,datestamp,stockName,open,close,low,high) VALUES (?,?,?,?,?,?,?)",
          (unix,date,'GOOG',opening,close,low,high))

conn.commit()

c.close()
conn.close()
print("Finnish")


