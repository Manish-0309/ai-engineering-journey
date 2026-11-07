import streamlit as st

st.title("User Profile Generator")

name = st.text_input("Your name")

age = st.number_input(
    "Your age",
    min_value=1,
    max_value=100,
    value=25
)

role = st.selectbox(
    "Your role",
    ["Student", "Developer", "AI Engineer", "Data Scientist"]
)

skills = st.multiselect(
    "Your skills",
    ["Python", "SQL", "Machine Learning", "Deep Learning", "GenAI"]
)

experience = st.slider(
    "Years of experience",
    0,
    20,
    1
)

available = st.checkbox("Available for opportunities")

if st.button("Generate Profile"):
    if not name.strip():
        st.error("Please enter your name.")
    else:
        st.subheader("Your Profile")

        st.write("Name:", name)
        st.write("Age:", age)
        st.write("Role:", role)
        st.write("Skills:", skills)
        st.write("Experience:", experience, "years")
        st.write("Available:", available)

        st.success("Profile generated successfully!")