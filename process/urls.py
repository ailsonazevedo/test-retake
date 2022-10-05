from django.conf import settings
from django.conf.urls.static import static
from process.views import home, process
from django.urls import path

urlpatterns =[
    path('', home, name='home'),
    path('process', process, name='process'),
]

if settings.DEBUG:
   urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)