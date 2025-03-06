import streamlit as st
st.set_page_config(page_title="Student Grade System", page_icon="📚",layout="centered")
st.title("📚 Student Grade System")
st.subheader("Enter the Student Marks")
marks = st.number_input("Enter the marks",min_value=0,max_value=100)
if st.button("Submit"):
    if marks >=90:
        st.success("Congrats🎉, You got A+ Grade")
    elif marks >=80:
        st.success("Congrats🎉, You got A Grade")
    elif marks >=70:
        st.success("Congrats🎉, You got B Grade")
    elif marks >= 60:
        st.success("Congrats🎉, You got C Grade")
    elif marks >= 50:
        st.success("Congrats🎉, You got D Grade")    
    else:
        st.error("You are failed")          
