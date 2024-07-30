import numpy as np
import pandas as pd
URL="https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29"

#Using the Pandas library to extract the required table directly as a DataFrame.
tables = pd.read_html(URL)
df = tables[3]
df.columns = range(df.shape[1])

df = df[[0,2]]
df = df.iloc[1:11,:]
df.columns = ['Country','GDP (Million USD)']


"""Modifying the GDP column of the DataFrame, converting the value available in Million USD to Billion USD. 
Using the `round()` method of Numpy library to round the value to 2 decimal places. Modifying the header of the DataFrame to GDP (Billion USD) """""
df['GDP (Million USD)'] = df['GDP (Million USD)'].astype(int)
df[['GDP (Million USD)']] = df[['GDP (Million USD)']]/1000
df[['GDP (Million USD)']] = np.round(df[['GDP (Million USD)']], 2)
df.rename(columns = {'GDP (Million USD)' : 'GDP (Billion USD)'})


#Loading the DataFrame to a CSV file
df.to_csv('./Largest_economies.csv')
