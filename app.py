from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
from src.mlproject.components.data_ingestion import DataIngestion
from src.mlproject.components.data_ingestion import DataIngestionConfig
from src.mlproject.utils import read_sql_data
import os
import sys

if __name__ == "__main__":
    logging.info("Starting the application...")
    #logging.info("Application started")
    
    #try:
     #   a = 1/0
    #except Exception as e:
     #   logging.info("Error occurred in the try block")
      #  raise CustomException(e, sys)
    
    
    try:
        data_ingestion=DataIngestion()
        data_ingestion.initiate_data_ingestion()
        
    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e, sys)
    
 
    
    logging.info("End of application")
    
    