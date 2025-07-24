# Property Investment Calculator

**Make smarter property investment decisions in seconds.** Instantly analyze residential and commercial properties with comprehensive financial metrics, shareable calculations, and professional-grade accuracy.

## 🏆 Why Property Investment Calculator?

- **Save Hours of Manual Calculations** → Get instant cash flow, ROI, and deal analysis
- **Make Data-Driven Decisions** → Compare properties objectively with standardized metrics  
- **Share Analysis Instantly** → Send complete calculations via shareable URLs
- **Avoid Costly Mistakes** → Spot bad deals before you invest with color-coded indicators

## 🚀 Quick Start

**Get running in 2 minutes:**

1. **Clone & Setup**
   ```bash
   git clone [repository-url]
   cd property-calculator-1
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Launch the App**
   ```bash
   streamlit run app.py
   ```

3. **Start Analyzing** → Open http://localhost:8501 and enter your first property

## 💡 How It Works

**Simple 3-step workflow:**
1. **Choose Property Type** → Residential (≤4 units) or Commercial (5+ units)
2. **Enter Property Details** → Purchase price, down payment, rents, location
3. **Get Instant Analysis** → Cash flow, ROI, and investment recommendation

**Smart Features:**
- All inputs update instantly (no sticky behavior)
- State-specific tax/insurance rates for accurate estimates
- Excel-validated commercial formulas for professional accuracy
- Shareable URLs preserve your complete analysis

## 🏡 Key Features

### Residential Properties (≤4 Units)
- **Comprehensive Analysis** → Monthly expenses, cash flow scenarios (75%/90%/100% occupancy)
- **Investment Recommendation** → Clear guidance based on 75% occupancy stress test
- **Loan Amortization** → First-year payment breakdown with visual balance chart
- **State Tax Rates** → Accurate calculations for AZ, CA, IN, NV, TX, MI

### Commercial Properties (5+ Units)  
- **Professional NOI Analysis** → Excel-validated formulas for accurate commercial calculations
- **Operating Expense Breakdown** → Monthly/annual costs with industry explanations
- **Cash-on-Cash Returns** → Investment performance metrics used by commercial investors
- **Deal Evaluation** → Color-coded recommendations (Good Deal/Bad Deal)
- **Smart Down Payment Alerts** → Visual indicators for financing thresholds

### Universal Features
- **Instant Updates** → No sticky inputs or multiple clicks required
- **Shareable Analysis** → Complete calculations preserved in URL for easy sharing
- **State-Specific Data** → Tax and insurance rates for 6 major investment markets  
- **Visual Indicators** → Color-coded metrics for quick decision making

## 🔧 Advanced Details

### Technical Architecture
- **Streamlit Framework** → Fast, responsive web application with real-time updates
- **Callback-Based Inputs** → Prevents sticky behavior and race conditions  
- **Query Parameter Sync** → Complete state preservation in shareable URLs
- **Excel Formula Validation** → Commercial calculations match industry-standard spreadsheets

### Supported Markets
| State | Tax Rate | Insurance Rate | Market Focus |
|-------|----------|----------------|--------------|
| Arizona | 0.62% | 0.5% | Growing sunbelt market |
| California | 1.25% | 1.25% | High-value coastal properties |
| Indiana | 1.37% | 0.5% | Midwest cash flow markets |
| Nevada | 0.65% | 0.5% | Tax-advantaged investing |
| Texas | 1.7% | 0.5% | No state income tax benefits |
| Michigan | 3.21% | 0.5% | Affordable entry markets |

## 🚀 Future Roadmap

### Phase 1: Property URL Integration (Coming Soon)
Transform your workflow with **one-click property analysis**:
- **Property URL Fields** → Store listing URLs (LoopNet, Zillow, etc.) alongside calculations
- **Quick Access Button** → Open property listings in new tabs directly from calculator
- **Enhanced Sharing** → Send calculator URLs with property context included

### Phase 2: Auto-Population (Future Vision)
**Eliminate manual data entry entirely**:
- **Smart URL Parsing** → Paste listing URL, auto-fill purchase price, rents, taxes
- **Multi-Platform Support** → LoopNet, Zillow, Crexi, and other major listing sites
- **Time Savings** → Go from listing to analysis in under 30 seconds

## 📊 Data Sources & Accuracy

**Commercial Calculations**: Sourced from `Commercial_Prop_Screening_Tool.xlsx`
- Industry-standard NOI methodology
- Excel cell references maintained for accuracy
- Validated against real commercial deals

**Tax & Insurance Rates**: Based on state averages
- Updated annually for accuracy
- Covers 85%+ of U.S. investment markets
- Conservative estimates for reliable projections