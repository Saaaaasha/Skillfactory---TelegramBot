import requests
import json
from config import keys


class APIException(Exception):
    pass


class CryptoConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        if quote == base:
            raise APIException(f"Невозможно перевести одинаковую валюты {base}.")
        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException(f"Не удалось обработать валюту {quote}. \
Убедитесь в правильности написания валюты, как в /values.")
        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIException(f"Не удалось обработать валюту {base}. \
Убедитесь в правильности написания валюты, как в /values.")
        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f"Не удалось обработать количество {amount}.")

        r = requests.get(f"https://v6.exchangerate-api.com/v6/38e91e4331bad24d9bd0c89a/pair/{quote_ticker}/{base_ticker}")
        rate = json.loads(r.content)["conversion_rate"]
        total_amount = rate * amount
        total_amount = round(total_amount, 2)
        return total_amount
