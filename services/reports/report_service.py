import numpy as np
import matplotlib.pyplot as plt
import collections
from models.merchandise_rate import MerchandiseRate
from models.candlestick import Candlestick
from models.day_analytic import DayAnalytic
from services.log_services import log, log_print
from helpers.utils import refactor_list_of_float
from helpers.constants import HOUR_LIST



def get_hour_data_prices(MERCHANDISE_RATE, DAYS, START_DATE=None, END_DATE=None):
  merchandise_rate = MerchandiseRate()
  merchandise_rate_id = merchandise_rate.find_by_slug(MERCHANDISE_RATE)
  candlestick = Candlestick(merchandise_rate_id, 'hour',
                            24*DAYS, "DESC", start_date=START_DATE, end_date=END_DATE)
  data_prices = candlestick.to_df()
  
  # data_prices['type_21'] = candlestick_type_by_hour(data_prices, 21)
  # data_prices['type_7'] = candlestick_type_by_hour(data_prices, 7)
  # data_prices['type_7'] = candlestick_type_by_hour(data_prices, 12)
  # data_prices['type_7'] = candlestick_type_by_hour(data_prices, 13)
  # data_prices['until_now'] = until_now_type(data_prices)
  log(data_prices)

  return data_prices, merchandise_rate_id


def get_analytic_hour(merchandise_rate_id, data_prices):
  start_date = data_prices['date_database'][-1]
  end_date = data_prices['date_database'][0]
  highest_hour_return, reverse_increase_hour, reverse_decrease_hour = DayAnalytic(
      merchandise_rate_id, start_date, end_date).get_analytic_hour()
  return highest_hour_return, reverse_increase_hour, reverse_decrease_hour


def draw_histogram(list, bin=10, round_number=2):
  plt.hist(refactor_list_of_float(list, round_number), bins=bin)
  plt.xlabel('Gio')
  plt.ylabel('So luong')
  plt.xticks(bin)
  return plt


def highest_hour_in_day_report(hour_list):
  log_print(hour_list, "highest_hour_list")
  group_hour_list = collections.Counter(hour_list)
  plt.bar(HOUR_LIST, [group_hour_list[hour] for hour in HOUR_LIST])
  plt.xlabel('Gio')
  plt.ylabel('So luong')
  plt.xticks(HOUR_LIST)
  plt.yticks(list(group_hour_list.values()))
  return plt


def reverse_increase_hour_report(hour_list):
  log_print(hour_list, "reverse_increase_hour")
  group_hour_list = collections.Counter(hour_list)
  plt.bar(HOUR_LIST, [group_hour_list[hour] for hour in HOUR_LIST])
  plt.xlabel('Gio')
  plt.ylabel('So luong')
  plt.xticks(HOUR_LIST)
  plt.yticks(list(group_hour_list.values()))
  return plt


def reverse_decrease_hour_report(hour_list):
  log_print(hour_list, "reverse_decrease_hour")
  group_hour_list = collections.Counter(hour_list)
  plt.bar(HOUR_LIST, [group_hour_list[hour] for hour in HOUR_LIST])
  plt.xlabel('Gio')
  plt.ylabel('So luong')
  plt.xticks(HOUR_LIST)
  plt.yticks(list(group_hour_list.values()))
  return plt


def hour_analytic(data_prices):
#   total = data_prices.iloc[:, 0].count()
#   first_date = data_prices.iloc[0].name.date()
#   last_date = data_prices.iloc[-1].name.date()

  bar_width = 0.35
  opacity = 0.8

  index = np.arange(24)
  bar_width = 0.35
  opacity = 0.8

  x = ()
  y = ()

  for i in np.arange(24):
      data_prices_x = data_prices[data_prices['hour'] == i]

      number_up = len(data_prices_x[data_prices_x['candlestick_type'] == 0])
      number_down = len(
          data_prices_x[data_prices_x['candlestick_type'] == 1])

      x = x + (number_up,)
      y = y + (number_down,)


  plt.figure(figsize=[20, 10])
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

  return plt

def detail_hour_analytic(data_prices, hour_observe=None):
  plt.figure(figsize=[20, 10])
  plt.rcParams['figure.figsize'] = [10, 10]

  data_prices_up = data_prices[(data_prices['hour'] == hour_observe) & (
      data_prices['candlestick_type'] == 0)]
  data_prices_down = data_prices[(data_prices['hour'] == hour_observe) & (
      data_prices['candlestick_type'] == 1)]

  print(f"Giờ {hour_observe}")
  print("________________________________")
  print(data_prices_up['return_oc'].describe())
  print(data_prices_up['return_oc'].sum())

  print("+++")
  print(data_prices_down['return_oc'].describe())
  print(data_prices_down['return_oc'].sum())

  hour_observe_data_prices = data_prices[data_prices['hour'] == hour_observe]
  hour_observe_data_prices['return_oc'].plot(figsize=[20, 10], kind='bar')
  
  type_continuous_group = hour_observe_data_prices.groupby(
      ['continue_by_hour']).size()
  print(type_continuous_group)

  labels = type_continuous_group.index.values
  sizes = type_continuous_group.values

  plt.figure()
  _, ax1 = plt.subplots(figsize=(12, 7))
  ax1.pie(sizes, labels=labels, autopct='%1.1f%%')
  ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

  plt.legend()
  return plt


def continuous_report(data_prices):
  type_continuous_group = data_prices.groupby(
      ['continue_by_day']).size()
  print(type_continuous_group)

  labels = type_continuous_group.index.values
  sizes = type_continuous_group.values

  plt.figure()
  _, ax1 = plt.subplots(figsize=(12, 7))
  ax1.pie(sizes, labels=labels, autopct='%1.1f%%')
  # Equal aspect ratio ensures that pie is drawn as a circle.
  ax1.axis('equal')

  plt.legend()
  return plt
