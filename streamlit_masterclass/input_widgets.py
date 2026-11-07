import streamlit as st

st.write("Use of text_input()")
name = st.text_input("Enter your name:")
if name:
    st.write("Hello, ", name)


st.write("Use of text_area()")
description = st.text_area("Enter Description")
if description:
    st.write(description)

st.write("Use of number_input")
age = st.number_input(
    "Enter Your Age:",
    min_value=18,
    max_value=80,
    value=25,
    step=1
) 
st.write("Your Age: ", age)


st.write("Use of slider()")
experience = st.slider(
    "Select your experiance in year",
    min_value=0,
    max_value=20,
    value=2
)
st.write("Your Experience: ", experience)

st.write("Use of selectbox()")
skill = st.selectbox(
    "Select your skill",
    ["Python", "ML", "DL", "Gen AI"]
)
if skill:
    st.write(skill)


st.write("Use of multiselect()")
skills = st.multiselect(
    "Select Your Skills",
    ["Python", "ML", "DL", "Gen AI"]
)
st.write("Your skills",skills)

st.write("Use of checkbox()")
subscribe = st.checkbox("Subscribe")
if subscribe:
    st.success("You Subscribed")
else:
    st.info("Not Subscribed")

st.write("Use of radio()")
gender = st.radio(
    "Select Your Gender", 
    ["Male", "Female"]
)


st.write("Use of button()")
if st.button("Click Here"):
    st.success("Button Clicked")