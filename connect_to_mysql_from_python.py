＃Connect to mysql database from python and run query

#import modules
import sqlalchemy
import mysql.connector as sql

#Database connection
database='database_name'
host='192.168.**.**'
user='username'
password='password'
connection_string='mysql+pymysql://'+user+':'+password+'@'+host+':3306/'+database
engine=sqlalchemy.create_engine(connection_string)
con=engine.connect()

#Write your query
sql1="""SELECT * FROM `Table_data_2019`;"""
sql2="""SELECT * FROM `Table_data_2020`;"""

#run your query to pull data to python dataframe
sub0=pd.read_sql(sql1,con)
sub0.shape

sub1=pd.read_sql(sql2,con)
sub1.shape
