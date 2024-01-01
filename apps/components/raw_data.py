import streamlit as st

class RawData:
  def __init__(self, dataframe, text=None):
    self.df = dataframe
    self.text = text

  def run(self):
    text = "Hiển thị raw data"
    if self.text:
      text = self.text
    if st.button(text):
      st.dataframe(self.df)
      print(self.df.sample(10).to_dict())
