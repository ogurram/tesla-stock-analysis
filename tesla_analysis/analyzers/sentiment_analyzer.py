import pandas as pd
from typing import Dict

class SentimentAnalyzer:
    """Class for performing market sentiment analysis"""
    
    def __init__(self, data: pd.DataFrame):
        """
        Initialize the sentiment analyzer
        
        Args:
            data: DataFrame containing stock data
        """
        self.data = data
        
    def calculate_returns(self) -> pd.Series:
        """
        Calculate daily returns
        
        Returns:
            Series containing daily returns
        """
        return self.data['Close'].pct_change()
    
    def calculate_volatility(self) -> pd.Series:
        """
        Calculate rolling volatility
        
        Returns:
            Series containing rolling volatility
        """
        returns = self.data['Close'].pct_change()
        return returns.rolling(window=20).std()
    
    def analyze_volume_sentiment(self) -> Dict[str, pd.Series]:
        """
        Analyze volume sentiment based on price changes
        
        Returns:
            Dictionary containing positive and negative volume series
        """
        positive_volume = self.data[self.data['Close'].pct_change() > 0]['Volume']
        negative_volume = self.data[self.data['Close'].pct_change() < 0]['Volume']
        return {
            'positive_volume': positive_volume,
            'negative_volume': negative_volume
        }
