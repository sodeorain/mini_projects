#%%
from datetime import date
from datetime import timedelta 
import pandas as pd
#%%
two_hurricanes = ["7/10/2016", "6/21/2017"]
two_hurricanes_dates = [date(2016,10,7), date(2017, 6, 21)]

print(two_hurricanes_dates[0].year)
print(two_hurricanes_dates[0].month)
print(two_hurricanes_dates[0].day)

print(two_hurricanes_dates[1].weekday())

d1 = date(2017, 11, 5)
d2 = date(2017, 12, 4)
l = [d1, d2]

print(min(l))

delta = d2 - d1 

print(delta.days)

td = timedelta(days=29)
print(d1 + td)

