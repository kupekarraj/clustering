# Import required libraries
import pandas as pd
import sys
from src.exception import CustomException
from src.logger import logging


class DataLoader:
    def __init__(self,filepath='notebook/dataset/Dealer_Export.csv'):
        self.filepath= filepath

    def load_data(self):
        logging.info("Data Loading Started")
        try:
            df= pd.read_csv(self.filepath)
            # Dropping rows having null values and storing the output the same dataset
            #df.dropna(subset=["trading_name"], inplace=True)
            df.dropna(inplace=True)

            logging.info("Data Loading Complete")
            return df

        except Exception as e:
            logging.error("Error in Data Loading")
            raise CustomException(e,sys)
        
if __name__ == '__main__':
    file_path= input("Enter the file path here: ").strip()
    data_loader= DataLoader(file_path)
    data= data_loader.load_data()