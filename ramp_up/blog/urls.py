from django.urls import path, re_path
from .views import GenericAuthorAPIView, GenericBlogAPIView, AuthorBlogsListAPIView


urlpatterns = [
    # path('blog', GenericBlogAPIView.as_view()),
    # path('blog/<int:id>', GenericBlogAPIView.as_view()),
    re_path(r'^blog/(?:(?P<id>\d+)/?)?$', GenericBlogAPIView.as_view()),


    # path('author', GenericAuthorAPIView.as_view()),
    # path('author/<int:id>', GenericAuthorAPIView.as_view()),
    re_path(r'^author/(?:(?P<id>\d+)/?)?$', GenericAuthorAPIView.as_view()),


    # path('author/<int:author_id>/blogs/', AuthorBlogsListAPIView.as_view()),
    re_path(r'^author/(?P<author_id>\d+)/blogs/?$', AuthorBlogsListAPIView.as_view()),
]