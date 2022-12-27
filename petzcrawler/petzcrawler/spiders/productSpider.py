import scrapy
import json
from ..items import PetzcrawlerItemPage
from ..items import PetzcrawlerItemNumberPage
from ..items import PetzcrawlerItemProduct

pages = [];

class ProductSpider(scrapy.Spider):
    name = 'productSpider'
    allowed_domains = ['www.petz.com.br']
    start_urls = ['https://www.petz.com.br']

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
        page_product = PetzcrawlerItemProduct()
        for jproduct in response.css('textarea.jsonGa'):
            page_product['page'] = response.url;
            page_product['product'] = json.loads(jproduct.css(".jsonGa::text").get()); # json.loads() - parse to json
            yield page_product;

