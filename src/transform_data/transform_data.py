import pandas as pd
import sys
from src.logger import logging
from src.exception import CustomException
from src.load_data.load_data import DataLoader
from src.preprocessing_data.preprocessing_data import DataPreprocessing
from sklearn.preprocessing import LabelEncoder, StandardScaler

class DataTransform:
    def __init__(self,processed_data):
        self.processed_data=processed_data

    def transform_data(self):
        logging.info("Data Transformation Started")
        
        # Creating a copy of the original dataset
        og_data= self.processed_data.copy()
        
        try:
            # Pulling categorical columns & storing it in an empty list
            categorical=[] # Creating an empty list
            categorical= [col for col in self.processed_data.columns if self.processed_data[col].dtypes=="O"]

            # Encode categorical features
            encoder= LabelEncoder() #Initialising Label Encoder
            self.processed_data[categorical] = self.processed_data[categorical].apply(lambda col: encoder.fit_transform(col))

            # Performing Scaler Trasnformation for numerical features
            scaler=StandardScaler()
            self.processed_data[self.processed_data.columns]=scaler.fit_transform(self.processed_data)

            logging.info("Data Transformation Complete")
            return self.processed_data,og_data
        
        except Exception as e:
            logging.error("Error in Data Transformation")
            raise CustomException(e,sys)
    

if __name__=='__main__':
    file_path= input("Enter the file path here: ").strip()
    data_loader= DataLoader(file_path)
    data_frame= data_loader.load_data()

    data_preprocess= DataPreprocessing(data_frame)
    data = data_preprocess.preprocess_data()

    data_transformation= DataTransform(data)
    data_transformed, original_data = data_transformation.transform_data()
