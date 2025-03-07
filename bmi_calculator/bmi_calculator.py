import streamlit as st
st.set_page_config(page_title="BMI Calculator", page_icon="🏋️",layout="centered")
st.title("🏋️ BMI Calculator")
weight = st.number_input("Enter Your Weight in KGs :", min_value=0)
format = st.radio("Select Your Height Format",( "cms","meters","feet"))
if format == "cms":
    height = st.number_input("Enter Your height in cms :")
    try:
        bmi = weight / ((height/100)**2) 
    except:
        st.text("Enter the height")
elif format == "meters":
    height=st.number_input("ENter your height in meters :")
    try:
        bmi = weight / height**2
    except:
        st.text("Please enter your height :")            
elif format == "feet":
    height = st.number_input("Enter your height in feet :")
    try:
        bmi = weight / (((height/3.28))**2)
    except:
        st.text("Please enter your height : ") 
if st.button("Calculate"):
    st.success(f"Your BMI Index is : {bmi}")
    if bmi < 16:
        st.error("You are Severely Underweight")
    elif bmi >= 16 and bmi < 18.5:
        st.warning("You are Underweight")
    elif bmi >= 18.5 and bmi < 25:
        st.success("Healthy")
    elif bmi >= 25 and bmi < 30:
        st.warning("Overweight")
    elif bmi >= 30:
        st.error("Extremely Overweight")
                       
