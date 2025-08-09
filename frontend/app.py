import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import pickle
from pathlib import Path
import numpy as np

def load_analysis_results():
    """Load the analysis results from pickle file via UI"""
    try:
        # Get absolute path to results file
        results_path = Path(__file__).parent.parent / 'tesla_analysis_results.pkl'
        with open(results_path, 'rb') as f:
            results = pickle.load(f)
            
            # Validate results structure
            required_keys = ['price_trend', 'volume_analysis', 'technical_analysis',
                           'sentiment_analysis', 'seasonal_analysis', 'correlation_analysis']
            missing_keys = [key for key in required_keys if key not in results]
            if missing_keys:
                raise ValueError(f"Missing required analysis results: {missing_keys}")
                
            return results
    except FileNotFoundError:
        st.error("Analysis results not found. Please run the analysis first.")
        return None
    except Exception as e:
        st.error(f"Error loading analysis results: {str(e)}")
        return None

def create_price_trend_chart(results):
    """Create price trend chart with moving averages"""
    fig = go.Figure()
    
    # Add price data
    fig.add_trace(go.Scatter(
        x=results['price_trend']['moving_averages']['sma_20'].index,
        y=results['price_trend']['moving_averages']['sma_20'],
        name='SMA 20',
        line=dict(color='blue', width=2)
    ))
    
    fig.add_trace(go.Scatter(
        x=results['price_trend']['moving_averages']['sma_50'].index,
        y=results['price_trend']['moving_averages']['sma_50'],
        name='SMA 50',
        line=dict(color='orange', width=2)
    ))
    
    fig.update_layout(
        title='Price Trend Analysis',
        xaxis_title='Date',
        yaxis_title='Price',
        template='plotly_dark'
    )
    return fig

def create_volume_chart(results):
    """Create volume analysis chart"""
    fig = go.Figure()
    
    # Add volume data
    fig.add_trace(go.Bar(
        x=results['volume_analysis']['volume_averages']['volume_ma_20'].index,
        y=results['volume_analysis']['volume_averages']['volume_ma_20'],
        name='Volume MA 20',
        marker_color='blue'
    ))
    
    fig.update_layout(
        title='Volume Analysis',
        xaxis_title='Date',
        yaxis_title='Volume',
        template='plotly_dark'
    )
    return fig

def create_technical_indicators_chart(results):
    """Create technical indicators chart"""
    fig = go.Figure()
    
    # Add RSI
    fig.add_trace(go.Scatter(
        x=results['technical_analysis']['rsi'].index,
        y=results['technical_analysis']['rsi'],
        name='RSI',
        line=dict(color='green', width=2)
    ))
    
    # Add overbought/oversold levels
    fig.add_hline(y=70, line_dash="dash", line_color="red")
    fig.add_hline(y=30, line_dash="dash", line_color="green")
    
    fig.update_layout(
        title='Technical Indicators',
        xaxis_title='Date',
        yaxis_title='RSI',
        template='plotly_dark'
    )
    return fig

def create_sentiment_chart(results):
    """Create sentiment analysis chart"""
    fig = go.Figure()
    
    # Add returns
    fig.add_trace(go.Scatter(
        x=results['sentiment_analysis']['returns'].index,
        y=results['sentiment_analysis']['returns'],
        name='Returns',
        line=dict(color='purple', width=2)
    ))
    
    # Add volatility
    fig.add_trace(go.Scatter(
        x=results['sentiment_analysis']['volatility'].index,
        y=results['sentiment_analysis']['volatility'],
        name='Volatility',
        line=dict(color='orange', width=2)
    ))
    
    fig.update_layout(
        title='Market Sentiment',
        xaxis_title='Date',
        yaxis_title='Value',
        template='plotly_dark'
    )
    return fig

def create_correlation_heatmap(results):
    """Create correlation heatmap"""
    corr_matrix = results['correlation_analysis']['correlation_matrix']
    
    fig = go.Figure(data=go.Heatmap(
        z=corr_matrix.values,
        x=corr_matrix.columns,
        y=corr_matrix.index,
        colorscale='RdBu',
        zmin=-1,
        zmax=1
    ))
    
    fig.update_layout(
        title='Correlation Matrix',
        xaxis_title='Features',
        yaxis_title='Features',
        template='plotly_dark'
    )
    return fig

def main():
    st.set_page_config(
        page_title="Tesla Stock Analysis Dashboard",
        page_icon="📈",
        layout="wide"
    )
    
    st.title("Tesla Stock Analysis Dashboard")
    st.write("""
    A comprehensive dashboard for analyzing Tesla stock data.
    This dashboard provides various visualizations of stock price trends,
    volume analysis, technical indicators, market sentiment, and correlations.
    """)
    
    # Load analysis results
    results = load_analysis_results()
    if results is None:
        return
    
    # Create tabs for different analysis types
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["Price Trend", "Volume", "Technical", "Sentiment", "Correlation"])
    
    with tab1:
        st.plotly_chart(create_price_trend_chart(results), use_container_width=True)
    
    with tab2:
        st.plotly_chart(create_volume_chart(results), use_container_width=True)
    
    with tab3:
        st.plotly_chart(create_technical_indicators_chart(results), use_container_width=True)
    
    with tab4:
        st.plotly_chart(create_sentiment_chart(results), use_container_width=True)
    
    with tab5:
        st.plotly_chart(create_correlation_heatmap(results), use_container_width=True)

if __name__ == "__main__":
    main()
