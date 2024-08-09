import os 
import sys
from src.mlproject.exception import CustomException
from src.mlproject.logger import logging
import pandas as pd
from dotenv import load_dotenv
import mysql
import pymysql

load_dotenv()

host=os.getenv("host")
user=os.getenv("user")
password=os.getenv("password")
db=os.getenv("db")




def read_sql_data():
    logging.info("Reading data from my sql database College")
    try:
        mydb=pymysql.connect(host=host, user=user, password=password, db=db)
        logging.info("Connection to mysql database successful")
        df=pd.read_sql_query('SELECT * FROM students', con=mydb)
        print(df.head)
        #df=pd.read_sql_table('stud', con=f'mysql+pymysql://{user}:{password}@{host}/{db}')
        return df
    except Exception as e:
        logging.info("Error occured in reading data from sql")
        raise CustomException(e,sys)
    
    