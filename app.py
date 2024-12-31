import streamlit as st
import sys
import pandas as pd
import warnings
from src.logger import logging
from src.exception import CustomException
from src.load_data.load_data import DataLoader
from src.preprocessing_data.preprocessing_data import DataPreprocessing
from src.transform_data.transform_data import DataTransform
from src.cluster_data.cluster_data import KMeansClustering
from src.elbow_output.elbow_output import ElbowMethodViz
from src.pca_analysis.pca_analysis import PCA_Analysis
from src.streamlit_ui.st_data_filter import STDataFilter

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

        # Preprocessing of loaded data
        data_preprocess= DataPreprocessing(data_frame)
        data_preprocessed = data_preprocess.preprocess_data()

        # Feature selection for clustering
        selected_features = st.multiselect(
            'Select features for Dealer Segmentation:',
            options= data_preprocessed.columns,
            default=data_preprocessed.columns
        )

        selected_features_df= data_preprocessed[selected_features]

        # Data filtering section
        st.sidebar.subheader('Filter Options')

        st_data_filter= STDataFilter(selected_features_df)
        filtered_data= st_data_filter.st_filter_options()

        st.write(f'There are a total of {len(filtered_data)} records available for cluster analysis',filtered_data)

        # Elbow Chart for Optimal Number of clusters
        num_clusters = st.slider('Select the cluster size based on the Elbow Chart below for optimal accuracy:', 2, 10, 3)

        if st.button("Apply Clustering"):
            if selected_features and not filtered_data.empty:
                st.subheader("Cluster Analysis")
                # Data Transformation
                data_transformation= DataTransform(filtered_data)
                data_transformed, original_data = data_transformation.transform_data()

                data_clusters=ElbowMethodViz(data_transformed)
                elbow_output=data_clusters.show_elbow_output()

                # Display elbow chart
                st.plotly_chart(elbow_output)

                # K Means Clustering Performance
                kmeans_clustering= KMeansClustering(data_transformed, original_data, cluster_size=num_clusters)
                kmeans_clusters= kmeans_clustering.cluster_data()
                st.write(f'Clustered Analysis available to view:',kmeans_clusters)

                # PCA Visualisation
                pca_components=PCA_Analysis(data_transformed,kmeans_clusters)
                pca_chart=pca_components.pca_viz()

                # Display PCA 2-D chart
                st.plotly_chart(pca_chart)

            else:
                st.warning('Please select at least one feature and ensure the filtered dataset is not empty.')

        logging.info("Streamlit UI Ready")

    except Exception as e:
        logging.error("Error in Setting Streamlit UI")
        raise CustomException(e,sys)
    
if __name__=='__main__':
    main()