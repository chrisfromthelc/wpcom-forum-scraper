# -*- coding: utf-8 -*-
import scrapy


class TagSpiderSpider(scrapy.Spider):
    name = 'tag_spider'
    allowed_domains = ['en.forums.wordpress.com']
    start_urls = ['https://en.forums.wordpress.com/tags/seo'] # edit this URL for the tag URL you want

    def parse(self, response):
        # follow links to topic pages
        for href in response.css('.topictitle a::attr(href)'):
            yield response.follow(href, self.parse_topic)

        #follow pagination links
        for href in response.css('.nav a.next::attr(href)'):
            yield response.follow(href, self.parse)

        # next_page = response.css('.nav a.next::attr(href)').extract_first()
        # if next_page is not None:
        #     yield response.follow(next_page, callback=self.parse)

    def parse_topic(self, response):
        def extract_first_with_css(query):
            return response.css(query).extract_first().strip()

        def extract_with_css(query):
            return response.css(query).extract()

        yield {
            'topic_title': extract_first_with_css('.topictitle div h2::text'),
            'topic_url': response.request.url,
            'topic_messages_text': ''.join(extract_with_css('.threadpost .post p::text,.threadpost .post li::text, .threadpost .post a::text')).replace("\n", " "),
        }

        pass
