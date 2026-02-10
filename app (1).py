#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
from reviewer import review_code

st.title("💻 AI Code Review Assistant")

st.write("Paste your code below")

code_input = st.text_area("Enter Code Here", height=300)

if st.button("Review Code"):

    if code_input:
        result = review_code(code_input)

        st.subheader("🔍 AI Review Result")
        st.write(result)

    else:
        st.warning("Please paste code first")

