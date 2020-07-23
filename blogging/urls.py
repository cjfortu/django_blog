from django.urls import path
from blogging.views import list_view, detail_view

app_name = 'blogging'
urlpatterns = [
    path('', list_view, name="blog_index"),
    path('posts/<int:post_id>/', detail_view, name="blog_detail"),
]
