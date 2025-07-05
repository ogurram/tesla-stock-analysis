import pandas as pd
from typing import Dict

class VolumeAnalyzer:
    """Class for performing volume analysis"""
    
    def __init__(self, data: pd.DataFrame):
        """
        Initialize the volume analyzer
        
        Args:
            data: DataFrame containing stock data
        """
        self.data = data
        
    def calculate_volume_averages(self) -> Dict[str, pd.Series]:
        """
        Calculate volume moving averages
        
        Returns:
            Dictionary containing volume moving averages
        """
        volume_ma_20 = self.data['Volume'].rolling(window=20).mean()
        volume_ma_50 = self.data['Volume'].rolling(window=50).mean()
        return {
            'volume_ma_20': volume_ma_20,
            'volume_ma_50': volume_ma_50
        }
    
    def calculate_volume_change(self) -> pd.Series:
        """
        Calculate daily volume change
        
        Returns:
            Series containing daily volume changes
        """
        return self.data['Volume'].pct_change()
