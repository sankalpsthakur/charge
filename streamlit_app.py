import streamlit as st

# Streamlit Page Configuration
st.title('Cashflow Analysis for Electric Charging Stations (2023)')

# Assumptions Section in Sidebar
st.sidebar.subheader('Key Assumptions:')

CAPEX = st.sidebar.number_input('Capital Expenditure (CAPEX) per station (₹ Crores)', value=2.5)
Lifespan = st.sidebar.slider('Lifespan of one charging station (years)', 1, 20, 10)
Operational_days = st.sidebar.slider('Operational days/year', 50, 365, 300)
Charging_capacity = st.sidebar.slider('Charging capacity per station (cars simultaneously)', 50, 200, 125)
Utilization_rate = st.sidebar.slider('Utilization rate (%)', 1, 100, 20) / 100
Discount_rate = st.sidebar.slider('Discount rate (%)', 1, 20, 10) / 100
Average_revenue = st.sidebar.number_input('Average revenue per 30-minute slot (₹ INR)', value=125)
Electricity_cost_per_charge = st.sidebar.number_input('Electricity cost per car for a 30-minute charge (₹ INR)', value=112.5)

# Revenue Calculation in Main Area
st.subheader('1. Revenue Calculation (Per Station for 2023):')

Slots_per_day = Charging_capacity * 48
Revenue = Slots_per_day * Utilization_rate * Average_revenue * Operational_days
st.write(f'Revenue: ₹{Revenue/10000000:.2f} crores INR.')

# Expense Calculation in Main Area
st.subheader('2. Expense Calculation (Per Station for 2023):')

OPEX = st.sidebar.number_input('OPEX (₹ crores annually)', value=0.25)
Depreciation = CAPEX / Lifespan
Electricity_Cost = Slots_per_day * Utilization_rate * Electricity_cost_per_charge * Operational_days / 10000000  # Convert to crores
Salary_Expense = st.sidebar.number_input('Salary Expense (for 2023) (₹ crores annually)', value=6)

Total_Expenses = OPEX + Depreciation + Electricity_Cost + Salary_Expense
st.write(f'Total Expenses: ₹{Total_Expenses:.2f} crores INR annually.')

# Profit Calculation in Main Area
st.subheader('3. Profit Calculation (Per Station for 2023):')

Profit = Revenue - Total_Expenses * 10000000  # Multiply by 10^7 to convert crores to actual value
st.write(f'Profit: ₹{Profit/10000000:.2f} crores INR.')

# Additional Insights in Main Area
st.subheader('4. Additional Insights:')

break_even_utilization = Total_Expenses * 10000000 / (Slots_per_day * Average_revenue * Operational_days)  # Multiply by 10^7 to convert crores to actual value
st.write(f'The breakeven utilization rate (for profitability) is approximately {break_even_utilization*100:.2f}%.')

if Profit < 0:
    st.write(f'As of now, with the given assumptions and expenses, each station operates at a loss of ₹{-Profit/10000000:.2f} crores annually.')
else:
    st.write(f'With the given assumptions and expenses, each station operates at a profit of ₹{Profit/10000000:.2f} crores annually.')

