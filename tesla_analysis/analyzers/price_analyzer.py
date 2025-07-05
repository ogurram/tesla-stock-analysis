import pandas as pd
from ta.trend import SMAIndicator, EMAIndicator
from typing import Dict

class PriceAnalyzer:
    """Class for performing price trend analysis"""
    
    def __init__(self, data: pd.DataFrame):
        """
        Initialize the price analyzer
        
        Args:
            data: DataFrame containing stock data
        """
        self.data = data
        
    def calculate_moving_averages(self) -> Dict[str, pd.Series]:
        """
        Calculate simple and exponential moving averages
        
        Returns:
            Dictionary containing SMA and EMA series
        """
        sma_20 = SMAIndicator(close=self.data['Close'], window=20).sma_indicator()
        sma_50 = SMAIndicator(close=self.data['Close'], window=50).sma_indicator()
        ema_20 = EMAIndicator(close=self.data['Close'], window=20).ema_indicator()
        ema_50 = EMAIndicator(close=self.data['Close'], window=50).ema_indicator()
        return {
            'sma_20': sma_20,
            'sma_50': sma_50,
            'ema_20': ema_20,
            'ema_50': ema_50
        }
    
    def calculate_price_change(self) -> pd.Series:
        """
        Calculate daily price change
        
        Returns:
            Series containing daily price changes
        """
        return self.data['Close'].pct_change()
