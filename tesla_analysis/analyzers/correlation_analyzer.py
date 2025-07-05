import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from typing import Dict, Any

class CorrelationAnalyzer:
    """Class for performing correlation analysis"""
    
    def __init__(self, data: pd.DataFrame):
        """
        Initialize the correlation analyzer
        
        Args:
            data: DataFrame containing stock data
        """
        self.data = data
        
    def calculate_correlation_matrix(self) -> pd.DataFrame:
        """
        Calculate correlation matrix between key indicators
        
        Returns:
            DataFrame containing correlation matrix
        """
        return self.data[['Close', 'Volume']].corr()
    
    def perform_pca(self) -> np.ndarray:
        """
        Perform Principal Component Analysis
        
        Returns:
            Array containing principal components
        """
        features = self.data[['Close', 'Volume']].dropna()
        scaler = StandardScaler()
        scaled_features = scaler.fit_transform(features)
        pca = PCA(n_components=2)
        return pca.fit_transform(scaled_features)
