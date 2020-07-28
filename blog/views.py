from django.shortcuts import render, get_object_or_404
from .models import Blog


def all_blogs(request):
    """This .all() gets all the blogs in one page"""
    blogs = Blog.objects.all()
    """This .order_by is used to get the blogs in an order and "-date" indicates latest blogs."""
    """[:5] this helps display only the top 5 blogs"""
    #blogs = Blog.objects.order_by('-date') [:5]
    return render(request, 'blog/all_blogs.html', {'blogs': blogs})


def detail(request, blog_id):
    # Blog is the name of the class.....pk= primary key means the id of the object in the date base
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': blog})
