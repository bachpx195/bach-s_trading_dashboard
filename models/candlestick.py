import pandas as pd
import pytz
from datetime import timezone
from database.pymysql_conn import DataBase
from services.log_services import log

db = DataBase()
INTERVAL_HASH = {"day": 1, "week": 2, "month": 3, "hour": 4, "15m": 5}
HOUR_COLUMN_HASH = {'date': 8, 'open': 3, 'high': 4, 'close': 5, 'low': 6, 'volumn': 9, 'date_database': 16, 'date_with_binane': 17, 'hour': 18,
                    'return_oc': 19, 'return_hl': 20, 'candlestick_type': 21, 'range_type': 22, 'is_same_btc': 26, 'continue_by_day': 27, 'continue_by_hour': 28}
DAY_COLUMN_HASH = {'date': 8, 'open': 3, 'high': 4, 'close': 5, 'low': 6, 'volumn': 9,
                   'candlestick_type': 18, 'range_type': 19, 'is_inside_day': 20, 'is_same_btc': 26, 'continue_type': 27}
CANDLESTICK_COLUMN_HASH = {'date': 8, 'open': 3,
                           'high': 4, 'close': 5, 'low': 6, 'volumn': 9}

class Candlestick:
    def __init__(self, merchandise_rate_id, interval="day", limit=None, sort="ASC", start_date=None, end_date=None, list_day=None):
        self.limit = limit if limit else 100000
        self.interval = interval
        self.merchandise_rate_id = merchandise_rate_id
        self.sort = sort
        self.start_date = start_date
        self.end_date = end_date
        if interval == 'day':
            self.join_analytic_table = 'day_analytics'
        elif interval == 'hour':
            self.join_analytic_table = 'hour_analytics'
        else:
            self.join_analytic_table = None
        self.list_day = list_day

    def get_sql_query(self):
        if self.join_analytic_table:
            sql_query = f"SELECT * FROM DailyTradingJournal_development.candlesticks candlesticks INNER JOIN DailyTradingJournal_development.{self.join_analytic_table} ON candlesticks.id = {self.join_analytic_table}.candlestick_id WHERE "
        else:
            sql_query = 'SELECT * FROM DailyTradingJournal_development.candlesticks WHERE '
        if self.start_date and self.end_date:
            sql_query = sql_query + \
                f"(candlesticks.date BETWEEN '{self.start_date} 00:00:00' AND '{self.end_date} 23:23:59') AND "
        if self.list_day:
            if len(self.list_day) == 1:
                sql_query = sql_query + \
                    f"(candlesticks.date BETWEEN '{day} 00:00:00' AND '{day} 23:23:59') AND "
            else:
                for idx, day in enumerate(self.list_day):
                    if idx == len(self.list_day) - 1:
                        sql_query = sql_query + \
                            f"(candlesticks.date BETWEEN '{day} 00:00:00' AND '{day} 23:23:59')) AND "
                    elif idx == 0:
                        sql_query = sql_query + \
                            f"((candlesticks.date BETWEEN '{day} 00:00:00' AND '{day} 23:23:59') OR "
                    else:
                        sql_query = sql_query + \
                            f"(candlesticks.date BETWEEN '{day} 00:00:00' AND '{day} 23:23:59') OR "
        if self.interval:
            sql_query = sql_query + \
                f"candlesticks.time_type = {INTERVAL_HASH[self.interval]} AND "
        if self.merchandise_rate_id:
            sql_query = sql_query + \
                f"candlesticks.merchandise_rate_id = {self.merchandise_rate_id} "
        if self.sort:
            sql_query = sql_query + \
                f"ORDER BY candlesticks.date {self.sort} "
        if self.limit:
            sql_query = sql_query + f"lIMIT {self.limit}"
        sql_query = sql_query + ';'

        log(
            "_________________________________________log query_________________________________________")
        log(sql_query)
        return sql_query

    def to_df(self):
        try:
            sql_query = self.get_sql_query()
            db.cur.execute(sql_query)
            if self.join_analytic_table:
                if self.join_analytic_table == 'hour_analytics':
                    columns = list(HOUR_COLUMN_HASH.keys())
                if self.join_analytic_table == 'day_analytics':
                    columns = list(DAY_COLUMN_HASH.keys())
            else:
                columns = list(CANDLESTICK_COLUMN_HASH.keys())
            datas = list(db.cur.fetchall())
            data = []
            for da in datas:
                row = []
                for column in columns:
                    row.append(da[HOUR_COLUMN_HASH[column]])
                data.append(tuple(row))
            df = pd.DataFrame(columns=columns, data=data)
            if not df['date'].empty:
                df['date'] = df['date'].dt.tz_localize(timezone.utc)
                my_timezone = pytz.timezone('Asia/Bangkok')
                df['date'] = df['date'].dt.tz_convert(my_timezone)
            else:
                print("**************data frame is null**************")
            df.set_index('date', inplace=True)
            return df
        except:
            if (df['date'].empty):
                print("data frame is null")
            else:
                print("Candlestick exception")
