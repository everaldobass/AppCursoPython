from django.shortcuts import render

# Create your views here.

from django.views.generic import DateDetailView, ListView
from django.views.generic.detail import DetailView

from .models import Post


class PostListView(ListView):
    model = "Post"

class PostDetailView(DetailView):
    model = "Post"
