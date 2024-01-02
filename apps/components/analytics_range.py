import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 

class AnalyticsRange:
  def __init__(self, dataframe):
    self.df = dataframe

  def run(self):
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;} </style>', unsafe_allow_html=True)
    st.write('<style>div.st-bf{flex-direction:column;} div.st-ag{font-weight:bold;padding-left:2px;}</style>', unsafe_allow_html=True)
    
    st.bar_chart(self.df['return_oc'])
    st.write(f"Trung binh giao dong Open Close la {self.df['return_oc'].apply(lambda x: abs(x)).mean()}")
    
    st.bar_chart(self.df['return_hl'])
    st.write(f"Trung binh giao dong High Low la {self.df['return_hl'].mean()}")

    
