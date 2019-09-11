import scrapy
from scrapy.http import Request
from pathlib import Path
import math
import re

from auto_trader_scraper.custom_functions import *

class CarSpider(scrapy.Spider):
    name = "car_ads"
    base_source = Path(__file__).parent
    file_source = (base_source / "../url_lists/models_list.txt").resolve()
    with open(file_source, 'r') as f:
        start_urls = [line.rstrip('\n') for line in f]

    def parse(self, response):
        page_results = len(response.xpath('//li[@class="search-page__result"]'))
        total_results = response.xpath('//h1[contains(@class, "search-form__count")]/text()').re(r'\d+')
        try:
            pages_to_search = math.ceil(int(total_results[0]) / page_results)
        except:
            print("Error extracting total results. Default to 1")
            pages_to_search = 1
        url_list = [response.url + '&page=' + str(page + 1) for page in range(pages_to_search)]
        print(url_list)
        for url in url_list:
            yield Request(url, callback = self.parseAds)

    def parseAds(self, response):

        for ad in response.xpath('//li[@class="search-page__result"]'):

            key_specs_r = ad.xpath('.//ul[contains(@class, "listing-key-specs")]/li/text()').getall()
            key_specs_dict = keySpecs(key_specs_r, response.url)

            seller_type_raw = ad.xpath('.//div[contains(@class, "seller-type")]/text()').get()
            if seller_type_raw:
                seller_type = replaceMultiple(seller_type_raw, ['\n', '-'], '')
            else:
                seller_type = 'N/A'
            car_make = response.url
            
            yield {
                'make': key_specs_dict['vehicle_make'],
                'model': key_specs_dict['vehicle_model'],
                'title': ad.xpath('.//h2[contains(@class, "listing-title")]/a/text()').get(),
                'url': ad.xpath('.//h2[contains(@class, "listing-title")]/a/@href').get(),
                #'ad_id': ad.xpath('.//h2[contains(@class, "listing-title")]/a/@href').re(r'(?:advert\/)(.*)(?:\?)'),
                'ad_id': ad.xpath('.//h2[contains(@class, "listing-title")]/a/@href').re(r'(?:\/)([0-9]{10,20})(?:\?)'),
                'number_images': ad.xpath('.//div[contains(@class, "listing-image-count")]/text()')[1].re(r'\d+'),
                'attention_grabber': ad.xpath('.//p[contains(@class, "listing-attention-grabber")]/text()').get(),
                'category_damage': ad.xpath('.//ul[contains(@class, "write-off-cat")]/li/a/@data-writeoff-cat').get(),
                'year': key_specs_dict['year'],
                'registration': key_specs_dict['registration'],
                'body_type': key_specs_dict['body_type'],
                'mileage': key_specs_dict['mileage'],
                'engine_size': key_specs_dict['engine_size'],
                'bhp': key_specs_dict['bhp'],
                'transmission': key_specs_dict['transmission'],
                'fuel_type': key_specs_dict['fuel_type'],
                'doors': key_specs_dict['doors'],
                'listing_description': ad.xpath('.//p[contains(@class, "listing-description")]/text()').get(),
                'seller_type': seller_type,
                'miles_from_wc2r': ad.xpath('.//div[contains(@class, "seller-location")]/text()').re(r'\d+'),
                'price': ad.xpath('.//div[contains(@class, "vehicle-price")]/text()').get()
            }