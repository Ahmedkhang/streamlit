import streamlit as st

st.title("Counter in Streamlit")
st.write(st.session_state)
if 'count' not in st.session_state:
    st.session_state.count = 0

button = st.button("Increment")
if button:
    st.session_state.count +=1
st.write("Count",st.session_state.count)    
# if 'count' not in st.session_state:
#     st.session_state.count = 0

# increment = st.button('Increment')
# if increment:
#     st.session_state.count += 1

# st.write('Count = ', st.session_state.count)
# # del st.session_state.count
# "Text" , st.session_state.count