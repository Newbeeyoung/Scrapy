import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
   
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        quotetext= 'quotes-%s.txt' % page
   
        with open(quotetext,'wb') as q:
        	q.write(self.findquote(response))
        self.log('Saved file %s' % filename)

    def findquote(self, response):
        string=""
    	for quote in response.css("div.quote"):
    	    text=quote.css("span.text::text").extract()
    	    string+=text[0].encode("utf-8")+"\n\t\t"
    	return string
