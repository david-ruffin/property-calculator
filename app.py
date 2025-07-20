import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")
st.title("Property Investment Calculator")

# Property type selection
property_type = st.radio("Property Type", ["Residential", "Commercial"], horizontal=True)

if property_type == "Residential":
    # Initialize query params with defaults if not present
    if "purchase_price" not in st.query_params:
        st.query_params["purchase_price"] = "650000"
    if "down_payment" not in st.query_params:
        st.query_params["down_payment"] = "20"
    if "interest_rate" not in st.query_params:
        st.query_params["interest_rate"] = "2.0"
    if "loan_years" not in st.query_params:
        st.query_params["loan_years"] = "15"
    if "monthly_rent" not in st.query_params:
        st.query_params["monthly_rent"] = "5000"
    if "state" not in st.query_params:
        st.query_params["state"] = "TX"

    # Sidebar inputs
    with st.sidebar:
        st.header("Property Details")
        purchase_price = st.number_input("Purchase Price", value=int(st.query_params["purchase_price"]), step=None, format="%d")
        if purchase_price != int(st.query_params["purchase_price"]):
            st.query_params["purchase_price"] = str(purchase_price)
        
        # Display formatted purchase price
        st.write(f"**Purchase Price:** ${purchase_price:,.0f}")
        # Down Payment
        down_payment_value = st.number_input("Down Payment %", value=int(st.query_params["down_payment"]), min_value=0, max_value=100, step=1)
        
        # Update query params
        if down_payment_value != int(st.query_params["down_payment"]):
            st.query_params["down_payment"] = str(down_payment_value)
        
        down_payment_pct = down_payment_value / 100
        
        # Calculate and display the actual down payment amount
        amount_down = purchase_price * down_payment_pct
        st.metric("Down Payment Amount", f"${amount_down:,.2f}")
        
        # Interest Rate
        interest_rate_value = st.number_input("Interest Rate %", value=float(st.query_params["interest_rate"]), min_value=0.0, max_value=10.0, step=0.1)
        
        # Update query params
        if abs(interest_rate_value - float(st.query_params["interest_rate"])) > 0.01:
            st.query_params["interest_rate"] = str(interest_rate_value)
        
        interest_rate = interest_rate_value / 100
        loan_years = st.selectbox("Loan Term (Years)", [15, 30], index=0 if st.query_params["loan_years"] == "15" else 1)
        if loan_years != int(st.query_params["loan_years"]):
            st.query_params["loan_years"] = str(loan_years)
            
        monthly_rent = st.number_input("Expected Monthly Rent", value=int(st.query_params["monthly_rent"]), step=100)
        if monthly_rent != int(st.query_params["monthly_rent"]):
            st.query_params["monthly_rent"] = str(monthly_rent)
        
        st.header("Location")
        states = ["AZ", "CA", "IN", "NV", "TX", "MI"]
        state = st.selectbox("State", states, index=states.index(st.query_params["state"]))
        if state != st.query_params["state"]:
            st.query_params["state"] = state
        
        TAX_RATES = {
            "AZ": 0.0062,
            "CA": 0.0125,
            "IN": 0.0137,
            "NV": 0.0065,
            "TX": 0.0170,
            "MI": 0.0321
        }
        
        # Display the tax rate for the selected state (converted to a percentage)
        selected_tax_rate = TAX_RATES[state]
        st.metric("Tax Rate", f"{selected_tax_rate * 100:.2f}%")

    # Calculations
    loan_amount = purchase_price * (1 - down_payment_pct)
    monthly_rate = interest_rate / 12
    num_payments = loan_years * 12
    
    # Monthly Principal & Interest Payment
    monthly_pi = loan_amount * (monthly_rate * (1 + monthly_rate) ** num_payments) / ((1 + monthly_rate) ** num_payments - 1)
    
    # Other monthly costs
    monthly_insurance = (purchase_price * 0.01) / 12
    monthly_tax = (purchase_price * TAX_RATES[state]) / 12
    pm_fee = monthly_rent * 0.10
    maintenance = 250
    
    total_monthly = monthly_pi + monthly_insurance + monthly_tax + pm_fee + maintenance
    
    # Cash flow analysis
    occupancy_rates = [0.75, 0.90, 1.0]
    cash_flows = []
    annual_returns = []
    
    for rate in occupancy_rates:
        monthly_income = monthly_rent * rate
        cash_flow = monthly_income - total_monthly
        annual_return = (cash_flow * 12) / (purchase_price * down_payment_pct) * 100
        cash_flows.append(cash_flow)
        annual_returns.append(annual_return)

    # Display results
    col1, col2 = st.columns(2)
    
    with col1:
        st.header("Monthly Expenses")
        expenses_df = pd.DataFrame({
            "Expense": ["Principal & Interest", "Insurance", "Property Tax", "Property Management", "Maintenance"],
            "Amount": [monthly_pi, monthly_insurance, monthly_tax, pm_fee, maintenance]
        })
        st.dataframe(expenses_df.style.format({"Amount": "${:,.2f}"}), hide_index=True)
    
    with col2:
        st.header("Investment Returns")
        returns_df = pd.DataFrame({
            "Scenario": ["75% Occupancy", "90% Occupancy", "100% Occupancy"],
            "Monthly Cash Flow": cash_flows,
            "Annual ROI": annual_returns
        })
        
        def color_negative_red(val):
            color = 'red' if val < 0 else 'green'
            return f'color: {color}'
        
        st.dataframe(
            returns_df.style
            .format({
                "Monthly Cash Flow": "${:,.2f}", 
                "Annual ROI": "{:.1f}%"
            })
            .map(color_negative_red, subset=["Monthly Cash Flow", "Annual ROI"]),
            hide_index=True
        )
    
    # Investment status
    st.header("Investment Status")
    if cash_flows[0] > 0:  # Profitable at 75% occupancy
        st.success("✅ Good Investment: Profitable even at 75% occupancy")
    else:
        st.error("❌ High Risk: Not profitable at 75% occupancy")
    
    # Amortization Schedule
    st.header("Amortization Schedule")
    schedule = []
    balance = loan_amount
    
    for payment in range(1, 13):  # First year only
        interest_payment = balance * monthly_rate
        principal_payment = monthly_pi - interest_payment
        balance = balance - principal_payment
        
        schedule.append({
            "Payment": payment,
            "Principal": principal_payment,
            "Interest": interest_payment,
            "Balance": balance
        })
    
    schedule_df = pd.DataFrame(schedule)
    st.dataframe(
        schedule_df.style.format({
            "Principal": "${:,.2f}",
            "Interest": "${:,.2f}",
            "Balance": "${:,.2f}"
        }),
        hide_index=True
    )
    
    # Balance Over Time chart
    fig = px.line(
        schedule_df, 
        x="Payment", 
        y="Balance",
        title="Loan Balance Over Time"
    )
    st.plotly_chart(fig, use_container_width=True)

