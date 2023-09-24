import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 

class AnalyticsRange:
  def __init__(self, dataframe):
    self.df = dataframe

  def get_plt(self):

    index = np.arange(len(self.df))
    bar_width = 0.2
    opacity = 0.8

    x = ()
    y = ()

    plt.figure(figsize=[20,10])
    plt.rcParams['figure.figsize'] = [10, 10]
    fig, ax = plt.subplots()

    # Add OC bar
    plt.bar(index, self.df['day_return_oc'].apply(lambda x: abs(x)), bar_width,
                    alpha=opacity, color='b', label='OC')

    # Add HL bar
    plt.bar(index + bar_width, self.df['day_return_hl'], bar_width,
                    alpha=opacity, color='green', label='HL')
    
    # Add CL bar
    plt.bar(index + bar_width*2, self.df['day_return_cl'].apply(lambda x: abs(x)), bar_width,
                    alpha=opacity, color='r', label='CL')

    # Add HC bar
    plt.bar(index + bar_width*3, self.df['day_return_hc'], bar_width,
                    alpha=opacity, color='yellow', label='HC')            

    plt.xlabel('Ngay')
    plt.ylabel('%')
    plt.title(
        f"Khoảng giao động trong ngày")
    plt.xticks(index + bar_width*3, self.df['day'].values)
    ax.xaxis_date()
    fig.autofmt_xdate()
    plt.legend()
    plt.tight_layout()

    return plt

  def run(self):
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;} </style>', unsafe_allow_html=True)
    st.write('<style>div.st-bf{flex-direction:column;} div.st-ag{font-weight:bold;padding-left:2px;}</style>', unsafe_allow_html=True)
    
    st.pyplot(self.get_plt())
    st.write(f"Trung binh giao dong OC la {self.df['day_return_oc'].apply(lambda x: abs(x)).mean()}")
    st.write(f"Trung binh giao dong HL la {self.df['day_return_hl'].mean()}")

    
