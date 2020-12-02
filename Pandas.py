#CNA330
# Final Group Project
# Group project participants: Igor Turcan, Saeid Nahali, Benjamin Bohnen
# Teacher: Justin Elis
# Tutoring help: Liviu Patrasco, liviu_patrasco@hotmail.com
import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as pp

# data=pd.read_html("https://www.kaggle.com/chrisbow/2018-calorie-exercise-and-weight-changes")

data = pd.read_csv("diet_data.csv")  # imports the data from csv

print(data.columns)    # prints columns from csv

data = data.dropna()     # removes empty lines
data = data.where(pd.notnull(data), None)     # removes empty lines
sql_engine = create_engine('mysql+pymysql://root:@localhost:3306/cna330')     # create database engine
db_connection = sql_engine.connect()  # create database connection
data.to_sql('diet_data', con=db_connection, if_exists='replace', index=False)     # write the data in to database
sql = "select * from diet_data limit 50"     # select SQL query
data = pd.read_sql(sql, db_connection)     # panda reads data from database
data.plot(x="calories", y="weight_oz", kind="scatter")     # creates the plot(graph)
data.plot(x="Date", y="Pounds", kind="bar")     # creates the plot(graph)
pp.show()     # show the plot(graph)
