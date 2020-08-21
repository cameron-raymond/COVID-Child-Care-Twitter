# Notebooks Directory

**Purpose:** Collect all relevant Tweet's pertaining to the reopening of schools in the COVID-19 pandemic between Jan. 1, 2020 and Sept. 15, 2020.

All data collected was done so in accordance with Twitter community guidelines. This project makes use of Twitter's [premium search API](https://developer.twitter.com/en/docs/tweets/search/overview/premium), which allows for access to Twitter's full archive of Tweets dating back to 2006. Below is a list of the filter's used to obtain the dataset. For a full list of operators available for this API see [here](https://developer.twitter.com/en/docs/tweets/search/overview/premium#AvailableOperators).

## Search Terms

* **Time-frame:** Feb. 15, 2020 - Sept. 15, 2020
* **Geo:** Canada, with province-by-province breakdown
* **Hashtags:**
  * \#safeseptember
  * \#unsafeseptember
  * \#safeseptember
  * \#safeseptemberAB
  * \#safeseptemberBC
  * \#safeseptemberMB
  * \#safeseptemberNB
  * \#safeseptemberNL
  * \#safeseptemberNS
  * \#safeseptemberON
  * \#safeseptemberPEI
  * \#safeseptemberQC
  * \#safeseptemberSK
  * \#safeseptemberYT
  * \#unsafeseptember
  * \#unsafeseptemberAB
  * \#unsafeseptemberBC
  * \#unsafeseptemberMB
  * \#unsafeseptemberNS
  * \#unsafeseptemberON
  * \#unsafeseptemberQC
* **Keywords:**
  * For each pillar, one term must be satisfied. All pillars must be satisfied.
  1. Elements of COVID:
     1. covid(-19)
     2. coronavirus
     3. virus
     4. pandemic
     5. (lock)(shut)down
     6. closure(s)
     7. (re)open
     8. risk
     9. safe(ty)(ly).
  2. Elements of School and Childcare:
     1. (pre)school(s)
     2. class(room)(s),
     3. (online)(distance)(remote) learning
     4. (day)(child)care
  3. Elements of Children/Parental Anxiety:
     1. child(ren)
     2. toddler(s)
     3. kid(s)
     4. parent(s)
     5. mom(s)
     6. mothers(s)
     7. dad(s)
     8. father(s)
     9. parent(s)
* **Mentions<sup>1</sup>:**
  * Premiers
    * Jason Kenny, [@jkenney](https://twitter.com/jkenney) (AB)
    * John Horgan, [@jjhorgan](https://twitter.com/jjhorgan) (BC)
    * Brian Pallister, [@BrianPallister](https://twitter.com/BrianPallister) (MB)
    * Blaine Higgs, [@blainehiggs](https://twitter.com/blainehiggs) (NB)
    * Dwight Ball, [@PremierofNL](https://twitter.com/PremierofNL) (NL)
    * Caroline Cochrane, [@CCochrane_NWT](https://twitter.com/CCochrane_NWT) (NT)
    * Stephen McNeil, [@StephenMcNeil](https://twitter.com/StephenMcNeil) (NS)
    * Joe Savikataaq, [@JSavikataaq](https://twitter.com/JSavikataaq) (NU)
    * Doug Ford, [@fordnation](https://twitter.com/fordnation) (ON)
    * Dennis King, [@dennyking](https://twitter.com/dennyking) (PE)
    * François Legault, [@francoislegault](https://twitter.com/francoislegault) (QC)
    * Scott Moe, [@PremierScottMoe](https://twitter.com/PremierScottMoe) (SK)
    * Sandy Silver, [@Premier_Silver](https://twitter.com/Premier_Silver) (YT)
  * Education Ministers
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
2. Collect all tweets that are: from Canadians<sup>2</sup> and satisfy one of the hashtag, keyword or mention rules.
3. Store collection of tweets in Pandas dataframe, and only keep relevant features (data, geo-code, text, author, *etc.*)
4. Add an extra column that is the cleaned tweet text.
   1. Add other derived columns (is_retweet, city/province, *etc.*)
5. Save dataframe to CSV
6. Solve the pandemic 🎊

<sup>1</sup> Tweets that mention a premier should also contain the keywords ((covid OR covid-19) (school OR childcare OR daycare))

<sup>2</sup> For more information on what tweets are geo-coded, see [Twitter's geo-filtering guide](https://developer.twitter.com/en/docs/tutorials/filtering-tweets-by-location)
