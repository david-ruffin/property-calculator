# Property Investment Calculator

A Streamlit web application for analyzing residential and commercial property investments. Calculate cash flow, ROI, and loan amortization with customizable parameters.

## Features

- **Property Type Selection**: Toggle between Residential and Commercial property analysis with completely different inputs and calculations
- **Residential Analysis**: Calculate monthly cash flow and annual ROI at different occupancy rates (75%, 90%, 100%)
- **Commercial Analysis**: NOI-based analysis with cash-on-cash returns, state-based tax/insurance lookups, and commercial loan terms
- **Excel-Driven Logic**: All commercial calculations sourced directly from `Commercial_Prop_Screening_Tool.xlsx` 
- **Loan Calculations**: Monthly principal & interest payments with amortization schedule
- **State-Specific Rates**: Tax and insurance rates for AZ, CA, IN, NV, TX, and MI
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

### Residential Parameters
- **Purchase Price**: Property purchase price
- **Down Payment %**: Percentage of purchase price paid upfront  
- **Interest Rate %**: Annual interest rate for the loan
- **Loan Term**: 15 or 30 year loan options
- **Expected Monthly Rent**: Projected rental income
- **State**: Select state for property tax calculations

### Commercial Parameters (from Excel)
- **State**: State for tax/insurance rate lookup (default: TX)
- **Purchase Price**: Commercial property purchase price (default: $1,970,000)
- **% Down**: Percentage of purchase price paid upfront (default: 30%)
- **Amount Down**: Calculated field with color coding (Green ≤$500K, Orange $500K-$750K, Red >$750K)
- **Annual Gross Rents**: Expected annual rental income (default: $152,195)
- **Vacancy Rate**: Expected vacancy percentage (default: 3%)
- **All Other Operating Expenses**: Additional annual operating costs (default: $5,000)
- **Loan Interest Rate**: Adjustable interest rate (default: 6.5%)
- **Loan Period**: Adjustable loan term from 1-30 years (default: 25 years)

## Investment Analysis

### Residential Analysis
- Monthly expenses breakdown (P&I, insurance, property tax, management, maintenance)
- Cash flow analysis at different occupancy scenarios (75%, 90%, 100%)
- Investment status recommendation based on 75% occupancy profitability
- First-year loan amortization schedule with balance visualization

### Commercial Analysis (Excel-Based Formulas)
- **Operating Expenses Table**: Shows both monthly and annual amounts for all expenses
  - Purchase Loan P&I, Property Insurance, Property Taxes, PM Fee, All Other Operating Expenses
- **NOI Calculation**: (Gross Rents × (1 - Vacancy Rate)) - Operating Expenses
- **Cash Flow Analysis**: NOI - Annual Debt Service  
- **Cash-on-Cash Return**: Annual Cash Flow ÷ Total Cash Down
- **Cash Down**: Color-coded display (Green ≤$500K, Orange $500K-$750K, Red >$750K)
  - Calculated as: Closing Costs (3% of purchase) + Amount Down
- **Deal Evaluation**: Color-coded results (Green = Cash Flow > 0, Red = Cash Flow ≤ 0)
- **Commercial Loan Terms**: User-adjustable period (1-30 years) and interest rate
- **State Lookup Tables**: 
  - Tax rates: AZ: 0.62%, CA: 1.25%, IN: 1.37%, NV: 0.65%, TX: 1.7%, MI: 3.21%
  - Insurance rates: AZ: 0.5%, CA: 1.25%, IN: 0.5%, NV: 0.5%, TX: 0.5%, MI: 0.5%

## Excel Source File
All commercial calculations are derived directly from: `Commercial_Prop_Screening_Tool.xlsx`
- Cell references maintained for formula accuracy
- State-based lookup tables implemented  
- NOI-focused analysis methodology