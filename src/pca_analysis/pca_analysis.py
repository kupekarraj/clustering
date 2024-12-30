import pandas as pd
import plotly.express as px
import sys
from sklearn.decomposition import PCA
from src.logger import logging
from src.exception import CustomException
from src.load_data.load_data import DataLoader
from src.preprocessing_data.preprocessing_data import DataPreprocessing
from src.transform_data.transform_data import DataTransform
from src.cluster_data.cluster_data import KMeansClustering

class PCA_Analysis:
    def __init__(self,transformed_data, clustered_output):
        self.transformed_data=transformed_data
        self.clustered_output=clustered_output
    
    def pca_viz(self):
        logging.info("PCA Analysis & Visualisation Started")
        try:
            # Reduce dimensions to 2D using PCA
            pca = PCA(n_components=2)
            pca_data = pca.fit_transform(self.transformed_data)

            # Create a DataFrame for the 2D visualization
            pca_df= pd.DataFrame(pca_data, columns=['PCA1','PCA2'])
            pca_df['Clusters']= self.clustered_output['cluster']
            pca_df['Trading_Name']= self.clustered_output['trading_name']
            pca_df['DID']= self.clustered_output['did']

            # Plot clusters in 2D using Plotly Express
            pca_output = px.scatter(
                pca_df, 
                x='PCA1', 
                y='PCA2',
                color='Clusters', 
                symbol='Clusters',
                hover_data={'Clusters': True,     # Show cluster number
                            'DID': True,          # Show dealer id
                            'Trading_Name': True, # Show trading_name
                            'PCA1': False,        # Hide PCA1 value
                            'PCA2': False         # Hide PCA2 value
                        },
                labels= {'Clusters': 'Cluster ID', 'DID': 'Dealer ID', 'Trading_Name': 'Dealer Name'},
                title='Dealer Segmentation'
            )

            # Update marker size for better visibility
            pca_output.update_traces(marker=dict(size=5))

            # Turn off the legend
            pca_output.update_layout(showlegend=False)

            # Save the plot to an HTML file
            # pca_output.write_html("pca_cluster.html")

            logging.info('PCA Analysis & Visualisation Completed')
            return pca_output

        except Exception as e:
            logging.error("Error in PCA Analysis & Visualisation")
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

    pca_components=PCA_Analysis(data_transformed,kmeans_clusters)
    pca_chart=pca_components.pca_viz()