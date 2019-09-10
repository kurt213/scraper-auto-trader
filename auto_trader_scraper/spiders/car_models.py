import scrapy
from pathlib import Path

class CarSpider(scrapy.Spider):
    base_source = Path(__file__).parent
    file_source = (base_source / "../url_lists/makes_list.txt").resolve()
    with open(file_source, 'r') as f:
        start_urls = [line.rstrip('\n') for line in f]
    name = "car_models"

    def parse(self, response):
        base_path = Path(__file__).parent
        file_path = (base_path / "../url_lists/models_list.txt").resolve()

        output = response.xpath('//div[@data-temp="model-flyout"]/div[contains(@class, "js-flyout-scrollable-options")]/div/button/@data-selected-value').getall()
        base_url = response.request.url + '&model='
        models_list = []
        for o in output:
            o_format = o.replace(" ", "%20").upper()
            models_list.append(base_url + o_format)

        with open (file_path, 'a') as f:
            for m in models_list:
                f.write(str(m) + "\n")
