from django.urls import path
from core import views
from core.views import product_list

from shopback.api.views import product_detail

urlpatterns=[

    path('products/', product_list),
    path('products/<int:product_id>', product_detail),
path('categories/', views.category_list),
path('categories/<int:pk>/', views.category_detail,
path('categories/<int:pk>/products/', views.category_products)

]