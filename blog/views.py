from .models import Blogger, BlogPost, Comment

from django.shortcuts import render
from django.views import generic


def index(request):
    """
    View function for the site homepage.
    """
    return render(request, 'index.html', context={})


class BlogPostListView(generic.ListView):
    model = BlogPost
    paginate_by = 5
