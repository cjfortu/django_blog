from django.contrib.syndication.views import Feed
from django.urls import reverse, reverse_lazy
from blogging.models import Post


class LatestPostsFeed(Feed):
    title = "The Latest Posts"
    link = "/latestposts/"
    description = "Updates on changes and additions to posts."

    def items(self):
        return Post.objects.order_by('-published_date')[:5]

    def item_title(self, item):
        return item.title

    def item_created_date(self, item):
        return item.created_date

    # item_link is only needed if NewsItem has no get_absolute_url method.
    def item_link(self, item):
        return reverse_lazy('blogging:blog_detail', args=[item.pk])
