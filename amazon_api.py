from amazon.api import AmazonAPI

access_key = ''
secret_key = ''
associate_id = ''

amazon = AmazonAPI(access_key, secret_key, associate_id, region="JP")
products = amazon.search(Keywords='kindle', SearchIndex='All')
# print(vars(products))

