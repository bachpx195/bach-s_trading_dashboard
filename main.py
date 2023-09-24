import streamlit as st
from hydralit_custom import HydraApp
import hydralit_components as hc
import apps

if __name__ == '__main__':
  app = HydraApp(
      title='The Big Trade',
  )

  app.add_app("Home", icon="🏠", app=apps.HomeApp(title='Home'),is_home=True)
  app.add_app("Data", app=apps.DataApp(title='Data'))
#   app.add_app("True Range", app=apps.TrueRangeApp(title='True Range'))
#   app.add_app("Hour Data", app=apps.HighestHourInDayApp(title='Hour Data'))

  app.add_loader_app(apps.MyLoadingApp(delay=0))

  app.run()
