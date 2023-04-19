import streamlit as st

def find_largest(a, b, c):
    return max(a, b, c)

st.title("Find the Largest Number")
st.write("Enter three numbers to find the largest among them:")

num1 = st.number_input("First number", min_value=-1e20, step=1.0)
num2 = st.number_input("Second number", min_value=-1e20, step=1.0)
num3 = st.number_input("Third number", min_value=-1e20, step=1.0)

if st.button("Calculate Largest Number"):
    largest = find_largest(num1, num2, num3)
    st.success(f"The largest number among {num1}, {num2}, and {num3} is: {largest}")
