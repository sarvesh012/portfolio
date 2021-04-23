
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.http import HttpResponse

from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string


def home(request):
    posts = Post.objects.filter(draft=False).order_by('-created')
    context = {'posts':posts}
    return render(request, 'blog/home.html', context)

# def posts(request):
#     posts = Post.objects.filter(draft=True)
#     context = {'posts':posts}
#     return render(request, 'blog/posts.html', context)

def post(request, slug):
    post = Post.objects.get(slug=slug)
    context = {'post':post}
    return render(request, 'blog/post.html', context)

# def post(request, id):
#     post = get_object_or_404(Post, id=id)
#     context = {'post':post}
#     return render(request, 'blog/post.html', context)

def about(request):
    return render(request, 'blog/about.html')


def contact(request):
    return render(request, 'blog/contact.html')

# Email
def sendEmail(request):

    if request.method == 'POST':

        template = render_to_string('blog/email_template.html',{
            'name':request.POST['name'],
            'email':request.POST['email'],
            'message':request.POST['message'],
        })

        email = EmailMessage(
            request.POST['subject'],
            template,
            settings.EMAIL_HOST_USER,
            [settings.EMAIL_HOST_USER]
            # ['name@gmail.com']
        )

        email.fail_silently=False
        email.send()

    # return HttpResponse('Email was sent!') # For testing - import HttpResponse
    return render(request, 'blog/email_sent.html')