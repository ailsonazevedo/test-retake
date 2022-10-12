from django.conf import settings
from django.conf.urls.static import static
from process.views import parts, process_delete, process_detail, scraping_process1, process, scraping_process2
from django.urls import path

urlpatterns =[
    path('', process, name='process'),
    path('detail/<int:pk>', process_detail, name='process_detail'),
    path('delete/<int:pk>', process_delete, name='process_delete'),
    path('partes', parts, name='parts'),
    path('process1', scraping_process1, name='process1'),
    path('process2', scraping_process2, name='process2'),
]

if settings.DEBUG:
   urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)