from django.urls import path
from . import views 


urlpatterns = [
    
    path('list/', views.ListFoodCategory),
    path('details/', views.ListFoodDetails),
    path('dishdetails/', views.DishDetails),
]