#!/usr/bin/env python
# coding: utf-8


#import Libraries
!python -m pip install pandas sqlalchemy pyodbc

 
#Read data from the file and handle null values
import pandas as pd
df = pd.read_csv('orders.csv',na_values=['Not Available', 'unknown'])
df['Ship Mode'].unique()


array(['Second Class', 'Standard Class', nan, 'First Class', 'Same Day'],
      dtype=object)


#Rename columns names and make them lower case and replace space with underscore
#df.rename(columns={'Order Id':'order_id', 'City': 'city'}) 
df.columns=df.columns.str.lower()
df.columns=df.columns.str.replace(' ','_')
df.head(5)

#Drive new columns discount, sale price and profit
df['discount']=df['list_price']*df['discount_percent']*.01
df['sale_price']=df['list_price']-df['discount']
df['profit']=df['sale_price']-df['cost_price']
df.head(5)


#convert order date from object data type to datetime
#df.dtypes
df['order_date']=pd.to_datetime(df['order_date'],format="%Y-%m-%d")


#drop cost price, list price and discount percent columns
#df.drop(['list_price', 'cost_price', 'discount_percent'], axis=1, inplace=True)
df.columns


from sqlalchemy import create_engine
engine = create_engine(
    "mssql+pyodbc://@localhost/mydatabase?driver=ODBC+Driver+18+for+SQL+Server&trusted_connection=yes&TrustServerCertificate=yes"
)

conn = engine.connect()
print("Connected successfully")
Connected successfully
import pyodbc
print(pyodbc.drivers())


df.to_sql('orders_data', con=engine, index=False, if_exists='replace')

 
 
