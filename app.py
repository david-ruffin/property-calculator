import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")
st.title("Property Investment Calculator")

# Property type selection
property_type = st.radio("Property Type", ["Residential", "Commercial"], horizontal=True)

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
