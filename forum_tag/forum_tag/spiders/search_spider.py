# -*- coding: utf-8 -*-
import scrapy


class TagSpiderSpider(scrapy.Spider):
    name = 'tag_spider'
    allowed_domains = ["wordpress.com"]
    start_urls = ['https://wordpress.com/forums/topic-tag/seo/'] # edit this URL for the tag URL you want
    custom_settings = {'CLOSESPIDER_PAGECOUNT': 100}

    def parse(self, response):
        # follow links to topic pages
        for href in response.css('a.jetpack-instant-search__search-result-title-link::attr(href)'):
            yield response.follow(href, self.parse_topic)

        #follow pagination links
        for href in response.css('.bbp-pagination-links a.next::attr(href)'):
            yield response.follow(href, self.parse)

        # next_page = response.css('.nav a.next::attr(href)').extract_first()
        # if next_page is not None:
        #     yield response.follow(next_page, callback=self.parse)

    def parse_topic(self, response):
        def extract_first_with_css(query):
            return response.css(query).extract_first().strip()

        def extract_with_xpath(query):
            return response.xpath(query).extract()

            # for post in response:
            #
            #     item = {}
            #
            #     item['topic_title'] = extract_first_with_css('h1::text').replace("\xa0", " ")
            #     item['topic_url'] = response.request.url
            #     item['topic_messages_text'] = ''.join(extract_with_xpath('//div[@class="bbp-reply-content"]/p/text()')).replace("\n", " ").replace("\xa0", " ")
            #
            #     return item


        yield {
            'topic_title': extract_first_with_css('h1::text').replace("\xa0", " "),
            'topic_url': response.request.url,
            'topic_messages_text': ' '.join(extract_with_xpath('//div[@class="bbp-reply-content"]/p/text()')).replace("\n", " ").replace("\xa0", " ")
        }

        pass
