import pandas as pd
from statsmodels.tsa.seasonal import seasonal_decompose
from typing import Dict

class SeasonalAnalyzer:
    """Class for performing seasonal pattern analysis"""
    
    def __init__(self, data: pd.DataFrame):
        """
        Initialize the seasonal analyzer
        
        Args:
            data: DataFrame containing stock data
        """
        self.data = data
        
    def decompose_time_series(self) -> Dict[str, pd.Series]:
        """
        Decompose time series into trend, seasonal, and residual components
        
        Returns:
            Dictionary containing decomposed components
        """
        decomposition = seasonal_decompose(
            self.data['Close'], 
            model='additive', 
            period=252
        )
        return {
            'trend': decomposition.trend,
            'seasonal': decomposition.seasonal,
            'residual': decomposition.resid
        }
