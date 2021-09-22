from django.urls import path
from .views import *
urlpatterns = [
    path('store/', store, name='store'),
    path('store/<slug:slug>/', store, name='product_by_category'),
    path('store/<slug:slug>/<slug:product_slug>/', product_detail, name='product_detail'),
]