import scrapy
import json
from ..items import PetzcrawlerItemPage
from ..items import PetzcrawlerItemNumberPage
from ..items import PetzcrawlerItemProduct

class PetzProductSpider(scrapy.Spider):
    name = 'petzProductSpider';
    allowed_domains = ['petz.com.br'];
    start_urls = ['https://www.petz.com.br'];

    def start_requests(self):
        urls = [
            'https://www.petz.com.br'
        ];

        for url in urls:
            yield scrapy.Request(url = url,callback=self.parse);


    def parse(self, response):
        page_item = PetzcrawlerItemPage();
        for menu in response.css('.dropdown-menu'):
            for page in menu.css('.submenu-text'):
                page_item['page'] = page.css('a::attr(href)').get();
                next_page = response.urljoin(page_item['page']);
                yield scrapy.Request(next_page, callback=self.numberPageParse);


    def numberPageParse(self, response):
        page_number = PetzcrawlerItemNumberPage();
        for pages in response.css('p#paginas'):
            for page in pages.css('span.paginaAtual'):
                page_number['page'] = response.url;
                page_number['pageNumber'] = response.url+"?page=1";
                yield scrapy.Request(page_number['pageNumber'] , callback=self.productParse);
                #yield page_number;
            for page in pages.css('.pagina:not([class*="setaCor"])'):
                page_number['page'] = response.url;
                page_number['pageNumber'] = response.urljoin(page.css('a::attr(href)').get());
                yield scrapy.Request(page_number['pageNumber'] , callback=self.productParse);
                #yield page_number;

    def productParse(self, response):
        item_product = PetzcrawlerItemProduct()
        for jproduct in response.css('textarea.jsonGa'):
            j_inf = json.loads(jproduct.css(".jsonGa::text").get());# json.loads() - parse to json
            item_product['url'] = response.url;
            item_product['price'] = j_inf['price'];
            item_product['name'] = j_inf['name'];
            item_product['id'] = j_inf['id'];
            item_product['sku'] = j_inf['sku'];
            item_product['category'] = j_inf['category'];
            item_product['brand'] = j_inf['brand'];
            yield item_product;

