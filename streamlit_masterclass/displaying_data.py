import streamlit as st
import pandas as pd

st.title("Employee Dashboard")

data = {
    "Name" : ["Amit", "Manish", "Robin"],
    "Department" :["Data Science", "AI", "Gen AI"],
    "Salary": [70000, 85000, 80000]
}

df = pd.DataFrame(data)

st.subheader("Displaying Employee Data")

st.text("Use of dataframe()")
st.dataframe(df)  #display data in interactive table, user can sort and explore data

st.text("Use of table()")
st.table(df)  #display data in normal or static table 


# displaying image
st.text("Use of image()")
st.image(
    "https://picsum.photos/600/300",
    caption="Sample Image",
    width="stretch"
)

st.write("Similarly we can make use of st.json(), st.metric()")