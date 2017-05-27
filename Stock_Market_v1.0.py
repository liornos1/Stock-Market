import ystockquote
import sqlite3
import time
import datetime

conn=sqlite3.connect('StockMarketDB2.db')
c=conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL,datestamp TEXT,stockName TEXT,stockValue REAL)')

stock=["GOOG","AAPL","^GSPC","TEVA","MSFT"]
numOfstock=5

i=0
while(i<=100):
    j=i%numOfstock
    unix =time.time()
    date=str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    stockName=stock[j]
    stockValue=ystockquote.get_price(stock[j])
    i+=1
    c.execute("INSERT INTO stuffToPlot(unix,datestamp,stockName,stockValue) VALUES (?,?,?,?)",
              (unix,date,stockName,stockValue))
    conn.commit()
    if (j==0): print(i)

c.close()
conn.close()
print("Finnish")


