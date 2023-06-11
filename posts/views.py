from django.contrib.auth import get_user_model
from rest_framework import viewsets

from .models import Post
from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerializer, UserSerializer


# method 1, more code
# class PostList(generics.ListCreateAPIView):
#     # view level authentication
#     # permission_classes = (permissions.IsAuthenticated,)
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
#
# class PostDetail(generics.RetrieveUpdateDestroyAPIView):
#     # custom permissions
#     permission_classes = (IsAuthorOrReadOnly,)
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
#
# class UserList(generics.ListCreateAPIView):  # new
#
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer
#
#
# class UserDetail(generics.RetrieveUpdateDestroyAPIView):  # new
#
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer

# method 2, less code

class PostViewSet(viewsets.ModelViewSet):  # new
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserViewSet(viewsets.ModelViewSet):  # new
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
