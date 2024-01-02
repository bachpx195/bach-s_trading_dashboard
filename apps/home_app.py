import os
import streamlit as st
from hydralit_custom import HydraHeadApp
from apps.concern.load_data import load_data, load_day_data, load_hour_data
from apps.components.analytics_range import AnalyticsRange
from apps.components.search_option import SearchOption
from apps.components.analytics_highest_hour_in_day import AnalyticsHighestHourInDay
from apps.components.analytics_type_hour import AnalyticsTypeHour
from apps.components.raw_data import RawData

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

      merchandise_rate, record_limit, start_date, end_date, list_day = SearchOption().run()

      day_prices = load_day_data(
          merchandise_rate, record_limit, start_date, end_date, True)
      hour_prices = load_hour_data(
          merchandise_rate, record_limit*24, start_date, end_date, list_day, 'hour_analytics')

      RawData(day_prices, "Hiển thị data ngày").run()
      RawData(hour_prices, "Hiển thị data giờ").run()

      if st.checkbox("Hiển thị phân tích range"):
         AnalyticsRange(day_prices).run()
         AnalyticsRange(hour_prices).run()
      if st.checkbox("Hiển thị phân tích theo giờ cao điểm"):
         AnalyticsHighestHourInDay(hour_prices).run()
      if st.checkbox("Hiển thị phân tích loại giờ"):
         AnalyticsTypeHour(hour_prices).run()
