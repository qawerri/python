from django.urls import path
from .views import index, top_sellers, adv_post, adv_detail

urlpatterns = [
    path('', index, name='main_page'),
    path('top-sellers/', top_sellers, name='top-sellers'),
    path('advertisement-post/', adv_post, name='advertisement-post'),
    path('advertisement/<int:pk>', adv_detail, name='adv-detail'),
]