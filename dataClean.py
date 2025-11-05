import pandas as pd
import numpy as np
import os
import re

# -----------------------------
# 1. Load the CSV file
# -----------------------------
csv_path = os.path.join(os.path.dirname(__file__), 'dummy_incident_tickets.csv')
df = pd.read_csv(csv_path, encoding='utf-8')

# -----------------------------
# 2. Drop Completely Empty Columns
# -----------------------------
df = df.dropna(axis=1, how='all')

# -----------------------------
# 3. Normalize Text Columns
# -----------------------------
df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
text_cols = df.select_dtypes(include='object').columns
for col in text_cols:
    df[col] = df[col].str.lower().replace({'y': 'yes', 'n': 'no'})

# -----------------------------
# 4. Handle Special Characters
# -----------------------------
df = df.applymap(lambda x: re.sub(r'&amp;amp;', 'and', x) if isinstance(x, str) else x)

# -----------------------------
# 5. Standardize Date Formats
# -----------------------------
date_cols = ['Opened Date', 'Ticket Resolved Date', 'Ticket Closed Date', 'Target Finish Date']
for col in date_cols:
    if col in df.columns:
        df[col] = pd.to_datetime(df[col], errors='coerce')

# -----------------------------
# 6. Remove Duplicates
# -----------------------------
if 'Ticket Number' in df.columns:
    df = df.drop_duplicates(subset=['Ticket Number'])

# -----------------------------
# 7. Validate Numeric Columns
# -----------------------------
if 'Time to resolve (min)' in df.columns:
    df['Time to resolve (min)'] = pd.to_numeric(df['Time to resolve (min)'], errors='coerce').fillna(0).astype(int)
    cap = df['Time to resolve (min)'].quantile(0.99)
    df['Time to resolve (min)'] = np.where(df['Time to resolve (min)'] > cap, cap, df['Time to resolve (min)'])

# -----------------------------
# 8. Derived Features for Insights
# -----------------------------
# Resolution Time in Hours
if 'Opened Date' in df.columns and 'Ticket Resolved Date' in df.columns:
    df['Resolution Time (hours)'] = (df['Ticket Resolved Date'] - df['Opened Date']).dt.total_seconds() / 3600
    df['Resolution Time (hours)'] = df['Resolution Time (hours)'].fillna(0)

# SLA Breach Flag
if 'Target Finish Date' in df.columns and 'Ticket Closed Date' in df.columns:
    df['SLA Breach'] = (df['Ticket Closed Date'] > df['Target Finish Date']).astype(int)

# Weekday & Hour Indicators
if 'Opened Date' in df.columns:
    df['Opened Weekday'] = df['Opened Date'].dt.day_name()
    df['Opened Hour'] = df['Opened Date'].dt.hour
    df['Opened Month'] = df['Opened Date'].dt.month
    df['Opened Quarter'] = df['Opened Date'].dt.quarter

# -----------------------------
# 9. Add New Insight Columns
# -----------------------------
# First Response Time (dummy placeholder if not available)
df['First Response Time (min)'] = np.nan  # Replace with actual logic if available

# Escalation Level (based on Queue ID or Priority)
df['Escalation Level'] = df['Ticket Priority'].apply(lambda x: 'L3' if x == 1 else ('L2' if x == 2 else 'L1'))

# Automation Success Flag
if 'Executed Automata' in df.columns:
    df['Automation Success'] = df['Executed Automata'].apply(lambda x: 'yes' if x == 'yes' else 'no')

# Impact Level (based on Priority)
df['Impact Level'] = df['Ticket Priority'].apply(lambda x: 'high' if x == 1 else ('medium' if x == 2 else 'low'))

# -----------------------------
# 10. Drop Unnecessary Columns
# -----------------------------
columns_to_drop = ['Comments & Work Notes', 'Resolution Text', 'Call code']  # Add more if irrelevant
df = df.drop(columns=[col for col in columns_to_drop if col in df.columns])

# -----------------------------
# 11. Drop Empty Rows
# -----------------------------
df = df.dropna(how='all')

# -----------------------------
# Save Cleaned & Enriched Data
# -----------------------------
df.to_csv('cleaned_enriched_incident_tickets_updated_for_visualization.csv', index=False, encoding='utf-8')

print("✅ Data cleaning & enrichment completed. File saved as 'cleaned_enriched_incident_tickets_updated_for_visualization.csv'")
