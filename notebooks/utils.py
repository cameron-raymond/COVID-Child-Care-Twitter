import plotly.express.colors as cols
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

CONSOLIDATED_PROVINCES = ["Alberta",
            "British Columbia",
            "Manitoba",
            "Ontario",
            "Quebec",
            "Saskatchewan",
            "Atlantic Province",
            "Northern Territory"]

PROVINCE_COLOR_MAP = { a : b for a,b in zip(PROVINCES+["Total","Atlantic Province","Northern Territory"],cols.qualitative.Dark24)}   

PROV_CONSOLIDATION = {
    "New Brunswick": "Atlantic Province",
    "Newfoundland and Labrador": "Atlantic Province",
    "Nova Scotia": "Atlantic Province",
    "Prince Edward Island": "Atlantic Provinces",
    "Yukon": "Northern Territory",
    "Northwest Territories": "Northern Territory",
    "Nunavut": "Northern Territory"}

PARSE_DATES = ["created_at"]

parse_list = lambda x : re.sub("[\[\]\']", '', x).split(',') if x else x

CONVERTERS = {"hashtags": parse_list,
            "urls": parse_list,
            "mentions": parse_list}

if __name__ == "__main__":
    # print(DTYPE)
    for p in PROVINCES+["Total"]:
        print(p,": ",PROVINCE_COLOR_MAP[p])
    # print(CONVERTERS)
    # print(PARSE_DATES)