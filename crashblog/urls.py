from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from django.contrib import admin
from django.urls import path, include

from core.views import robots_txt
from crashblog.sitemaps import PostSitemap, CategorySitemap

sitemaps = {'category': CategorySitemap, 'post': PostSitemap}

urlpatterns = [
                  path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
                  path('robots.txt', robots_txt, name='robots_txt'),
                  path('admin/', admin.site.urls),

                  path('', include('core.urls')),
                  path('', include('blog.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
