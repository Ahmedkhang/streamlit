import streamlit as st
import re
st.set_page_config(page_title="Password Strength Meter", page_icon="🔓",layout="centered")
st.title("Password Strength Meter")
st.subheader("Check your Password's Strength")
# def main():
#     st.title("Password Strength Meter")
#     st.subheader("")
# 
def password_checker(password):
    score =0

    if len(password) >= 8:
     
         score += 1
    else:
         st.warning("Password must be at least 8 characters")     
    if re.search(r"[A-Z]",password) and re.search(r"[a-z]", password):
         score += 1
    else:
         st.warning("Password must contain both uppercase and lowercase characters")     
    if re.search(r"\d",password):
         score += 1
    else:
         st.warning("password must contain at least one digit")
    if re.search(r"[-#@$%&*!]",password):
         score += 1
    else:
         st.warning("password must contain at least on special character")
    if score == 4:
         st.success("Password is strong") 
    elif score == 3:
         st.warning("Password is moderate")
    else:
         st.error("Password is too weak")                             
password = st.text_input("Enter your password",type="password")
if st.button("Check"):
     password_checker(password)
else:
     st.error("Please enter a password to check")     


if __name__ == '__main__':
#     main()
