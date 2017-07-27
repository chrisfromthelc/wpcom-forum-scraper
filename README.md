# WordPress.com Forum Scraper 2: Electric Boogaloo
Scrapy-powered forum scraper for WordPress.com forums to scrape based on tags.

This Scrapy crawler is intended to scrape the public WordPress.com forums based on a tag's URL, and save the resulting post title, URL, and text of the messages into a MySQL database. You can install the needed packages using `pip install -r requirements.txt`; it's recommended to run this in a virtualenv.

1. Use the `create.sql` file to create your database table.
2. Update the authentication information for MySQL in `forum_tag/forum_tag/pipelines.py`
3. Edit the `start_urls` in `forum_tag/forum_tag/spiders/tag_spider.py` to reflect the URL for the tag/tags that you want to scrape.
4. Run the spider by using `scrapy runspider forum_tag/forum_tag/spiders/tag_spider.py`

While this is written specifically for the WordPress.com forums, it should be easily modifiable to work on any forum software by tweaking the selectors in the `parse` and `parse_topic` functions in `tag_spider.py`.
