# Tesla Stock Analysis Dashboard

A comprehensive dashboard for analyzing Tesla stock data with features including:
- Price trend analysis (SMA, EMA)
- Volume analysis (Moving Averages)
- Technical indicators (RSI, Bollinger Bands)
- Market sentiment analysis
- Seasonal pattern analysis
- Correlation analysis

## Project Structure

```
tesla_analysis/
├── __init__.py
├── data_loader.py
├── analyzers/
│   ├── __init__.py
│   ├── price_analyzer.py
│   ├── volume_analyzer.py
│   ├── technical_analyzer.py
│   ├── sentiment_analyzer.py
│   ├── seasonal_analyzer.py
│   └── correlation_analyzer.py
└── main.py

input_folder/
└── Tesla_stock_data.csv

frontend/
└── app.py
```

## Setup Instructions

1. **Install Dependencies**
```bash
pip install -r requirements.txt
```

2. **Prepare Data**
   - Place your Tesla stock data CSV in the `input_folder/` directory
   - Ensure the CSV has the following columns: Date, Close, High, Low, Open, Volume
   - The Date column should be in YYYY-MM-DD format

3. **Run Analysis**
```bash
# Navigate to the project root directory
python -m tesla_analysis.main
```
This will:
- Load and preprocess the stock data
- Perform all analysis calculations
- Save results to tesla_analysis_results.pkl

4. **Start the Dashboard**
```bash
# Navigate to the frontend directory
cd frontend
streamlit run app.py
```

The dashboard will open automatically in your default browser. You'll see tabs for:
- Price Trend: Moving averages and price changes
- Volume: Volume analysis and trends
- Technical: RSI and Bollinger Bands
- Sentiment: Returns and volatility analysis
- Correlation: Correlation matrix and PCA

## Usage

1. **Analysis Phase**
   - The analysis script must be run first to generate results
   - Results are saved in tesla_analysis_results.pkl
   - The script validates data quality and handles errors

2. **Dashboard Phase**
   - Interactive charts with zoom, pan, and hover capabilities
   - Dark theme for better visualization
   - Error messages for missing or invalid data
   - Automatic loading of analysis results

## Troubleshooting

1. **Missing Data File**
   - Ensure Tesla_stock_data.csv is in the input_folder
   - Check the file format matches requirements

2. **Analysis Errors**
   - Check the console for error messages
   - Validate data quality (no missing values, correct data types)

3. **Dashboard Not Starting**
   - Ensure streamlit is installed
   - Check if port 8501 is available
   - Try running with different port: streamlit run app.py --server.port 8502

## Analysis Components

### 1. Price Trend Analysis
- Simple Moving Averages (20 and 50 day)
- Exponential Moving Averages (20 and 50 day)
- Price change calculations

### 2. Volume Analysis
- Volume moving averages
- Volume change calculations
- Volume trend analysis

### 3. Technical Analysis
- RSI (Relative Strength Index)
- Bollinger Bands
- Moving averages

### 4. Market Sentiment Analysis
- Daily returns calculation
- Volatility analysis
- Volume sentiment analysis

### 5. Seasonal Pattern Analysis
- Time series decomposition
- Trend analysis
- Seasonal component extraction

### 6. Correlation Analysis
- Correlation matrix
- Principal Component Analysis
- Feature relationships

## Output
The analysis results are stored in `tesla_analysis_results.pkl` file which can be loaded for further analysis or visualization.
