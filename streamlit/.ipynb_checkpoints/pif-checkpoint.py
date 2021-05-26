import streamlit as st
import pandas as pd
import numpy as np

DATE_TIME = 'date/time'

st.title('Public Incentive Funding')


sidebar = st.sidebar.title("Panels")

select = st.sidebar.selectbox("Select",("Mission", "Programs", "Program Voting", "Copyright"), 1)

if select == "Mission":
    
    st.write("""
    ## PIF
    ### Mission: To fund public innovation and education through efficient allocation programs and activities.
    ### Vision: To cultivate a better future by increasing access to educational resources.  To encourage the public to learn more.""")

    
if select == "Programs":
    st.write("""## Program Directory""")
    if st.checkbox("Tech Resources for Red Bank Charter School"):
        st.subheader("Addresses: ")
        st.write("ETH: ")
        st.write("BTC: 36o2gsxQuZ9eLppHNEyFts8AWX8PRiuRA3")
        st.write("DAI: ")
    
    if st.checkbox("Financial Literacy at Red Bank Charter School"):
        st.subheader("Addresses: ")
        st.write("ETH: ")
        st.write("BTC: ")
        st.write("DAI: ")
        
if select == "Program Voting":
    st.subheader("Become a PIF Programmer")

if select == "Copyright":
    st.subheader("Copyright your PIF Program")