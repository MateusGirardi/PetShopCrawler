# PetShopCrawler

pipreqs --encoding utf-8 "./venv"

pip install -r /tmp/requirements.txt

# Crawling
 scrapy crawl cobasiProductSpider -O cobasiResults.json
 scrapy crawl petzProductSpider -O petzResults.json

# XML
pip install scrapy-dynamic-spiders
https://stackoverflow.com/questions/5033955/xpath-select-text-node

# css
https://stackoverflow.com/questions/34255232/exclude-div-from-scrapy

# Json
Por padrão o encode do json exportado é encoding (\uXXXX sequences) for historic reasons.
Para que o json utilize o encoding utf-8 é necessário deixar a configuração explícita.
https://docs.scrapy.org/en/latest/topics/feed-exports.html#std-setting-FEED_EXPORT_ENCODING
FEED_EXPORT_ENCODING = 'utf-8'

json.loads(response.body_as_unicode().replace("'", '"'));

response.json;

json.loads(response.text);

# Parse Json
json.loads()
Função retira todos os espaços do texto e converte o json em string para o json formatado sem aspas.
Com ele não precisamos retirar manualmente os \n \t e " do texto.

# Scrapy
css
xpath

# Splash

download and install docker
configure docker

docker pull scrapinghub/splash

docker run -it -p 8050:8050 --rm scrapinghub/splash

https://stackoverflow.com/questions/48834080/scrapy-splash-crawling-javascript-website
https://splash.readthedocs.io/en/stable/api.html#executing-custom-javascript-code-within-page-context

Se não passar o parâmetro --js-cross-domain-access, o script javascript não é executado.

docker run -it -p 8050:8050 scrapinghub/splash --js-cross-domain-access

docker run -it -p 8050:8050 scrapinghub/splash --max-timeout 3600

docker run -it -p 8050:8050 scrapinghub/splash --disable-private-mode -v3 --js-cross-domain-access --max-timeout 3600

# Selenium

https://chromedriver.chromium.org/downloads

# for Chrome driver
from shutil import which

SELENIUM_DRIVER_NAME = 'chrome'
SELENIUM_DRIVER_EXECUTABLE_PATH = which('chromedriver')
print("Mateus : " + which('chromedriver'))
SELENIUM_DRIVER_ARGUMENTS = ['--headless']

DOWNLOADER_MIDDLEWARES = {
    'scrapy_selenium.SeleniumMiddleware': 800
}
