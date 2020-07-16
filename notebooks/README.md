# Notebooks Directory

**Purpose:** Collect all relevant Tweet's pertaining to the reopening of schools in the COVID-19 pandemic between Jan. 1, 2020 and Sept. 15, 2020.

All data collected was done so in accordance with Twitter community guidelines. This project makes use of Twitter's [premium search API](https://developer.twitter.com/en/docs/tweets/search/overview/premium), which allows for access to Twitter's full archive of Tweets dating back to 2006. Below is a list of the filter's used to obtain the dataset. For a full list of operators available for this API see [here](https://developer.twitter.com/en/docs/tweets/search/overview/premium#AvailableOperators).

## Search Terms

* **Time-frame:** Jan. 1, 2020 - Sept. 30, 2020
* **Geo:** Canada, with province-by-province breakdown
* **Keywords:**
  * 'back to school'
  * 'school reopening'
  * 'child care'
* **Mentions (Education Ministers):**
  * David Eggen, [@davideggenAB](https://twitter.com/davideggenAB) (AB)
  * Rob Fleming, [@Rob_Fleming](https://twitter.com/Rob_Fleming)(BC)
  * Kelvin Goertzen, [@mingoertzen](https://twitter.com/mingoertzen) (MB)
  * Dominic Cardy, [@DominicCardy](https://twitter.com/DominicCardy) (NB)
  * Brian Warr, [@BrianWarr709](https://twitter.com/BrianWarr709) (NL)
  * R.J. Simpson, [@RJSimpson_NWT](https://twitter.com/RJSimpson_NWT) (NT)
  * Zach Chruchill, [@zachchurchill](https://twitter.com/zachchurchill) (NS)
  * David Joanasie *TODO* (NU)
  * Stephen Lecce, [@Sflecce](https://twitter.com/Sflecce) (ON)
  * Brad Trivers, [@bradtrivers](https://twitter.com/bradtrivers) (PE)
  * Jean-François Roberge, [@jfrobergeQc](https://twitter.com/jfrobergeQc) (QC)
  * Gordon Wyant, [@GordWyant](https://twitter.com/GordWyant) (SK)
  * Tracy-Anne McPhee, [@TracyMcPheeRS](https://twitter.com/TracyMcPheeRS) (YT)

## Data Pipeline

1. Connect to Twitter's Search Tweets API, to the `full archive` endpoint
2. Go province by province<sup>1</sup> and:
    1. Collect all tweets that mention that an education minister
    2. Collect all tweets that contain a dedicated list of keywords/hashtags
3. Store collection of tweets in Pandas dataframe, and only keep relevant features (data, geo-code, text, author, *etc.*)
4. Add an extra column that is the cleaned tweet text.
5. Save dataframe to CSV
6. Solve the pandemic 🎊

<sup>1</sup> For more information on what tweets are geo-coded, see [Twitter's geo-filtering guide](https://developer.twitter.com/en/docs/tutorials/filtering-tweets-by-location)
