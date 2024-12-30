import streamlit as st
import sys
import warnings
from src.logger import logging
from src.exception import CustomException
from src.load_data.load_data import DataLoader
from src.preprocessing_data.preprocessing_data import DataPreprocessing
from src.transform_data.transform_data import DataTransform
from src.cluster_data.cluster_data import KMeansClustering
from src.elbow_output.elbow_output import ElbowMethodViz
from src.pca_analysis.pca_analysis import PCA_Analysis

# Suppress all warnings
warnings.filterwarnings("ignore") 

def main():
    logging.info("Setting Streamlit UI")
    try:
        st.title('Carzone Dealer Segmentation')

        # Load Dataset
        #file_path= input("Enter the file path here: ").strip()
        data_loader= DataLoader()
        data_frame= data_loader.load_data()

        # Writing the Imported dataset for reference
        st.write("Dealer's Data for Analysis", data_frame)

        # Feature selection for clustering
        selected_features = st.multiselect(
            'Select features for Dealer Segmentation:',
            options= data_frame.columns,
            default=data_frame.columns
        )

        logging.info("Streamlit UI Ready")

    except Exception as e:
        logging.error("Error in Setting Streamlit UI")
        raise CustomException(e,sys)
    
if __name__=='__main__':
    main()