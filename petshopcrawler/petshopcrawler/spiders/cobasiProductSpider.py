import scrapy
import json
from ..items import CobasicrawlerItemCategory
from ..items import CobasicrawlerItemProduct

class CobasiProductSpider(scrapy.Spider):
    name = 'cobasiProductSpider';
    allowed_domains = ['cobasi.com.br'];
    start_urls = ['https://cobasi.com.br','https://mid-back.cobasi.com.br/catalog/products/categories/'];
    split = "/c/";
    def start_requests(self):
        urls = [
            'https://cobasi.vteximg.com.br/arquivos/categorias.xml'
        ];

        for url in urls:
            yield scrapy.Request(url = url,callback=self.parse);

    def parse(self, response):
        item = CobasicrawlerItemCategory();
        for loc in response.xpath("//url/loc"):
            item["category"] = loc.xpath("text()").get();
            next_page = item["category"];
            next_page = self.start_urls[1]+next_page[next_page.find(self.split) + len(self.split):];
            for i in range(1,51):
                yield scrapy.Request(next_page + f"?page={i}&pageSize=50", callback=self.productParse);

    def productParse(self, response):
        item_product = CobasicrawlerItemProduct();
        j_response = json.loads(response.text);
        for product in j_response["products"]:
            self.cleanProduct(product);
            for sp in product["items"]:
                for sell in sp["sellers"]:
                    item_product["brand"] = product["brandName"];
                    item_product["url"] = product["link"];
                    item_product["name"] = sp["completeName"];
                    item_product["id"] = sp["id"];
                    item_product["price"] = sell["price"];
                    yield item_product;

    def cleanProduct(self,p):
        del p["name"];
        del p["id"];
        del p["clusterHighlights"];
        del p["linkText"];
        del p["metaTagDescription"];
        del p["reference"];
        del p["status"];
        del p["title"];
        del p["brandId"];
        del p["categoryId"];
        del p["rating"];





'''
XMLFeedSpider version

import scrapy
from ..items import CobasicrawlerItemCategory

class CobasiProductSpider(scrapy.spiders.XMLFeedSpider):
    name = 'cobasiProductSpider';
    allowed_domains = ['cobasi.com.br'];
    start_urls = ['https://cobasi.vteximg.com.br/arquivos/categorias.xml'];
    iterator = 'iternodes';  # This is actually unnecessary, since it's the default value
    itertag = 'loc';
    def parse_node(self, response, node):
        item = CobasicrawlerItemCategory();
        item['category'] = node.xpath("text()").get();
        return item;

'''
