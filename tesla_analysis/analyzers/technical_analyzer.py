import pandas as pd
from ta.momentum import RSIIndicator
from typing import Dict

class TechnicalAnalyzer:
    """Class for performing technical analysis"""
    
    def __init__(self, data: pd.DataFrame):
        """
        Initialize the technical analyzer
        
        Args:
            data: DataFrame containing stock data
        """
        self.data = data
        
    def calculate_rsi(self) -> pd.Series:
        """
        Calculate Relative Strength Index
        
        Returns:
            Series containing RSI values
        """
        return RSIIndicator(close=self.data['Close'], window=14).rsi()
    
    def calculate_bollinger_bands(self) -> Dict[str, pd.Series]:
        """
        Calculate Bollinger Bands
        
        Returns:
            Dictionary containing Bollinger Bands
        """
        rolling_std = self.data['Close'].rolling(window=20).std()
        upper_band = self.data['Close'].rolling(window=20).mean() + (rolling_std * 2)
        lower_band = self.data['Close'].rolling(window=20).mean() - (rolling_std * 2)
        return {
            'upper': upper_band,
            'lower': lower_band
        }
