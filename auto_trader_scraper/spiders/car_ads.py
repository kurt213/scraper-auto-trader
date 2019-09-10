import scrapy
from scrapy.http import Request
from pathlib import Path

from auto_trader_scraper.custom_functions import *

class CarSpider(scrapy.Spider):
    name = "car_ads"
    base_source = Path(__file__).parent
    file_source = (base_source / "../url_lists/models_list.txt").resolve()
    with open(file_source, 'r') as f:
        start_urls = [line.rstrip('\n') for line in f]

    def parse(self, response):
        for ad in response.xpath('//li[@class="search-page__result"]'):

            key_specs_r = response.xpath('.//ul[contains(@class, "listing-key-specs")]/li/text()').getall()
            key_specs_dict = keySpecs(key_specs_r)

            seller_type_raw = ad.xpath('.//div[contains(@class, "seller-type")]/text()').get()
            seller_type = replaceMultiple(seller_type_raw, ['\n', '-'], '')
            
            yield {
                'title': ad.xpath('.//h2[contains(@class, "listing-title")]/a/text()').get(),
                'url': ad.xpath('.//h2[contains(@class, "listing-title")]/a/@href').get(),
                'ad_id': ad.xpath('.//h2[contains(@class, "listing-title")]/a/@href').re(r'(?:advert\/)(.*)(?:\?)'),
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
                'listing_description': ad.xpath('.//p[contains(@class, "listing-description")]/text()').get(),
                'seller_type': seller_type,
                'miles_from_wc2r': ad.xpath('.//div[contains(@class, "seller-location")]/text()').re(r'\d+'),
                'price': ad.xpath('.//div[contains(@class, "vehicle-price")]/text()').get()
            }