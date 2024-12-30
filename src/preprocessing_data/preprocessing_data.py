import pandas as pd
import sys
import warnings
from src.logger import logging
from src.exception import CustomException
from src.load_data.load_data import DataLoader

# Suppress all warnings
warnings.filterwarnings("ignore")  

class DataPreprocessing:
    def __init__(self,data_frame):
        self.data_frame= data_frame

    # Defined a function to clean the pacakge info
    def package_restructure(self,x):
            # First check if the value is NaN
            if pd.isna(x):
                return "No Package Info"
            # Ensure x is a string before using string operations
            x= str(x) # Convert to string to safely use 'in' or 'startswith'
            if "Level 0" in x:
                return "CZ Level 0 Package"
            elif "Level 1" in x:
                return "CZ Level 1 Package"
            elif "Level 2" in x:
                return "CZ Level 2 Package"
            elif "Level 3" in x:
                return "CZ Level 3 Package"
            elif "Level 4" in x:
                return "CZ Level 4 Package"
            elif x.startswith('Accelerate'):
                return "CZ Accelerate Package"
            elif x.startswith('Ignite'):
                return "CZ Ignite Package"
            elif x.startswith('Rev'):
                return "CZ Rev Package"
            else:
                return "Other Package"

    def preprocess_data(self):
        logging.info("Data Preprocessing Started")
        try:
            # Correcting the data types for certain columns
            self.data_frame['did'] = self.data_frame['did'].astype('object')
            self.data_frame['reg_code']=self.data_frame['reg_code'].astype('object')
            self.data_frame['created_date']=pd.to_datetime(self.data_frame['created_date'])

            # Adding two new columns for Ad Created Month-Year & Package Redefining
            self.data_frame['ad_created_in']=self.data_frame['created_date'].dt.strftime('%b, %Y')
            self.data_frame['package_redefined'] = self.data_frame['package'].apply(self.package_restructure)

            # Dropping unwanted columns from the data frame
            self.data_frame.drop(columns=['package','created_date'], inplace=True)

            # Correcting the data types for certain columns\n",
            self.data_frame['did'] = self.data_frame['did'].astype('object')
            self.data_frame['reg_code']=self.data_frame['reg_code'].astype('object')

            logging.info("Data Preprocessing Completed")
            return self.data_frame

        except Exception as e:
            logging.error("Error in Data Preprocessing")
            raise CustomException(e,sys)
        
if __name__ == '__main__':
    file_path= input("Enter the file path here: ").strip()
    data_loader= DataLoader(file_path)
    data_frame= data_loader.load_data()

    data_preprocess= DataPreprocessing(data_frame)
    data = data_preprocess.preprocess_data()

    