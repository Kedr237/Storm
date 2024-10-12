import aiohttp
import os
from http import HTTPStatus
import logging

from .urls import CITY_URL

API_TOKEN = os.environ.get("API_TOKEN")


async def get_city_info(query: str, lang: str = "ru") -> dict | None:
    params = {
        "q": query,
        "lang": lang,
        "key": API_TOKEN,
    }
    async with aiohttp.ClientSession() as session:
        async with session.get(CITY_URL, params=params) as response:
            if response.status == HTTPStatus.OK:
                return await response.json()
            elif response.status == HTTPStatus.UNAUTHORIZED:
                logging.error("Invalid api token.")
            else:
                resp = await response.json()
                logging.error(f"Problem in search_city : {resp}.")
            return None
