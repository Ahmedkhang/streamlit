import streamlit as st
st.title("Counter in Streamlit with args")
if 'count' not in st.session_state:
    st.session_state.count = 0
increment_val = st.number_input("Enter the Increment value", value =1, step =5)
def Counter(increment_val):
    st.session_state.count += increment_val  
button = st.button("Increment",on_click=Counter, args=(increment_val, ))    
st.write("Count :",st.session_state.count)