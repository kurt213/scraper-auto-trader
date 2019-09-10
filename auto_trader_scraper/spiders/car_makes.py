import scrapy
from pathlib import Path

class CarSpider(scrapy.Spider):
    name = "car_makes"
    start_urls = [
        "https://www.autotrader.co.uk/car-search?sort=sponsored&radius=20&postcode=wc2r2ns"
    ]

    def parse(self, response):
        base_path = Path(__file__).parent
        file_path = (base_path / "../url_lists/makes_list.txt").resolve()

        output = response.xpath('//div[@data-temp="make-flyout"]/div[contains(@class, "js-flyout-scrollable-options")]/div/button/@data-selected-value').getall()
        base_url = "https://www.autotrader.co.uk/car-search?sort=sponsored&radius=20&postcode=wc2r2ns&onesearchad=Used&onesearchad=Nearly%20New&onesearchad=New&make="
        makes_list = []
        for o in output:
            o_format = o.replace(" ", "%20").upper()
            makes_list.append(base_url + o_format)

        with open (file_path, 'w') as f:
            for m in makes_list:
                f.write(str(m) + "\n")
