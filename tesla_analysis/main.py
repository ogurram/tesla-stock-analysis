from .data_loader import StockDataLoader
from .analyzers import (
    PriceAnalyzer,
    VolumeAnalyzer,
    TechnicalAnalyzer,
    SentimentAnalyzer,
    SeasonalAnalyzer,
    CorrelationAnalyzer
)
import pickle
from typing import Dict, Any

class TeslaStockAnalysis:
    """Main class that coordinates all components analysis"""
    
    def __init__(self, data_path: str):
        """
        Initialize the analysis system
        
        Args:
            data_path: Path to the stock data CSV file
        """
        self.data_path = data_path
        self.data_loader = StockDataLoader(data_path)
        self.data = None
        self.analysis_results = {}
        
    def run_analysis(self) -> Dict[str, Any]:
        """
        Run complete analysis pipeline
        
        Returns:
            Dictionary containing all analysis results
        """
        try:
            # Load and preprocess data
            self.data = self.data_loader.load_data()
            
            # Initialize analyzers
            analyzers = [
                ('price_trend', PriceAnalyzer(self.data)),
                ('volume_analysis', VolumeAnalyzer(self.data)),
                ('technical_analysis', TechnicalAnalyzer(self.data)),
                ('sentiment_analysis', SentimentAnalyzer(self.data)),
                ('seasonal_analysis', SeasonalAnalyzer(self.data)),
                ('correlation_analysis', CorrelationAnalyzer(self.data))
            ]
            
            # Perform analysis with error handling for each analyzer
            self.analysis_results = {}
            for analysis_type, analyzer in analyzers:
                try:
                    if analysis_type == 'price_trend':
                        self.analysis_results[analysis_type] = {
                            'moving_averages': analyzer.calculate_moving_averages(),
                            'price_change': analyzer.calculate_price_change()
                        }
                    elif analysis_type == 'volume_analysis':
                        self.analysis_results[analysis_type] = {
                            'volume_averages': analyzer.calculate_volume_averages(),
                            'volume_change': analyzer.calculate_volume_change()
                        }
                    elif analysis_type == 'technical_analysis':
                        self.analysis_results[analysis_type] = {
                            'rsi': analyzer.calculate_rsi(),
                            'bollinger_bands': analyzer.calculate_bollinger_bands()
                        }
                    elif analysis_type == 'sentiment_analysis':
                        self.analysis_results[analysis_type] = {
                            'returns': analyzer.calculate_returns(),
                            'volatility': analyzer.calculate_volatility(),
                            'volume_sentiment': analyzer.analyze_volume_sentiment()
                        }
                    elif analysis_type == 'seasonal_analysis':
                        self.analysis_results[analysis_type] = analyzer.decompose_time_series()
                    elif analysis_type == 'correlation_analysis':
                        self.analysis_results[analysis_type] = {
                            'correlation_matrix': analyzer.calculate_correlation_matrix(),
                            'pca_components': analyzer.perform_pca()
                        }
                except Exception as e:
                    self.analysis_results[analysis_type] = {
                        'error': f"Error in {analysis_type}: {str(e)}"
                    }
            
            # Save results
            self._save_results()
            return self.analysis_results
            
        except Exception as e:
            raise Exception(f"Error running analysis: {str(e)}")
    
    def _save_results(self):
        """Save analysis results to file"""
        with open('tesla_analysis_results.pkl', 'wb') as f:
            pickle.dump(self.analysis_results, f)

# Example usage when run as a script
if __name__ == "__main__":
    from pathlib import Path
    
    # Get the absolute path to the data file
    data_path = str(Path(__file__).parent.parent / 'input_folder' / 'Tesla_stock_data.csv')
    
    # Run analysis
    analyzer = TeslaStockAnalysis(data_path)
    results = analyzer.run_analysis()
    print("Analysis complete. Results saved to tesla_analysis_results.pkl")
