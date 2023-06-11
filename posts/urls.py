from django.urls import path

app_name = 'posts'

from .views import PostList, PostDetail

urlpatterns = [
    path('<int:pk>', PostDetail.as_view()),
    path('', PostList.as_view()),
]
