from django.conf import settings
from django.conf.urls.static import static
from process.views import process, scraping_process2
from django.urls import path

urlpatterns =[
    path('', process, name='process'),
    path('partes', scraping_process2, name='parts'),
]

if settings.DEBUG:
   urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)