from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    def items(self):
        return ['setup'] # setup 페이지를 사이트맵에 포함

    def location(self, item):
        return reverse(item)