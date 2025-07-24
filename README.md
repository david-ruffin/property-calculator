# Property Investment Calculator

A Streamlit web application for analyzing residential and commercial property investments. Calculate cash flow, ROI, and loan amortization with customizable parameters.

## Features

- **Property Type Selection**: Toggle between Residential and Commercial property analysis with completely different inputs and calculations
  - Clear explanation: "Residential: 4 units or less | Commercial: 5 units or more"
  - Property type preserved in shareable URLs
- **Residential Analysis**: Calculate monthly cash flow and annual ROI at different occupancy rates (75%, 90%, 100%)
- **Commercial Analysis**: NOI-based analysis with cash-on-cash returns, state-based tax/insurance lookups, and commercial loan terms
- **Excel-Driven Logic**: All commercial calculations sourced directly from `Commercial_Prop_Screening_Tool.xlsx` 
- **Interactive Help Text**: Hover tooltips on key input fields provide contextual guidance
- **Color-Coded Indicators**: Visual feedback for Amount Down thresholds and Annual Cash Flow status
- **Loan Calculations**: Monthly principal & interest payments with user-adjustable terms (1-30 years)
- **State-Specific Rates**: Tax and insurance rates for AZ, CA, IN, NV, TX, and MI (defaults to California)
- **Visual Charts**: Loan balance over time visualization for residential properties
- **Responsive Input System**: All inputs update immediately without requiring multiple clicks or Enter presses
- **Shareable Links**: All parameters including property type are preserved in the URL for easy sharing and bookmarking

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
- **State**: Select state for property tax calculations (defaults to California)

### Commercial Parameters (from Excel)
- **State**: State for tax/insurance rate lookup (defaults to California, located in Location section)
- **Purchase Price**: Commercial property purchase price (default: $1,970,000) - with hover text explaining "Purchase Price or Amount we want to offer"
- **% Down**: Percentage of purchase price paid upfront (default: 30%) - with detailed hover explanation about loan requirements
- **Amount Down**: Calculated field with color coding (Green ≤$500K, Orange $500K-$750K, Red >$750K)
- **Estimated Closing Costs**: Automatically calculated as 3% of purchase price
- **Annual Gross Rents**: Expected annual rental income (default: $152,195) - with hover text "Typically provided in the listing on LoopNet, etc."
- **Annual NOI from Listing**: NOI value from property listing (default: $106,548)
- **Vacancy Rate**: Expected vacancy percentage (default: 3%)
- **All Other Operating Expenses**: Additional annual operating costs (default: $5,000)
- **Loan Interest Rate**: User-adjustable interest rate (default: 6.5%)
- **Loan Period**: User-adjustable loan term from 1-30 years (default: 25 years)

## Investment Analysis

### Residential Analysis
- Monthly expenses breakdown (P&I, insurance, property tax, management, maintenance)
- Cash flow analysis at different occupancy scenarios (75%, 90%, 100%)
- Investment status recommendation based on 75% occupancy profitability
- First-year loan amortization schedule with balance visualization

### Commercial Analysis (Excel-Based Formulas)
- **Operating Expenses Table**: Shows both monthly and annual amounts for all expenses
  - Purchase Loan P&I (showing monthly payment), Property Insurance Insurance, Property Taxes, PM Fee, All Other Operating Expenses
  - Includes expandable "Expense Notes" section with explanations for key expenses
- **Investment Analysis Table**: Displays key financial metrics in aligned format
  - Annual Gross Rents, Adjusted Gross Income, Annual NOI (Estimated), Annual Debt Service, Annual Cash Flow, Cash-on-Cash Return, Cash Down
- **NOI Calculation**: (Gross Rents × (1 - Vacancy Rate)) - Operating Expenses
  - Formula matches Excel exactly: =(K4*(1-L5))-SUM(J8:J11)
- **Cash Flow Analysis**: NOI - Annual Debt Service  
- **Cash-on-Cash Return**: Annual Cash Flow ÷ Total Cash Down
- **Annual Cash Flow**: Displayed with proper metric sizing and color indicators (Positive/Negative cash flow)
- **Cash Down**: Integrated into Investment Analysis table
  - Calculated as: Closing Costs (3% of purchase) + Amount Down
- **Deal Evaluation**: Color-coded results (Green = GOOD DEAL for positive cash flow, Red = BAD DEAL for negative)
- **Investment Summary**: Two-column layout with all key metrics including Purchase Price, Down Payment, Closing Costs, Total Cash Investment, Loan Amount, Monthly Payment, and color-coded Annual Cash Flow
- **State Lookup Tables**: 
  - Tax rates: AZ: 0.62%, CA: 1.25%, IN: 1.37%, NV: 0.65%, TX: 1.7%, MI: 3.21%
  - Insurance rates: AZ: 0.5%, CA: 1.25%, IN: 0.5%, NV: 0.5%, TX: 0.5%, MI: 0.5%

## Technical Features

### Input System
- **Callback-Based Updates**: All inputs use `on_change` callbacks to prevent race conditions
- **Immediate Response**: No sticky behavior - inputs update instantly without multiple clicks
- **Query Parameter Sync**: All values automatically saved to URL for sharing
- **Session State Management**: Reliable state persistence across reruns

### URL Sharing
- **Complete State Preservation**: Property type, all input values, and state selections preserved in URLs
- **Cross-Platform Compatibility**: Shared links work across different devices and browsers
- **Bookmark-Friendly**: All calculator states can be bookmarked for future reference

## Future Roadmap

### Phase 1: Property URL Integration (Next)
- **Property URL Field**: Add URL input fields for both residential and commercial properties
- **Listing URL Storage**: Property listing URLs (LoopNet, Zillow, etc.) preserved in query parameters
- **Load Property Details Button**: One-click button to open property listings in new tabs
- **Enhanced URL Sharing**: Shared calculator URLs will include property listing URLs for complete context

### Phase 2: Auto-Population (Future)
- **Smart Data Extraction**: Enter a property listing URL to automatically populate calculator fields
- **Supported Data Points**: Purchase price, annual rent/income, property taxes, and other listing details
- **Multi-Platform Support**: Integration with major listing platforms (LoopNet, Zillow, commercial sites)
- **Time-Saving Workflow**: Eliminate manual data entry by pulling information directly from listings

## Excel Source File
All commercial calculations are derived directly from: `Commercial_Prop_Screening_Tool.xlsx`
- Cell references maintained for formula accuracy
- State-based lookup tables implemented  
- NOI-focused analysis methodology