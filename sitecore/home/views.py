from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from django.contrib.admin.views.decorators import staff_member_required
from home.models import Topbar,header_carousel_pics, Footer
from services.models import Service
from abouts.models import About
from blog.models  import Post
from django.views.generic import (
    ListView,
)

def index(request):
    services = Service.objects.order_by('-reload').filter(is_published=True)[:4]
    topbars = Topbar.objects.order_by('-reload').filter(is_published=True)[:1]
    header_carousel_picss = header_carousel_pics.objects.order_by('-reload').filter(is_published=True)[:1]
    footers = Footer.objects.order_by('-reload').filter(is_published=True)[:1]
    posts = Post.objects.all()[:3]

    context = {
        'services': services,
        'posts': posts,
        'topbars': topbars,
        'header_carousel_picss': header_carousel_picss,
        'footers': footers,
    }
    return render(request, 'home/home.html', context) 

class PostListView(ListView):
    model = Post
    template_name = 'blog/blog.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-created_on']
    paginate_by = 5


def about(request):
    abouts = About.objects.order_by('-reload').filter(is_published=True)[:1]
    topbars = Topbar.objects.order_by('-reload').filter(is_published=True)[:1]
    footers = Footer.objects.order_by('-reload').filter(is_published=True)[:1]

    context = {
        'abouts': abouts,
        'topbars': topbars,
        'footers': footers,
    }
    return render(request, 'home/about.html') 


def contact(request):
    return render(request, 'home/contact.html')

@staff_member_required
def mobile(request):
    return render(request, 'home/mobile.html') 

@staff_member_required
def tablet(request):
    return render(request, 'home/tablet.html') 

@staff_member_required
def laptop(request):
    return render(request, 'home/laptop.html') 
