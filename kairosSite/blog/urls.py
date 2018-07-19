from django.conf.urls import url
import blog.views as  blogviews
urlpatterns = [
    url(r'^$', blogviews.blog_index),
]
