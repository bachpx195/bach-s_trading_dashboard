from models.merchandise_rate import MerchandiseRate
from models.candlestick import Candlestick
from services.log_services import log


def get_day_data_prices(MERCHANDISE_RATE, DAYS):
  merchandise_rate = MerchandiseRate()
  merchandise_rate_id = merchandise_rate.find_by_slug(MERCHANDISE_RATE)
  candlestick = Candlestick(merchandise_rate_id, 'day', DAYS, "DESC")
  data_prices = candlestick.to_df()

  # data_prices['type_21'] = candlestick_type_by_hour(data_prices, 21)
  # data_prices['type_7'] = candlestick_type_by_hour(data_prices, 7)
  # data_prices['type_7'] = candlestick_type_by_hour(data_prices, 12)
  # data_prices['type_7'] = candlestick_type_by_hour(data_prices, 13)
  # data_prices['until_now'] = until_now_type(data_prices)
  log(data_prices)

  return data_prices, merchandise_rate_id
