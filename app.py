import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")
st.title("Property Investment Calculator")

# Sidebar inputs
with st.sidebar:
    st.header("Property Details")
    purchase_price = st.number_input("Purchase Price", value=650000, step=1000)
    down_payment_pct = st.slider("Down Payment %", 0, 100, 20) / 100
    
    # Display the actual down payment amount
    amount_down = purchase_price * down_payment_pct
    st.metric("Down Payment Amount", f"${amount_down:,.2f}")
    
    interest_rate = st.slider("Interest Rate %", 0.0, 10.0, 2.0) / 100
    loan_years = st.selectbox("Loan Term (Years)", [15, 30], index=0)
    monthly_rent = st.number_input("Expected Monthly Rent", value=5000, step=100)
    
    st.header("Location")
    state = st.selectbox("State", 
                          ["AZ", "CA", "IN", "NV", "TX", "MI"],
                          index=4)
    
    TAX_RATES = {
        "AZ": 0.0062,
        "CA": 0.0125,
        "IN": 0.0137,
        "NV": 0.0065,
        "TX": 0.0170,
        "MI": 0.0321
    }

# Calculations
loan_amount = purchase_price * (1 - down_payment_pct)
monthly_rate = interest_rate / 12
num_payments = loan_years * 12

# Monthly Principal & Interest Payment (Mortgage Payment)
monthly_pi = loan_amount * (monthly_rate * (1 + monthly_rate)**num_payments) / ((1 + monthly_rate)**num_payments - 1)

# Other monthly costs (Overhead)
monthly_insurance = (purchase_price * 0.01) / 12
monthly_tax = (purchase_price * TAX_RATES[state]) / 12
pm_fee = monthly_rent * 0.10
maintenance = 250

# Total monthly payment including overhead
total_monthly = monthly_pi + monthly_insurance + monthly_tax + pm_fee + maintenance

# Cash flow analysis for different occupancy rates
occupancy_rates = [0.75, 0.90, 1.0]
cash_flows = []
annual_returns = []

for rate in occupancy_rates:
    monthly_income = monthly_rent * rate
    cash_flow = monthly_income - total_monthly
    annual_return = (cash_flow * 12) / (purchase_price * down_payment_pct) * 100
    cash_flows.append(cash_flow)
    annual_returns.append(annual_return)

# Display results: Monthly Expenses and Investment Returns
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
        .applymap(color_negative_red, subset=["Monthly Cash Flow", "Annual ROI"]),
        hide_index=True
    )

# New Loan Summary Section
st.header("Loan Summary")

# Calculate additional metrics
monthly_overhead = monthly_insurance + monthly_tax + pm_fee + maintenance
total_interest = (monthly_pi * num_payments) - loan_amount
total_cost = total_monthly * num_payments

summary_df = pd.DataFrame({
    "Metric": [
        "Loan Amount",
        "Monthly Payment (P&I)",
        "Monthly Overhead",
        "Total Monthly Payment",
        "Number of Payments",
        "Total Interest",
        "Total Cost of Loan"
    ],
    "Value": [
        loan_amount,
        monthly_pi,
        monthly_overhead,
        total_monthly,
        num_payments,
        total_interest,
        total_cost
    ]
})

# Format values: use currency formatting for monetary amounts but not for the number of payments.
summary_df["Formatted Value"] = summary_df.apply(
    lambda row: f"{row['Value']}" if row["Metric"] == "Number of Payments" 
                else f"${row['Value']:,.2f}",
    axis=1
)
st.table(summary_df[["Metric", "Formatted Value"]])

# Investment status based on 75% occupancy
st.header("Investment Status")
if cash_flows[0] > 0:
    st.success("✅ Good Investment: Profitable even at 75% occupancy")
else:
    st.error("❌ High Risk: Not profitable at 75% occupancy")

# Amortization Schedule for the first 12 payments (1 year)
st.header("Amortization Schedule")
schedule = []
balance = loan_amount

for payment in range(1, 13):
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

# Loan Balance Over Time chart for the first year
fig = px.line(
    schedule_df, 
    x="Payment", 
    y="Balance",
    title="Loan Balance Over Time"
)
st.plotly_chart(fig, use_container_width=True)
