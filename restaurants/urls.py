
from django.urls import path, re_path


from restaurants.views import (
    RestaurantListView,
    RestaurantDetailView,
    RestaurantCreatView,
    RestaurantUpdateView,

  #  MexicanRestaurantListView,
   # AsianFusionRestaurantListView,

)

urlpatterns = [
    path('', RestaurantListView.as_view(), name='list'),
    path('create/', RestaurantCreatView.as_view(), name='create'),
    #re_path('(?P<slug>[\w-]+)/edit/$', RestaurantUpdateView.as_view(), name='edit'),
    re_path('(?P<slug>[\w-]+)/$', RestaurantUpdateView.as_view(), name='detail'),

]

"""
 path('restaurants/create', restaurant_createview), 
    # re_path(r'^restaurants/(?P<slug>\w+)/$', RestaurantListView.as_view()),
   path('restaurants/asian/', AsianFusionRestaurantListView.as_view()), 

"""
