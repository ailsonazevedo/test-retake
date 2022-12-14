from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from process.views import (
    parts,
    parts_add,
    parts_delete, 
    process_add, 
    process_delete, 
    process_detail,
    process_update, 
    scraping_process1, 
    process, 
    scraping_process2
)


urlpatterns =[
    path('', process, name='process'),
    path('add', process_add, name='add_process'),
    path('add_parts', parts_add, name='add_parts'),
    path('detail/<int:pk>', process_detail, name='process_detail'),
    path('update/<int:pk>', process_update, name='process_update'),
    path('delete/<int:pk>', process_delete, name='process_delete'),
    path('partes', parts, name='parts'),
    path('parts/parte_delete/<int:pk>', parts_delete, name='parts_delete'),
    path('process1', scraping_process1, name='process1'),
    path('process2', scraping_process2, name='process2'),
]

if settings.DEBUG:
   urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)