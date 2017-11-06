from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.shortcuts import render
from .forms import TweetModelForm
from .models import Tweet
from django import forms
from .mixins import FormUserNeededMixin
# Create your views here.


#Create

class TweetCreateView(FormUserNeededMixin,CreateView):
    template_name = "tweet/create_view.html"
    form_class = TweetModelForm
    success_url = '/tweets/create'
    # login_url = "/admin/"
#retrieve

#Update View
class TweetUpdateView(UpdateView):
    model =Tweet
    template_name = 'tweet/update_view.html'
    form_class = TweetModelForm
    success_url = '/tweets/'


#Create function View
def tweet_create_view(request):
    form = TweetModelForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
    context = {
        "form":form
    }
    return render(request, 'tweet/create_view.html', context )
        


#Generic Class Based Views
class TweetDetailView(DetailView):
    template_name = "tweet/detail_view.html"
    queryset = Tweet.objects.all()

    # def get_object(self):
    #     pk  = self.kwargs.get("pk")
    #     return Tweet.objects.get(id = pk)


class TweetListView(ListView):
    template_name =  "tweet/list_view.html"
    queryset = Tweet.objects.all()







# Function based views

def tweet_detail_view(request, id = 1):
    obj = Tweet.objects.get(id=id)
    context = {
        "object":obj
    }
    return render(request, "tweet/detail_view.html", context)

def tweet_list_view(request):
    queryset = Tweet.objects.all()
    context = {
        "object_list":queryset
    }
    return render(request, "tweet/list_view.html", context)

