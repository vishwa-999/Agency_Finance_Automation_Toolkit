import pandas as pd
import matplotlib.pyplot as plt

# SCENARIO: 
# Mulenga (CEO) wants to know which Squad is actually making money.
# Squad Alpha relies heavily on expensive freelancers.
# Squad Beta uses internal staff and tools.

data = {
    'Squad': ['Squad Alpha', 'Squad Beta', 'Squad Gamma'],
    'Revenue_Retainer': [50000, 45000, 60000],
    'Internal_Staff_Cost': [15000, 25000, 20000],
    'Freelancer_Cost': [25000, 2000, 5000], # Alpha spends huge on freelancers
    'Tech_Stack_Alloc': [2000, 2000, 2000]
}

df = pd.DataFrame(data)

# Calculate Unit Economics
df['Total_Cost'] = df['Internal_Staff_Cost'] + df['Freelancer_Cost'] + df['Tech_Stack_Alloc']
df['Gross_Margin_GBP'] = df['Revenue_Retainer'] - df['Total_Cost']
df['Margin_Percent'] = (df['Gross_Margin_GBP'] / df['Revenue_Retainer']) * 100

print("--- Squad Unit Economics Report ---")
print(df[['Squad', 'Revenue_Retainer', 'Total_Cost', 'Gross_Margin_GBP', 'Margin_Percent']])

# VISUALIZATION (Simple ASCII for Console or Matplotlib for image)
# This simulates the "Dashboard" view
print("\n--- Visualizing Efficiency ---")
for index, row in df.iterrows():
    bar = "█" * int(row['Margin_Percent'] / 2)
    print(f"{row['Squad']} Margin: {row['Margin_Percent']:.1f}% | {bar}")

print("\nINSIGHT: Squad Alpha has high revenue but low margin (20%) due to freelancer reliance.")
print("RECOMMENDATION: Convert key freelancers in Squad Alpha to full-time staff to improve margin.")
