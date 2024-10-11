from services.log_services import log
from database.pymysql_conn import DataBase
db = DataBase()

class DayAnalytic:
  def __init__(self, merchandise_rate_id, start_date=None, end_date=None):
    self.merchandise_rate_id = merchandise_rate_id
    self.start_date = start_date
    self.end_date = end_date


  # highest_hour_return, reverse_increase_hour, reverse_decrease_hour
  def get_analytic_hour(self):
    sql_query = 'SELECT date, highest_hour_return, reverse_increase_hour, reverse_decrease_hour FROM DailyTradingJournal_development.day_analytics WHERE '
    if self.start_date and self.end_date:
      sql_query = sql_query + \
          f"(day_analytics.date BETWEEN '{self.start_date} 00:00:00' AND '{self.end_date} 23:23:59') AND "
    if self.merchandise_rate_id:
      sql_query = sql_query + \
          f"day_analytics.merchandise_rate_id = {self.merchandise_rate_id} "
    sql_query = sql_query + ';'
    log(sql_query)
    db.cur.execute(sql_query)
    datas = list(db.cur.fetchall())
    highest_hour_return = []
    reverse_increase_hour = []
    reverse_decrease_hour = []
    for da in datas:
      if da[1] is not None:
        highest_hour_return.append(da[1])
      if da[2] is not None:
        reverse_increase_hour.append(da[2])
      if da[3] is not None:
        reverse_decrease_hour.append(da[3])
    return highest_hour_return, reverse_increase_hour, reverse_decrease_hour

