import streamlit as st #type: ignore

st.title("Counter Application: ")

# Initialize counter
if "count" not in st.session_state:
    st.session_state.count = 0


# increment counter
if st.button("Increment"):
    st.session_state.count += 1

# decrement counter
if st.button("Decrement"):
    st.session_state.count -= 1

# reset counter 
if st.button("Reset"):
    st.session_state.count = 0

# Display counter
st.write("Current Count: ", st.session_state.count)