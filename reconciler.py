---

#### **File 2: `reconciler.py` (The "Fintech" Solution)**
*This script solves the "Messy Data" problem. It takes two messy CSVs and finds the gaps.*

```python
import pandas as pd

# MOCK DATA GENERATION (In real life, this comes from Xero/Facebook API)
# ---------------------------------------------------------
print("--- Loading Data Streams ---")

# 1. The Facebook Invoice Data (What we actually spent)
fb_data = {
    'Campaign_ID': ['CMP-001', 'CMP-002', 'CMP-003', 'CMP-004'],
    'Client_Name': ['Client A', 'Client A', 'Client B', 'Client C'],
    'Ad_Spend_GBP': [5000, 12000, 4500, 8000],
    'Status': ['Billed', 'Billed', 'Billed', 'Billed']
}
df_fb = pd.DataFrame(fb_data)

# 2. The Internal Xero Ledger (What we recorded in Client Funds)
xero_data = {
    'Ref_ID': ['CMP-001', 'CMP-002', 'CMP-003'], # Note: CMP-004 is missing (A Variance!)
    'Client_Account': ['Client A', 'Client A', 'Client B'],
    'Ledger_Amount': [5000, 12000, 4000] # Note: Client B is 4000, but spent 4500 (A Variance!)
}
df_xero = pd.DataFrame(xero_data)

# THE RECONCILIATION LOGIC
# ---------------------------------------------------------
print("--- Running Reconciliation Engine ---")

# Merge the two datasets based on Campaign ID
reconciled = pd.merge(df_fb, df_xero, left_on='Campaign_ID', right_on='Ref_ID', how='left')

# Calculate Variance (Ledger vs Actual Spend)
reconciled['Variance'] = reconciled['Ledger_Amount'] - reconciled['Ad_Spend_GBP']

# LOGIC:
# If Variance is 0 = Perfect Match.
# If Variance is Negative = We overspent (Burn Risk).
# If NaN = Invoice exists but not recorded in Xero (Process Failure).

def flag_status(row):
    if pd.isna(row['Ledger_Amount']):
        return "MISSING IN XERO - URGENT"
    elif row['Variance'] < 0:
        return f"OVERSPEND RISK: {row['Variance']}"
    elif row['Variance'] == 0:
        return "Reconciled"
    else:
        return "Under Budget"

reconciled['Audit_Status'] = reconciled.apply(flag_status, axis=1)

# OUTPUT FOR CFO
# ---------------------------------------------------------
print("\n--- CEO/CFO Exception Report ---")
# We only show the rows that need attention
exceptions = reconciled[reconciled['Audit_Status'] != "Reconciled"]
print(exceptions[['Client_Name', 'Campaign_ID', 'Ad_Spend_GBP', 'Ledger_Amount', 'Audit_Status']])

# In a real scenario, this exports to Excel:
# exceptions.to_csv('Daily_Variance_Report.csv')
