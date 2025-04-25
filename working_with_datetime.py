#%%
from datetime import date
from datetime import datetime
from datetime import timedelta 
import pandas as pd
df = pd.read_csv("daily-minimum-temperatures-in-me.csv")
# %%
print(df["Date"].dtype)

# %%
df["Date"] = pd.to_datetime(df["Date"], format='%m/%d/%Y')    
# %%
formatted_dates = df["Date"].dt.strftime("%d.%m.$Y")
df

# %%
df["Year"] = df["Date"].dt.year
formatted_dates
# %%
df
# %%
df["Year"].dtype
# %%
df["Date"].dtype
# %%
