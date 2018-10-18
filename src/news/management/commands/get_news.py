import feedparser 
import re
import dateutil.parser
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from news.models import News

class Command(BaseCommand):

    def handle(self, *args, **options):
        google_trends_rss = feedparser.parse("https://trends.google.com/trends/trendingsearches/daily/rss?geo=US")
        cnn_news_rss = feedparser.parse("http://rss.cnn.com/rss/edition_us.rss")

        # for trend in google_trends_rss['entries']:
        #     for news in cnn_news_rss['entries']:
        #         if re.sub('!@#$,.', '',trend['title'].lower()) in re.sub('!@#$,.', '',news['title'].lower()): 
        #             n_title = news['title']
        #             n_link = news['link']
        #             n_trend = trend['title']
        #             try:
        #                 n_pub_date = dateutil.parser.parse(news.published)
        #             except AttributeError:
        #                 n_pub_date = None

        #             n, created = News.objects.get_or_create(
        #                 title = n_title,
        #                 pub_date = n_pub_date,
        #                 link = n_link,
        #                 trend = n_trend
        #                 )

        '''to get more results just comment loop upper and uncomment this code'''
        for trend in google_trends_rss['entries']:
            for news in cnn_news_rss['entries']:
                for word in re.sub('!@#$,.', '',trend['title'].lower()).split(' '):
                    if word in re.sub('!@#$,.', '',news['title'].lower()): 
                        n_title = news['title']
                        n_link = news['link']
                        n_trend = trend['title']
                        try:
                            n_pub_date = dateutil.parser.parse(news.published)
                        except AttributeError:
                            n_pub_date = None
                        n, created = News.objects.get_or_create(
                            title = n_title,
                            pub_date = n_pub_date,
                            link = n_link,
                            trend = n_trend
                        )
        return('News are renewed')