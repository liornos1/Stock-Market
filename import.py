import ystockquote
import os
import time
from time import gmtime, strftime
import shutil
os.chdir('C:\\Users\\liornos\\Google Drive')
numOfstock=5
#time.strptime("30 Nov 00", "%d %b %y")
print("Running...")
while True:
    localtime=strftime("%a, %d %b %Y %H:%M:%S +0000", time.localtime())
    sec=localtime[23:25]
    min=localtime[20:22]
    hour=localtime[17:19]
    print(hour+":"+min+":"+sec)
    hour1=strftime("%H", time.localtime())
    
    
    if (hour!='16'):
        print(hour+":"+min+":"+sec)
        break
    time.sleep(50)
stock=["GOOG","AAPL","^GSPC","TEVA","MSFT"]
j=0
while(j<=numOfstock-1):
    f = open(stock[j]+'.txt', 'w')
    j+=1
    
i=1
while(i<=100):
    j=0
    while(j<=numOfstock-1):
        f = open(stock[j]+'.txt', 'a')
        #f.write(ystockquote.get_price(stock[j])+'\n')
        j+=1
        print(strftime("%H:%M:%S", time.localtime()))
        #f.close()
        #time.sleep(1) # Wait for 5 seconds
    i+=1 # end of first while

j=0
while(j<=numOfstock-1): 
    shutil.copy2(stock[j]+'.txt', stock[j]+'_.txt')
    j+=1

import time
time=strftime("%a, %d %b %Y %H:%M:%S +0000", time.localtime())
sec=time[23:25]
min=time[20:22]
hour=time[17:19]
print(hour+":"+min+":"+sec)
f.close()
print("Finnish")


