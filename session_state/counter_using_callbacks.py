import streamlit as st
if 'count' not in st.session_state:
    st.session_state.count = 0
def Counter():
    st.session_state.count += 1    
button = st.button("Count",on_click=Counter)
st.write("Count :",st.session_state.count)