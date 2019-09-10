
# get list of makes
# response.xpath('//div[@data-temp="make-flyout"]/div[contains(@class, "js-flyout-scrollable-options")]/div/button/@data-selected-value').getall()

# get list of models
# response.xpath('//div[@data-temp="model-flyout"]/div[contains(@class, "js-flyout-scrollable-options")]/div/button/@data-selected-value').getall()

# Abarth example - 7 pages for 63 cars - 9 per page

## Advert info - 12 minimum dependent, 1 independent variables currently

# whole advert

# ********
# NOTE: Need to have a './/' when looping through a response

# Car title
# response.xpath('//h2[contains(@class, "listing-title")]/a/text()').getall()

# Car URL
# response.xpath('//h2[contains(@class, "listing-title")]/a/@href').getall()

# Car ID
# take from URL with regex

# listing number of images
# response.xpath('//div[contains(@class, "listing-image-count")]/text()').getall()
# NOTE: Need to trip out \n and all spaces, leaving only number

# listing attention grabber
#response.xpath('//p[contains(@class, "listing-attention-grabber")]/text()').getall()

# unordered list of key specs
#response.xpath('//ul[contains(@class, "listing-key-specs")]/li/text()').getall()

# unordered list cat exists
# response.xpath('//ul[contains(@class, "write-off-cat")]/li/a/@data-writeoff-cat').getall()


# age
# body type
# mileage
# engine size
# engine power
# transmission
# fuel type

# listing description
# response.xpath('//p[contains(@class, "listing-description")]/text()').getall()


# seller type
# response.xpath('//div[contains(@class, "seller-type")]/text()').getall()

# seller town
# response.xpath('//span[contains(@class, "seller-town")]/text()').getall()

# seller location
# response.xpath('//div[contains(@class, "seller-location")]/text()').re(r'\d+')

# vehicle price