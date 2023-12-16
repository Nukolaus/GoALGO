"""Module for fill db with test deals"""
import uuid
from src.trader.bot import Bot

from datetime import datetime, timedelta

import pandas as pd
import tqdm
from moexalgo import Ticker
from src.db.sql import SQLManager
from src.trader.repository import BotDAL, DealDAL
from src.utils.logger import conf_logger

logger = conf_logger(__name__, "D")
bot_dal = BotDAL(SQLManager())
deal_dal = DealDAL(SQLManager())
last_candles_df: dict[str, pd.DataFrame] = {}

def create_list_of_test_dataframes(instrument_code) -> list[pd.DataFrame]:
    def make_candles(instrument_code, date, period="1h"):
        now = date
        now = now.replace(minute=0, second=0, microsecond=0) - timedelta(hours=1)
        now = now.replace(tzinfo=None)
        start = now - timedelta(days=10)
        ticket = Ticker(instrument_code)
        data = pd.DataFrame(ticket.candles(date=start, till_date=now, period=period))
        data = data[-30:].reset_index(drop=True)
        return data


    start = datetime.strptime("2023-12-06 23:00:00", "%Y-%m-%d %H:%M:%S")
    days = 3
    end = start + timedelta(days=days)
    current = start
    date_time = []
    while current <= end:
        if not (0 <= current.hour <= 8):
            date_time.append(current)
        current += timedelta(hours=1)

    dataframes_list = []
    for date in tqdm.tqdm(date_time):
        dataframes_list.append(make_candles(instrument_code, date, period="10m"))
    return dataframes_list


def fill_db_with_test_deals(instrument_code, user_id = "332097ee-807e-4958-b053-1bbf8c35e846"):
    bot_in_db = bot_dal.get(uuid.UUID(user_id), instrument_code)
    if not bot_in_db:
        raise Exception("Bot not found")

    bot = Bot(
        user_id=bot_in_db.user_id,
        instrument_code=bot_in_db.instrument_code,
        status=bot_in_db.status,
        start_balance=bot_in_db.start_balance,
    )
    candles = bot.get_candles()
    candles_list = create_list_of_test_dataframes(instrument_code)
    for candles in candles_list:
        saved_candles = last_candles_df.get(bot.instrument_code)

        if not candles.equals(saved_candles):
            last_candles_df[bot.instrument_code] = candles.copy(deep=True)
            desision, price = bot.make_prediction(candles)
            if desision == 1 and bot.in_stock > 0:
                bot.sell_request(price)
            elif desision == 2:
                current_balance = bot.get_current_balance()
                quantity = current_balance // price
                if quantity > 0:
                    bot.buy_request(price, quantity)
            logger.debug("current_balance: %s", bot.get_current_balance())

        else:
            logger.debug("Nothing to do")

