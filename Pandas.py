#CNA330
# Final Group Project
# Group project participants: Igor Turcan, Saeid Nahali, Benjamin Bohnen
# Teacher: Justin Elis
# Tutoring help: Liviu Patrasco, liviu_patrasco@hotmail.com
import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as pp

data= "https://storage.googleapis.com/kagglesdsdata/datasets/100171/236755/diet_data.csv?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20201203%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20201203T030243Z&X-Goog-Expires=259199&X-Goog-SignedHeaders=host&X-Goog-Signature=01aac892dce1549e4ddd02c5cbffb6a11cd2d9aaf46c745afdd3c0656e24d35fb648c08f1fe186ef0f834394ffe5c2cb2527b92d3aef2e73f943b2c5800b4e666424603867b41951f2575788844ee9e9ae4341e16bf57b6fa5ae212b950c00d8ca455602a44c4e95ad25556dd83a99f63a20bf1d4f529510d0405328c865e645f15ebad67b4c675723be6082bc050c54a41a515edfb5128e6b81a0679850ab90714fe0f03cc4c89e4e83feeb19cbefdec05f54858cf9c4af55d1452882886bd6a01e82b842e1b625929b149f594ed76b192e725b21b471ebfe8787a91d6101f23fbac813d8de980d98dade041aaf388c35ecc4b92835df4ec3372366182a01f5"
data = pd.read_csv(data)
# data = pd.read_csv("diet_data.csv")  # imports the data from csv

print(data.columns)    # prints columns from csv

data = data.dropna()     # removes empty lines
data = data.where(pd.notnull(data), None)     # removes empty lines
sql_engine = create_engine('mysql+pymysql://pythoneverything:python123@18.216.19.4:3306/CNA330_project')     # create database engine
db_connection = sql_engine.connect()  # create database connection
data.to_sql('diet_data', con=db_connection, if_exists='replace', index=False)     # write the data in to database
sql = "select * from diet_data limit 50"     # select SQL query
data = pd.read_sql(sql, db_connection)     # panda reads data from database
data.plot(x="calories", y="weight_oz", kind="scatter")     # creates the plot(graph)
data.plot(x="Date", y="Pounds", kind="bar")     # creates the plot(graph)
data.plot(x="Date", y="walk", kind="bar")     # creates the plot(graph)
data.plot(x="Date", y="Pounds", kind="pie")     # creates the plot(graph)
pp.show()     # show the plot(graph)
