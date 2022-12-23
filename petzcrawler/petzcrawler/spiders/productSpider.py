import scrapy

class ProductspiderSpider(scrapy.Spider):
    name = 'productSpider';
    allowed_domains = ['www.petz.com.br'];

    def start_requests(self):
        urls = [
            'https://www.petz.com.br/outros-pets/coelhos?page=1&np=90'
        ];

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse);

    def parse(self, response):
        page = response.url.split("/")[-2];
        filename = f'quotes-{page}.html';
        with open(filename, 'wb') as f:
            f.write(response.body);
        self.log(f'Saved file {filename}');