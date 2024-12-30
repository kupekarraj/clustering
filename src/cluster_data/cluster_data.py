import sys
from sklearn.cluster import KMeans
from src.logger import logging
from src.exception import CustomException
from src.load_data.load_data import DataLoader
from src.preprocessing_data.preprocessing_data import DataPreprocessing
from src.transform_data.transform_data import DataTransform


class KMeansClustering:
    def __init__(self,transformed_data, original_data, cluster_size= 3):
        self.transformed_data= transformed_data
        self.original_data= original_data
        self.cluster_size= cluster_size

    def cluster_data(self):
        logging.info("Data Clustering Started")
        try:
            # Perform KMeans clustering with optimal clusters
            optimal_clusters = self.cluster_size  # Set based on the elbow graph
            kmeans = KMeans(n_clusters=optimal_clusters, random_state=42)
            clusters = kmeans.fit_predict(self.transformed_data)
            # Add cluster labels to the original data
            self.original_data['cluster'] = clusters
            print(self.original_data)
            return self.original_data

        except Exception as e:
            logging.error("Error in Data Clustering")
            raise CustomException(e,sys)
        
if __name__=='__main__':
    file_path= input("Enter the file path here: ").strip()
    data_loader= DataLoader(file_path)
    data_frame= data_loader.load_data()

    data_preprocess= DataPreprocessing(data_frame)
    data = data_preprocess.preprocess_data()

    data_transformation= DataTransform(data)
    data_transformed, original_data = data_transformation.transform_data()

    kmeans_clustering= KMeansClustering(data_transformed, original_data, cluster_size=3)
    kmeans_clusters= kmeans_clustering.cluster_data()
