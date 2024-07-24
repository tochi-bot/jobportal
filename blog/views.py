from django.shortcuts import render,  redirect, get_object_or_404
from django.views.generic import ListView
from .models import BlogPost 


class BlogListView(ListView):
    queryset = BlogPost.objects.all()
    template_name = "blog/index.html"
    context_object_name = 'blog_list'
    paginate_by = 6

def post_detail(request,slug ):
    """
    Display an individual :model:`blog.BlogPost`.

    **Context**

    ``post``
        An instance of :model:`blog.BlogPost`.

    **Template:**

    :template:`blog/post_detail.html`
    """

    queryset = BlogPost.objects.filter(approved=True)
    post = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "blog/post_detail.html",
        {"BlogPost": BlogPost},
    )  
