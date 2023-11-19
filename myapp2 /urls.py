from django.urls import path
from myapp2.views import get_orders_by_user, get_orders_last_7_days, get_orders_last_30_days, get_orders_last_year, create_product

urlpatterns = [
    path('get_orders_by_user/<int:user_id>/', get_orders_by_user, name='get_orders_by_user'),
    path('get_orders_last_7_days/<int:user_id>/', get_orders_last_7_days, name='get_orders_about_week'),
    path('get_orders_last_30_days/<int:user_id>/', get_orders_last_30_days, name='get_orders_about_month'),
    path('get_orders_last_year/<int:user_id>/', get_orders_last_year, name='get_orders_about_year'),
    path('create_product/', create_product, name='create_product'),
]
