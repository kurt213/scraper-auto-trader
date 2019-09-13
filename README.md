# scraper-auto-trader
A python project utilising the scrapy framework to scrape Auto Trader adverts data. 

Data to be used for a personal Machine Learning project to predict car ad pricing based on a number of feature variables.

NOTE: This project is for educational purposes and should not be used for purposes that would break the TOS of the Auto Trader platform.

## Getting Started

These instructions will get the project set up on your local machine for running the tool.

### Prerequisites

1. Python (version 3+) installed
2. pip package installer installed (usually installed with python versions later than 2.7.9 or 3.4)
3. (optional) virtualenv package installed 
4. requirements.txt run to install project dependencies

## Running Package

There are three spiders that will crawl Auto Trader for the necessary data:

1. car_makes - Spider for crawling all root car makes URLs e.g. Ford, Mercedes
2. car_models - Spider for crawling all root car models URLs e.g. Ford Focus, Mercedes GLA Class
3. car_ads - Spider for crawling all ad pages for provided car models

These three spiders have been separated out to give flexibility to the user if they want to scrape a specific make and model of car for ad data.

### Running Spiders

The three spiders need to be run in the sequential order as stated above.

#### car_makes

```
scrapy crawl car_makes
```
- Running this spider will populate the *url_lists/makes_list.txt* file with a list of URLs for all car makes.
- Before running the next spider, the user can remove URLs for car makes they do not want to scrape.

#### car_models
```
scrapy crawl car_models
```
- Running this spider will populate the *url_lists/models_list.txt* file with a list of URLs for all car models that were present in the *makes_list.txt* file.
- Before running the final spider, the user can remove URLs for car models they do not want to scrape.

#### car_ads
```
scrapy crawl car_ads -o ads_output.csv
```
**NOTE:** You can also output a JSON file and change the name of the output file by changing the 'ads_output.csv' parameter when running the spider. 

- This spider will loop through the *models_list.txt* file, finding all search results pages and will scrape the following information:
```
[
    'make',
    'model'
    'title',
    'url',
    'ad_id',
    'number_images',
    'attention_grabber',
    'extra_detail',
    'category_damage',
    'year',
    'registration',
    'body_type',
    'mileage',
    'engine_size',
    'bhp',
    'transmission',
    'fuel_type',
    'doors',
    'listing_description',
    'seller_type',
    'miles_from_wc2r',
    'price'
]
```

#### logs
When the spiders are running, there will be some high level information in the command prompt / terminal while running. 

For more detail, a *log.txt* file is generated that shows more detailed information such as time spider run, errors, number of pages scraped etc.

## Extra Information

Hope you enjoy this scraping tool. Please let me know your feedback or suggestion for improvements. 

#### To Do
- add logging information to show progress to end user in command prompt