from django.shortcuts import render


posts = [
    {
        'author': 'Saimun Hassan',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'June 02, 2021'
    },

    {
        'author': 'John Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'February 28, 2021'
    }
]


# Create your views here.


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'about'})
