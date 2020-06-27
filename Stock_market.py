#Importing Libraries
from alpha_vantage.timeseries import TimeSeries
import time
#My Api Key
api_key = 'X828406OK1MG9ZBU'

#Loading the Real_Time Data
ts = TimeSeries(key = api_key ,output_format = 'pandas')
data ,meta_data = ts.get_intraday(symbol = 'MSFT' , interval = '1min' , outputsize = 'full')
print(data)
#Creating a Loop to Exporting the Data
i =1
#while i ==1:
    #data.to_csv("output.csv")#Csv file genarates Automatically
   #time.sleep(60)#time period 1min = 60 sec
close = data['4.close'] # taking the column to 
percentage_change = close.pct_change()
print(percentage_change)


last_change = percentage_change[-1]

if abs(last_change) > 0.0004:
    print("Alert"+ last_change)
