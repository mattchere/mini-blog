from .models import Blogger, BlogPost, Comment

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.views.generic.edit import CreateView



def index(request):
    """
    View function for the site homepage.
    """
    return render(request, 'index.html', context={})


class BlogPostListView(generic.ListView):
    """
    Generic view class for a list of all blog posts.
    """
    model = BlogPost
    paginate_by = 5


class BloggerListView(generic.ListView):
    """
    Generic view class for a list of all bloggers.
    """
    model = Blogger


class BlogPostDetailView(generic.DetailView):
    """
    Generic view class for the detail view of each blog post.
    """
    model = BlogPost

    
class BloggerDetailView(generic.DetailView):
    """
    Generic view class for the detail view of each blogger.
    """
    model = Blogger


class CommentCreate(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['text']

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(CreateView, self).get_context_data(**kwargs)
        # Get the blogger object from the "pk" URL parameter and add it to the context
        context['blogger'] = get_object_or_404(Blogger, pk = self.kwargs['pk'])
        return context


    def form_valid(self, form):
        """
        Add author and associated blog to form data before setting it as valid (so it is saved to model)
        """
        #Add logged-in user as author of comment
        form.instance.commenter = self.request.user
        #Associate comment with blog based on passed id
        form.instance.blog_post = get_object_or_404(BlogPost, pk = self.kwargs['pk'])
        # Call super-class form validation behaviour
        return super(CommentCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse('blog-detail', args=[self.kwargs['pk']])
