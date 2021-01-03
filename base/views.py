from django.shortcuts import render, redirect
from .models import Post
from django.http import HttpResponse

from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
# Create your views here.

def home(request):
    posts = Post.objects.filter(active=True, featured=True)[0:3]
    context = {'posts':posts}
    return render(request, 'base/home.html', context)

def posts(request):
    posts = Post.objects.filter(active=True)
    context = {'posts':posts}
    return render(request, 'base/posts.html', context)

def post(request, slug):
    # post = get_object_or_404(Post, id=id)
    post = Post.objects.get(slug=slug)
    context = {'post':post}
    return render(request, 'base/post.html', context)


# Email
def sendEmail(request):

    if request.method == 'POST':

        template = render_to_string('base/email_template.html',{
            'name':request.POST['name'],
            'email':request.POST['email'],
            'message':request.POST['message'],
        })

        email = EmailMessage(
            request.POST['subject'],
            template,
            settings.EMAIL_HOST_USER,
            ['adialb982@gmail.com']        
        )

        email.fail_silently=False
        email.send()

    # return HttpResponse('Email was sent!') # For testing - import HttpResponse
    return render(request, 'base/email_sent.html')


