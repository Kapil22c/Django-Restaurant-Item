"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from profiles.views import ProfileFollowToggle, RegisterView, activate_user_view
from menus.views import HomeView


# from restaurants.views import (
#     restaurant_listview,
#     RestaurantListView,
#     RestaurantDetailView,
#     restaurant_createview,
#     RestaurantCreatView,
#
#   #  MexicanRestaurantListView,
#    # AsianFusionRestaurantListView,
#
# )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),

    path('register/', RegisterView.as_view(), name='register'),
    path('activate/(?P<code>[a-z0-9].*)/', activate_user_view, name='activate'),

    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('u/', include(('profiles.urls', 'profiles'), namespace='profiles')),

    path('profile-follow/', ProfileFollowToggle.as_view(), name='follow'),

    path('items/', include(('menus.urls', 'menus'), namespace='menus')),
    path('restaurants/', include(('restaurants.urls', 'restaurants'), namespace='restaurants')),



    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('content/', TemplateView.as_view(template_name='content.html'), name='content'),


]
'''
#  path('restaurants/', RestaurantListView.as_view(), name='restaurants'),
#  #path('restaurants/create', restaurant_createview),
#  path('restaurants/create', RestaurantCreatView.as_view(), name='restaurants-create'),
#  # re_path(r'^restaurants/(?P<slug>\w+)/$', RestaurantListView.as_view()),
#  re_path('restaurants/(?P<slug>[\w-]+)/$', RestaurantDetailView.as_view(), name='restaurant-detail'),
# # path('restaurants/asian/', AsianFusionRestaurantListView.as_view()),

'''