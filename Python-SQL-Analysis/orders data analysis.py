import pandas as pd

# Load data
df = pd.read_csv('orders.csv', na_values=['Not Available', 'unknown'])

# Clean column names
df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace(' ', '_')

# Create new columns
df['discount'] = df['list_price'] * df['discount_percent'] * 0.01
df['sale_price'] = df['list_price'] - df['discount']
df['profit'] = df['sale_price'] - df['cost_price']

# Convert date
df['order_date'] = pd.to_datetime(df['order_date'])

# Connect to SQL
from sqlalchemy import create_engine

engine = create_engine(
    "mssql+pyodbc://@localhost/mydatabase?driver=ODBC+Driver+18+for+SQL+Server&trusted_connection=yes&TrustServerCertificate=yes"
)

conn = engine.connect()
print("Connected successfully")

# Load to SQL
df.to_sql('orders_data', con=engine, index=False, if_exists='replace', schema='dbo')


