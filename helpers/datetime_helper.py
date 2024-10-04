import datetime
from dateutil.relativedelta import relativedelta

FORMAT_DATE_YEAR = "%Y-%m-%d"

def next_day(date):
  return (to_date(date) + datetime.timedelta(days=1)).strftime(FORMAT_DATE_YEAR)

def previous_day(date, format=FORMAT_DATE_YEAR):
  return (to_date(date) - datetime.timedelta(days=1)).strftime(format)

def previous_week(date):
  return to_date(date) - datetime.timedelta(weeks=1)

def next_month(month):
  date = to_date(f"2020-{month}-01")
  return (date + relativedelta(months=+1)).strftime('%m')

def previous_month(month):
  date = to_date(f"2020-{month}-01")
  return (date - relativedelta(months=+1)).strftime('%m')

def to_date(date_str):
  return datetime.datetime.strptime(date_str, FORMAT_DATE_YEAR)

def to_str(date):
  if type(date) == str:
    return date
  return date.strftime(FORMAT_DATE_YEAR)

def day_week_name(date_str):
  return to_date(date_str).strftime("%A")

def date_with_name(date_str):
  return to_date(date_str).strftime("%Y-%m-%d %A")

def date_name(date_str):
  return to_date(date_str).strftime("%A")

# Lấy ngày bắt đầu của tuần dựa vào ngày truyền vào
def get_start_of_week(today):
  start = today - datetime.timedelta(days=today.weekday())
  return start.strftime(FORMAT_DATE_YEAR)

def get_list_day_of_week(today):
  start = today - datetime.timedelta(days=today.weekday())
  list_dates = []
  next_day = start
  while next_day != today:
    list_dates.append(next_day.strftime(FORMAT_DATE_YEAR))
    next_day = next_day + datetime.timedelta(days=1)
  list_dates.append(today.strftime(FORMAT_DATE_YEAR))
  return list_dates
