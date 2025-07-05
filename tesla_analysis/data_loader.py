import pandas as pd
import numpy as np
from typing import Optional

class StockDataLoader:
    """Class responsible for loading and preprocessing stock data"""
    
    def __init__(self, data_path: str):
        """
        Initialize the data loader
        
        Args:
            data_path: Path to the stock data CSV file
        """
        self.data_path = data_path
        self.data = None
        
    def load_data(self) -> pd.DataFrame:
        """
        Load and preprocess stock data from CSV file
        
        Returns:
            DataFrame containing preprocessed stock data
        """
        try:
            self.data = pd.read_csv(self.data_path)
            self._preprocess_data()
            return self.data
        except FileNotFoundError:
            raise FileNotFoundError(f"Data file not found at: {self.data_path}")
        except Exception as e:
            raise Exception(f"Error loading data: {str(e)}")
    
    def _preprocess_data(self):
        """Private method to preprocess the data"""
        if self.data is not None:
            self.data['Date'] = pd.to_datetime(self.data['Date'])
            self.data.set_index('Date', inplace=True)
            self._validate_data()
    
    def _validate_data(self):
        """Validate the data structure"""
        required_columns = ['Close', 'High', 'Low', 'Open', 'Volume']
        missing_cols = [col for col in required_columns if col not in self.data.columns]
        if missing_cols:
            raise ValueError(f"Missing required columns: {missing_cols}")
            
        # Check for missing or invalid data points
        if self.data.isna().any().any():
            raise ValueError("Data contains missing values")
            
        # Check for non-numeric values
        for col in required_columns:
            if not pd.api.types.is_numeric_dtype(self.data[col]):
                raise ValueError(f"Column {col} contains non-numeric values")
            
        # Check for zero or negative volumes
        if (self.data['Volume'] <= 0).any():
            raise ValueError("Volume data contains zero or negative values")
    
    def get_data(self) -> Optional[pd.DataFrame]:
        """Get the preprocessed data"""
        return self.data
