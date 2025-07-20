# Property Investment Calculator

A Streamlit web application for analyzing residential and commercial property investments. Calculate cash flow, ROI, and loan amortization with customizable parameters.

## Features

- **Property Type Selection**: Toggle between Residential and Commercial property analysis
- **Investment Analysis**: Calculate monthly cash flow and annual ROI at different occupancy rates (75%, 90%, 100%)
- **Loan Calculations**: Monthly principal & interest payments with amortization schedule
- **State-Specific Tax Rates**: Support for AZ, CA, IN, NV, TX, and MI
- **Interactive Inputs**: Purchase price, down payment %, interest rate %, loan term, and expected rent
- **Visual Charts**: Loan balance over time visualization
- **Shareable Links**: All parameters are preserved in the URL for easy sharing and bookmarking

## Installation

1. Clone the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment: `source venv/bin/activate` (Linux/Mac) or `venv\Scripts\activate` (Windows)
4. Install dependencies: `pip install -r requirements.txt`

## Usage

Run the application:
```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## Parameters

- **Purchase Price**: Property purchase price
- **Down Payment %**: Percentage of purchase price paid upfront
- **Interest Rate %**: Annual interest rate for the loan
- **Loan Term**: 15 or 30 year loan options
- **Expected Monthly Rent**: Projected rental income
- **State**: Select state for property tax calculations

## Investment Analysis

The calculator provides:
- Monthly expenses breakdown (P&I, insurance, property tax, management, maintenance)
- Cash flow analysis at different occupancy scenarios
- Investment status recommendation based on 75% occupancy profitability
- First-year loan amortization schedule with balance visualization

## Future Development

- **Commercial Property Analysis**: Future editions will include commercial property assessment features with different criteria and calculations specific to commercial real estate investments
- The current toggle button is positioned for this upcoming functionality