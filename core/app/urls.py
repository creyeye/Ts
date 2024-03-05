from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('category/<int:pk>/', views.category_list, name='category_list')
]
