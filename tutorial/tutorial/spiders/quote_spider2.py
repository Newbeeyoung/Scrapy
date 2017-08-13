import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes2"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
    ]

    def parse(self, response):
        text=""
        for quote in response.css('div.quote'):
            l={
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.css('small.author::text').extract_first(),
                'tags': quote.css('div.tags a.tag::text').extract(),
            }
            text=text+"text:"+''.join(l['text']).encode('utf-8')+"\t"+"author:"+''.join(l['author']).encode('utf-8')+"\t"+"tags:"+''.join(l['tags']).encode('utf-8')

        with open('sets.txt',"a") as s:
                s.write(text)

        next_page = response.css('li.next a::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield  scrapy.Request(next_page, callback=self.parse)