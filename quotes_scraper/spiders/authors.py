import scrapy
from quotes_scraper.items import AuthorItem

class AuthorsSpider(scrapy.Spider):
    name = "authors"
    start_urls = ["http://quotes.toscrape.com"]

    def parse(self, response):
        # Збираємо посилання на авторів
        author_links = response.css("small.author ~ a[href*='/author/']::attr(href)").getall()
        author_links = list(set(author_links))  # Унікальні посилання
        for link in author_links:
            yield response.follow(link, self.parse_author)
        
        # Переходимо на наступну сторінку
        next_page = response.css("li.next a::attr(href)").get()
        if next_page:
            yield response.follow(next_page, self.parse)

    def parse_author(self, response):
        item = AuthorItem()
        item["fullname"] = response.css("h3.author-title::text").get().strip()
        item["born_date"] = response.css("span.author-born-date::text").get()
        item["born_location"] = response.css("span.author-born-location::text").get()
        item["description"] = response.css("div.author-description::text").get().strip()
        yield item
