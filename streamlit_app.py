import streamlit as st

# Streamlit Page Configuration
st.title('Cashflow Analysis for Electric Charging Stations (2023)')

# Assumptions Section
st.subheader('1. Key Assumptions:')

CAPEX = st.number_input('Capital Expenditure (CAPEX) per station (₹ Crores)', value=2.5)
Lifespan = st.slider('Lifespan of one charging station (years)', 1, 20, 10)
Operational_days = st.slider('Operational days/year', 50, 365, 300)
Charging_capacity = st.slider('Charging capacity per station (cars simultaneously)', 50, 200, 125)
Utilization_rate = st.slider('Utilization rate (%)', 1, 100, 20) / 100
Discount_rate = st.slider('Discount rate (%)', 1, 20, 10) / 100
Average_revenue = st.number_input('Average revenue per 30-minute slot (₹ INR)', value=125)

# Revenue Calculation
st.subheader('2. Revenue Calculation (Per Station for 2023):')

Slots_per_day = Charging_capacity
Revenue = Slots_per_day * Utilization_rate * Average_revenue * Operational_days
st.write(f'Revenue: ₹{Revenue/10000000:.2f} crores INR.')

# Expense Calculation
st.subheader('3. Expense Calculation (Per Station for 2023):')

OPEX = st.number_input('OPEX (₹ crores annually)', value=0.25)
Depreciation = CAPEX / Lifespan
Electricity_Cost = st.number_input('Electricity Cost (based on utilization) (₹ crores annually)', value=4.05)
Salary_Expense = st.number_input('Salary Expense (for 2023) (₹ crores annually)', value=6)

Total_Expenses = OPEX + Depreciation + Electricity_Cost + Salary_Expense
st.write(f'Total Expenses: ₹{Total_Expenses/10000000:.2f} crores INR annually.')

# Profit Calculation
st.subheader('4. Profit Calculation (Per Station for 2023):')

Profit = Revenue - Total_Expenses * 10000000  # Multiply by 10^7 to convert crores to actual value
st.write(f'Profit: ₹{Profit/10000000:.2f} crores INR.')

# Additional Insights
st.subheader('5. Additional Insights:')

break_even_utilization = Total_Expenses / (Slots_per_day * Average_revenue * Operational_days)
st.write(f'The breakeven utilization rate (for profitability) is approximately {break_even_utilization*100:.2f}%.')

if Profit < 0:
    st.write(f'As of now, with the given assumptions and expenses, each station operates at a loss of ₹{-Profit/10000000:.2f} crores annually.')
else:
    st.write(f'With the given assumptions and expenses, each station operates at a profit of ₹{Profit/10000000:.2f} crores annually.')

