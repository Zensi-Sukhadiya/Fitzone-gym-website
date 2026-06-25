from django.shortcuts import render, redirect, get_object_or_404
from .models import Trainer, MembershipPlan, Gallery, Contact, BlogPost
from django.contrib import messages

def home(request):
    trainers = Trainer.objects.all()[:3]
    plans = MembershipPlan.objects.all()[:3]
    gallery_items = Gallery.objects.order_by('-id')[:3]
    return render(request, 'gym/home.html', {
        'trainers': trainers,
        'plans': plans,
        'gallery': gallery_items
    })



def trainers(request):
    trainers_list = Trainer.objects.all()
    return render(request, 'gym/trainers.html', {'trainers': trainers_list})

def plans(request):
    plans_list = MembershipPlan.objects.all()
    return render(request, 'gym/plans.html', {'plans': plans_list})

def gallery(request):
    gallery_items = Gallery.objects.all()
    return render(request, 'gym/gallery.html', {'gallery': gallery_items})

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        Contact.objects.create(name=name, email=email, message=message)
        messages.success(request, 'Your message has been sent successfully!')
        return redirect('contact')
    return render(request, 'gym/contact.html')



def blog_list(request):
    posts = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'gym/blog.html', {'posts': posts})

def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    return render(request, 'gym/blog_detail.html', {'post': post})
