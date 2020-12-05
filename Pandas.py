# CNA330
# Teacher: Justin Elis
# Final Group Project: Weight loss tracker
# Chris Bow 2018 calorie, exercise and weight changes
# Daily calorie intake and exercise information with daily weight loss/gain
# Group project participants: Igor Turcan, Saeid Nahali, Benjamin Bohnen
# Teacher: Justin Elis
# Tutoring help: Liviu Patrasco, liviu_patrasco@hotmail.com

import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as pp

#Grabs table from the website (Can connect to local .csv file or website)
data = "https://storage.googleapis.com/kagglesdsdata/datasets/100171/236755/diet_data.csv?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20201203%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20201203T030243Z&X-Goog-Expires=259199&X-Goog-SignedHeaders=host&X-Goog-Signature=01aac892dce1549e4ddd02c5cbffb6a11cd2d9aaf46c745afdd3c0656e24d35fb648c08f1fe186ef0f834394ffe5c2cb2527b92d3aef2e73f943b2c5800b4e666424603867b41951f2575788844ee9e9ae4341e16bf57b6fa5ae212b950c00d8ca455602a44c4e95ad25556dd83a99f63a20bf1d4f529510d0405328c865e645f15ebad67b4c675723be6082bc050c54a41a515edfb5128e6b81a0679850ab90714fe0f03cc4c89e4e83feeb19cbefdec05f54858cf9c4af55d1452882886bd6a01e82b842e1b625929b149f594ed76b192e725b21b471ebfe8787a91d6101f23fbac813d8de980d98dade041aaf388c35ecc4b92835df4ec3372366182a01f5"
# data = pd.read_csv("diet_data.csv")  # imports the data from csv

#Prints columns and cleans up empty lines
data=pd.read_csv(data)
print(data.columns)    # prints columns from csv
data = data.dropna()     # removes empty lines
data = data.where(pd.notnull(data), None)     # removes empty lines
data['Stone'] = data['Stone'] * 14
data.rename(columns = {'Stone':'Pounds'})
print(data['Pounds'])

#Creates, connects, and writes to database
sql_engine = create_engine('mysql+pymysql://root:@localhost:3306/cna330')
db_connection = sql_engine.connect()  # create database connection
data.to_sql('diet_data', con=db_connection, if_exists='replace', index=False)     # write the data in to database

#Queries and reads the database
sql = "select * from diet_data limit 100"     # select SQL query
data = pd.read_sql(sql, db_connection)     # panda reads data from database

# Creates various graphs, effect of calories and exercise on changes in Chris Bow weight:
## Uncomment to generate the graph
#data.plot(x="Date", y="Pounds", kind="bar")  # sql = 20(data limit): creates the bar graph, and showing how many pounds gain the person through time.
#pp.title("Chris Bow diet data on daily pounds\n\nper day")  # graph title.

#data.plot(x="Date", y="calories", kind="hist")  # sql = 100(data limit): creates the histograph skewd to the right and showing calories the person eat through time.
#pp.title("Chris Bow diet data on daily calories\n\neat through time")  # graph title.

#data.plot(x="calories", y="weight_oz", kind="box")  # sql = 100(data limit): creates the plot(graph) creates the boxplot graph, which can easly show the average of caloryes eating per day.
#pp.title("Chris Bow diet data on daily average of\n\ncalories eating per day")  # graph title.

pp.show()  # show the plot(graph)
