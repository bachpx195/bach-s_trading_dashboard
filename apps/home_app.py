import os
import streamlit as st
from hydralit_custom import HydraHeadApp
from apps.concern.load_data import load_data, load_day_data
from apps.components.analytics_range import AnalyticsRange

MENU_LAYOUT = [1,1,1,7,2]
CONFIG = {'displayModeBar': False, 'responsive': False}

class HomeApp(HydraHeadApp):
   def __init__(self, title = 'Hydralit Explorer', **kwargs):
      self.__dict__.update(kwargs)
      self.title = title

   #This one method that must be implemented in order to be used in a Hydralit application.
   #The application must also inherit from the hydrapp class in order to correctly work within Hydralit.
   def run(self):
      st.write('HI, IM A TRADER!')

      alt_name = 'LTCUSDT'

      day_number = st.number_input('Nhập số lượng dữ liệu (đơn vị: ngày)', value=50)
      day_prices = load_day_data(alt_name, day_number, None, None, True)

      st.dataframe(day_prices)

      AnalyticsRange(day_prices).run()
