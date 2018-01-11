from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from about.models import Articles

urlpatterns = [
    url(r'^$', ListView.as_view(queryset=Articles.objects.all().order_by("-pub_date")[:10], template_name="about/posts.html")),
    url(r'^(?P<pk>\d+)$', DetailView.as_view(model = Articles,template_name="about/post.html")),
]