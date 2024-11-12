import logging
import pandas as pd
from config.application import DEBUG_MODE

def log(obj, title=None):
  if not DEBUG_MODE:
    return
  logging.basicConfig(
      level=logging.DEBUG, format='%(asctime)s %(levelname)s\n\r%(message)s', datefmt='%H:%M:%S')


  if isinstance(obj, pd.DataFrame):
    pd.get_option('display.max_columns')
    logging.debug('\t' + obj.to_string().replace('\n', '\n\t'))
  else:
    if title is not None:
      logging.debug(title)
    logging.debug(obj)


def log_print(obj, title=None):
  logging.basicConfig(
      level=logging.INFO, format='%(asctime)s %(levelname)s\n\r%(message)s', datefmt='%H:%M:%S')

  if isinstance(obj, pd.DataFrame):
    pd.get_option('display.max_columns')
    logging.info('\t' + obj.to_string().replace('\n', '\n\t'))
  else:
    if title is not None:
      logging.info(title)
    logging.info(obj)
