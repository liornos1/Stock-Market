import ystockquote
import sqlite3
import time
import datetime
#test123
conn=sqlite3.connect('StockMarketDB3.db')
c=conn.cursor() # make c our cursor
c.execute('CREATE TABLE IF NOT EXISTS stuffToPlot4(unix REAL,date TEXT,stockName TEXT,open REAL,close REAL,low REAL,high REAL,lastPrice REAL)')

stocks=["GOOGL","AAPL","^GSPC","TEVA","MSFT"]

#price=ystockquote.get_historical_prices('GOOGL', '2017-05-09', '2017-05-11')

numOfstock=5
stock=stocks[0]
days=20
try:
    getStock=ystockquote.get_all(stock)
except:
    print('fail read all')
    
todayOpen=getStock["today_open"]
tradeDate=getStock["last_trade_date"]
tradePrice=getStock["last_trade_price"]
#trade_date
rang=getStock["todays_range_realtime"]
print('rang ',rang)
low=rang[1:7]
high=rang[9:16]
#fifty_sma
#company_name
#volume
#low_limit
#high_limit
#close=goog["previous_close"]
close=getStock["todays_value_change"]
lastPrice=getStock["last_trade_price"]
lastPrice=lastPrice[13:19]


                      
unix =time.time()
date=datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d')
year=datetime.datetime.fromtimestamp(unix).strftime('%Y')
month=datetime.datetime.fromtimestamp(unix).strftime('%m')
day=datetime.datetime.fromtimestamp(unix).strftime('%d')



c.execute("DELETE FROM stuffToPlot4")

c.execute("INSERT INTO stuffToPlot4(unix,date,stockName,open,close,low,high,lastPrice) VALUES (?,?,?,?,?,?,?,?)",
    (unix,date,stock,todayOpen,close,low,high,lastPrice))

conn.commit()
for i in range(60):
    #### update last price 
    time.sleep(5)
    getStock=ystockquote.get_all(stock)
    close=getStock["todays_value_change"]
    print(close)
    c.execute("UPDATE stuffToPlot4 SET close=? WHERE date=?", (close, '2017-05-19'))
    print(i)
    conn.commit()
#c.execute("DELETE FROM stuffToPlot4 WHERE date='2017-05-20';")

conn.commit()
#cur.execute("DROP TABLE IF EXISTS Cars")
#conn.execute("UPDATE COMPANY set SALARY = 25000.00 where ID=1")

##cursor = conn.execute("SELECT unix,datestamp,stockName,open,close,low,high,lastPrice from stuffToPlot3")
##for row in cursor:
##    print(row[2] +" stockName")
##    print(str(row[7])+ " lastPrice")
c.close()
conn.close()
print("Finnish")


