#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv("Dot.env")

genai.configure(api_key=os.getenv("API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


def review_code(code):

    prompt = f"""
    You are an expert software engineer.

    Analyze this code and give:
    1. Bugs or Errors
    2. Fix Suggestions
    3. Optimized Code (if possible)
    4. Explanation in simple language

    CODE:
    {code}
    """

    response = model.generate_content(prompt)

    return response.text

