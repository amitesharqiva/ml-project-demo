from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
import sys

if __name__ == "__main__":
    logging.info("Starting the application...")
    logging.info("Application started")
    
    try:
        a = 1/0
    except Exception as e:
        logging.info("Error occurred in the try block")
        raise CustomException(e, sys)
    
    
 
    
    logging.info("End of application")
    
    