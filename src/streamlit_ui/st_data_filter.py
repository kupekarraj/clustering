import pandas as pd
import sys
import streamlit as st
from src.logger import logging
from src.exception import CustomException

class STDataFilter:
    def __init__(self,selected_features):
        self.selected_features=selected_features

    def st_filter_options(self):
        logging.info("Streamlit Data Filter Options Started")

        try:
            # Loop through columns and create filters
            for column in self.selected_features.columns:
                if self.selected_features[column].dtype == 'object':
                    # Create a dropdown filter for categorical columns
                    unique_values = self.selected_features[column].unique()
                    selected_values = st.sidebar.multiselect(
                        f'Select values for {column}:',
                        options=unique_values,
                        default=unique_values
                    )
                    # Filter DataFrame by selected values
                    self.selected_features = self.selected_features[self.selected_features[column].isin(selected_values)]

                elif self.selected_features[column].dtype in ['int64', 'float64']:
                    # Create a slider filter for numeric columns
                    min_val = float(self.selected_features[column].min())
                    max_val = float(self.selected_features[column].max())
                    range_min, range_max = st.sidebar.slider(
                        f'Select the range for {column}:',
                        min_value=min_val,
                        max_value=max_val,
                        value=(min_val, max_val)
                    )
                    # Filter DataFrame by selected range
                    self.selected_features = self.selected_features[
                        (self.selected_features[column] >= range_min) & 
                        (self.selected_features[column] <= range_max)
                    ]
            logging.info("Streamlit Data Filter Options Completed")
            return self.selected_features
        except Exception as e:
            logging.error("Error in Streamlit Data Filter Options")
            raise CustomException(e,sys)