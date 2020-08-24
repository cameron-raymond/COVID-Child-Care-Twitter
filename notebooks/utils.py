import numpy as np
import re


DTYPE = {
    "id": "str",
    "created_at": "str",
    "screen_name": "str",
    "source": "str",
    "clean_text": "str",
    "original_text": "str",
    "is_retweet": "bool",
    "favorite_count": "int",
    "retweet_count": "int",
    "city": "str",
    "province": "str",
    "longitude": "float",
    "latitude": "float",
}

PROVINCES = ["Alberta",
            "British Columbia",
            "Manitoba",
            "New Brunswick",
            "Newfoundland and Labrador",
            "Northwest Territories",
            "Nova Scotia",
            "Nunavut",
            "Ontario",
            "Prince Edward Island",
            "Quebec",
            "Saskatchewan",
            "Yukon"]

PARSE_DATES = ["created_at"]

parse_list = lambda x : re.sub("[\[\]\']", '', x).split(',') if x else x

CONVERTERS = {"hashtags": parse_list,
            "urls": parse_list,
            "mentions": parse_list}