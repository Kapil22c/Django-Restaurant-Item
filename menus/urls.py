from django.urls import path, re_path


from .views import (
    ItemListView,
    ItemDetailView,
    ItemCreateView,
    ItemUpdateView,
)

urlpatterns = [
    path('create/', ItemCreateView.as_view(), name='create'),
   # re_path('(?P<pk>\d+)/edit/$', ItemUpdateView.as_view(), name='update'),
    re_path('(?P<pk>\d+)/$', ItemUpdateView.as_view(), name='detail'),
    path('', ItemListView.as_view(), name='list'),

]
