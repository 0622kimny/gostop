from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from gostop_app.sitemaps import StaticViewSitemap
from django.views.generic.base import TemplateView

sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('gostop_app.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path("ads.txt", TemplateView.as_view(template_name="ads.txt", content_type="text/plain")),
    path("robots.txt", TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
]