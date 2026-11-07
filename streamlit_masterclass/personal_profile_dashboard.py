import streamlit as st #type: ignore[reportMissing]

# Application Title
st.title("My Personal Dashboard")

# Introduction
st.header("About me")

st.write(
    "Hello! I am an AI Engineer "
    "interested in Machine Learning "
    "and Generative AI."
)

# Professional information
st.subheader("Professional Information")

st.text("Role: AI Engineer")
st.text("Primary Language: Python")


# Technical Skills
st.subheader("Technical Skills")

skills = [
    "Python",
    "Machine Learning",
    "Deep Learning",
    "Generative AI",
    "SQL"
]

st.write(skills) #write function can display wide range of objects inclusding list, string, numbers, dictionary, dataframes, charts, etc..

st.subheader("My current project: ")

st.markdown("""
I am learning **Streamlit** to build:

- Data Science Applications
- Machine Learning Dashboards
- AI-powered Applications
""")


# completion message
st.success("Dashboard is ready.")