import streamlit as st
import pandas as pd

st.title("Sales Dashboard")

# Sample data
data = {
    "Product": ["Laptop", "Mobile", "Tablet", "Monitor"],
    "Sales": [50000, 30000, 20000, 15000],
    "Units Sold": [10, 20, 15, 8]
}

df = pd.DataFrame(data)

# Calculate metrics
total_sales = df["Sales"].sum()
total_units = df["Units Sold"].sum()
total_products = len(df)

# Display metrics
col1, col2, col3 = st.columns(3)

col1.metric("Total Sales", f"₹{total_sales:,}")
col2.metric("Units Sold", total_units)
col3.metric("Products", total_products)

# Display data
st.subheader("Product Sales Details")
st.dataframe(df, use_container_width=True)

# Display summary
st.subheader("Sales Data")
st.table(df[["Product", "Sales"]])