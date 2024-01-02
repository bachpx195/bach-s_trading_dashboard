import plotly.graph_objects as go
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from apps.helpers.constants import LIST_HOUR_IN_DAY, LIST_DAY_IN_WEEK

class AnalyticsHighestHourInDay:
  def __init__(self, dataframe):
    self.df = dataframe

  def analytics_highest_return(self, day_name=None):
    list_hour_highest_return = []
    hovertext=[]

    for hour in LIST_HOUR_IN_DAY:
      if day_name:
        hour_dataframe = self.df[(self.df['hour'] == hour) & (
          self.df['is_highest_hour_return'] == 1) & (self.df['day_name'] == day_name)]
        
      else:
        hour_dataframe = self.df[(self.df['hour'] == hour) & (
            self.df['is_highest_hour_return'] == 1)]
      
      hovertext.append(
          f"mean {round(hour_dataframe.return_hl.mean(),2)} - max {round(hour_dataframe.return_hl.max(),2)} - min {round(hour_dataframe.return_hl.min(),2)}")
      list_hour_highest_return.append(len(hour_dataframe))
        
    fig = go.Figure(data=[go.Bar(
      x=LIST_HOUR_IN_DAY, y=list_hour_highest_return,
      text=list_hour_highest_return, hovertext=hovertext,
    )])

    fig.update_layout(xaxis={'type': 'category'})

    if day_name:
      st.write(day_name)

    st.plotly_chart(fig, use_container_width=True)

  def run(self):
    st.write(
        '<style>div.row-widget.stRadio > div{flex-direction:row;} </style>', unsafe_allow_html=True)
    st.write(
        '<style>div.st-bf{flex-direction:column;} div.st-ag{font-weight:bold;padding-left:2px;}</style>', unsafe_allow_html=True)

    self.analytics_highest_return()

    for day_name in LIST_DAY_IN_WEEK:
      self.analytics_highest_return(day_name)
