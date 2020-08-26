# Data Directory

The data directory stores the raw and processed CSVs scraped from Twitter. For more information on how the data is collected and processed see [`/notebooks`](../notebooks/README.md). All features, except for the `clean_text` column, are directly derived from the [Tweet object](https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/tweet-object#tweet-dictionary) provided by Twitter.

## Data Structure

* `/data/raw_data`: A list of JSON objects given directly by the historical search API (list of Tweet objects)
* `/data/processed_data`: Stored dataframes containing cleaned data

### Cleaned Data

| id             | created_at      | screen_name       | source            | clean_text              | is_retweet      | favorite_count | retweet_count  | hashtags     | urls         | mentions     | city         | province     | longitude        | latitude         |
|----------------|-----------------|-------------------|-------------------|-------------------------|-----------------|----------------|----------------|--------------|--------------|--------------|--------------|--------------|------------------|------------------|
| int (!null) | date (!null) | string (!null) | string (!null) | string (!null) | bool (!null) | int (!null) | int (!null) | list[string] | list[string] | list[string] | list[string] | list[string] | float (!null) | float (!null) |
