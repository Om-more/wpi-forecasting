# Wholesale Price Index (WPI) Forecasting Dashboard

## Overview
This project focuses on forecasting **monthly Wholesale Price Index (WPI)** trends for key agricultural commodities using **Facebook Prophet**.  
The goal is to understand long-term price movements and seasonal patterns, and to present these insights through a simple, interactive web application.

The project uses **real government data**, follows an **end-to-end machine learning workflow**, and is deployed as a **public Streamlit application**.

---

## Problem Context
Agricultural commodity prices are influenced by multiple factors such as:
- Harvest cycles  
- Supply and demand dynamics  
- Weather conditions  
- Policy interventions  

These factors introduce both **long-term trends** and **strong seasonality** in prices.  

**Objective:**
- Forecast future WPI values on a monthly basis  
- Capture underlying trends and seasonal behavior  
- Provide interpretable and accessible forecasts  

---

## Data Source
- **Provider:** Government of India (data.gov.in)  
- **Dataset:** Wholesale Price Index (Base Year 2011–12)  
- **Frequency:** Monthly  
- **Time Period:** 2012 – 2023 (latest available)  

**Note:**  
WPI data is published with a delay, and the most recent months may be provisional.  
The forecasting system generates predictions beyond the last available data point.

---

## Commodities Included
The dashboard currently supports forecasts for:
- Bajra  
- Moong  
- Masur  
- Cauliflower  

Each commodity is modeled independently to preserve its unique price behavior.

---

## Modeling Approach

### Algorithm
- **Model:** Facebook Prophet  

### Why Prophet?
Prophet is well suited for economic and price time series because it:
- Automatically models **trend** and **yearly seasonality**
- Handles missing values gracefully
- Produces **interpretable components**
- Requires minimal feature engineering

The model focuses on capturing **structural patterns**, not short-term shocks.

---

## Model Evaluation
Models were evaluated using time-aware train–validation splits.

**Metrics used:**
- Mean Absolute Percentage Error (MAPE)  
- Root Mean Squared Error (RMSE)  

Observed errors (typically around 15–20% MAPE) are reasonable for agricultural price indices, which are influenced by external and unpredictable factors.

---

## Application Features
The deployed dashboard provides:
- Commodity selection from the sidebar  
- Historical WPI visualization  
- Forecasts for the next 6–24 months  
- Confidence intervals to express uncertainty  
- Trend and seasonality decomposition  
- Downloadable forecast results  
- Clear indication of the last available data date  

The interface is designed to be simple, transparent, and easy to interpret.

---

## Deployment
- **Framework:** Streamlit  
- **Platform:** Streamlit Community Cloud  
- **Python Version:** 3.10  

The application is publicly accessible and automatically rebuilds when updates are pushed to GitHub.

 **Live Application:**  
 *(https://wpi-forecasting-bpqg5xhcikmz7dhsaymrjn.streamlit.app/)*

---

## Monitoring and Updates
- Forecasts extend beyond the most recent published data  
- When new monthly WPI data becomes available:
  - Forecasts can be compared with actual values  
  - Error metrics can be monitored over time  
  - Models can be retrained if performance degrades  

This mirrors real-world economic forecasting workflows where data availability lags behind real time.

---

## Tech Stack
- Python 3.10  
- Facebook Prophet  
- Pandas, NumPy  
- Matplotlib  
- Streamlit  


## Project Structure
