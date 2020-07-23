from django.shortcuts import render, redirect
from rest_framework import viewsets
from django.contrib.auth.models import User, Group
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from blogging.models import Post, Category
from django import forms
from django.utils import timezone
from blogging.forms import MyPostForm
from blogging.serializers import UserSerializer, GroupSerializer, PostSerializer, CategorySerializer


def list_view(request):
    published = Post.objects.exclude(published_date__exact=None)
    posts = published.order_by('-published_date')
    # template = loader.get_template('blogging/list.html')
    context = {'posts': posts}
    # body = template.render(context)
    # return HttpResponse(body, content_type="text/html")
    return render(request, 'blogging/list.html', context)


def detail_view(request, post_id):
    published = Post.objects.exclude(published_date__exact=None)
    try:
        post = published.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404
    context = {'post': post}
    return render(request, 'blogging/detail.html', context)


def add_model(request):

    if request.method == "POST":
        form = MyPostForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.timestamp = timezone.now()
            model_instance.save()
            return redirect('/')

    else:

        form = MyPostForm()

        return render(request, "my_template.html", {'form': form})


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Post.objects.all().order_by('-created_date')
    serializer_class = PostSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# def stub_view(request, *args, **kwargs):
    # body = "Stub View\n\n"
    # if args:
    #     body += "Args:\n"
    #     body += "\n".join(["\t%s" % a for a in args])
    # if kwargs:
    #     body += "Kwargs:\n"
    #     body += "\n".join(["\t%s: %s" % i for i in kwargs.items()])
    # return HttpResponse(body, content_type="text/plain")
