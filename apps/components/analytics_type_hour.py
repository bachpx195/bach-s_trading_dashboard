import plotly.graph_objects as go
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from apps.helpers.constants import LIST_HOUR_IN_DAY

class AnalyticsTypeHour:
  def __init__(self, dataframe):
    self.df = dataframe

  def analytics_type_hour(self):
    bar_width = 0.35
    opacity = 0.8

    index = np.arange(24)
    bar_width = 0.35
    opacity = 0.8

    x = ()
    y = ()

    for i in np.arange(24):
        data_prices_x = self.df[self.df['hour'] == i]

        number_up = len(data_prices_x[data_prices_x['candlestick_type'] == 0])
        number_down = len(
            data_prices_x[data_prices_x['candlestick_type'] == 1])

        x = x + (number_up,)
        y = y + (number_down,)

    plt.figure(figsize=[20,10])
    plt.rcParams['figure.figsize'] = [10, 10]

    rects1 = plt.bar(index, x, bar_width,
                    alpha=opacity, color='b', label='up')

    rects2 = plt.bar(index + bar_width, y, bar_width,
                    alpha=opacity, color='r', label='down')
    plt.xlabel('Giờ')
    plt.ylabel('Hiệu ứng')
    plt.title(
        f"Hiệu ứng thời gian trong ngày")
    plt.xticks(index + bar_width, tuple(np.arange(24)))
    plt.legend()
    plt.tight_layout()

    st.pyplot(plt)

  def run(self):
    st.write(
        '<style>div.row-widget.stRadio > div{flex-direction:row;} </style>', unsafe_allow_html=True)
    st.write(
        '<style>div.st-bf{flex-direction:column;} div.st-ag{font-weight:bold;padding-left:2px;}</style>', unsafe_allow_html=True)

    self.analytics_type_hour()
