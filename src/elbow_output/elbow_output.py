import sys
from src.logger import logging
from src.exception import CustomException
from sklearn.cluster import KMeans
import plotly.express as px
from src.load_data.load_data import DataLoader
from src.preprocessing_data.preprocessing_data import DataPreprocessing
from src.transform_data.transform_data import DataTransform

class ElbowMethodViz:
    def __init__(self, transformed_data):
        self.transformed_data= transformed_data

    def show_elbow_output(self):
        logging.info("Cluster Size Analysis Started Using Elbow Method")
        try:
            # Determine optimal number of clusters (Elbow Method)
            inertia = []
            for k in range(1, 10):
                kmeans = KMeans(n_clusters=k, random_state=42)
                kmeans.fit(self.transformed_data)
                inertia.append(kmeans.inertia_)
            
            # Create the Elbow graph using Plotly Express
            elbow_output = px.line(x=range(1, 10), y=inertia, title='Elbow Method', labels={'x': 'Number of Clusters', 'y': 'Inertia'})
            elbow_output.update_traces(mode='markers+lines')  # Adding markers to the line plot
            
            return elbow_output

        except Exception as e:
            logging.error("Error in CLuster Size Analysis Using Elbow Method")
            raise CustomException(e,sys)
        
if __name__=='__main__':
    file_path= input("Enter the file path here: ").strip()
    data_loader= DataLoader(file_path)
    data_frame= data_loader.load_data()

    data_preprocess= DataPreprocessing(data_frame)
    data = data_preprocess.preprocess_data()

    data_transformation= DataTransform(data)
    data_transformed, original_data = data_transformation.transform_data()

    data_clusters=ElbowMethodViz(data_transformed)
    data_clusters.show_elbow_output()
