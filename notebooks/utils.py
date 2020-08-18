import ast

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
    "hashtags": "str",
    "urls": "str",
    "mentions": "str",
    "city": "str",
    "province": "str",
    "longitude": "float",
    "latitude": "float",
}

PROVINCES = set(["Alberta",
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
            "Yukon"])

PARSE_DATES = ["created_at"]