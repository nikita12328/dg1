from django.urls import path
from .views import HelloView
from .views import year_post, MonthPost, post_detail, TemplIf, view_for, author_posts, post_full


urlpatterns = [
    path('hello/', HelloView.as_view(), name='hello2'),
    path('temp_if/', TemplIf.as_view(), name='temp_if'),
    path('temp_for/', view_for, name='temp_for'),
    path('posts/<int:year>/', year_post, name='year_post'),
    path('posts/<int:year>/<int:month>/', MonthPost.as_view(), name='month_post'),
    path('posts/<int:year>/<int:month>/<slug:slug>/', post_detail, name='post_detail'),
    path('author/<int:author_id>/', author_posts, name='author_posts'),
    path('post/<int:post_id>/', post_full, name='post_full')
]
