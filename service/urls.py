from django.urls import path

from service.views import page, about, json_show


urlpatterns = [   
    path('service/<int:page_num>', page),
    path('about/<int:id>', about, name = 'about' ),
    path('json', json_show, name='json_show')
]