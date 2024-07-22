from django.shortcuts import render
from django.views.generic import ListView
from .models import BlogPost  

class BlogListView(ListView):
    queryset = BlogPost.objects.all()
    template_name = "blog/index.html"
    context_object_name = 'blog_list'
    paginate_by = 9
   