elif property_type == "Commercial":
    # Commercial property logic
    
    # Initialize commercial query params with Excel defaults
    if "comm_state" not in st.query_params:
        st.query_params["comm_state"] = "TX"
    if "comm_purchase_price" not in st.query_params:
        st.query_params["comm_purchase_price"] = "1970000"
    if "comm_down_payment" not in st.query_params:
        st.query_params["comm_down_payment"] = "30"
    if "comm_annual_gross_rents" not in st.query_params:
        st.query_params["comm_annual_gross_rents"] = "152195"
    if "comm_annual_noi_listing" not in st.query_params:
        st.query_params["comm_annual_noi_listing"] = "106548"
    if "comm_vacancy_rate" not in st.query_params:
        st.query_params["comm_vacancy_rate"] = "3"
    if "comm_other_expenses" not in st.query_params:
        st.query_params["comm_other_expenses"] = "5000"
    if "comm_loan_years" not in st.query_params:
        st.query_params["comm_loan_years"] = "25"
    
    # Commercial tax and insurance rates
    COMMERCIAL_TAX_RATES = {
        "AZ": 0.0062,
        "CA": 0.0125,
        "IN": 0.0137,
        "NV": 0.0065,
        "TX": 0.0170,
        "MI": 0.0321
    }
    
    COMMERCIAL_INSURANCE_RATES = {
        "AZ": 0.005,
        "CA": 0.005,
        "IN": 0.005,
        "NV": 0.005,
        "TX": 0.005,
        "MI": 0.005
    }
    
    # Commercial sidebar inputs
    with st.sidebar:
        st.header("Commercial Property Details")
        
        # State selection
        states = ["AZ", "CA", "IN", "NV", "TX", "MI"]
        comm_state = st.selectbox("State", states, index=states.index(st.query_params["comm_state"]))
        if comm_state != st.query_params["comm_state"]:
            st.query_params["comm_state"] = comm_state
        
        # Purchase Price
        comm_purchase_price = st.number_input("Purchase Price", value=int(st.query_params["comm_purchase_price"]), step=None, format="%d")
        if comm_purchase_price != int(st.query_params["comm_purchase_price"]):
            st.query_params["comm_purchase_price"] = str(comm_purchase_price)
        
        st.write(f"**Purchase Price:** ${comm_purchase_price:,.0f}")
        
        # Down Payment %
        comm_down_payment_pct = st.number_input("% Down Payment", value=int(st.query_params["comm_down_payment"]), min_value=0, max_value=100, step=1)
        if comm_down_payment_pct != int(st.query_params["comm_down_payment"]):
            st.query_params["comm_down_payment"] = str(comm_down_payment_pct)
        
        # Calculate Amount Down with color coding
        amount_down = comm_purchase_price * (comm_down_payment_pct / 100)
        
        if amount_down <= 500000:
            st.markdown(f"**Amount Down:** :green[${amount_down:,.0f}]")
        elif amount_down <= 750000:
            st.markdown(f"**Amount Down:** :orange[${amount_down:,.0f}]")
        else:
            st.markdown(f"**Amount Down:** :red[${amount_down:,.0f}]")
        
        # Annual Gross Rents
        comm_annual_gross_rents = st.number_input("Annual Gross Rents", value=int(st.query_params["comm_annual_gross_rents"]), step=1000)
        if comm_annual_gross_rents != int(st.query_params["comm_annual_gross_rents"]):
            st.query_params["comm_annual_gross_rents"] = str(comm_annual_gross_rents)
        
        # Annual NOI from Listing
        comm_annual_noi_listing = st.number_input("Annual NOI from Listing", value=int(st.query_params["comm_annual_noi_listing"]), step=1000)
        if comm_annual_noi_listing != int(st.query_params["comm_annual_noi_listing"]):
            st.query_params["comm_annual_noi_listing"] = str(comm_annual_noi_listing)
        
        # Vacancy Rate
        comm_vacancy_rate = st.number_input("Vacancy Rate %", value=int(st.query_params["comm_vacancy_rate"]), min_value=0, max_value=50, step=1)
        if comm_vacancy_rate != int(st.query_params["comm_vacancy_rate"]):
            st.query_params["comm_vacancy_rate"] = str(comm_vacancy_rate)
        
        # All Other Operating Expenses
        comm_other_expenses = st.number_input("All Other Operating Expenses", value=int(st.query_params["comm_other_expenses"]), step=500)
        if comm_other_expenses != int(st.query_params["comm_other_expenses"]):
            st.query_params["comm_other_expenses"] = str(comm_other_expenses)
        
        st.header("Loan Details")
        # Loan Period
        loan_years_options = list(range(1, 31))  # 1 to 30 years
        comm_loan_years = st.selectbox("Loan Period (Years)", loan_years_options, index=loan_years_options.index(int(st.query_params["comm_loan_years"])))
        if comm_loan_years != int(st.query_params["comm_loan_years"]):
            st.query_params["comm_loan_years"] = str(comm_loan_years)
        
        st.header("Lookup Rates")
        selected_tax_rate = COMMERCIAL_TAX_RATES[comm_state]
        selected_insurance_rate = COMMERCIAL_INSURANCE_RATES[comm_state]
        st.metric("Tax Rate", f"{selected_tax_rate * 100:.2f}%")
        st.metric("Insurance Rate", f"{selected_insurance_rate * 100:.1f}%")
    
    # Commercial calculations based on Excel formulas
    
    # Annual operating expenses
    annual_insurance = comm_purchase_price * selected_insurance_rate
    annual_property_tax = comm_purchase_price * selected_tax_rate
    annual_pm_fee = comm_annual_gross_rents * 0.04  # 4% of gross rents
    
    # NOI Estimated calculation: (K4*(1-L5))-SUM(J8:J11)
    noi_estimated = (comm_annual_gross_rents * (1 - comm_vacancy_rate/100)) - (annual_insurance + annual_property_tax + annual_pm_fee + comm_other_expenses)
    
    # Commercial loan calculations (user-defined years, 6.5%)
    comm_loan_amount = comm_purchase_price - amount_down
    comm_annual_interest_rate = 0.065
    comm_monthly_rate = comm_annual_interest_rate / 12
    comm_num_payments = comm_loan_years * 12
    
    # Annual debt service
    monthly_payment = comm_loan_amount * (comm_monthly_rate * (1 + comm_monthly_rate) ** comm_num_payments) / ((1 + comm_monthly_rate) ** comm_num_payments - 1)
    annual_debt_service = monthly_payment * 12
    
    # Cash flow calculation: NOI - Annual Debt Service
    annual_cash_flow = noi_estimated - annual_debt_service
    
    # Closing costs (3% of purchase price)
    closing_costs = comm_purchase_price * 0.03
    
    # Total cash down
    total_cash_down = amount_down + closing_costs
    
    # Cash-on-cash return calculation
    cash_on_cash_return = (annual_cash_flow / total_cash_down) * 100 if total_cash_down > 0 else 0
    
    # Display commercial results
    col1, col2 = st.columns(2)
    
    with col1:
        st.header("Operating Expenses")
        expenses_df = pd.DataFrame({
            "Expense": ["Insurance", "Property Tax", "Property Management (4%)", "Other Operating Expenses"],
            "Annual Amount": [annual_insurance, annual_property_tax, annual_pm_fee, comm_other_expenses]
        })
        st.dataframe(expenses_df.style.format({"Annual Amount": "${:,.0f}"}), hide_index=True)
        
        st.metric("Total Annual Operating Expenses", f"${annual_insurance + annual_property_tax + annual_pm_fee + comm_other_expenses:,.0f}")
    
    with col2:
        st.header("Investment Analysis")
        analysis_df = pd.DataFrame({
            "Metric": ["Annual Gross Rents", "Adjusted Gross Income", "Annual NOI (Estimated)", "Annual Debt Service", "Annual Cash Flow", "Cash-on-Cash Return"],
            "Amount": [
                f"${comm_annual_gross_rents:,.0f}",
                f"${comm_annual_gross_rents * (1 - comm_vacancy_rate/100):,.0f}",
                f"${noi_estimated:,.0f}",
                f"${annual_debt_service:,.0f}",
                f"${annual_cash_flow:,.0f}",
                f"{cash_on_cash_return:.1f}%"
            ]
        })
        st.dataframe(analysis_df, hide_index=True)
    
    # Deal evaluation
    st.header("Deal Evaluation")
    if annual_cash_flow > 0:
        st.success("✅ GOOD DEAL: Positive annual cash flow")
    else:
        st.error("❌ BAD DEAL: Negative annual cash flow")
    
    # Investment summary
    st.header("Investment Summary")
    summary_col1, summary_col2 = st.columns(2)
    
    with summary_col1:
        st.metric("Purchase Price", f"${comm_purchase_price:,.0f}")
        st.metric("Down Payment", f"${amount_down:,.0f} ({comm_down_payment_pct}%)")
        st.metric("Closing Costs", f"${closing_costs:,.0f}")
        st.metric("Total Cash Investment", f"${total_cash_down:,.0f}")
    
    with summary_col2:
        st.metric("Loan Amount", f"${comm_loan_amount:,.0f}")
        st.metric("Monthly Payment", f"${monthly_payment:,.0f}")
        st.metric("Annual NOI (Estimated)", f"${noi_estimated:,.0f}")
        
        # Color-coded cash flow metric
        if annual_cash_flow > 0:
            st.markdown(f"**Annual Cash Flow:** :green[${annual_cash_flow:,.0f}]")
        else:
            st.markdown(f"**Annual Cash Flow:** :red[${annual_cash_flow:,.0f}]")
