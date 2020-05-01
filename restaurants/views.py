import random
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView
from .forms import RestaurantCreateForm, RestaurantLocationCreateForm
from .models import RestaurantLocation
from django.template import RequestContext
# Create your views here.

"""
@login_required()   #login_url='/login/' in argument... for path...if you want it universal then there is another method

def restaurant_createview(request):
    # first form was commented... it is model form

    form = RestaurantLocationCreateForm(request.POST or None)
    errors = None
    if form.is_valid():
        if request.user.is_authenticated:
            instance = form.save(commit=False)
            instance.owner = request.user
            instance.save()

            return HttpResponseRedirect("/restaurants/")
        else:
            return HttpResponseRedirect("/login/")
    else:
        errors= form.errors
        # form = RestaurantLocationCreateForm()
    # if form.errors:
    #              # print(form.errors)
    #     errors = form.errors

        template_name = "restaurants/form.html"

        context = {"form": form, "errors": errors}

        return render(request, template_name, context)

"""

#     form = RestaurantCreateForm(request.POST or None)
#     errors = None
#    # print(request.GET)
#     #print(request.POST)
#    # if request.method == 'GET':
#     #    print('get data')
#     # if request.method == 'POST':
#     #     form = RestaurantCreateForm(request.POST)   .....because form is already done in first line
#      #   print('post data')
#       #  print(request.POST)
# #        title = request.POST.get("title")
# #        location = request.POST.get("location")
# #        category = request.POST.get("category")
#
#     if form.is_valid():
#         obj = RestaurantLocation.objects.create(
#             name = form.cleaned_data.get('name'),
#             location= form.cleaned_data.get('location'),
#             category = form.cleaned_data.get('category'),
#         )
#
#         return HttpResponseRedirect("/restaurants/")
#
#     if form.errors:
#         # print(form.errors)
#         errors = form.errors
#
#     template_name = "restaurants/form.html"
#
#     context = {"form": form, "errors": errors}
#     return render(request, template_name, context)

""" 
class HomeView(TemplateView):
    template_name = 'home.html'
    def get_context_data(self,*args, **kwargs):
        context =super(HomeView, self).get_context_data(*args, **kwargs)
        num = None
        some_list = [
            random.randint(0, 5000),
            random.randint(0, 5000),
            random.randint(0, 5000),
        ]
        condition_bool_item = True
        if condition_bool_item:
            num = random.randint(0, 5000)
        context = {
            "num": num,
            "some_list": some_list,
        }

        return context
"""
"""
def restaurant_listview(request):
    template_name = 'restaurants/restaurantlocation_list.html'
    queryset = RestaurantLocation.objects.all()
    context = {
        'object_list': queryset,
    }
    return render(request, template_name, context)

def restaurant_detailview(request, slug):
    template_name = 'restaurants/restaurantlocation_detail.html'
    obj = RestaurantLocation.objects.get(slug=slug)
    context = {
        'object': obj,
    }
    return render(request, template_name, context)
"""


class RestaurantListView(LoginRequiredMixin, ListView):
    #template_name = 'restaurants/restaurantlocation_list.html'
    def get_queryset(self):
        return RestaurantLocation.objects.filter(owner=self.request.user)
        # slug = self.kwargs.get("slug")
        # if slug:
        #     queryset = RestaurantLocation.objects.filter(
        #         Q(category__iexact=slug) |
        #         Q(category__icontains=slug)
        #     )
        # else:
        #     queryset = RestaurantLocation.objects.all()
        # return queryset

class RestaurantDetailView(LoginRequiredMixin, DetailView):
    def get_queryset(self):
        return RestaurantLocation.objects.filter(owner=self.request.user)

class RestaurantCreatView(LoginRequiredMixin, CreateView):
    form_class = RestaurantLocationCreateForm
    login_url = '/login/'
    template_name = 'form.html'
    #success_url = "/restaurants/"

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        # instance.save()
        return super(RestaurantCreatView, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(RestaurantCreatView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Add Restaurant'
        return context

#    def get_object(self, *args, **kwargs):
 #       rest_id = self.kwargs.get('rest_id')
  #      obj = get_object_or_404(RestaurantLocation, id=rest_id)
   #     return obj
"""
    def get_context_data(self,*args, **kwargs):   
        print(self.kwargs)
        context = super(RestaurantDetailView,self).get_context_data(*args, **kwargs)
        print(context)
        return context
"""
"""
class MexicanRestaurantListView(ListView):
    queryset = RestaurantLocation.objects.all().filter(category__iexact='mexican')
    template_name = 'restaurants/restaurantlocation_list.html'



class AsianFusionRestaurantListView(ListView):
    queryset = RestaurantLocation.objects.all().filter(category__iexact='asian fusion')
    template_name = 'restaurants/restaurantlocation_list.html'

"""

class RestaurantUpdateView(LoginRequiredMixin, CreateView):
    form_class = RestaurantLocationCreateForm
    login_url = '/login/'
    template_name = 'restaurants/detail-update.html'

    def get_queryset(self):
        return RestaurantLocation.objects.filter(owner=self.request.user)

    def get_context_data(self, *args, **kwargs):
        context = super(RestaurantUpdateView, self).get_context_data(*args, **kwargs)
        name = self.get_object().name
        context['title'] = f'Update Restaurant: {name}'
        return context




