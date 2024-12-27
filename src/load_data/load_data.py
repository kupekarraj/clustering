# Import required libraries
import pandas as pd
import sys
from src.exception import CustomException
from src.logger import logging


class DataLoader:
    def __init__(self,filepath):
        self.filepath= filepath

    def load_data(self):
        logging.info("Data Loading Started")
        try:
            df= pd.read_csv(self.filepath)
            # Dropping rows having null values and storing the output the same dataset
            df.dropna(subset=["trading_name"], inplace=True)
            return df
            logging.info("Data Loading Complete")

        except Exception as e:
            logging.error("Error in Data Loading")
            raise CustomException(e,sys)
        
if __name__ == '__main__':
    file_path= input().strip()
    data_loader= DataLoader(file_path)