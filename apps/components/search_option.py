import streamlit as st
from apps.helpers.constants import LIST_MERCHANDISE_RATE, HOURS_IN_DAY

class SearchOption:
  def __init__(self):
    self.merchandise_rate = LIST_MERCHANDISE_RATE[1]
    self.record_limit = None
    self.start_date = None
    self.end_date = None
    self.list_day = None

  def run(self):
    # config css
    st.write(
        '<style>div.row-widget.stRadio > div{flex-direction:row;} </style>', unsafe_allow_html=True)
    st.write(
        '<style>div.st-bf{flex-direction:column;} div.st-ag{font-weight:bold;padding-left:2px;}</style>', unsafe_allow_html=True)

    self.select_merchandise_rate()
    self.select_record_limit()
    self.select_day()

    return self.merchandise_rate, self.record_limit, self.start_date, self.end_date, self.list_day

  def select_merchandise_rate(self):
    c1,_ = st.columns([2, 2])
    with c1:
      self.merchandise_rate = st.radio(
          "Chọn loại tài sản cần phân tích: ", LIST_MERCHANDISE_RATE, index=1)
  
  def select_record_limit(self):
    c1, c2 = st.columns([4, 4])
    with c1:
      input_record_limit = st.number_input(
          'Nhập số lượng dữ liệu (đơn vị: giờ)', value=50)
    with c2:
      self.record_limit = st.radio(
        "",
        [input_record_limit, 7, 30, 100, None],
        captions = ["Nhập", "1 Tuần", "1 Tháng", "3 Tháng", "Tất cả"]
      )

  def select_day(self):
    if st.checkbox("Chọn khoảng thời gian"):
      self.list_day = None
      c1, c2 = st.columns([2, 2])
      with c1:
        if st.checkbox("Ngày bắt đầu phân tích"):
          self.start_date = st.date_input('Chọn ngày bắt đầu')
        else:
          self.start_date = None

      with c2:
        if st.checkbox("Ngày kết thúc phân tích"):
          self.end_date = st.date_input('Chọn ngày kết thúc')
        else:
          self.end_date = None

    if st.checkbox("Chọn danh sách ngày"):
      self.start_date = None
      self.end_date = None
      self.list_day = st.text_input(
        "Chọn list ngày: ",
        label_visibility="visible",
        disabled=False,
        placeholder="2023-12-20, 2023-12-21, ..."
      )

    